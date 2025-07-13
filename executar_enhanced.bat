@echo off
echo Iniciando Gerenciador de Backup - Saves do Jogo Repo (Versao Aprimorada)...
echo.

REM Verificar se o Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Python não encontrado!
    echo.
    echo Por favor, instale o Python 3 em: https://www.python.org/downloads/
    echo Durante a instalação, marque a opção "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

REM Executar o programa aprimorado
python backup_saves_enhanced.py

REM Se houver erro, mostrar mensagem
if %errorlevel% neq 0 (
    echo.
    echo ERRO: Falha ao executar o programa.
    echo Verifique se o arquivo backup_saves_enhanced.py está na mesma pasta.
    echo.
    pause
)

