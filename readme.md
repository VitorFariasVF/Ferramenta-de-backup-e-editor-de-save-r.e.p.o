# Ferramenta de Backup e Edição de Saves do REPO

## Sumário

- [Visão Geral do Projeto](#visão-geral-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Como Instalar](#como-instalar)
- [Como Usar](#como-usar)
  - [Fazer Backup de Saves](#fazer-backup-de-saves)
  - [Restaurar Backups](#restaurar-backups)
  - [Usar o Editor de Saves](#usar-o-editor-de-saves)
  - [Alterar Pasta de Saves](#alterar-pasta-de-saves)
- [Solução de Problemas Comuns](#solução-de-problemas-comuns)
- [Licença](#licença)
- [Baixar o Executável (Opcional)](#baixar-o-executável-opcional)

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [How to Install](#how-to-install)
- [How to Use](#how-to-use)
  - [Backing Up Saves](#backing-up-saves)
  - [Restoring Backups](#restoring-backups)
  - [Using the Save Editor](#using-the-save-editor)
  - [Changing Save Folder](#changing-save-folder)
- [Common Troubleshooting](#common-troubleshooting)
- [License](#license)
- [Download the Executable (Optional)](#download-the-executable-optional)


## Visão Geral do Projeto

Esta ferramenta foi desenvolvida para facilitar o gerenciamento dos saves do jogo REPO, permitindo que os usuários criem backups de suas pastas de save, restaurem backups anteriores e, futuramente, editem o conteúdo dos saves. O objetivo é proporcionar uma maneira segura e conveniente de proteger o progresso do jogo e experimentar diferentes cenários sem o risco de perder dados importantes.

O aplicativo é construído em Python, utilizando a biblioteca Tkinter para a interface gráfica, tornando-o acessível e fácil de usar para jogadores de todos os níveis de experiência. Ele foi projetado para ser portátil, com todos os arquivos necessários para execução contidos em uma única pasta, facilitando a distribuição e o uso.




## Project Overview

This tool was developed to facilitate the management of REPO game saves, allowing users to create backups of their save folders, restore previous backups, and, in the future, edit the content of the saves. The goal is to provide a safe and convenient way to protect game progress and experiment with different scenarios without the risk of losing important data.

The application is built in Python, using the Tkinter library for the graphical interface, making it accessible and easy to use for players of all experience levels. It was designed to be portable, with all necessary execution files contained in a single folder, facilitating distribution and use.




## Funcionalidades

- **Backup de Saves**: Crie cópias de segurança das suas pastas de save, organizadas por data e hora.
- **Restauração de Backups**: Restaure facilmente saves anteriores a partir dos backups criados.
- **Editor de Saves (em desenvolvimento)**: Uma funcionalidade para editar o conteúdo dos saves, permitindo personalização avançada (esta funcionalidade está em fase de desenvolvimento e será aprimorada em futuras versões).
- **Interface Gráfica Intuitiva**: Desenvolvida com Tkinter para uma experiência de usuário amigável.
- **Suporte a Múltiplos Idiomas**: O aplicativo oferece suporte a diferentes idiomas para uma melhor acessibilidade.
- **Portabilidade**: Todos os arquivos necessários para execução estão contidos em uma única pasta, facilitando o uso sem a necessidade de instalação complexa.




## Features

- **Save Backup**: Create secure copies of your save folders, organized by date and time.
- **Backup Restoration**: Easily restore previous saves from created backups.
- **Save Editor (under development)**: A feature to edit save content, allowing advanced customization (this feature is under development and will be improved in future versions).
- **Intuitive Graphical Interface**: Developed with Tkinter for a user-friendly experience.
- **Multi-language Support**: The application offers support for different languages for better accessibility.
- **Portability**: All necessary execution files are contained in a single folder, facilitating use without the need for complex installation.




## Como Instalar

Para utilizar a ferramenta de backup e edição de saves do REPO, siga os passos abaixo:

1.  **Baixe o Pacote**: Faça o download do arquivo `backup_saves_flat_structure.zip` (o pacote mais recente que você recebeu) e extraia todo o conteúdo para uma pasta de sua preferência (ex: `C:\BackupRepoSimples`). É crucial que todos os arquivos estejam na mesma pasta, sem subdiretórios.

2.  **Instale as Dependências**: O programa requer algumas bibliotecas Python para funcionar. O arquivo `executar_tudo.bat` cuidará da instalação automática dessas dependências. Certifique-se de ter uma conexão ativa com a internet na primeira execução.

    *   **Execução**: Dê um duplo clique no arquivo `executar_tudo.bat`. Uma janela de terminal será aberta, e você verá o processo de instalação das dependências. Após a instalação, o programa será iniciado automaticamente.

    *   **Problemas na Instalação**: Se você encontrar erros durante a instalação das dependências, verifique sua conexão com a internet e as permissões de escrita na pasta. Você também pode tentar instalar manualmente as dependências abrindo um Prompt de Comando na pasta do projeto e executando: `pip install -r requirements.txt`.

3.  **Crie o Ícone (Opcional)**: Se você deseja que o executável tenha um ícone personalizado, você pode gerar o arquivo `.ico` a partir do `repo_icon.png` usando o script `convert_icon.py`.

    *   Abra um Prompt de Comando na pasta do projeto e execute: `python convert_icon.py repo_icon.png repo_icon.ico`.

Após a instalação e, opcionalmente, a criação do ícone, o programa estará pronto para ser utilizado.




## How to Install

To use the REPO save backup and editing tool, follow the steps below:

1.  **Download the Package**: Download the `backup_saves_flat_structure.zip` file (the latest package you received) and extract all its contents to a folder of your choice (e.g., `C:\BackupRepoSimple`). It is crucial that all files are in the same folder, without subdirectories.

2.  **Install Dependencies**: The program requires some Python libraries to function. The `executar_tudo.bat` file will handle the automatic installation of these dependencies. Make sure you have an active internet connection on the first run.

    *   **Execution**: Double-click the `executar_tudo.bat` file. A terminal window will open, and you will see the dependency installation process. After installation, the program will start automatically.

    *   **Installation Issues**: If you encounter errors during dependency installation, check your internet connection and write permissions in the folder. You can also try to manually install the dependencies by opening a Command Prompt in the project folder and running: `pip install -r requirements.txt`.

3.  **Create the Icon (Optional)**: If you want the executable to have a custom icon, you can generate the `.ico` file from `repo_icon.png` using the `convert_icon.py` script.

    *   Open a Command Prompt in the project folder and run: `python convert_icon.py repo_icon.png repo_icon.ico`.

After installation and, optionally, icon creation, the program will be ready for use.




## Como Usar

Após a instalação, o programa pode ser iniciado a qualquer momento clicando duas vezes em `executar_tudo.bat`. A interface principal do aplicativo será exibida, permitindo que você gerencie seus saves do jogo REPO.

### Fazer Backup de Saves

1.  **Selecione o Save**: Na interface principal, você verá uma lista dos saves disponíveis na pasta do jogo. Selecione o save (ou saves) que deseja fazer backup.
2.  **Clique em "Fazer Backup"**: O programa criará uma subpasta `backup` dentro da pasta do save selecionado e copiará os arquivos para lá, organizando-os por data e hora.

### Restaurar Backups

1.  **Selecione o Save**: Na interface principal, selecione o save para o qual você deseja restaurar um backup.
2.  **Clique em "Restaurar Backup"**: Uma nova janela será aberta, mostrando uma lista dos backups disponíveis para aquele save.
3.  **Escolha o Backup**: Selecione o backup que deseja restaurar na lista.
4.  **Clique em "Restaurar"**: O programa copiará os arquivos do backup selecionado de volta para a pasta principal do save, sobrescrevendo os arquivos existentes (será solicitada uma confirmação antes de sobrescrever).

### Usar o Editor de Saves

1.  **Selecione o Save**: Na interface principal, selecione o save que você deseja editar.
2.  **Clique em "Editar Save"**: Uma nova janela será aberta com o editor de saves. Esta funcionalidade permite visualizar e modificar o conteúdo do save. (Lembre-se que esta funcionalidade está em desenvolvimento e pode ter limitações).
3.  **Faça as Edições**: Realize as modificações desejadas no save.
4.  **Salve as Alterações**: Clique no botão "Salvar" para aplicar as alterações ao save.

### Alterar Pasta de Saves

Se a pasta padrão dos saves do jogo não for detectada automaticamente ou se você deseja usar uma pasta diferente, você pode alterá-la através da interface do programa, usando o botão "Alterar Pasta de Saves".




## How to Use

After installation, the program can be started at any time by double-clicking `executar_tudo.bat`. The main application interface will be displayed, allowing you to manage your REPO game saves.

### Backing Up Saves

1.  **Select the Save**: In the main interface, you will see a list of available saves in the game folder. Select the save (or saves) you want to back up.
2.  **Click "Backup"**: The program will create a `backup` subfolder within the selected save's folder and copy the files there, organizing them by date and time.

### Restoring Backups

1.  **Select the Save**: In the main interface, select the save for which you want to restore a backup.
2.  **Click "Restore Backup"**: A new window will open, showing a list of available backups for that save.
3.  **Choose the Backup**: Select the backup you want to restore from the list.
4.  **Click "Restore"**: The program will copy the files from the selected backup back to the main save folder, overwriting existing files (a confirmation will be requested before overwriting).

### Using the Save Editor

1.  **Select the Save**: In the main interface, select the save you want to edit.
2.  **Click "Edit Save"**: A new window will open with the save editor. This feature allows you to view and modify the save content. (Note that this feature is under development and may have limitations).
3.  **Make Edits**: Make the desired modifications to the save.
4.  **Save Changes**: Click the "Save" button to apply the changes to the save.

### Changing Save Folder

If the default game save folder is not automatically detected or if you want to use a different folder, you can change it through the program's interface, using the "Change Save Folder" button.




## Solução de Problemas Comuns

### Erro: `ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'`

Este erro indica que o arquivo `requirements.txt` não foi encontrado. Certifique-se de que você extraiu **todos** os arquivos do ZIP para a mesma pasta e que o `requirements.txt` está presente nela.

### Erro: `ModuleNotFoundError: No module named 'PIL'` ou outros `ModuleNotFoundError`

Isso significa que uma ou mais bibliotecas Python necessárias não foram instaladas corretamente. Verifique sua conexão com a internet e tente executar o `executar_tudo.bat` novamente. Se o problema persistir, tente instalar manualmente as dependências abrindo um Prompt de Comando na pasta do projeto e executando: `pip install -r requirements.txt`.

### Erro ao Excluir/Restaurar Backup: `backup_not_found` ou `FileNotFoundError`

Este erro geralmente ocorre quando o programa não consegue encontrar a pasta de backup no caminho especificado. Isso pode ser devido a:

*   **Caminho Incorreto**: Verifique se a pasta de saves do jogo está configurada corretamente no programa.
*   **Nome da Pasta**: Certifique-se de que os nomes das pastas de backup não foram alterados manualmente ou que não contêm caracteres especiais que possam estar causando problemas.
*   **Permissões**: Verifique se o programa tem permissão para ler e escrever nas pastas de saves e backups.

### O Executável Não Abre (sem mensagem de erro)

Se o executável não abre e não exibe nenhuma mensagem de erro, pode ser um problema mais complexo. Tente o seguinte:

*   **Execute via CMD**: Abra o Prompt de Comando, navegue até a pasta do executável e execute-o diretamente (ex: `seu_programa.exe`). Isso pode revelar mensagens de erro ocultas.
*   **Antivírus/Firewall**: Seu software de segurança pode estar bloqueando a execução. Tente desativá-lo temporariamente (com cautela) para verificar se é a causa.
*   **Dependências Ocultas**: Embora o `executar_tudo.bat` instale as dependências, em alguns casos raros, pode haver dependências que não são detectadas. Se você estiver tentando gerar um `.exe` com PyInstaller, certifique-se de que todos os `--add-data`, `--paths` e `--hidden-import` estão configurados corretamente.




## Common Troubleshooting

### Error: `ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'`

This error indicates that the `requirements.txt` file was not found. Make sure you have extracted **all** files from the ZIP to the same folder and that `requirements.txt` is present there.

### Error: `ModuleNotFoundError: No module named 'PIL'` or other `ModuleNotFoundError`

This means that one or more necessary Python libraries were not installed correctly. Check your internet connection and try running `executar_tudo.bat` again. If the problem persists, try manually installing the dependencies by opening a Command Prompt in the project folder and running: `pip install -r requirements.txt`.

### Error when Deleting/Restoring Backup: `backup_not_found` or `FileNotFoundError`

This error usually occurs when the program cannot find the backup folder at the specified path. This can be due to:

*   **Incorrect Path**: Verify that the game save folder is correctly configured in the program.
*   **Folder Name**: Make sure that backup folder names have not been manually changed or do not contain special characters that might be causing issues.
*   **Permissions**: Check if the program has permission to read and write to the save and backup folders.

### Executable Does Not Open (no error message)

If the executable does not open and displays no error message, it might be a more complex issue. Try the following:

*   **Run via CMD**: Open Command Prompt, navigate to the executable's folder, and run it directly (e.g., `your_program.exe`). This might reveal hidden error messages.
*   **Antivirus/Firewall**: Your security software might be blocking the execution. Try temporarily disabling it (with caution) to check if it's the cause.
*   **Dependências Ocultas**: Embora o `executar_tudo.bat` instale as dependências, em alguns casos raros, pode haver dependências que não são detectadas. Se você estiver tentando gerar um `.exe` com PyInstaller, certifique-se de que todos os `--add-data`, `--paths` e `--hidden-import` estão configurados corretamente.




## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.




## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.





### Baixar o Executável (Opcional)

Se você preferir uma versão pré-compilada do aplicativo, você pode baixá-la diretamente:

- [Baixar RepoBackupTool.exe](https://github.com/VitorFariasVF/Ferramenta-de-backup-e-editor-de-save-r.e.p.o/blob/main/App/RepoBackupTool.exe)






### Download the Executable (Optional)

If you prefer a pre-compiled version of the application, you can download it directly:

- [Download RepoBackupTool.exe](https://github.com/VitorFariasVF/Ferramenta-de-backup-e-editor-de-save-r.e.p.o/blob/main/App/RepoBackupTool.exe)


<img width="1210" height="737" alt="Captura de tela 2025-07-16 163624" src="https://github.com/user-attachments/assets/a269574e-416c-4595-a084-8a0aa2e565a4" />
<img width="296" height="274" alt="Captura de tela 2025-07-16 163812" src="https://github.com/user-attachments/assets/57ce5c6c-5262-4441-a846-419c6ffec3ca" />
<img width="634" height="507" alt="Captura de tela 2025-07-16 163854" src="https://github.com/user-attachments/assets/0d3bb0b3-eb38-4f86-af4d-202ae559753b" />
<img width="644" height="509" alt="Captura de tela 2025-07-16 163835" src="https://github.com/user-attachments/assets/61b1819b-9d07-451b-909b-135ab6c6d404" />
<img width="797" height="624" alt="Captura de tela 2025-07-16 163909" src="https://github.com/user-attachments/assets/514095ee-02ff-4b09-a371-e3da2264e39c" />
<img width="795" height="633" alt="Captura de tela 2025-07-16 163917" src="https://github.com/user-attachments/assets/bacd539c-3dfe-495d-9591-fffb34b7e932" />





