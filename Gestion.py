# app.py
from flask import Flask, render_template, request, jsonify
import csv
import os
from datetime import datetime

app = Flask(__name__)

# Datos de ejemplo (puedes reemplazar con base de datos o CSV)
datos_ejemplo = [
    {
        'Marca': 'Ejemplo1',
        'Zona': 'Norte',
        'Grupo': 'A',
        'Cliente': 'CL001',
        'Nombre': 'Tienda Central',
        'Dirección': 'Av. Principal 123',
        'Telefono': '555-1234',
        'PQ': '10',
        'CJ': '5',
        '$$': '1500.50',
        'DIA': 'Lunes',
        'CAMION': 'CAM001',
        'CHOFER': 'Juan Pérez',
        'O': '✓',
        'Obs.': 'Entrega prioritaria',
        'CODIGO': 'ABC123'
    },
    {
        'Marca': 'Ejemplo2',
        'Zona': 'Sur',
        'Grupo': 'B',
        'Cliente': 'CL002',
        'Nombre': 'Supermercado Sur',
        'Dirección': 'Calle Secundaria 456',
        'Telefono': '555-5678',
        'PQ': '8',
        'CJ': '3',
        '$$': '980.75',
        'DIA': 'Martes',
        'CAMION': 'CAM002',
        'CHOFER': 'María Gómez',
        'O': '✗',
        'Obs.': 'Pedido pendiente',
        'CODIGO': 'DEF456'
    },
    # Agrega más datos según necesites
]

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html', datos=datos_ejemplo)

# Ruta para agregar nuevos registros
@app.route('/agregar', methods=['POST'])
def agregar_registro():
    try:
        nuevo_registro = {
            'Marca': request.form.get('marca', ''),
            'Zona': request.form.get('zona', ''),
            'Grupo': request.form.get('grupo', ''),
            'Cliente': request.form.get('cliente', ''),
            'Nombre': request.form.get('nombre', ''),
            'Dirección': request.form.get('direccion', ''),
            'Telefono': request.form.get('telefono', ''),
            'PQ': request.form.get('pq', ''),
            'CJ': request.form.get('cj', ''),
            '$$': request.form.get('costo', ''),
            'DIA': request.form.get('dia', ''),
            'CAMION': request.form.get('camion', ''),
            'CHOFER': request.form.get('chofer', ''),
            'O': request.form.get('estado', ''),
            'Obs.': request.form.get('obs', ''),
            'CODIGO': request.form.get('codigo', '')
        }
        
        datos_ejemplo.append(nuevo_registro)
        return jsonify({'success': True, 'message': 'Registro agregado'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

# Ruta para exportar a CSV
@app.route('/exportar')
def exportar_csv():
    try:
        filename = f'datos_exportados_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        filepath = os.path.join('static', 'exports', filename)
        
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            campos = ['Marca', 'Zona', 'Grupo', 'Cliente', 'Nombre', 'Dirección', 
                     'Telefono', 'PQ', 'CJ', '$$', 'DIA', 'CAMION', 'CHOFER', 
                     'O', 'Obs.', 'CODIGO']
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            writer.writeheader()
            writer.writerows(datos_ejemplo)
        
        return jsonify({'success': True, 'filename': filename})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)