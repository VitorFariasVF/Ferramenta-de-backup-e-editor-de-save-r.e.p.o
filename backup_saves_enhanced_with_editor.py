#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BackupSavesEnhancedApp - Enhanced Backup Tool for Repo Game Saves with Editor
This application provides a modern graphical interface for backing up, restoring, and editing save files for the game Repo. It supports multiple languages and integrates advanced save editing features.
Main Features:
- Backup and restore save folders, including historical backups with timestamps.
- Edit save files (.es3) using a built-in editor with world and player data tabs, and raw JSON editing.
- Multi-language support with translations loaded from a JSON file.
- Modern dark-themed UI using Tkinter.
- Configuration management for language and save folder paths.
- Status bar and user-friendly dialogs for warnings, errors, and confirmations.
Classes:
- Translations: Loads and manages language translations from a JSON file.
- ModernStyle: Defines color constants for the application's dark theme.
- SaveEditorWindow: Provides a window for editing save files, including world and player data.
- BackupSavesEnhancedApp: Main application class for backup, restore, and save editing operations.
Usage:
Run the script to launch the GUI. Select a save folder to backup, restore, or edit. Change language and save folder path as needed.
Note:
Requires the save_editor_core module and translation/config JSON files in the same directory.

Programa de Backup dos Saves do Jogo Repo - Versão Aprimorada com Editor
Permite fazer backup, restaurar e EDITAR saves do jogo Repo com interface moderna e suporte a múltiplos idiomas
Integra funcionalidades do R.E.P.O-Save-Editor
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import shutil
import json
from datetime import datetime
import platform
from save_editor_core import SaveEditorCore
import sys

def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller.
    For .bat execution with flat structure, it should just return the relative_path.
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Not running as a PyInstaller bundle, assume flat structure for .bat
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Translations:
    """Classe para gerenciar as traduções do programa, carregando de um arquivo JSON"""
    def __init__(self, json_file):
        self.json_file = json_file
        self.LANGUAGES = self._load_translations()

    def _load_translations(self):
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            messagebox.showerror("Erro", f"Arquivo de tradução não encontrado: {self.json_file}. Verifique se o arquivo está na mesma pasta do executável.")
            return {}
        except json.JSONDecodeError:
            messagebox.showerror("Erro", f"Erro ao decodificar JSON no arquivo: {self.json_file}. Verifique a sintaxe do JSON.")
            return {}

class ModernStyle:
    """Classe para definir o estilo moderno da aplicação"""
    
    # Cores do tema escuro moderno
    BG_DARK = "#1a1a1a"
    BG_MEDIUM = "#2d2d2d"
    BG_LIGHT = "#3d3d3d"
    ACCENT_BLUE = "#0078d4"
    ACCENT_BLUE_HOVER = "#106ebe"
    TEXT_PRIMARY = "#ffffff"
    TEXT_SECONDARY = "#cccccc"
    TEXT_MUTED = "#999999"
    SUCCESS_GREEN = "#107c10"
    WARNING_ORANGE = "#ff8c00"
    ERROR_RED = "#d13438"
    BORDER_COLOR = "#484848"

