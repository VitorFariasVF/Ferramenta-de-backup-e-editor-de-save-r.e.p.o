@echo off
echo Iniciando Gerenciador de Backup - Saves do Jogo Repo (Versao Aprimorada com Editor)...
echo.

REM Verificar se o Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Python nao encontrado. Por favor, instale o Python 3.7 ou superior.
    echo Voce pode baixar em: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Verificar se o arquivo principal existe
if not exist "backup_saves_enhanced_with_editor.py" (
    echo ERRO: Arquivo backup_saves_enhanced_with_editor.py nao encontrado.
    echo Certifique-se de que este arquivo .bat esta na mesma pasta do programa.
    pause
    exit /b 1
)

REM Verificar se o arquivo de traduções existe
if not exist "translations.json" (
    echo ERRO: Arquivo translations.json nao encontrado.
    echo Certifique-se de que este arquivo esta na mesma pasta do programa.
    pause
    exit /b 1
)

REM Verificar se o módulo core existe
if not exist "save_editor_core.py" (
    echo ERRO: Arquivo save_editor_core.py nao encontrado.
    echo Certifique-se de que este arquivo esta na mesma pasta do programa.
    pause
    exit /b 1
)

REM Instalar dependências se necessário
echo Verificando dependencias...
python -c "import tkinter, json, os, shutil, datetime, platform" >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Algumas dependencias basicas nao estao disponiveis.
    pause
    exit /b 1
)

python -c "from Crypto.Cipher import AES" >nul 2>&1
if %errorlevel% neq 0 (
    echo Instalando dependencia pycryptodome...
    pip install pycryptodome
    if %errorlevel% neq 0 (
        echo ERRO: Falha ao instalar pycryptodome. Tente executar como administrador.
        pause
        exit /b 1
    )
)

echo Dependencias verificadas com sucesso!
echo.

REM Executar o programa
echo Iniciando o programa...
python backup_saves_enhanced_with_editor.py

REM Verificar se houve erro na execução
if %errorlevel% neq 0 (
    echo.
    echo ERRO: Falha ao executar o programa.
    echo Verifique se o arquivo backup_saves_enhanced_with_editor.py esta na mesma pasta.
)

echo.
echo Pressione qualquer tecla para continuar...
pause >nul

