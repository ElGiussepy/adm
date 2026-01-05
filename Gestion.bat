@echo off
echo Iniciando aplicacion Gestion...
cd /d "%~dp0"
start "" http://localhost:5000
python Gestion.py
pause