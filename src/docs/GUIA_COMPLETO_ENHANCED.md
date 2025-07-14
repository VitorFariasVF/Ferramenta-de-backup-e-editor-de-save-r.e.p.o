# 🎮 Guia Completo - Gerenciador de Backup R.E.P.O (Versão Aprimorada com Editor)

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Instalação e Configuração](#instalação-e-configuração)
3. [Funcionalidades Principais](#funcionalidades-principais)
4. [Editor de Saves](#editor-de-saves)
5. [Guia de Uso Passo a Passo](#guia-de-uso-passo-a-passo)
6. [Solução de Problemas](#solução-de-problemas)
7. [Perguntas Frequentes](#perguntas-frequentes)

---

## 🌟 Visão Geral

O **Gerenciador de Backup R.E.P.O (Versão Aprimorada com Editor)** é uma ferramenta completa que combina:

- ✅ **Backup e Restauração** de saves do jogo R.E.P.O
- ✅ **Editor de Saves** integrado para modificar dados do jogo
- ✅ **Interface Multilíngue** (Português, Inglês, Francês, Chinês, Japonês)
- ✅ **Tema Moderno** com visual gaming
- ✅ **Criptografia/Descriptografia** de arquivos .es3

### 🆕 Novidades da Versão Aprimorada

- **🔧 Editor de Saves Integrado**: Edite dados de jogadores, mundo e configurações
- **🔐 Suporte a Arquivos .es3**: Descriptografa, edita e criptografa saves do R.E.P.O
- **📊 Interface com Abas**: Dados do mundo, jogadores e JSON bruto
- **✅ Validação de Dados**: Previne corrupção de saves com validação automática
- **🎨 Interface Aprimorada**: Novo botão "Editar Save" e melhor organização

---

## 🚀 Instalação e Configuração

### Requisitos do Sistema

- **Sistema Operacional**: Windows 7/8/10/11, Linux, macOS
- **Python**: Versão 3.7 ou superior
- **Dependências**: `tkinter`, `pycryptodome`

### Instalação Rápida (Windows)

1. **Baixe e Extraia**: Descompacte o arquivo ZIP em uma pasta de sua preferência
2. **Execute**: Dê um duplo clique em `executar_enhanced.bat`
3. **Aguarde**: O script verificará e instalará dependências automaticamente

### Instalação Manual

1. **Instale o Python**: Baixe em [python.org](https://www.python.org/downloads/)
2. **Instale Dependências**:
   ```bash
   pip install pycryptodome
   ```
3. **Execute o Programa**:
   ```bash
   python backup_saves_enhanced_with_editor.py
   ```

### Estrutura de Arquivos

```
📁 Pasta do Programa/
├── 📄 backup_saves_enhanced_with_editor.py  # Programa principal
├── 📄 save_editor_core.py                   # Módulo do editor
├── 📄 translations.json                     # Traduções
├── 📄 executar_enhanced.bat                 # Script de execução (Windows)
├── 📄 GUIA_COMPLETO_ENHANCED.md            # Este guia
└── 📄 test_enhanced_editor.py               # Testes (opcional)
```

---

## ⚡ Funcionalidades Principais

### 💾 Backup e Restauração

- **Backup Automático**: Cria backup atual + histórico com timestamp
- **Restauração Segura**: Confirmação antes de sobrescrever
- **Visualização Dupla**: Saves e backups lado a lado
- **Indicadores Visuais**: ✅ tem backup, ❌ sem backup

### 🔧 Editor de Saves (NOVO!)

- **Edição de Dados do Mundo**:
  - Nome da equipe
  - Nível atual
  - Moeda/dinheiro
  - Vidas restantes
  - Carga da estação
  - Total de carga coletada

- **Edição de Dados dos Jogadores**:
  - Vida/saúde
  - Upgrades (resistência, pulo, velocidade, força, etc.)
  - Estatísticas individuais

- **Edição JSON Bruta**:
  - Acesso completo aos dados do save
  - Edição avançada para usuários experientes

### 🌐 Multilíngue

- **5 Idiomas Suportados**: PT, EN, FR, ZH, JA
- **Troca Instantânea**: Botão "🌐 Idioma" no canto superior
- **Persistência**: Idioma escolhido é salvo automaticamente

---

## 🔧 Editor de Saves

### Como Acessar o Editor

1. **Selecione um Save**: Clique em uma pasta de save na lista esquerda
2. **Clique em "Editar Save"**: Botão laranja na barra inferior
3. **Escolha o Arquivo**: Se houver múltiplos .es3, selecione um
4. **Aguarde**: O editor abrirá em uma nova janela

### Interface do Editor

#### 🌍 Aba "Dados do Mundo"
- **Nome da Equipe**: Altere o nome da sua equipe
- **Nível**: Modifique o nível atual da campanha
- **Moeda**: Ajuste a quantidade de dinheiro
- **Vidas**: Defina o número de vidas restantes
- **Estação de Carregamento**: Configure a carga da estação
- **Total de Carga**: Modifique o total coletado

#### 👥 Aba "Dados dos Jogadores"
- **Vida**: Ajuste a vida de cada jogador
- **Upgrades**: Modifique todos os upgrades:
  - Resistência (Stamina)
  - Pulo Extra
  - Velocidade
  - Força
  - Alcance
  - Arremesso
  - E mais...

#### 📝 Aba "JSON Bruto"
- **Edição Avançada**: Acesso completo aos dados
- **Sintaxe JSON**: Para usuários experientes
- **Backup Automático**: Sempre faça backup antes de editar

### Validação e Segurança

- **Validação Automática**: Previne valores inválidos
- **Limites Seguros**: Evita corrupção do save
- **Confirmação**: Sempre confirma antes de salvar
- **Backup Recomendado**: Faça backup antes de editar

---

## 📖 Guia de Uso Passo a Passo

### Primeiro Uso

1. **Execute o Programa**: Use `executar_enhanced.bat` ou execute manualmente
2. **Verifique a Pasta**: O programa detecta automaticamente a pasta de saves
3. **Altere se Necessário**: Use "Alterar" se a pasta estiver incorreta
4. **Escolha o Idioma**: Clique em "🌐 Idioma" para trocar

### Fazendo Backup

⚠️ **IMPORTANTE**: Faça backup **APENAS** quando:
- Estiver em uma loja (ponto seguro)
- Ao iniciar um novo mapa/área
- **NUNCA** durante combate ou transições

**Passos**:
1. Selecione a pasta de save na lista esquerda
2. Clique em "💾 Fazer Backup"
3. Aguarde a confirmação de sucesso
4. Verifique na lista direita (backup aparecerá)

### Editando Saves

**Passos**:
1. **FAÇA BACKUP PRIMEIRO** (muito importante!)
2. Selecione a pasta de save
3. Clique em "✏️ Editar Save"
4. Escolha o arquivo .es3 (se houver múltiplos)
5. Edite os dados nas abas:
   - **Mundo**: Para configurações gerais
   - **Jogadores**: Para estatísticas individuais
   - **JSON**: Para edição avançada
6. Clique em "Salvar Alterações"
7. Confirme a operação

### Restaurando Backup

**Passos**:
1. Selecione o backup na lista direita
2. Clique em "🔄 Restaurar Backup"
3. **LEIA O AVISO**: A pasta original será substituída
4. Confirme se tem certeza
5. Aguarde a conclusão

### Excluindo Backup

**Passos**:
1. Selecione o backup na lista direita
2. Clique em "🗑️ Excluir Backup"
3. **ATENÇÃO**: Ação irreversível
4. Confirme a exclusão

---

## 🔧 Solução de Problemas

### Problemas Comuns

#### "Pasta de saves não encontrada"
- **Causa**: Pasta padrão não existe ou está em local diferente
- **Solução**: Use "Alterar" para selecionar a pasta correta
- **Localização Padrão**: `C:\Users\[USUÁRIO]\AppData\LocalLow\semiwork\Repo\saves`

#### "Nenhum arquivo .es3 encontrado"
- **Causa**: Pasta selecionada não contém saves válidos
- **Solução**: Verifique se selecionou a pasta correta do save
- **Dica**: Procure por arquivos com extensão `.es3`

#### "Erro ao abrir editor"
- **Causa**: Arquivo de save corrompido ou dependência faltando
- **Solução**: 
  1. Verifique se `pycryptodome` está instalado
  2. Tente com outro arquivo de save
  3. Execute `pip install pycryptodome`

#### "Erro de criptografia"
- **Causa**: Arquivo não é um save válido do R.E.P.O
- **Solução**: Certifique-se de que está editando um arquivo .es3 original do jogo

#### Interface não aparece
- **Causa**: Problema com Tkinter
- **Solução**: 
  - **Windows**: Reinstale Python com "tcl/tk and IDLE" marcado
  - **Linux**: `sudo apt install python3-tk`
  - **macOS**: Use Python do python.org

### Logs e Depuração

- **Mensagens de Erro**: Aparecem em pop-ups informativos
- **Status Bar**: Mostra o status atual na parte inferior
- **Console**: Execute via terminal para ver logs detalhados

---

## ❓ Perguntas Frequentes

### Sobre Backup

**P: Com que frequência devo fazer backup?**
R: Recomendamos fazer backup sempre que chegar em uma loja ou iniciar um novo mapa. Evite fazer durante combate.

**P: Quantos backups posso ter?**
R: Não há limite. O programa cria backups "atuais" (substituem o anterior) e "históricos" (com timestamp).

**P: Os backups ocupam muito espaço?**
R: Não, saves do R.E.P.O são pequenos (alguns KB cada).

### Sobre Edição

**P: É seguro editar saves?**
R: Sim, desde que faça backup antes. O programa inclui validação para prevenir corrupção.

**P: Posso quebrar meu save editando?**
R: Improvável com a validação automática, mas sempre faça backup antes de editar.

**P: Que valores são seguros para editar?**
R: O programa impõe limites seguros automaticamente. Evite valores extremamente altos.

### Sobre Compatibilidade

**P: Funciona com todas as versões do R.E.P.O?**
R: Testado com versões recentes. Se houver problemas, reporte para atualizarmos.

**P: Funciona no Linux/Mac?**
R: Sim, mas você precisará executar manualmente com Python.

**P: Preciso do jogo instalado?**
R: Não, apenas acesso à pasta de saves.

### Sobre Idiomas

**P: Como adicionar um novo idioma?**
R: Edite o arquivo `translations.json` seguindo o padrão existente.

**P: As traduções estão incorretas**
R: Reporte erros para corrigirmos nas próximas versões.

---

## 🆘 Suporte e Contato

### Reportar Problemas

Se encontrar bugs ou problemas:

1. **Descreva o Problema**: O que estava fazendo quando ocorreu
2. **Inclua Detalhes**: Sistema operacional, versão do Python
3. **Passos para Reproduzir**: Como fazer o erro acontecer novamente
4. **Mensagens de Erro**: Copie exatamente as mensagens que apareceram

### Recursos Adicionais

- **Repositório Original**: [R.E.P.O-Save-Editor](https://github.com/seregonwar/R.E.P.O-Save-Editor)
- **Documentação Python**: [python.org](https://www.python.org/)
- **Tkinter Tutorial**: Para quem quer entender a interface

---

## 📝 Notas de Versão

### Versão Aprimorada (Atual)
- ✅ Editor de saves integrado
- ✅ Suporte a arquivos .es3
- ✅ Interface com abas
- ✅ Validação de dados
- ✅ Criptografia/descriptografia
- ✅ Traduções atualizadas

### Versões Anteriores
- Backup e restauração básicos
- Interface multilíngue
- Tema moderno

---

## ⚖️ Licença e Créditos

- **Programa Base**: Desenvolvido para gerenciamento de saves
- **Editor Core**: Baseado no [R.E.P.O-Save-Editor](https://github.com/seregonwar/R.E.P.O-Save-Editor)
- **Criptografia**: Utiliza pycryptodome
- **Interface**: Tkinter (Python padrão)

---

**🎮 Divirta-se jogando R.E.P.O com segurança e controle total sobre seus saves!**

