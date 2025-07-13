# 🎮 Guia Completo de Uso - Gerenciador de Backup dos Saves do Jogo Repo

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Instalação](#instalação)
3. [Primeira Execução](#primeira-execução)
4. [Interface do Programa](#interface-do-programa)
5. [Como Fazer Backup](#como-fazer-backup)
6. [Como Restaurar Backup](#como-restaurar-backup)
7. [Como Excluir Backup](#como-excluir-backup)
8. [Trocar Idioma](#trocar-idioma)
9. [Solução de Problemas](#solução-de-problemas)
10. [Perguntas Frequentes](#perguntas-frequentes)

---

## 🌟 Visão Geral

O **Gerenciador de Backup dos Saves do Jogo Repo** é um programa que permite fazer backup e restaurar as pastas de save do jogo Repo de forma simples e segura. O programa possui:

- ✅ **Interface moderna** com tema escuro
- ✅ **Suporte a 5 idiomas**: Português, Inglês, Francês, Chinês e Japonês
- ✅ **Visualização dupla**: Saves e backups lado a lado
- ✅ **Backup automático** com timestamp
- ✅ **Restauração segura** com confirmação
- ✅ **Exclusão de backups** desnecessários

---

## 🚀 Instalação

### Pré-requisitos
- **Python 3.7 ou superior** instalado no sistema
- **Sistema operacional**: Windows, Linux ou macOS

### Passo a Passo

#### Windows:
1. **Baixe o Python**: Acesse https://www.python.org/downloads/
2. **Instale o Python**: Durante a instalação, **marque a opção "Add Python to PATH"**
3. **Baixe o programa**: Extraia o arquivo ZIP do programa
4. **Execute**: Duplo clique em `executar_multilang.bat`

#### Linux/macOS:
1. **Verifique o Python**: Execute `python3 --version` no terminal
2. **Instale se necessário**: 
   - Ubuntu/Debian: `sudo apt install python3 python3-tk`
   - macOS: `brew install python-tk`
3. **Execute**: `python3 backup_saves_multilang.py`

---

## 🏁 Primeira Execução

### 1. Iniciar o Programa
- **Windows**: Duplo clique em `executar_multilang.bat`
- **Linux/macOS**: Execute `python3 backup_saves_multilang.py` no terminal

### 2. Verificar Pasta dos Saves
O programa tentará encontrar automaticamente a pasta dos saves em:
```
C:\Users\[SEU_USUARIO]\AppData\LocalLow\semiwork\Repo\saves
```

### 3. Configurar Pasta (se necessário)
Se a pasta não for encontrada:
1. Clique no botão **"Alterar"**
2. Navegue até a pasta correta dos saves do jogo
3. Clique em **"OK"**

---

## 🖥️ Interface do Programa

### Layout Principal
```
┌─────────────────────────────────────────────────────────────┐
│ 🎮 Gerenciador de Backup - Saves do Jogo Repo    🌐 Idioma │
├─────────────────────────────────────────────────────────────┤
│ 📁 Pasta Base dos Saves: [caminho]  [Alterar] [🔄 Atualizar]│
├─────────────────────────────────────────────────────────────┤
│  📂 Pastas de Save        │  💾 Backups Disponíveis        │
│ ┌─────────────────────────┐ ┌─────────────────────────────┐ │
│ │ Nome │ Data │ Backup   │ │ Nome │ Data │ Tipo         │ │
│ │ save1│ 01/01│   ✅     │ │ save1│ 01/01│ ⚡ Atual     │ │
│ │ save2│ 02/01│   ❌     │ │ save1│ 31/12│ 🕒 Histórico │ │
│ └─────────────────────────┘ └─────────────────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│ [💾 Fazer Backup] [🔄 Restaurar] [🗑️ Excluir] [❌ Sair]    │
├─────────────────────────────────────────────────────────────┤
│ ✅ Status: Pronto para uso                                  │
└─────────────────────────────────────────────────────────────┘
```

### Elementos da Interface

#### 🔝 Cabeçalho
- **Título**: Nome do programa
- **Botão Idioma**: Acesso ao menu de idiomas

#### 📁 Configuração de Pasta
- **Campo de Pasta**: Mostra o caminho atual dos saves
- **Botão Alterar**: Permite escolher outra pasta
- **Botão Atualizar**: Recarrega as listas

#### 📂 Lista de Saves (Esquerda)
- **Nome da Pasta**: Nome da pasta de save
- **Data Modificação**: Última modificação
- **Status Backup**: ✅ tem backup / ❌ sem backup

#### 💾 Lista de Backups (Direita)
- **Nome do Backup**: Nome da pasta de backup
- **Data Criação**: Quando foi criado
- **Tipo**: ⚡ Atual (mais recente) / 🕒 Histórico (com timestamp)

#### 🎛️ Botões de Ação
- **💾 Fazer Backup**: Cria backup da pasta selecionada
- **🔄 Restaurar Backup**: Restaura backup selecionado
- **🗑️ Excluir Backup**: Remove backup selecionado
- **❌ Sair**: Fecha o programa

#### 📊 Barra de Status
- Mostra informações sobre operações e status atual

---

## 💾 Como Fazer Backup

### ⚠️ **AVISO IMPORTANTE: QUANDO FAZER O BACKUP?**

Para garantir a integridade dos seus saves e evitar erros, é crucial fazer o backup em momentos específicos do jogo:

*   **Ao chegar em uma loja:** Este é um ponto seguro onde o jogo geralmente salva o progresso de forma estável.
*   **Ao iniciar um novo mapa/área:** Antes de entrar em uma nova área, o jogo costuma criar um novo save point.

**Fazer o backup durante o jogo ativo, especialmente em momentos de transição ou combate, pode resultar em saves corrompidos ou incompletos.** Sempre que possível, faça o backup em um momento de "calma" no jogo.

### Passo a Passo
1. **Selecione uma pasta de save** na lista esquerda (clique uma vez)
2. **Clique no botão "💾 Fazer Backup"**
3. **Aguarde** a confirmação de sucesso
4. **Verifique** que o backup apareceu na lista direita

### O que Acontece
- O programa cria uma pasta `backup` (se não existir)
- Copia toda a pasta de save selecionada
- Cria **duas versões**:
  - **Backup Atual**: `nome_da_pasta` (para restauração rápida)
  - **Backup Histórico**: `nome_da_pasta_backup_20250101_143022` (com timestamp)

### Exemplo
```
Antes:
saves/
├── meu_save/
│   ├── data.txt
│   └── config.ini

Depois:
saves/
├── meu_save/
│   ├── data.txt
│   └── config.ini
└── backup/
    ├── meu_save/                    ← Backup atual
    │   ├── data.txt
    │   └── config.ini
    └── meu_save_backup_20250101_143022/  ← Backup histórico
        ├── data.txt
        └── config.ini
```

---

## 🔄 Como Restaurar Backup

### Passo a Passo
1. **Selecione um backup** na lista direita (clique uma vez)
2. **Clique no botão "🔄 Restaurar Backup"**
3. **Leia a mensagem de confirmação** cuidadosamente
4. **Clique "Sim"** para confirmar ou "Não" para cancelar
5. **Aguarde** a confirmação de sucesso

### ⚠️ Importante
- A pasta original será **completamente substituída**
- **Todos os dados atuais serão perdidos**
- Esta operação **não pode ser desfeita**
- Sempre faça backup antes de restaurar

### Tipos de Backup
- **⚡ Atual**: Versão mais recente, restauração rápida
- **🕒 Histórico**: Versões antigas com data/hora específica

---

## 🗑️ Como Excluir Backup

### Passo a Passo
1. **Selecione um backup** na lista direita (clique uma vez)
2. **Clique no botão "🗑️ Excluir Backup"**
3. **Confirme a exclusão** clicando "Sim"
4. **Aguarde** a confirmação

### ⚠️ Cuidado
- Backups excluídos **não podem ser recuperados**
- Recomenda-se manter pelo menos um backup de cada save
- Exclua apenas backups antigos desnecessários

---

## 🌐 Trocar Idioma

### Como Trocar
1. **Clique no botão "🌐 Idioma"** no canto superior direito
2. **Escolha o idioma desejado** na janela que abrir:
   - 🇧🇷 **Português**
   - 🇺🇸 **English**
   - 🇫🇷 **Français**
   - 🇨🇳 **中文** (Chinês)
   - 🇯🇵 **日本語** (Japonês)
3. **A interface será atualizada** automaticamente

### Persistência
- O idioma escolhido é **salvo automaticamente**
- Na próxima execução, o programa abrirá no idioma selecionado
- As configurações são salvas no arquivo `config.json`

---

## 🛠️ Solução de Problemas

### Erro: "No module named 'tkinter'"
**Solução:**
- **Windows**: Reinstale o Python marcando "tcl/tk and IDLE"
- **Linux**: Execute `sudo apt install python3-tk`
- **macOS**: Execute `brew install python-tk`

### Erro: "Pasta de saves não encontrada"
**Solução:**
1. Verifique se o jogo foi executado pelo menos uma vez
2. Use o botão "Alterar" para selecionar a pasta manualmente
3. Procure por: `C:\Users\[USUARIO]\AppData\LocalLow\semiwork\Repo\saves`

### Erro: "Permissão negada"
**Solução:**
- **Windows**: Execute como administrador (clique direito → "Executar como administrador")
- **Linux/macOS**: Verifique permissões da pasta dos saves

### Interface não aparece ou está cortada
**Solução:**
- Verifique se a resolução da tela é pelo menos 1200x700
- Tente redimensionar a janela
- Reinicie o programa

### Caracteres estranhos nos idiomas asiáticos
**Solução:**
- Verifique se o sistema suporta fontes Unicode
- No Windows, instale suporte a idiomas asiáticos
- Reinicie o programa

---

## ❓ Perguntas Frequentes

### P: Posso fazer backup de múltiplas pastas ao mesmo tempo?
**R:** Não, o programa faz backup de uma pasta por vez. Repita o processo para cada pasta.

### P: Quantos backups posso ter?
**R:** Não há limite. O programa mantém todos os backups até você excluí-los manualmente.

### P: O programa funciona com outros jogos?
**R:** Sim, basta alterar a pasta base para a pasta de saves de outro jogo.

### P: Posso usar o programa em rede/nuvem?
**R:** Sim, desde que você tenha acesso de leitura/escrita à pasta dos saves.

### P: O programa faz backup automático?
**R:** Não, todos os backups são manuais. Você decide quando fazer.

### P: Posso renomear os backups?
**R:** Não diretamente pelo programa, mas você pode renomear as pastas manualmente no explorador de arquivos.

### P: O que acontece se eu mover a pasta dos saves?
**R:** Use o botão "Alterar" para atualizar o caminho no programa.

### P: O programa funciona offline?
**R:** Sim, o programa funciona completamente offline.

---

## 📞 Suporte

Se você encontrar problemas não listados neste guia:

1. **Verifique** se seguiu todos os passos corretamente
2. **Reinicie** o programa
3. **Verifique** as permissões de arquivo
4. **Consulte** a documentação técnica (README_Enhanced.md)

---

**🎮 Divirta-se jogando com a segurança de ter seus saves protegidos!**

*Versão do Guia: 1.0 | Última atualização: Janeiro 2025*

