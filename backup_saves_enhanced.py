#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programa de Backup dos Saves do Jogo Repo - Versão Aprimorada
Permite fazer backup e restaurar saves do jogo Repo com interface moderna
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import shutil
from datetime import datetime
import platform

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

class BackupSavesEnhancedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Backup - Saves do Jogo Repo")
        self.root.geometry("1200x700")
        self.root.resizable(True, True)
        self.root.configure(bg=ModernStyle.BG_DARK)
        
        # Caminho padrão dos saves (Windows)
        if platform.system() == "Windows":
            self.saves_base_path = r"C:\Users\joaov\AppData\LocalLow\semiwork\Repo\saves"
        else:
            # Para teste no Linux, usar um caminho local
            self.saves_base_path = "/home/ubuntu/C:/Users/joaov/AppData/LocalLow/semiwork/Repo/saves"
        
        self.setup_styles()
        self.setup_ui()
        self.refresh_saves_list()
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
        
        # Título principal
        title_label = ttk.Label(main_frame, text="🎮 Gerenciador de Backup - Saves do Jogo Repo", 
                               style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 30))
        
        # Frame para caminho dos saves
        path_frame = ttk.Frame(main_frame, style='Medium.TFrame', padding="15")
        path_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        path_frame.columnconfigure(1, weight=1)
        
        ttk.Label(path_frame, text="📁 Pasta Base dos Saves:", style='Normal.TLabel').grid(row=0, column=0, sticky=tk.W)
        self.path_var = tk.StringVar(value=self.saves_base_path)
        path_entry = ttk.Entry(path_frame, textvariable=self.path_var, state="readonly", 
                              style='Modern.TEntry', font=('Segoe UI', 9))
        path_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 10))
        
        ttk.Button(path_frame, text="Alterar", command=self.change_path, 
                  style='Normal.TButton').grid(row=0, column=2, padx=(5, 0))
        ttk.Button(path_frame, text="🔄 Atualizar", command=self.refresh_all, 
                  style='Normal.TButton').grid(row=0, column=3, padx=(5, 0))
        
        # Frame principal para as duas listas
        content_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        content_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 20))
        content_frame.columnconfigure(0, weight=1)
        content_frame.columnconfigure(1, weight=1)
        content_frame.rowconfigure(0, weight=1)
        
        # Frame esquerdo - Lista de saves
        saves_frame = ttk.LabelFrame(content_frame, text="  📂 Pastas de Save  ", 
                                    style='Medium.TFrame', padding="10")
        saves_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        saves_frame.columnconfigure(0, weight=1)
        saves_frame.rowconfigure(0, weight=1)
        
        # Treeview para lista de saves
        saves_columns = ("Nome", "Data Modificação", "Tem Backup")
        self.saves_tree = ttk.Treeview(saves_frame, columns=saves_columns, show="headings", 
                                      height=15, style='Modern.Treeview')
        
        # Configurar colunas dos saves
        self.saves_tree.heading("Nome", text="Nome da Pasta")
        self.saves_tree.heading("Data Modificação", text="Data Modificação")
        self.saves_tree.heading("Tem Backup", text="Backup")
        
        self.saves_tree.column("Nome", width=200)
        self.saves_tree.column("Data Modificação", width=130)
        self.saves_tree.column("Tem Backup", width=60)
        
        # Scrollbar para saves
        saves_scrollbar = ttk.Scrollbar(saves_frame, orient=tk.VERTICAL, command=self.saves_tree.yview)
        self.saves_tree.configure(yscrollcommand=saves_scrollbar.set)
        
        self.saves_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        saves_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Frame direito - Lista de backups
        backups_frame = ttk.LabelFrame(content_frame, text="  💾 Backups Disponíveis  ", 
                                      style='Medium.TFrame', padding="10")
        backups_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(10, 0))
        backups_frame.columnconfigure(0, weight=1)
        backups_frame.rowconfigure(0, weight=1)
        
        # Treeview para lista de backups
        backups_columns = ("Nome", "Data Criação", "Tipo")
        self.backups_tree = ttk.Treeview(backups_frame, columns=backups_columns, show="headings", 
                                        height=15, style='Modern.Treeview')
        
        # Configurar colunas dos backups
        self.backups_tree.heading("Nome", text="Nome do Backup")
        self.backups_tree.heading("Data Criação", text="Data Criação")
        self.backups_tree.heading("Tipo", text="Tipo")
        
        self.backups_tree.column("Nome", width=200)
        self.backups_tree.column("Data Criação", width=130)
        self.backups_tree.column("Tipo", width=80)
        
        # Scrollbar para backups
        backups_scrollbar = ttk.Scrollbar(backups_frame, orient=tk.VERTICAL, command=self.backups_tree.yview)
        self.backups_tree.configure(yscrollcommand=backups_scrollbar.set)
        
        self.backups_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        backups_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Frame para botões de ação
        buttons_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        buttons_frame.grid(row=3, column=0, columnspan=3, pady=(20, 0))
        
        # Botões principais
        ttk.Button(buttons_frame, text="💾 Fazer Backup", command=self.make_backup, 
                  style="Accent.TButton", width=15).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(buttons_frame, text="🔄 Restaurar Backup", command=self.restore_backup, 
                  style="Normal.TButton", width=15).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(buttons_frame, text="🗑️ Excluir Backup", command=self.delete_backup, 
                  style="Normal.TButton", width=15).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(buttons_frame, text="❌ Sair", command=self.root.quit, 
                  style="Normal.TButton", width=10).pack(side=tk.RIGHT)
        
        # Status bar moderna
        status_frame = ttk.Frame(main_frame, style='Medium.TFrame', padding="10")
        status_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(20, 0))
        
        self.status_var = tk.StringVar(value="✅ Pronto para uso")
        status_label = ttk.Label(status_frame, textvariable=self.status_var, 
                                style='Normal.TLabel', font=('Segoe UI', 9))
        status_label.pack(anchor=tk.W)
    
    def change_path(self):
        """Permite alterar o caminho base dos saves"""
        new_path = filedialog.askdirectory(title="Selecionar pasta base dos saves", 
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
            self.status_var.set(f"❌ Pasta base não encontrada: {self.saves_base_path}")
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
            
            self.status_var.set(f"📂 Encontradas {len(save_folders)} pastas de save")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao listar pastas de saves: {str(e)}")
            self.status_var.set("❌ Erro ao listar pastas de saves")
    
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
                    backup_type = "🕒 Histórico"
                else:
                    backup_type = "⚡ Atual"
                
                self.backups_tree.insert("", tk.END, values=(foldername, mod_time, backup_type))
                
        except Exception as e:
            self.status_var.set(f"❌ Erro ao listar backups: {str(e)}")
    
    def get_selected_save_folder(self):
        """Obtém o nome da pasta de save selecionada"""
        selection = self.saves_tree.selection()
        if not selection:
            messagebox.showwarning("Aviso", "Por favor, selecione uma pasta de save.")
            return None
        
        item = self.saves_tree.item(selection[0])
        return item["values"][0]  # Nome da pasta
    
    def get_selected_backup_folder(self):
        """Obtém o nome da pasta de backup selecionada"""
        selection = self.backups_tree.selection()
        if not selection:
            messagebox.showwarning("Aviso", "Por favor, selecione um backup.")
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
            
            messagebox.showinfo("Sucesso", f"✅ Backup da pasta '{foldername}' criado com sucesso!\n\n📁 Backup salvo em: {backup_dest_folder_name}")
            self.status_var.set(f"✅ Backup criado: {foldername}")
            self.refresh_all()
            
        except Exception as e:
            messagebox.showerror("Erro", f"❌ Erro ao criar backup da pasta '{foldername}': {str(e)}")
            self.status_var.set("❌ Erro ao criar backup")
    
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
            messagebox.showwarning("Aviso", f"❌ Backup não encontrado: {backup_foldername}")
            return
        
        # Confirmar restauração
        result = messagebox.askyesno("Confirmar Restauração", 
                                   f"🔄 Tem certeza que deseja restaurar o backup:\n'{backup_foldername}'?\n\n"
                                   f"A pasta '{original_name}' será sobrescrita/removida!")
        
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
            
            messagebox.showinfo("Sucesso", f"✅ Backup '{backup_foldername}' restaurado com sucesso!\n\n📁 Restaurado para: {original_name}")
            self.status_var.set(f"✅ Backup restaurado: {original_name}")
            self.refresh_all()
            
        except Exception as e:
            messagebox.showerror("Erro", f"❌ Erro ao restaurar backup '{backup_foldername}': {str(e)}")
            self.status_var.set("❌ Erro ao restaurar backup")
    
    def delete_backup(self):
        """Exclui um backup selecionado"""
        backup_foldername = self.get_selected_backup_folder()
        if not backup_foldername:
            return
        
        # Confirmar exclusão
        result = messagebox.askyesno("Confirmar Exclusão", 
                                   f"🗑️ Tem certeza que deseja excluir o backup:\n'{backup_foldername}'?\n\n"
                                   "Esta ação não pode ser desfeita!")
        
        if not result:
            return
        
        try:
            backup_base_dir = os.path.join(self.saves_base_path, "backup")
            backup_path = os.path.join(backup_base_dir, backup_foldername)
            
            if os.path.exists(backup_path):
                shutil.rmtree(backup_path)
                messagebox.showinfo("Sucesso", f"✅ Backup '{backup_foldername}' excluído com sucesso!")
                self.status_var.set(f"✅ Backup excluído: {backup_foldername}")
                self.refresh_backups_list()
            else:
                messagebox.showwarning("Aviso", f"❌ Backup não encontrado: {backup_foldername}")
                
        except Exception as e:
            messagebox.showerror("Erro", f"❌ Erro ao excluir backup '{backup_foldername}': {str(e)}")
            self.status_var.set("❌ Erro ao excluir backup")

def main():
    """Função principal"""
    root = tk.Tk()
    app = BackupSavesEnhancedApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

