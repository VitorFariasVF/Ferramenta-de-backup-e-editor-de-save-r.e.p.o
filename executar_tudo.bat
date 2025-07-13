@echo off
CHCP 65001 > nul

echo Iniciando Gerenciador de Backup - Saves do Jogo Repo (Versao Aprimorada com Editor)...
echo.

REM --- VERIFICACAO DE PYTHON ---
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Python nao encontrado. Por favor, instale o Python 3.7 ou superior.
    echo Voce pode baixar em: https://www.python.org/downloads/
    echo.
    echo Pressione qualquer tecla para sair...
    pause >nul
    exit /b 1
)

REM --- VERIFICACAO DE ARQUIVOS ESSENCIAIS ---
set "PROGRAM_FILE=backup_saves_enhanced_with_editor.py"
set "TRANSLATIONS_FILE=translations.json"
set "EDITOR_CORE_FILE=save_editor_core.py"

if not exist "%PROGRAM_FILE%" (
    echo ERRO: Arquivo %PROGRAM_FILE% nao encontrado.
    echo Certifique-se de que este arquivo .bat esta na mesma pasta do programa.
    echo.
    echo Pressione qualquer tecla para sair...
    pause >nul
    exit /b 1
)

if not exist "%TRANSLATIONS_FILE%" (
    echo ERRO: Arquivo %TRANSLATIONS_FILE% nao encontrado.
    echo Certifique-se de que este arquivo esta na mesma pasta do programa.
    echo.
    echo Pressione qualquer tecla para sair...
    pause >nul
    exit /b 1
)

if not exist "%EDITOR_CORE_FILE%" (
    echo ERRO: Arquivo %EDITOR_CORE_FILE% nao encontrado.
    echo Certifique-se de que este arquivo esta na mesma pasta do programa.
    echo.
    echo Pressione qualquer tecla para sair...
    pause >nul
    exit /b 1
)

REM --- INSTALACAO DE DEPENDENCIAS ---
echo Verificando e instalando dependencias Python...

REM Verifica se pycryptodome esta instalado
python -c "from Crypto.Cipher import AES" >nul 2>&1
if %errorlevel% neq 0 (
    echo Instalando pycryptodome...
    pip install pycryptodome
    if %errorlevel% neq 0 (
        echo ERRO: Falha ao instalar pycryptodome.
        echo Tente executar este .bat como ADMINISTRADOR.
        echo.
        echo Pressione qualquer tecla para sair...
        pause >nul
        exit /b 1
    )
    echo pycryptodome instalado com sucesso!
) else (
    echo pycryptodome ja esta instalado.
)

echo.
echo Todas as dependencias verificadas com sucesso!
echo.

REM --- EXECUCAO DO PROGRAMA ---
echo Iniciando o programa...
python "%PROGRAM_FILE%"

REM --- VERIFICACAO DE ERRO NA EXECUCAO ---
if %errorlevel% neq 0 (
    echo.
    echo ERRO: O programa foi encerrado com um erro.
    echo Verifique as mensagens acima para mais detalhes.
)

echo.
echo Pressione qualquer tecla para continuar...
pause >nul


