#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programa de Backup dos Saves do Jogo Repo - Versão Multilíngue
Permite fazer backup e restaurar saves do jogo Repo com interface moderna e suporte a múltiplos idiomas
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os # Garante que 'os' esteja sempre importado e acessível
import shutil
import json
from datetime import datetime
import platform

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
            messagebox.showerror("Erro", f"Arquivo de tradução não encontrado: {self.json_file}")
            return {}
        except json.JSONDecodeError:
            messagebox.showerror("Erro", f"Erro ao decodificar JSON no arquivo: {self.json_file}")
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

class BackupSavesMultiLangApp:
    def __init__(self, root):
        self.root = root
        
        # Inicializa a classe de traduções
        self.translations_obj = Translations(os.path.join(os.path.dirname(__file__), 'translations.json'))
        self.current_language = 'pt'  # Idioma padrão
        self.config_file = os.path.join(os.path.dirname(__file__), 'config.json')
        
        # Carregar configurações salvas
        self.load_config()
        
        self.root.title(self.get_text('title'))
        self.root.geometry("1200x750")
        self.root.resizable(True, True)
        self.root.configure(bg=ModernStyle.BG_DARK)
        
        # Caminho padrão dos saves (Windows)
        if platform.system() == "Windows":
            username = os.getenv('USERNAME', 'Usuario')
            self.saves_base_path = rf"C:\Users\{username}\AppData\LocalLow\semiwork\Repo\saves"
        else:
            # Para teste no Linux, usar um caminho local
            self.saves_base_path = "/home/ubuntu/C:/Users/Usuario/AppData/LocalLow/semiwork/Repo/saves"
        
        self.setup_styles()
        self.setup_ui()
        self.refresh_saves_list()
        self.refresh_backups_list()
    
    def get_text(self, key, **kwargs):
        """Obtém o texto traduzido para o idioma atual"""
        text = self.translations_obj.LANGUAGES[self.current_language]['translations'].get(key, key)
        if kwargs:
            return text.format(**kwargs)
        return text
    
    def load_config(self):
        """Carrega as configurações salvas"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    self.current_language = config.get('language', 'pt')
        except Exception:
            self.current_language = 'pt'
    
    def save_config(self):
        """Salva as configurações"""
        try:
            config = {
                'language': self.current_language
            }
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
        except Exception:
            pass
    
    def change_language(self, new_language):
        """Muda o idioma da interface"""
        self.current_language = new_language
        self.save_config()
        self.update_ui_texts()
    
    def update_ui_texts(self):
        """Atualiza todos os textos da interface"""
        # Atualizar título da janela
        self.root.title(self.get_text('title'))
        
        # Atualizar labels
        self.title_label.config(text=self.get_text('title'))
        self.path_label.config(text=self.get_text('folder_path'))
        self.change_button.config(text=self.get_text('change'))
        self.update_button.config(text=self.get_text('update'))
        
        # Atualizar frames
        self.saves_frame.config(text=self.get_text('saves_list'))
        self.backups_frame.config(text=self.get_text('backups_list'))
        
        # Atualizar cabeçalhos das colunas
        self.saves_tree.heading("Nome", text=self.get_text('folder_name'))
        self.saves_tree.heading("Data Modificação", text=self.get_text('modified_date'))
        self.saves_tree.heading("Tem Backup", text=self.get_text('backup_status'))
        
        self.backups_tree.heading("Nome", text=self.get_text('backup_name'))
        self.backups_tree.heading("Data Criação", text=self.get_text('creation_date'))
        self.backups_tree.heading("Tipo", text=self.get_text('type'))
        
        # Atualizar botões
        self.make_backup_button.config(text=self.get_text('make_backup'))
        self.restore_backup_button.config(text=self.get_text('restore_backup'))
        self.delete_backup_button.config(text=self.get_text('delete_backup'))
        self.exit_button.config(text=self.get_text('exit'))
        self.language_button.config(text=self.get_text('language'))
        
        # Atualizar status
        self.status_var.set(self.get_text('ready'))
        
        # Atualizar listas para aplicar novos tipos
        self.refresh_backups_list()
    
    def setup_styles(self):
        """Configura os estilos personalizados"""
        style = ttk.Style()
        
        # Configurar tema
        style.theme_use('clam')
        
        # Estilo para frames
        style.configure('Dark.TFrame', 
                       background=ModernStyle.BG_DARK,
                       borderwidth=0)
        
        style.configure('Medium.TFrame', 
                       background=ModernStyle.BG_MEDIUM,
                       borderwidth=1,
                       relief='solid')
        
        # Estilo para labels
        style.configure('Title.TLabel',
                       background=ModernStyle.BG_DARK,
                       foreground=ModernStyle.TEXT_PRIMARY,
                       font=('Segoe UI', 16, 'bold'))
        
        style.configure('Subtitle.TLabel',
                       background=ModernStyle.BG_MEDIUM,
                       foreground=ModernStyle.TEXT_SECONDARY,
                       font=('Segoe UI', 10, 'bold'))
        
        style.configure('Normal.TLabel',
                       background=ModernStyle.BG_DARK,
                       foreground=ModernStyle.TEXT_SECONDARY,
                       font=('Segoe UI', 9))
        
        # Estilo para botões
        style.configure('Accent.TButton',
                       background=ModernStyle.ACCENT_BLUE,
                       foreground=ModernStyle.TEXT_PRIMARY,
                       font=('Segoe UI', 9, 'bold'),
                       borderwidth=0,
                       focuscolor='none')
        
        style.map('Accent.TButton',
                 background=[('active', ModernStyle.ACCENT_BLUE_HOVER)])
        
        style.configure('Normal.TButton',
                       background=ModernStyle.BG_LIGHT,
                       foreground=ModernStyle.TEXT_SECONDARY,
                       font=('Segoe UI', 9),
                       borderwidth=1,
                       focuscolor='none')
        
        # Estilo para Treeview
        style.configure('Modern.Treeview',
                       background=ModernStyle.BG_MEDIUM,
                       foreground=ModernStyle.TEXT_SECONDARY,
                       fieldbackground=ModernStyle.BG_MEDIUM,
                       borderwidth=0,
                       font=('Segoe UI', 9))
        
        style.configure('Modern.Treeview.Heading',
                       background=ModernStyle.BG_LIGHT,
                       foreground=ModernStyle.TEXT_PRIMARY,
                       font=('Segoe UI', 9, 'bold'),
                       borderwidth=1,
                       relief='solid')
        
        # Estilo para Entry
        style.configure('Modern.TEntry',
                       fieldbackground=ModernStyle.BG_MEDIUM,
                       foreground=ModernStyle.TEXT_SECONDARY,
                       borderwidth=1,
                       insertcolor=ModernStyle.TEXT_PRIMARY)
    
    def setup_ui(self):
        """Configura a interface gráfica moderna"""
        # Frame principal
        main_frame = ttk.Frame(self.root, style='Dark.TFrame', padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar redimensionamento
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Frame do cabeçalho
        header_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        header_frame.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 30))
        header_frame.columnconfigure(0, weight=1)
        
        # Título principal
        self.title_label = ttk.Label(header_frame, text=self.get_text('title'), 
                                    style='Title.TLabel')
        self.title_label.grid(row=0, column=0, sticky=tk.W)
        
        # Botão de idioma
        self.language_button = ttk.Button(header_frame, text=self.get_text('language'), 
                                         command=self.show_language_menu, style='Normal.TButton')
        self.language_button.grid(row=0, column=1, sticky=tk.E)
        
        # Frame para caminho dos saves
        path_frame = ttk.Frame(main_frame, style='Medium.TFrame', padding="15")
        path_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        path_frame.columnconfigure(1, weight=1)
        
        self.path_label = ttk.Label(path_frame, text=self.get_text('folder_path'), style='Normal.TLabel')
        self.path_label.grid(row=0, column=0, sticky=tk.W)
        
        self.path_var = tk.StringVar(value=self.saves_base_path)
        path_entry = ttk.Entry(path_frame, textvariable=self.path_var, state="readonly", 
                              style='Modern.TEntry', font=('Segoe UI', 9))
        path_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 10))
        
        self.change_button = ttk.Button(path_frame, text=self.get_text('change'), 
                                       command=self.change_path, style='Normal.TButton')
        self.change_button.grid(row=0, column=2, padx=(5, 0))
        
        self.update_button = ttk.Button(path_frame, text=self.get_text('update'), 
                                       command=self.refresh_all, style='Normal.TButton')
        self.update_button.grid(row=0, column=3, padx=(5, 0))
        
        # Frame principal para as duas listas
        content_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        content_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 20))
        content_frame.columnconfigure(0, weight=1)
        content_frame.columnconfigure(1, weight=1)
        content_frame.rowconfigure(0, weight=1)
        
        # Frame esquerdo - Lista de saves
        self.saves_frame = ttk.LabelFrame(content_frame, text=self.get_text('saves_list'), 
                                         style='Medium.TFrame', padding="10")
        self.saves_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        self.saves_frame.columnconfigure(0, weight=1)
        self.saves_frame.rowconfigure(0, weight=1)
        
        # Treeview para lista de saves
        saves_columns = ("Nome", "Data Modificação", "Tem Backup")
        self.saves_tree = ttk.Treeview(self.saves_frame, columns=saves_columns, show="headings", 
                                      height=15, style='Modern.Treeview')
        
        # Configurar colunas dos saves
        self.saves_tree.heading("Nome", text=self.get_text('folder_name'))
        self.saves_tree.heading("Data Modificação", text=self.get_text('modified_date'))
        self.saves_tree.heading("Tem Backup", text=self.get_text('backup_status'))
        
        self.saves_tree.column("Nome", width=200)
        self.saves_tree.column("Data Modificação", width=130)
        self.saves_tree.column("Tem Backup", width=60)
        
        # Scrollbar para saves
        saves_scrollbar = ttk.Scrollbar(self.saves_frame, orient=tk.VERTICAL, command=self.saves_tree.yview)
        self.saves_tree.configure(yscrollcommand=saves_scrollbar.set)
        
        self.saves_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        saves_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Frame direito - Lista de backups
        self.backups_frame = ttk.LabelFrame(content_frame, text=self.get_text('backups_list'), 
                                           style='Medium.TFrame', padding="10")
        self.backups_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(10, 0))
        self.backups_frame.columnconfigure(0, weight=1)
        self.backups_frame.rowconfigure(0, weight=1)
        
        # Treeview para lista de backups
        backups_columns = ("Nome", "Data Criação", "Tipo")
        self.backups_tree = ttk.Treeview(self.backups_frame, columns=backups_columns, show="headings", 
                                        height=15, style='Modern.Treeview')
        
        # Configurar colunas dos backups
        self.backups_tree.heading("Nome", text=self.get_text('backup_name'))
        self.backups_tree.heading("Data Criação", text=self.get_text('creation_date'))
        self.backups_tree.heading("Tipo", text=self.get_text('type'))
        
        self.backups_tree.column("Nome", width=200)
        self.backups_tree.column("Data Criação", width=130)
        self.backups_tree.column("Tipo", width=80)
        
        # Scrollbar para backups
        backups_scrollbar = ttk.Scrollbar(self.backups_frame, orient=tk.VERTICAL, command=self.backups_tree.yview)
        self.backups_tree.configure(yscrollcommand=backups_scrollbar.set)
        
        self.backups_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        backups_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Frame para botões de ação
        buttons_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        buttons_frame.grid(row=3, column=0, columnspan=3, pady=(20, 0))
        
        # Botões principais
        self.make_backup_button = ttk.Button(buttons_frame, text=self.get_text('make_backup'), 
                                            command=self.make_backup, style="Accent.TButton", width=15)
        self.make_backup_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.restore_backup_button = ttk.Button(buttons_frame, text=self.get_text('restore_backup'), 
                                               command=self.restore_backup, style="Normal.TButton", width=15)
        self.restore_backup_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.delete_backup_button = ttk.Button(buttons_frame, text=self.get_text('delete_backup'), 
                                              command=self.delete_backup, style="Normal.TButton", width=15)
        self.delete_backup_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.exit_button = ttk.Button(buttons_frame, text=self.get_text('exit'), 
                                     command=self.root.quit, style="Normal.TButton", width=10)
        self.exit_button.pack(side=tk.RIGHT)
        
        # Status bar moderna
        status_frame = ttk.Frame(main_frame, style='Medium.TFrame', padding="10")
        status_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(20, 0))
        
        self.status_var = tk.StringVar(value=self.get_text('ready'))
        status_label = ttk.Label(status_frame, textvariable=self.status_var, 
                                style='Normal.TLabel', font=('Segoe UI', 9))
        status_label.pack(anchor=tk.W)
    
    def show_language_menu(self):
        """Mostra o menu de seleção de idioma"""
        language_window = tk.Toplevel(self.root)
        language_window.title(self.get_text('language'))
        language_window.geometry("300x400")
        language_window.configure(bg=ModernStyle.BG_DARK)
        language_window.resizable(False, False)
        
        # Centralizar a janela
        language_window.transient(self.root)
        language_window.grab_set()
        
        # Frame principal
        frame = ttk.Frame(language_window, style='Dark.TFrame', padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(frame, text=self.get_text('language'), style='Title.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Botões de idioma
        for lang_code, lang_data in self.translations_obj.LANGUAGES.items():
            button_text = f"{lang_data['flag']} {lang_data['name']}"
            
            # Destacar idioma atual
            if lang_code == self.current_language:
                button_style = "Accent.TButton"
            else:
                button_style = "Normal.TButton"
            
            lang_button = ttk.Button(frame, text=button_text, 
                                    command=lambda lc=lang_code: self.select_language(lc, language_window),
                                    style=button_style, width=20)
            lang_button.pack(pady=5, fill=tk.X)
    
    def select_language(self, language_code, window):
        """Seleciona um idioma e fecha a janela"""
        self.change_language(language_code)
        window.destroy()
    
    def change_path(self):
        """Permite alterar o caminho base dos saves"""
        new_path = filedialog.askdirectory(title=self.get_text('select_folder'), 
                                         initialdir=self.saves_base_path)
        if new_path:
            self.saves_base_path = new_path
            self.path_var.set(new_path)
            self.refresh_all()
    
    def refresh_all(self):
        """Atualiza ambas as listas"""
        self.refresh_saves_list()
        self.refresh_backups_list()
    
    def refresh_saves_list(self):
        """Atualiza a lista de pastas de saves"""
        # Limpar lista atual
        for item in self.saves_tree.get_children():
            self.saves_tree.delete(item)
        
        if not os.path.exists(self.saves_base_path):
            self.status_var.set(f"{self.get_text('folder_not_found')}: {self.saves_base_path}")
            return
        
        try:
            entries = os.listdir(self.saves_base_path)
            save_folders = [e for e in entries if os.path.isdir(os.path.join(self.saves_base_path, e)) and e != "backup"]
            
            for foldername in sorted(save_folders):
                folderpath = os.path.join(self.saves_base_path, foldername)
                
                # Obter informações da pasta
                stat = os.stat(folderpath)
                mod_time = datetime.fromtimestamp(stat.st_mtime).strftime("%d/%m/%Y %H:%M")
                
                # Verificar se tem backup
                backup_path = os.path.join(self.saves_base_path, "backup", foldername)
                has_backup = "✅" if os.path.exists(backup_path) else "❌"
                
                self.saves_tree.insert("", tk.END, values=(foldername, mod_time, has_backup))
            
            self.status_var.set(self.get_text('found_folders', count=len(save_folders)))
            
        except Exception as e:
            messagebox.showerror(self.get_text('error'), f"{self.get_text('error_listing')}: {str(e)}")
            self.status_var.set(self.get_text('error_listing'))
    
    def refresh_backups_list(self):
        """Atualiza a lista de backups"""
        # Limpar lista atual
        for item in self.backups_tree.get_children():
            self.backups_tree.delete(item)
        
        backup_base_dir = os.path.join(self.saves_base_path, "backup")
        if not os.path.exists(backup_base_dir):
            return
        
        try:
            backup_folders = [f for f in os.listdir(backup_base_dir) 
                            if os.path.isdir(os.path.join(backup_base_dir, f))]
            
            for foldername in sorted(backup_folders):
                folderpath = os.path.join(backup_base_dir, foldername)
                stat = os.stat(folderpath)
                mod_time = datetime.fromtimestamp(stat.st_mtime).strftime("%d/%m/%Y %H:%M")
                
                # Determinar tipo de backup
                if "_backup_" in foldername:
                    backup_type = self.get_text('historical_type')
                else:
                    backup_type = self.get_text('current_type')
                
                self.backups_tree.insert("", tk.END, values=(foldername, mod_time, backup_type))
                
        except Exception as e:
            self.status_var.set(f"{self.get_text('error_listing_backups')}: {str(e)}")
    
    def get_selected_save_folder(self):
        """Obtém o nome da pasta de save selecionada"""
        selection = self.saves_tree.selection()
        if not selection:
            messagebox.showwarning(self.get_text('warning'), self.get_text('select_save'))
            return None
        
        item = self.saves_tree.item(selection[0])
        return item["values"][0]  # Nome da pasta
    
    def get_selected_backup_folder(self):
        """Obtém o nome da pasta de backup selecionada"""
        selection = self.backups_tree.selection()
        if not selection:
            messagebox.showwarning(self.get_text('warning'), self.get_text('select_backup'))
            return None
        
        item = self.backups_tree.item(selection[0])
        return item["values"][0]  # Nome da pasta de backup
    
    def make_backup(self):
        """Faz backup da pasta de save selecionada"""
        foldername = self.get_selected_save_folder()
        if not foldername:
            return
        
        try:
            # Caminho da pasta de origem
            source_folder_path = os.path.join(self.saves_base_path, foldername)
            
            # Criar pasta de backup se não existir
            backup_base_dir = os.path.join(self.saves_base_path, "backup")
            os.makedirs(backup_base_dir, exist_ok=True)
            
            # Caminho de destino do backup (com timestamp para múltiplas versões)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_dest_folder_name = f"{foldername}_backup_{timestamp}"
            backup_dest_path = os.path.join(backup_base_dir, backup_dest_folder_name)
            
            # Copiar a pasta inteira
            shutil.copytree(source_folder_path, backup_dest_path)
            
            # Manter uma cópia simples para facilitar a restauração da versão mais recente
            simple_backup_path = os.path.join(backup_base_dir, foldername)
            if os.path.exists(simple_backup_path):
                shutil.rmtree(simple_backup_path)
            shutil.copytree(source_folder_path, simple_backup_path)
            
            messagebox.showinfo(self.get_text('success'), 
                              self.get_text('backup_created', name=foldername, backup_name=backup_dest_folder_name))
            self.status_var.set(self.get_text('backup_created_status', name=foldername))
            self.refresh_all()
            
        except Exception as e:
            messagebox.showerror(self.get_text('error'), 
                               self.get_text('error_creating_backup', name=foldername, error=str(e)))
            self.status_var.set(self.get_text('error_creating_backup_status'))
    
    def restore_backup(self):
        """Restaura um backup de pasta"""
        backup_foldername = self.get_selected_backup_folder()
        if not backup_foldername:
            return
        
        # Determinar o nome original da pasta
        if "_backup_" in backup_foldername:
            original_name = backup_foldername.split("_backup_")[0]
        else:
            original_name = backup_foldername
        
        backup_base_dir = os.path.join(self.saves_base_path, "backup")
        backup_source_path = os.path.join(backup_base_dir, backup_foldername)
        
        if not os.path.exists(backup_source_path):
            messagebox.showwarning(self.get_text('warning'), 
                                 self.get_text('backup_not_found', name=backup_foldername))
            return
        
        # Confirmar restauração
        result = messagebox.askyesno(self.get_text('confirm'), 
                                   self.get_text('confirm_restore', 
                                               backup_name=backup_foldername, 
                                               original_name=original_name))
        
        if not result:
            return
        
        try:
            # Caminho de destino original
            dest_folder_path = os.path.join(self.saves_base_path, original_name)
            
            # Remover a pasta original se existir
            if os.path.exists(dest_folder_path):
                shutil.rmtree(dest_folder_path)
                
            # Restaurar backup
            shutil.copytree(backup_source_path, dest_folder_path)
            
            messagebox.showinfo(self.get_text('success'), 
                              self.get_text('backup_restored', 
                                          backup_name=backup_foldername, 
                                          original_name=original_name))
            self.status_var.set(self.get_text('backup_restored_status', name=original_name))
            self.refresh_all()
            
        except Exception as e:
            messagebox.showerror(self.get_text('error'), 
                               self.get_text('error_restoring_backup', name=backup_foldername, error=str(e)))
            self.status_var.set(self.get_text('error_restoring_backup_status'))
    
    def delete_backup(self):
        """Exclui um backup selecionado"""
        backup_foldername = self.get_selected_backup_folder()
        if not backup_foldername:
            return
        
        # Confirmar exclusão
        result = messagebox.askyesno(self.get_text('confirm_deletion'), 
                                   self.get_text('confirm_delete', name=backup_foldername))
        
        if not result:
            return
        
        try:
            backup_base_dir = os.path.join(self.saves_base_path, "backup")
            backup_path = os.path.join(backup_base_dir, backup_foldername)
            
            if os.path.exists(backup_path):
                shutil.rmtree(backup_path)
                messagebox.showinfo(self.get_text('success'), 
                                  self.get_text('backup_deleted', name=backup_foldername))
                self.status_var.set(self.get_text('backup_deleted_status', name=backup_foldername))
                self.refresh_backups_list()
            else:
                messagebox.showwarning(self.get_text('warning'), 
                                     self.get_text('backup_not_found', name=backup_foldername))
                
        except Exception as e:
            messagebox.showerror(self.get_text('error'), 
                               self.get_text('error_deleting_backup', name=backup_foldername, error=str(e)))
            self.status_var.set(self.get_text('error_deleting_backup_status'))

def main():
    """Função principal"""
    root = tk.Tk()
    app = BackupSavesMultiLangApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()