class SaveEditorWindow:
    """Janela para edição de saves do jogo R.E.P.O"""
    
    def __init__(self, parent, save_file_path, translations, current_language):
        self.parent = parent
        self.save_file_path = save_file_path
        self.translations = translations
        self.current_language = current_language
        self.save_editor = SaveEditorCore()
        
        # Criar janela
        self.window = tk.Toplevel(parent)
        self.window.title(self.get_text("save_editor_title"))
        self.window.geometry("800x600")
        self.window.minsize(400, 300) # Definindo tamanho mínimo
        self.window.configure(bg=ModernStyle.BG_DARK)
        self.window.resizable(True, True)
        
        # Centralizar janela
        self.center_window()
        
        # Carregar o arquivo de save
        self.load_save_file()
        
        # Criar interface
        self.create_widgets()
        
    def center_window(self):
        """Centraliza a janela na tela"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        
    def get_text(self, key):
        """Obtém texto traduzido"""
        try:
            return self.translations.LANGUAGES[self.current_language][key]
        except KeyError:
            return key
            
    def load_save_file(self):
        """Carrega o arquivo de save"""
        success, message = self.save_editor.open_save_file(self.save_file_path)
        if not success:
            messagebox.showerror(self.get_text("error"), message)
            self.window.destroy()
            return
            
    def create_widgets(self):
        """Cria os widgets da interface"""
        # Frame principal
        main_frame = tk.Frame(self.window, bg=ModernStyle.BG_DARK)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        title_label = tk.Label(
            main_frame,
            text=self.get_text("save_editor_title"),
            font=("Segoe UI", 16, "bold"),
            bg=ModernStyle.BG_DARK,
            fg=ModernStyle.TEXT_PRIMARY
        )
        title_label.pack(pady=(0, 20))
        
        # Notebook para abas
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Configurar estilo do notebook
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background=ModernStyle.BG_MEDIUM)
        style.configure("TNotebook.Tab", background=ModernStyle.BG_LIGHT, foreground=ModernStyle.TEXT_PRIMARY)
        
        # Criar abas
        self.create_world_tab()
        self.create_players_tab()
        self.create_raw_json_tab()
        
        # Frame de botões
        button_frame = tk.Frame(main_frame, bg=ModernStyle.BG_DARK)
        button_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Botão Salvar
        save_btn = tk.Button(
            button_frame,
            text=self.get_text("save_changes"),
            command=self.save_changes,
            bg=ModernStyle.SUCCESS_GREEN,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=8
        )
        save_btn.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Botão Cancelar
        cancel_btn = tk.Button(
            button_frame,
            text=self.get_text("cancel"),
            command=self.window.destroy,
            bg=ModernStyle.BG_LIGHT,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Segoe UI", 10),
            relief=tk.FLAT,
            padx=20,
            pady=8
        )
        cancel_btn.pack(side=tk.RIGHT)
        
    def create_world_tab(self):
        """Cria a aba de dados do mundo"""
        world_frame = tk.Frame(self.notebook, bg=ModernStyle.BG_MEDIUM)
        self.notebook.add(world_frame, text=self.get_text("world_data"))
        
        # Obter dados do mundo
        world_data = self.save_editor.get_world_data()
        
        # Criar campos de entrada
        self.world_entries = {}
        
        # Nome da equipe
        self.create_entry_field(world_frame, "team_name", world_data.get("team_name", ""), 0)
        
        # Nível
        self.create_entry_field(world_frame, "level", world_data.get("level", 1), 1, entry_type="int")
        
        # Moeda
        self.create_entry_field(world_frame, "currency", world_data.get("currency", 0), 2, entry_type="int")
        
        # Vidas
        self.create_entry_field(world_frame, "lives", world_data.get("lives", 3), 3, entry_type="int")
        
        # Estação de carregamento
        self.create_entry_field(world_frame, "charging_station", world_data.get("charging_station", 100), 4, entry_type="int")
        
        # Total de carga
        self.create_entry_field(world_frame, "total_haul", world_data.get("total_haul", 0), 5, entry_type="int")
        
    def create_players_tab(self):
        """Cria a aba de dados dos jogadores"""
        players_frame = tk.Frame(self.notebook, bg=ModernStyle.BG_MEDIUM)
        self.notebook.add(players_frame, text=self.get_text("players_data"))
        
        # Obter dados dos jogadores
        players_data = self.save_editor.get_player_data()
        
        if not players_data:
            no_players_label = tk.Label(
                players_frame,
                text=self.get_text("no_players_found"),
                bg=ModernStyle.BG_MEDIUM,
                fg=ModernStyle.TEXT_MUTED,
                font=("Segoe UI", 12)
            )
            no_players_label.pack(expand=True)
            return
            
        # Criar notebook para jogadores
        players_notebook = ttk.Notebook(players_frame)
        players_notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.player_entries = {}
        
        for player in players_data:
            player_frame = tk.Frame(players_notebook, bg=ModernStyle.BG_LIGHT)
            players_notebook.add(player_frame, text=f"{player["name"]} (ID: {player["id"]})")
            
            self.player_entries[player["id"]] = {}
            
            # Vida do jogador
            self.create_player_entry_field(player_frame, player["id"], "health", player["health"], 0)
            
            # Upgrades
            upgrades = player["upgrades"]
            row = 1
            for upgrade_key, upgrade_value in upgrades.items():
                self.create_player_entry_field(player_frame, player["id"], upgrade_key, upgrade_value, row)
                row += 1
                
    def create_raw_json_tab(self):
        """Cria a aba de edição JSON bruta"""
        json_frame = tk.Frame(self.notebook, bg=ModernStyle.BG_MEDIUM)
        self.notebook.add(json_frame, text=self.get_text("raw_json"))
        
        # Área de texto para JSON
        text_frame = tk.Frame(json_frame, bg=ModernStyle.BG_MEDIUM)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Text widget
        self.json_text = tk.Text(
            text_frame,
            bg=ModernStyle.BG_DARK,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Consolas", 10),
            yscrollcommand=scrollbar.set,
            wrap=tk.WORD
        )
        self.json_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.json_text.yview)
        
        # Inserir JSON atual
        if self.save_editor.is_file_loaded():
            json_str = json.dumps(self.save_editor.json_data, indent=2, ensure_ascii=False)
            self.json_text.insert(tk.END, json_str)
            
    def create_entry_field(self, parent, field_name, value, row, entry_type="str"):
        """Cria um campo de entrada para dados do mundo"""
        # Label
        label = tk.Label(
            parent,
            text=self.get_text(field_name) + ":",
            bg=ModernStyle.BG_MEDIUM,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Segoe UI", 10)
        )
        label.grid(row=row, column=0, sticky="w", padx=10, pady=5)
        
        # Entry
        entry = tk.Entry(
            parent,
            bg=ModernStyle.BG_DARK,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Segoe UI", 10),
            relief=tk.FLAT,
            bd=1
        )
        entry.grid(row=row, column=1, sticky="ew", padx=10, pady=5)
        entry.insert(0, str(value))
        
        # Configurar grid
        parent.grid_columnconfigure(1, weight=1)
        
        self.world_entries[field_name] = {"entry": entry, "type": entry_type}
        
    def create_player_entry_field(self, parent, player_id, field_name, value, row):
        """Cria um campo de entrada para dados do jogador"""
        # Label
        label = tk.Label(
            parent,
            text=self.get_text(field_name) + ":",
            bg=ModernStyle.BG_LIGHT,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Segoe UI", 10)
        )
        label.grid(row=row, column=0, sticky="w", padx=10, pady=5)
        
        # Entry
        entry = tk.Entry(
            parent,
            bg=ModernStyle.BG_DARK,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Segoe UI", 10),
            relief=tk.FLAT,
            bd=1
        )
        entry.grid(row=row, column=1, sticky="ew", padx=10, pady=5)
        
        # Inserir valor, garantindo que seja uma string
        entry.insert(0, str(value))
        
        # Configurar grid
        parent.grid_columnconfigure(1, weight=1)
        
        if player_id not in self.player_entries:
            self.player_entries[player_id] = {}
        self.player_entries[player_id][field_name] = entry
        
    def save_changes(self):
        """Salva as alterações no arquivo"""
        try:
            # Atualizar dados do mundo
            world_data = {}
            for field_name, field_info in self.world_entries.items():
                value = field_info["entry"].get()
                if field_info["type"] == "int":
                    value = int(value)
                world_data[field_name] = value
                
            # Validar e atualizar dados do mundo
            valid, message = self.save_editor.validate_world_data(world_data)
            if not valid:
                messagebox.showerror(self.get_text("error"), message)
                return
                
            self.save_editor.update_world_data(world_data)
            
            # Atualizar dados dos jogadores
            for player_id, player_fields in self.player_entries.items():
                health = int(player_fields["health"].get())
                upgrades = {}
                for field_name, entry in player_fields.items():
                    if field_name != "health":
                        upgrades[field_name] = int(entry.get())
                        
                # Validar e atualizar dados do jogador
                valid, message = self.save_editor.validate_player_data(player_id, health, upgrades)
                if not valid:
                    messagebox.showerror(self.get_text("error"), message)
                    return
                    
                self.save_editor.update_player_data(player_id, health, upgrades)
            
            # Atualizar JSON bruto se foi modificado
            json_content = self.json_text.get("1.0", tk.END).strip()
            if json_content:
                try:
                    new_json_data = json.loads(json_content)
                    self.save_editor.json_data = new_json_data
                except json.JSONDecodeError as e:
                    messagebox.showerror(self.get_text("error"), f"JSON inválido: {str(e)}")
                    return
            
            # Salvar arquivo
            success, message = self.save_editor.save_file(self.save_file_path)
            if success:
                messagebox.showinfo(self.get_text("success"), message)
                self.window.destroy()
            else:
                messagebox.showerror(self.get_text("error"), message)
                
        except ValueError as e:
            messagebox.showerror(self.get_text("error"), f"Valor inválido: {str(e)}")
        except Exception as e:
            messagebox.showerror(self.get_text("error"), f"Erro inesperado: {str(e)}")

class BackupSavesEnhancedApp:
    """Aplicação principal de backup e edição de saves"""
    
    def __init__(self, root):
        self.root = root
        self.current_language = "pt"
        
        # Carregar traduções
        # Caminho ajustado para a estrutura de pasta única
        translations_file = resource_path("translations.json")
        self.translations = Translations(translations_file)
        
        # Configurar janela principal
        self.setup_main_window()
        
        # Configurar pasta padrão dos saves
        self.setup_default_saves_path()
        
        # Carregar configurações
        self.load_config()
        
        # Criar interface
        self.create_widgets()
        
        # Atualizar listas
        self.update_lists()
        
    def setup_main_window(self):
        """Configura a janela principal"""
        self.root.title(self.get_text("app_title"))
        self.root.geometry("1200x700")
        self.root.configure(bg=ModernStyle.BG_DARK)
        self.root.resizable(True, True)
        
        # Centralizar janela
        self.center_window()
        
    def center_window(self):
        """Centraliza a janela na tela"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
    def setup_default_saves_path(self):
        """Configura o caminho padrão dos saves"""
        if platform.system() == "Windows":
            username = os.environ.get("USERNAME", "Usuario")
            self.saves_base_path = f"C:/Users/{username}/AppData/LocalLow/semiwork/Repo/saves"
        else:
            # Para Linux/Mac, usar pasta home do usuário
            home = os.path.expanduser("~")
            self.saves_base_path = os.path.join(home, ".local/share/semiwork/Repo/saves")
            
    def get_text(self, key):
        """Obtém texto traduzido"""
        try:
            return self.translations.LANGUAGES[self.current_language][key]
        except KeyError:
            return key
            
    def load_config(self):
        """Carrega configurações do arquivo config.json"""
        config_file = resource_path("config.json")
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                self.current_language = config.get('language', 'pt')
                self.saves_base_path = config.get('saves_path', self.saves_base_path)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
            
    def save_config(self):
        """Salva configurações no arquivo config.json"""
        config_file = resource_path("config.json")
        config = {
            'language': self.current_language,
            'saves_path': self.saves_base_path
        }
        try:
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar configurações: {e}")
            
    def create_widgets(self):
        """Cria os widgets da interface"""
        # Frame do cabeçalho
        header_frame = tk.Frame(self.root, bg=ModernStyle.BG_DARK, height=60)
        header_frame.pack(fill=tk.X, padx=10, pady=(10, 0))
        header_frame.pack_propagate(False)
        
        # Título
        title_label = tk.Label(
            header_frame,
            text=self.get_text("app_title"),
            font=("Segoe UI", 18, "bold"),
            bg=ModernStyle.BG_DARK,
            fg=ModernStyle.TEXT_PRIMARY
        )
        title_label.pack(side=tk.LEFT, pady=15)
        
        # Botão de idioma
        language_btn = tk.Button(
            header_frame,
            text="🌐 " + self.get_text("language"),
            command=self.show_language_menu,
            bg=ModernStyle.ACCENT_BLUE,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=8
        )
        language_btn.pack(side=tk.RIGHT, pady=15)
        
        # Frame de configuração da pasta
        config_frame = tk.Frame(self.root, bg=ModernStyle.BG_MEDIUM, height=50)
        config_frame.pack(fill=tk.X, padx=10, pady=5)
        config_frame.pack_propagate(False)
        
        # Label da pasta
        folder_label = tk.Label(
            config_frame,
            text="📁 " + self.get_text("saves_folder") + ":",
            font=("Segoe UI", 10, "bold"),
            bg=ModernStyle.BG_MEDIUM,
            fg=ModernStyle.TEXT_PRIMARY
        )
        folder_label.pack(side=tk.LEFT, padx=10, pady=15)
        
        # Entry da pasta
        self.folder_var = tk.StringVar(value=self.saves_base_path)
        folder_entry = tk.Entry(
            config_frame,
            textvariable=self.folder_var,
            font=("Segoe UI", 10),
            bg=ModernStyle.BG_DARK,
            fg=ModernStyle.TEXT_PRIMARY,
            relief=tk.FLAT,
            bd=1
        )
        folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=15)
        
        # Botão Alterar
        change_btn = tk.Button(
            config_frame,
            text=self.get_text("change"),
            command=self.change_folder,
            bg=ModernStyle.BG_LIGHT,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Segoe UI", 9),
            relief=tk.FLAT,
            padx=15,
            pady=5
        )
        change_btn.pack(side=tk.RIGHT, padx=5, pady=15)
        
        # Botão Atualizar
        refresh_btn = tk.Button(
            config_frame,
            text="🔄 " + self.get_text("refresh"),
            command=self.update_lists,
            bg=ModernStyle.BG_LIGHT,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Segoe UI", 9),
            relief=tk.FLAT,
            padx=15,
            pady=5
        )
        refresh_btn.pack(side=tk.RIGHT, padx=5, pady=15)
        
        # Frame principal com duas colunas
        main_frame = tk.Frame(self.root, bg=ModernStyle.BG_DARK)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Coluna esquerda - Saves
        left_frame = tk.Frame(main_frame, bg=ModernStyle.BG_MEDIUM)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # Título da coluna esquerda
        left_title = tk.Label(
            left_frame,
            text="📂 " + self.get_text("save_folders"),
            font=("Segoe UI", 12, "bold"),
            bg=ModernStyle.BG_MEDIUM,
            fg=ModernStyle.TEXT_PRIMARY
        )
        left_title.pack(pady=10)
        
        # Listbox de saves
        saves_frame = tk.Frame(left_frame, bg=ModernStyle.BG_MEDIUM)
        saves_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        saves_scrollbar = tk.Scrollbar(saves_frame)
        saves_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.saves_listbox = tk.Listbox(
            saves_frame,
            bg=ModernStyle.BG_DARK,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Segoe UI", 10),
            selectbackground=ModernStyle.ACCENT_BLUE,
            selectforeground=ModernStyle.TEXT_PRIMARY,
            yscrollcommand=saves_scrollbar.set,
            relief=tk.FLAT,
            bd=1
        )
        self.saves_listbox.pack(fill=tk.BOTH, expand=True)
        saves_scrollbar.config(command=self.saves_listbox.yview)
        
        # Coluna direita - Backups
        right_frame = tk.Frame(main_frame, bg=ModernStyle.BG_MEDIUM)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        # Título da coluna direita
        right_title = tk.Label(
            right_frame,
            text="💾 " + self.get_text("available_backups"),
            font=("Segoe UI", 12, "bold"),
            bg=ModernStyle.BG_MEDIUM,
            fg=ModernStyle.TEXT_PRIMARY
        )
        right_title.pack(pady=10)
        
        # Listbox de backups
        backups_frame = tk.Frame(right_frame, bg=ModernStyle.BG_MEDIUM)
        backups_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        backups_scrollbar = tk.Scrollbar(backups_frame)
        backups_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.backups_listbox = tk.Listbox(
            backups_frame,
            bg=ModernStyle.BG_DARK,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Segoe UI", 10),
            selectbackground=ModernStyle.ACCENT_BLUE,
            selectforeground=ModernStyle.TEXT_PRIMARY,
            yscrollcommand=backups_scrollbar.set,
            relief=tk.FLAT,
            bd=1
        )
        self.backups_listbox.pack(fill=tk.BOTH, expand=True)
        backups_scrollbar.config(command=self.backups_listbox.yview)
        
        # Frame de botões
        button_frame = tk.Frame(self.root, bg=ModernStyle.BG_DARK, height=60)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        button_frame.pack_propagate(False)
        
        # Botão Fazer Backup
        backup_btn = tk.Button(
            button_frame,
            text="💾 " + self.get_text("make_backup"),
            command=self.make_backup,
            bg=ModernStyle.SUCCESS_GREEN,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Segoe UI", 11, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=10
        )
        backup_btn.pack(side=tk.LEFT, padx=5)
        
        # Botão Editar Save
        edit_btn = tk.Button(
            button_frame,
            text="✏️ " + self.get_text("edit_save"),
            command=self.edit_save,
            bg=ModernStyle.WARNING_ORANGE,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Segoe UI", 11, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=10
        )
        edit_btn.pack(side=tk.LEFT, padx=5)
        
        # Botão Restaurar Backup
        restore_btn = tk.Button(
            button_frame,
            text="🔄 " + self.get_text("restore_backup"),
            command=self.restore_backup,
            bg=ModernStyle.ACCENT_BLUE,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Segoe UI", 11, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=10
        )
        restore_btn.pack(side=tk.LEFT, padx=5)
        
        # Botão Excluir Backup
        delete_btn = tk.Button(
            button_frame,
            text="🗑️ " + self.get_text("delete_backup"),
            command=self.delete_backup,
            bg=ModernStyle.ERROR_RED,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Segoe UI", 11, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=10
        )
        delete_btn.pack(side=tk.LEFT, padx=5)
        
        # Botão Sair
        exit_btn = tk.Button(
            button_frame,
            text="❌ " + self.get_text("exit"),
            command=self.root.quit,
            bg=ModernStyle.BG_LIGHT,
            fg=ModernStyle.TEXT_PRIMARY,
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            padx=20,
            pady=10
        )
        exit_btn.pack(side=tk.RIGHT, padx=5)
        
        # Barra de status
        self.status_var = tk.StringVar(value=self.get_text("ready"))
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=("Segoe UI", 9),
            bg=ModernStyle.BG_MEDIUM,
            fg=ModernStyle.TEXT_SECONDARY,
            anchor=tk.W,
            relief=tk.FLAT,
            bd=1
        )
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)
        
    def show_language_menu(self):
        """Mostra o menu de seleção de idioma"""
        language_window = tk.Toplevel(self.root)
        language_window.title(self.get_text("select_language"))
        language_window.geometry("300x250")
        language_window.configure(bg=ModernStyle.BG_DARK)
        language_window.resizable(False, False)
        
        # Centralizar janela
        language_window.transient(self.root)
        language_window.grab_set()
        
        # Título
        title_label = tk.Label(
            language_window,
            text=self.get_text("select_language"),
            font=("Segoe UI", 14, "bold"),
            bg=ModernStyle.BG_DARK,
            fg=ModernStyle.TEXT_PRIMARY
        )
        title_label.pack(pady=20)
        
        # Botões de idioma
        languages = [
            ("pt", "🇧🇷 Português"),
            ("en", "🇺🇸 English"),
            ("fr", "🇫🇷 Français"),
            ("zh", "🇨🇳 中文"),
            ("ja", "🇯🇵 日本語"),
            ("es", "🇪🇸 Español"),
            ("de", "🇩🇪 Deutsch")
        ]
        
        for lang_code, lang_name in languages:
            btn = tk.Button(
                language_window,
                text=lang_name,
                command=lambda lc=lang_code: self.change_language(lc, language_window),
                bg=ModernStyle.ACCENT_BLUE if lang_code == self.current_language else ModernStyle.BG_LIGHT,
                fg=ModernStyle.TEXT_PRIMARY,
                font=("Segoe UI", 11),
                relief=tk.FLAT,
                padx=20,
                pady=8,
                width=20
            )
            btn.pack(pady=5)
            
    def change_language(self, language_code, window):
        """Altera o idioma da aplicação"""
        self.current_language = language_code
        self.save_config()
        window.destroy()
        
        # Recriar a interface com o novo idioma
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_widgets()
        self.update_lists()
        
    def change_folder(self):
        """Altera a pasta base dos saves"""
        folder = filedialog.askdirectory(
            title=self.get_text("select_saves_folder"),
            initialdir=self.saves_base_path
        )
        if folder:
            self.saves_base_path = folder
            self.folder_var.set(folder)
            self.save_config()
            self.update_lists()
            
    def update_lists(self):
        """Atualiza as listas de saves e backups"""
        # Limpar listas
        self.saves_listbox.delete(0, tk.END)
        self.backups_listbox.delete(0, tk.END)
        
        # Verificar se a pasta existe
        if not os.path.exists(self.saves_base_path):
            self.status_var.set(self.get_text("folder_not_found"))
            return
            
        # Listar pastas de save
        try:
            for item in os.listdir(self.saves_base_path):
                item_path = os.path.join(self.saves_base_path, item)
                if os.path.isdir(item_path) and item != "backup":
                    # Verificar se tem backup
                    backup_path = os.path.join(self.saves_base_path, "backup", item)
                    has_backup = "✅" if os.path.exists(backup_path) else "❌"
                    
                    # Obter data de modificação
                    mod_time = os.path.getmtime(item_path)
                    mod_date = datetime.fromtimestamp(mod_time).strftime("%d/%m %H:%M")
                    
                    display_text = f"{has_backup} {item} | {mod_date}"
                    self.saves_listbox.insert(tk.END, display_text)
                    
        except PermissionError:
            self.status_var.set(self.get_text("permission_denied"))
            return
            
        # Listar backups
        backup_folder = os.path.join(self.saves_base_path, "backup")
        if os.path.exists(backup_folder):
            try:
                for item in os.listdir(backup_folder):
                    item_path = os.path.join(backup_folder, item)
                    if os.path.isdir(item_path):
                        # Obter data de criação
                        create_time = os.path.getctime(item_path)
                        create_date = datetime.fromtimestamp(create_time).strftime("%d/%m %H:%M")
                        
                        # Determinar tipo de backup
                        if "_backup_" in item:
                            backup_type = "🕒 " + self.get_text("historical")
                        else:
                            backup_type = "⚡ " + self.get_text("current")
                            
                        display_text = f"{backup_type} {item} | {create_date}"
                        self.backups_listbox.insert(tk.END, display_text)
                        
            except PermissionError:
                pass
                
        self.status_var.set(self.get_text("ready"))
        
    def make_backup(self):
        """Faz backup da pasta selecionada"""
        selection = self.saves_listbox.curselection()
        if not selection:
            messagebox.showwarning(self.get_text("warning"), self.get_text("select_save_folder"))
            return
            
        # Obter nome da pasta selecionada
        selected_text = self.saves_listbox.get(selection[0])
        folder_name = selected_text.split(" | ")[0][2:].strip()  # Remove emoji e espaços
        
        source_path = os.path.join(self.saves_base_path, folder_name)
        backup_base_path = os.path.join(self.saves_base_path, "backup")
        
        # Criar pasta de backup se não existir
        os.makedirs(backup_base_path, exist_ok=True)
        
        try:
            # Backup atual (substitui o anterior)
            current_backup_path = os.path.join(backup_base_path, folder_name)
            if os.path.exists(current_backup_path):
                shutil.rmtree(current_backup_path)
            shutil.copytree(source_path, current_backup_path)
            
            # Backup histórico (com timestamp)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            historical_backup_path = os.path.join(backup_base_path, f"{folder_name}_backup_{timestamp}")
            shutil.copytree(source_path, historical_backup_path)
            
            self.status_var.set(self.get_text("backup_success"))
            self.update_lists()
            messagebox.showinfo(self.get_text("success"), self.get_text("backup_created"))
            
        except Exception as e:
            error_msg = f"{self.get_text("backup_error")}: {str(e)}"
            self.status_var.set(error_msg)
            messagebox.showerror(self.get_text("error"), error_msg)
            
    def edit_save(self):
        """Abre o editor de saves para a pasta selecionada"""
        selection = self.saves_listbox.curselection()
        if not selection:
            messagebox.showwarning(self.get_text("warning"), self.get_text("select_save_folder"))
            return
            
        # Obter nome da pasta selecionada
        selected_text = self.saves_listbox.get(selection[0])
        folder_name = selected_text.split(" | ")[0][2:].strip()  # Remove emoji e espaços
        
        save_folder_path = os.path.join(self.saves_base_path, folder_name)
        
        # Procurar por arquivos .es3 na pasta
        es3_files = []
        try:
            for file in os.listdir(save_folder_path):
                if file.endswith(".es3"):
                    es3_files.append(os.path.join(save_folder_path, file))
        except Exception as e:
            messagebox.showerror(self.get_text("error"), f"Erro ao acessar pasta: {str(e)}")
            return
            
        if not es3_files:
            messagebox.showwarning(self.get_text("warning"), self.get_text("no_es3_files"))
            return
            
        # Se há apenas um arquivo, abrir diretamente
        if len(es3_files) == 1:
            save_file_path = es3_files[0]
        else:
            # Se há múltiplos arquivos, deixar o usuário escolher
            file_names = [os.path.basename(f) for f in es3_files]
            choice_window = tk.Toplevel(self.root)
            choice_window.title(self.get_text("select_save_file"))
            choice_window.geometry("640x480")
            choice_window.minsize(640, 480) # Definindo tamanho mínimo
            choice_window.configure(bg=ModernStyle.BG_DARK)
            choice_window.transient(self.root)
            choice_window.grab_set()
            
            tk.Label(
                choice_window,
                text=self.get_text("select_save_file"),
                font=("Segoe UI", 12, "bold"),
                bg=ModernStyle.BG_DARK,
                fg=ModernStyle.TEXT_PRIMARY
            ).pack(pady=20)
            
            listbox = tk.Listbox(
                choice_window,
                bg=ModernStyle.BG_MEDIUM,
                fg=ModernStyle.TEXT_PRIMARY,
                font=("Segoe UI", 10),
                selectbackground=ModernStyle.ACCENT_BLUE,
                selectforeground=ModernStyle.TEXT_PRIMARY,
                relief=tk.FLAT,
                bd=1
            )
            listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
            
            for file_name in file_names:
                listbox.insert(tk.END, file_name)
                
            selected_file = [None]
            
            def on_select():
                selection = listbox.curselection()
                if selection:
                    selected_file[0] = es3_files[selection[0]]
                    choice_window.destroy()
                else:
                    # Se nada for selecionado, fechar a janela sem selecionar arquivo
                    choice_window.destroy()
                    
            tk.Button(
                choice_window,
                text=self.get_text("select"),
                command=on_select,
                bg=ModernStyle.ACCENT_BLUE,
                fg=ModernStyle.TEXT_PRIMARY,
                font=("Segoe UI", 10, "bold"),
                relief=tk.FLAT,
                padx=20,
                pady=8
            ).pack(pady=10)
            
            choice_window.wait_window()
            
            if not selected_file[0]:
                return
                
            save_file_path = selected_file[0]
        
        # Abrir editor de saves
        try:
            SaveEditorWindow(self.root, save_file_path, self.translations, self.current_language)
        except Exception as e:
            messagebox.showerror(self.get_text("error"), f"Erro ao abrir editor: {str(e)}")
            
