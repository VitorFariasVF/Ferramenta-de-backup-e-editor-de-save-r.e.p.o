# Gerenciador de Backup - Saves do Jogo Repo

Este programa permite fazer backup e restaurar as **pastas de save** do jogo Repo de forma simples e intuitiva.

## Funcionalidades

- **Listar Pastas de Saves**: Visualiza todas as pastas de save na pasta base do jogo
- **Fazer Backup**: Cria uma cópia de segurança da pasta de save selecionada
- **Restaurar Backup**: Restaura um backup de pasta previamente criado
- **Visualizar Backups**: Lista todos os backups de pastas disponíveis
- **Interface Gráfica**: Interface simples e fácil de usar

## Como Usar

### Instalação

1. Cetifique-se de ter o Python 3 instalado no seu sistema
2. No Windows, você pode baixar o Python em: https://www.python.org/downloads/
3. Durante a instalação, marque a opção "Add Python to PATH"

### Executando o Programa

1. Baixe o arquivo `backup_saves.py`
2. Execute o programa de uma das seguintes formas:
   - Duplo clique no arquivo (se o Python estiver associado aos arquivos .py)
   - Abra o prompt de comando e execute: `python backup_saves.py`
   - No terminal/cmd, navegue até a pasta do arquivo e execute: `python3 backup_saves.py`

### Usando o Programa

1. **Primeira Execução**:
   - O programa tentará localizar automaticamente a pasta base dos saves em:
   - `C:\Users\[seu_usuario]\AppData\LocalLow\semiwork\Repo\saves`
   - Se a pasta não for encontrada, use o botão "Alterar" para selecionar a pasta correta

2. **Fazendo Backup**:
   - Selecione uma pasta de save na lista
   - Clique no botão "Fazer Backup"
   - O programa criará uma pasta "backup" dentro da pasta base dos saves e copiará a pasta selecionada para lá.

3. **Restaurando Backup**:
   - Selecione a pasta de save que deseja restaurar na lista
   - Clique no botão "Restaurar Backup"
   - Confirme a operação (a pasta atual será sobrescrita/removida)

4. **Visualizando Backups**:
   - Clique no botão "Ver Backups" para listar todos os backups de pastas criados
   - A janela mostrará o nome da pasta de backup e a data de criação do backup

## Estrutura de Pastas

```
pasta_base_dos_saves/
├── save_game_1/       # Pasta de save original
│   └── data.txt
├── save_game_2/       # Pasta de save original
│   └── config.ini
└── backup/             # Pasta criada automaticamente para armazenar backups
    ├── save_game_1/    # Backup simples da pasta (para restauração rápida)
    ├── save_game_1_backup_20250704_HHMMSS/  # Backup com timestamp (múltiplas versões)
    └── save_game_2_backup_20250704_HHMMSS/
```

## Recursos Técnicos

- **Linguagem**: Python 3
- **Interface**: Tkinter (incluído no Python)
- **Compatibilidade**: Windows, Linux, macOS
- **Dependências**: Apenas bibliotecas padrão do Python

## Segurança

- O programa nunca deleta pastas originais sem confirmação
- Sempre cria cópias antes de qualquer operação
- Solicita confirmação antes de sobrescrever pastas
- Mantém múltiplas versões de backup com timestamp

## Solução de Problemas

### "No module named \'tkinter\'"
- **Windows**: Reinstale o Python marcando a opção "tcl/tk and IDLE"
- **Linux**: Execute `sudo apt install python3-tk`
- **macOS**: Execute `brew install python-tk`

### Pasta de saves não encontrada
- Use o botão "Alterar" para selecionar manualmente a pasta correta
- Verifique se o jogo foi executado pelo menos uma vez para criar a pasta

### Permissões negadas
- Execute o programa como administrador (Windows)
- Verifique se você tem permissão de escrita na pasta dos saves

## Contato

Se encontrar problemas ou tiver sugestões, entre em contato através dos issues do projeto.

