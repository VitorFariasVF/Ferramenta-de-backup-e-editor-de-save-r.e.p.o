# Gerenciador de Backup - Saves do Jogo Repo (Versão Multilíngue)

Este programa permite fazer backup e restaurar as **pastas de save** do jogo Repo de forma simples e intuitiva, com uma interface moderna e suporte a múltiplos idiomas.

## ✨ Novidades da Versão Multilíngue

- **🌐 Suporte a 5 Idiomas**: Português, Inglês, Francês, Chinês (Mandarim) e Japonês
- **🔄 Troca de Idioma em Tempo Real**: Botão dedicado para mudança instantânea
- **💾 Persistência de Configuração**: O idioma escolhido é salvo automaticamente
- **🎨 Interface Moderna**: Tema escuro moderno inspirado em aplicações gaming
- **📱 Layout Duplo**: Visualização simultânea de saves e backups em duas janelas lado a lado
- **🎯 Melhor Usabilidade**: Ícones, cores e tipografia aprimoradas
- **⚡ Funcionalidades Extras**: Exclusão de backups e melhor organização visual
- **🔄 Atualização Automática**: Ambas as listas se atualizam automaticamente
- **🌍 Detecção Automática de Usuário**: Não requer configuração manual do nome de usuário
- **✅ Correção de Erros**: Resolvido o `UnboundLocalError` e problemas de sintaxe nas traduções.

## 🌐 Idiomas Suportados

| Idioma | Código | Bandeira | Nome Nativo |
|--------|--------|----------|-------------|
| Português | `pt` | 🇧🇷 | Português |
| Inglês | `en` | 🇺🇸 | English |
| Francês | `fr` | 🇫🇷 | Français |
| Chinês | `zh` | 🇨🇳 | 中文 |
| Japonês | `ja` | 🇯🇵 | 日本語 |

## 🚀 Funcionalidades

- **📂 Listar Pastas de Saves**: Visualiza todas as pastas de save na pasta base do jogo
- **💾 Fazer Backup**: Cria uma cópia de segurança da pasta de save selecionada
- **🔄 Restaurar Backup**: Restaura um backup de pasta previamente criado
- **👁️ Visualizar Backups**: Lista todos os backups de pastas disponíveis em tempo real
- **🗑️ Excluir Backups**: Remove backups desnecessários para economizar espaço
- **🌐 Trocar Idioma**: Interface completamente traduzida em 5 idiomas
- **🎮 Interface Gráfica Moderna**: Interface inspirada em aplicações gaming

## 📋 Como Usar

### Instalação

1. Certifique-se de ter o Python 3 instalado no seu sistema
2. No Windows, você pode baixar o Python em: https://www.python.org/downloads/
3. Durante a instalação, marque a opção "Add Python to PATH"

### Executando o Programa

1. Baixe o arquivo `backup_saves_multilang.zip` (ou a versão mais recente)
2. Extraia o conteúdo do ZIP para uma pasta de sua preferência.
3. Execute o programa de uma das seguintes formas:
   - **Windows (Recomendado)**: Dê um duplo clique no arquivo `executar_multilang.bat`.
   - **Manual (Windows/Linux/macOS)**: Abra um terminal ou prompt de comando, navegue até a pasta onde extraiu os arquivos e execute: `python backup_saves_multilang.py`

### Usando o Programa

1. **🏁 Primeira Execução**:
   - O programa detectará automaticamente o usuário atual do Windows.
   - Tentará localizar automaticamente a pasta base dos saves em:
     `C:\Users\[SEU_USUARIO]\AppData\LocalLow\semiwork\Repo\saves`
   - Se a pasta não for encontrada, use o botão "Alterar" para selecionar a pasta correta.

2. **🌐 Trocar Idioma**:
   - Clique no botão "🌐 Idioma" no canto superior direito.
   - Selecione o idioma desejado na janela que abrir.
   - A interface será atualizada instantaneamente.
   - O idioma escolhido será salvo automaticamente.

