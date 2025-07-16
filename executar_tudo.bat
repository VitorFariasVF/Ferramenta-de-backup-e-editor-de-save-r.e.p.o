@echo off

:: Define o diretório atual como o diretório de trabalho
cd /d "%~dp0"

:: Verifica se o Python está instalado e no PATH
python --version >NUL 2>&1
if %errorlevel% neq 0 (
    echo Python nao encontrado. Por favor, instale o Python 3.x e adicione-o ao PATH.
    echo Download: https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Verifica se o pip esta instalado
pip --version >NUL 2>&1
if %errorlevel% neq 0 (
    echo Pip nao encontrado. Por favor, instale o pip.
    pause
    exit /b 1
)

:: Instala as dependencias
python -m pip install -r requirements.txt --break-system-packages
if %errorlevel% neq 0 (
    echo Erro ao instalar dependencias. Verifique sua conexao com a internet ou permissoes.
    pause
    exit /b 1
)

:: Executa o programa principal
python backup_saves_enhanced_with_editor.py

pause