import os
import shutil
import re

class BackupSavesEnhancedApp(BackupSavesEnhancedApp):
    def extract_backup_name(self, selected_text):
        """Extrai o nome real da pasta de backup a partir do texto da listbox"""
        parts = selected_text.split(' | ')
        if not parts:
            return None

        name_with_type = parts[0].strip()

        historical_prefix = f"🕒 {self.get_text('historical')}"
        current_prefix = f"⚡ {self.get_text('current')}"

        if name_with_type.startswith(historical_prefix):
            return name_with_type[len(historical_prefix):].strip()
        elif name_with_type.startswith(current_prefix):
            return name_with_type[len(current_prefix):].strip()

        # Fallback: tenta extrair após o primeiro espaço
        tokens = name_with_type.split(" ", 1)
        return tokens[1].strip() if len(tokens) > 1 else tokens[0]

    def restore_backup(self):
        """Restaura o backup selecionado"""
        selection = self.backups_listbox.curselection()
        if not selection:
            messagebox.showwarning(self.get_text("warning"), self.get_text("select_backup"))
            return

        selected_text = self.backups_listbox.get(selection[0])
        actual_backup_name = self.extract_backup_name(selected_text)

        if not actual_backup_name:
            messagebox.showerror(self.get_text("error"), self.get_text("invalid_backup_selection"))
            return

        backup_path = os.path.join(self.saves_base_path, "backup", actual_backup_name)

        if not messagebox.askyesno(
            self.get_text("confirm_restore_title"),
            f"{self.get_text('confirm_restore_message')} \n{self.get_text('warning_overwrite')}"
        ):
            return

        try:
            original_save_folder_name = actual_backup_name.split("_backup_")[0] if "_backup_" in actual_backup_name else actual_backup_name
            original_save_path = os.path.join(self.saves_base_path, original_save_folder_name)

            if os.path.exists(original_save_path):
                shutil.rmtree(original_save_path)

            shutil.copytree(backup_path, original_save_path)

            self.status_var.set(self.get_text("restore_success"))
            self.update_lists()
            messagebox.showinfo(self.get_text("success"), self.get_text("backup_restored"))

        except FileNotFoundError:
            error_msg = f"{self.get_text('restore_error')}: {self.get_text('backup_not_found')}: {backup_path}"
            self.status_var.set(error_msg)
            messagebox.showerror(self.get_text("error"), error_msg)
        except Exception as e:
            error_msg = f"{self.get_text('restore_error')}: {str(e)}"
            self.status_var.set(error_msg)
            messagebox.showerror(self.get_text("error"), error_msg)

    def delete_backup(self):
        """Exclui o backup selecionado"""
        selection = self.backups_listbox.curselection()
        if not selection:
            messagebox.showwarning(self.get_text("warning"), self.get_text("select_backup"))
            return

        selected_text = self.backups_listbox.get(selection[0])
        actual_backup_name = self.extract_backup_name(selected_text)

        if not actual_backup_name:
            messagebox.showerror(self.get_text("error"), self.get_text("invalid_backup_selection"))
            return

        backup_path = os.path.join(self.saves_base_path, "backup", actual_backup_name)

        if not messagebox.askyesno(
            self.get_text("confirm_delete_title"),
            f"{self.get_text('confirm_delete_message')} \n{actual_backup_name}"
        ):
            return

        try:
            if os.path.exists(backup_path):
                shutil.rmtree(backup_path)
                self.status_var.set(self.get_text("delete_success"))
                self.update_lists()
                messagebox.showinfo(self.get_text("success"), self.get_text("backup_deleted"))
            else:
                error_msg = f"{self.get_text('delete_error')}: {self.get_text('backup_not_found')}: {backup_path}"
                self.status_var.set(error_msg)
                messagebox.showerror(self.get_text("error"), error_msg)
        except Exception as e:
            error_msg = f"{self.get_text('delete_error')}: {str(e)}"
            self.status_var.set(error_msg)
            messagebox.showerror(self.get_text("error"), error_msg)


if __name__ == "__main__":
    root = tk.Tk()
    app = BackupSavesEnhancedApp(root)
    root.mainloop()
