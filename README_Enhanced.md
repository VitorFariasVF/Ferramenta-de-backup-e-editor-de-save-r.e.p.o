# Gerenciador de Backup - Saves do Jogo Repo (Versão Aprimorada)

Este programa permite fazer backup e restaurar as **pastas de save** do jogo Repo de forma simples e intuitiva, com uma interface moderna e aprimorada visualmente.

## ✨ Novidades da Versão Aprimorada

- **🎨 Interface Moderna**: Tema escuro moderno inspirado em aplicações gaming
- **📱 Layout Duplo**: Visualização simultânea de saves e backups em duas janelas lado a lado
- **🎯 Melhor Usabilidade**: Ícones, cores e tipografia aprimoradas
- **⚡ Funcionalidades Extras**: Exclusão de backups e melhor organização visual
- **🔄 Atualização Automática**: Ambas as listas se atualizam automaticamente

## 🚀 Funcionalidades

- **📂 Listar Pastas de Saves**: Visualiza todas as pastas de save na pasta base do jogo
- **💾 Fazer Backup**: Cria uma cópia de segurança da pasta de save selecionada
- **🔄 Restaurar Backup**: Restaura um backup de pasta previamente criado
- **👁️ Visualizar Backups**: Lista todos os backups de pastas disponíveis em tempo real
- **🗑️ Excluir Backups**: Remove backups desnecessários para economizar espaço
- **🎮 Interface Gráfica Moderna**: Interface inspirada em aplicações gaming

## 📋 Como Usar

### Instalação

1. Certifique-se de ter o Python 3 instalado no seu sistema
2. No Windows, você pode baixar o Python em: https://www.python.org/downloads/
3. Durante a instalação, marque a opção "Add Python to PATH"

### Executando o Programa

1. Baixe o arquivo `backup_saves_enhanced.py`
2. Execute o programa de uma das seguintes formas:
   - **Windows**: Duplo clique em `executar_enhanced.bat`
   - **Manual**: Execute `python backup_saves_enhanced.py`
   - **Terminal**: `python3 backup_saves_enhanced.py`

### Usando o Programa

1. **🏁 Primeira Execução**:
   - O programa tentará localizar automaticamente a pasta base dos saves em:
   - `C:\Users\[seu_usuario]\AppData\LocalLow\semiwork\Repo\saves`
   - Se a pasta não for encontrada, use o botão "Alterar" para selecionar a pasta correta

2. **💾 Fazendo Backup**:
   - Selecione uma pasta de save na **lista esquerda**
   - Clique no botão "💾 Fazer Backup"
   - O backup aparecerá automaticamente na **lista direita**

3. **🔄 Restaurando Backup**:
   - Selecione um backup na **lista direita**
   - Clique no botão "🔄 Restaurar Backup"
   - Confirme a operação (a pasta atual será sobrescrita)

4. **🗑️ Excluindo Backups**:
   - Selecione um backup na **lista direita**
   - Clique no botão "🗑️ Excluir Backup"
   - Confirme a exclusão

5. **🔄 Atualizando Listas**:
   - Use o botão "🔄 Atualizar" para atualizar ambas as listas
   - As listas se atualizam automaticamente após operações

## 📁 Estrutura de Pastas

```
pasta_base_dos_saves/
├── save_game_1/       # 📂 Pasta de save original
│   ├── data.txt
│   └── config.ini
├── save_game_2/       # 📂 Pasta de save original
│   └── progress.dat
└── backup/             # 💾 Pasta criada automaticamente para backups
    ├── save_game_1/    # ⚡ Backup atual (restauração rápida)
    ├── save_game_1_backup_20250704_143022/  # 🕒 Backup histórico
    └── save_game_2_backup_20250704_150815/  # 🕒 Backup histórico
```

## 🎨 Interface Visual

### Tema Escuro Moderno
- **Cores**: Paleta escura com acentos azuis
- **Tipografia**: Fonte Segoe UI para melhor legibilidade
- **Ícones**: Emojis para identificação rápida das funcionalidades
- **Layout**: Duas colunas para visualização simultânea

### Indicadores Visuais
- **✅ Verde**: Operações bem-sucedidas
- **❌ Vermelho**: Erros ou avisos
- **🔄 Azul**: Operações em andamento
- **⚡ Atual**: Backup mais recente
- **🕒 Histórico**: Backups com timestamp

## ⚙️ Recursos Técnicos

- **Linguagem**: Python 3
- **Interface**: Tkinter com estilos personalizados
- **Compatibilidade**: Windows, Linux, macOS
- **Dependências**: Apenas bibliotecas padrão do Python
- **Tema**: Escuro moderno inspirado em aplicações gaming

## 🔒 Segurança

- O programa nunca deleta pastas originais sem confirmação
- Sempre cria cópias antes de qualquer operação
- Solicita confirmação antes de sobrescrever ou excluir
- Mantém múltiplas versões de backup com timestamp
- Backup atual sempre disponível para restauração rápida

## 🛠️ Solução de Problemas

### "No module named 'tkinter'"
- **Windows**: Reinstale o Python marcando a opção "tcl/tk and IDLE"
- **Linux**: Execute `sudo apt install python3-tk`
- **macOS**: Execute `brew install python-tk`

### Pasta de saves não encontrada
- Use o botão "Alterar" para selecionar manualmente a pasta correta
- Verifique se o jogo foi executado pelo menos uma vez para criar a pasta

### Interface não aparece corretamente
- Certifique-se de que o sistema suporta Tkinter
- Verifique se a resolução da tela é adequada (mínimo 1200x700)

### Permissões negadas
- Execute o programa como administrador (Windows)
- Verifique se você tem permissão de escrita na pasta dos saves

## 📞 Contato

Se encontrar problemas ou tiver sugestões, entre em contato através dos issues do projeto.

---

**🎮 Versão Aprimorada - Interface Moderna para Gamers!**

