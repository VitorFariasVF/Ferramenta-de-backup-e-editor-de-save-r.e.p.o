#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programa de Backup dos Saves do Jogo Repo
Permite fazer backup e restaurar saves do jogo Repo
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import shutil
from datetime import datetime
import platform

class BackupSavesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Backup dos Saves - Jogo Repo")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Caminho padrão dos saves (Windows)
        if platform.system() == "Windows":
            self.saves_base_path = r"C:\Users\joaov\AppData\LocalLow\semiwork\Repo\saves"
        else:
            # Para teste no Linux, usar um caminho local
            self.saves_base_path = "/home/ubuntu/C:/Users/joaov/AppData/LocalLow/semiwork/Repo/saves"
        
        self.setup_ui()
        self.refresh_saves_list()
    
    def setup_ui(self):
        """Configura a interface gráfica"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar redimensionamento
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Título
        title_label = ttk.Label(main_frame, text="Gerenciador de Backup - Saves do Jogo Repo", 
                               font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Caminho dos saves
        path_frame = ttk.Frame(main_frame)
        path_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        path_frame.columnconfigure(1, weight=1)
        
        ttk.Label(path_frame, text="Pasta Base dos Saves:").grid(row=0, column=0, sticky=tk.W)
        self.path_var = tk.StringVar(value=self.saves_base_path)
        path_entry = ttk.Entry(path_frame, textvariable=self.path_var, state="readonly")
        path_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 5))
        
        ttk.Button(path_frame, text="Alterar", command=self.change_path).grid(row=0, column=2)
        ttk.Button(path_frame, text="Atualizar", command=self.refresh_saves_list).grid(row=0, column=3, padx=(5, 0))
        
        # Lista de saves
        list_frame = ttk.LabelFrame(main_frame, text="Pastas de Save", padding="5")
        list_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        # Treeview para lista de saves
        columns = ("Nome", "Data Modificação", "Tem Backup")
        self.saves_tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=10)
        
        # Configurar colunas
        self.saves_tree.heading("Nome", text="Nome da Pasta")
        self.saves_tree.heading("Data Modificação", text="Data Modificação")
        self.saves_tree.heading("Tem Backup", text="Tem Backup")
        
        self.saves_tree.column("Nome", width=250)
        self.saves_tree.column("Data Modificação", width=150)
        self.saves_tree.column("Tem Backup", width=80)
        
        # Scrollbar para a lista
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.saves_tree.yview)
        self.saves_tree.configure(yscrollcommand=scrollbar.set)
        
        self.saves_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Botões de ação
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=3, column=0, columnspan=3, pady=(10, 0))
        
        ttk.Button(buttons_frame, text="Fazer Backup", command=self.make_backup, 
                  style="Accent.TButton").pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(buttons_frame, text="Restaurar Backup", command=self.restore_backup).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(buttons_frame, text="Ver Backups", command=self.view_backups).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(buttons_frame, text="Sair", command=self.root.quit).pack(side=tk.RIGHT)
        
        # Status bar
        self.status_var = tk.StringVar(value="Pronto")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
    
    def change_path(self):
        """Permite alterar o caminho base dos saves"""
        new_path = filedialog.askdirectory(title="Selecionar pasta base dos saves", initialdir=self.saves_base_path)
        if new_path:
            self.saves_base_path = new_path
            self.path_var.set(new_path)
            self.refresh_saves_list()
    
    def refresh_saves_list(self):
        """Atualiza a lista de pastas de saves"""
        # Limpar lista atual
        for item in self.saves_tree.get_children():
            self.saves_tree.delete(item)
        
        if not os.path.exists(self.saves_base_path):
            self.status_var.set(f"Pasta base não encontrada: {self.saves_base_path}")
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
                has_backup = "Sim" if os.path.exists(backup_path) else "Não"
                
                self.saves_tree.insert("", tk.END, values=(foldername, mod_time, has_backup))
            
            self.status_var.set(f"Encontradas {len(save_folders)} pastas de save")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao listar pastas de saves: {str(e)}")
            self.status_var.set("Erro ao listar pastas de saves")
    
    def get_selected_save_folder(self):
        """Obtém o nome da pasta de save selecionada"""
        selection = self.saves_tree.selection()
        if not selection:
            messagebox.showwarning("Aviso", "Por favor, selecione uma pasta de save.")
            return None
        
        item = self.saves_tree.item(selection[0])
        return item["values"][0]  # Nome da pasta
    
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
                shutil.rmtree(simple_backup_path) # Remover a versão anterior
            shutil.copytree(source_folder_path, simple_backup_path)
            
            messagebox.showinfo("Sucesso", f"Backup da pasta '{foldername}' criado com sucesso!\n\nBackup salvo em: {backup_dest_folder_name}")
            self.status_var.set(f"Backup criado: {foldername}")
            self.refresh_saves_list()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar backup da pasta '{foldername}': {str(e)}")
            self.status_var.set("Erro ao criar backup")
    
    def restore_backup(self):
        """Restaura um backup de pasta"""
        foldername = self.get_selected_save_folder()
        if not foldername:
            return
        
        backup_base_dir = os.path.join(self.saves_base_path, "backup")
        if not os.path.exists(backup_base_dir):
            messagebox.showwarning("Aviso", "Pasta de backup não encontrada.")
            return
        
        # Verificar se existe backup simples para esta pasta
        simple_backup_source_path = os.path.join(backup_base_dir, foldername)
        if not os.path.exists(simple_backup_source_path):
            messagebox.showwarning("Aviso", f"Backup não encontrado para a pasta: {foldername}")
            return
        
        # Confirmar restauração
        result = messagebox.askyesno("Confirmar Restauração", 
                                   f"Tem certeza que deseja restaurar o backup da pasta '{foldername}'?\n\n"
                                   "A pasta atual será sobrescrita/removida!")
        
        if not result:
            return
        
        try:
            # Caminho de destino original
            dest_folder_path = os.path.join(self.saves_base_path, foldername)
            
            # Remover a pasta original se existir para evitar erros de cópia
            if os.path.exists(dest_folder_path):
                shutil.rmtree(dest_folder_path)
                
            # Restaurar backup
            shutil.copytree(simple_backup_source_path, dest_folder_path)
            
            messagebox.showinfo("Sucesso", f"Backup da pasta '{foldername}' restaurado com sucesso!")
            self.status_var.set(f"Backup restaurado: {foldername}")
            self.refresh_saves_list()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao restaurar backup da pasta '{foldername}': {str(e)}")
            self.status_var.set("Erro ao restaurar backup")
    
    def view_backups(self):
        """Abre uma janela para visualizar todos os backups"""
        backup_base_dir = os.path.join(self.saves_base_path, "backup")
        if not os.path.exists(backup_base_dir):
            messagebox.showinfo("Informação", "Pasta de backup não encontrada.")
            return
        
        # Criar janela de backups
        backup_window = tk.Toplevel(self.root)
        backup_window.title("Visualizar Backups")
        backup_window.geometry("500x400")
        
        # Frame principal
        frame = ttk.Frame(backup_window, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Lista de backups
        ttk.Label(frame, text="Pastas de Backup:", font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=(0, 10))
        
        # Listbox com scrollbar
        listbox_frame = ttk.Frame(frame)
        listbox_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        backup_listbox = tk.Listbox(listbox_frame)
        backup_scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=backup_listbox.yview)
        backup_listbox.configure(yscrollcommand=backup_scrollbar.set)
        
        backup_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        backup_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listar pastas de backup
        try:
            backup_folders = [f for f in os.listdir(backup_base_dir) if os.path.isdir(os.path.join(backup_base_dir, f))]
            for foldername in sorted(backup_folders):
                folderpath = os.path.join(backup_base_dir, foldername)
                stat = os.stat(folderpath)
                mod_time = datetime.fromtimestamp(stat.st_mtime).strftime("%d/%m/%Y %H:%M")
                backup_listbox.insert(tk.END, f"{foldername} (Criado em: {mod_time})")
        except Exception as e:
            backup_listbox.insert(tk.END, f"Erro ao listar backups: {str(e)}")
        
        # Botão para fechar
        ttk.Button(frame, text="Fechar", command=backup_window.destroy).pack(pady=(10, 0))

def main():
    """Função principal"""
    root = tk.Tk()
    app = BackupSavesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