3. **💾 Fazendo Backup**:
   - Selecione uma pasta de save na **lista esquerda**.
   - Clique no botão "💾 Fazer Backup" (ou equivalente no idioma selecionado).
   - O backup aparecerá automaticamente na **lista direita**.

4. **🔄 Restaurando Backup**:
   - Selecione um backup na **lista direita**.
   - Clique no botão "🔄 Restaurar Backup".
   - Confirme a operação (a pasta atual será sobrescrita).

5. **🗑️ Excluindo Backups**:
   - Selecione um backup na **lista direita**.
   - Clique no botão "🗑️ Excluir Backup".
   - Confirme a exclusão.

6. **🔄 Atualizando Listas**:
   - Use o botão "🔄 Atualizar" para atualizar ambas as listas.
   - As listas se atualizam automaticamente após operações.

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

### Elementos Multilíngues
- **Títulos**: Traduzidos em todos os idiomas
- **Botões**: Textos e ícones localizados
- **Mensagens**: Confirmações e erros traduzidos
- **Status**: Informações de status localizadas

## ⚙️ Recursos Técnicos

- **Linguagem**: Python 3
- **Interface**: Tkinter com estilos personalizados
- **Compatibilidade**: Windows, Linux, macOS
- **Dependências**: Apenas bibliotecas padrão do Python
- **Tema**: Escuro moderno inspirado em aplicações gaming
- **Internacionalização**: Sistema de tradução baseado em arquivo JSON externo (`translations.json`)
- **Persistência**: Configurações salvas em JSON (`config.json`)
- **Detecção de Sistema**: Adaptação automática ao sistema operacional

## 🔧 Configuração

### Arquivo de Configuração
O programa cria automaticamente um arquivo `config.json` na mesma pasta do executável com as seguintes configurações:

```json
{
  "language": "pt"
}
```

### Arquivo de Traduções
As traduções são carregadas do arquivo `translations.json`, que deve estar na mesma pasta do executável.

## 🔒 Segurança

- O programa nunca deleta pastas originais sem confirmação
- Sempre cria cópias antes de qualquer operação
- Solicita confirmação antes de sobrescrever ou excluir
- Mantém múltiplas versões de backup com timestamp
- Backup atual sempre disponível para restauração rápida
- Detecção automática de usuário evita conflitos de permissão

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
- Verifique se a resolução da tela é adequada (mínimo 1200x750)

### Caracteres não aparecem corretamente
- Verifique se o sistema suporta fontes Unicode
- No Windows, instale suporte a idiomas asiáticos se necessário

### Permissões negadas
- Execute o programa como administrador (Windows)
- Verifique se você tem permissão de escrita na pasta dos saves

### Erros de JSON ou Traduções
- Verifique se o arquivo `translations.json` está na mesma pasta do programa.
- Certifique-se de que o `translations.json` é um JSON válido e que não há erros de sintaxe (como aspas ou vírgulas faltando).
- O erro `Invalid \escape` indica que há barras invertidas (`\`) em excesso ou mal formatadas nas strings do JSON. Elas devem ser escapadas corretamente (`\\`) ou removidas se não forem necessárias.

## 🌍 Contribuindo com Traduções

Para adicionar novos idiomas ou melhorar traduções existentes:

1. Edite o arquivo `translations.json`.
2. Adicione um novo dicionário no formato:
```json
"codigo_idioma": {
    "name": "Nome do Idioma",
    "flag": "🏳️ Bandeira",
    "translations": {
        "chave": "Tradução",
        // ... mais traduções
    }
}
```
3. Teste todas as funcionalidades no novo idioma.
4. Verifique a exibição correta de caracteres especiais.

## 📞 Contato

Se encontrar problemas ou tiver sugestões, entre em contato através dos issues do projeto.

---

**🎮 Versão Multilíngue - Interface Moderna para Gamers do Mundo Todo!**



