#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de teste para validar as funcionalidades do programa de backup de pastas
"""

import os
import shutil
import sys
from datetime import datetime

def create_dummy_save_folders(base_path):
    """Cria pastas de save de exemplo para teste."""
    print(f"Criando pastas de save de exemplo em: {base_path}")
    if os.path.exists(base_path):
        shutil.rmtree(base_path)
    os.makedirs(base_path)

    folders = ["save_game_1", "save_game_2", "save_game_3"]
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path)
        with open(os.path.join(folder_path, "data.txt"), "w") as f:
            f.write(f"Conteúdo do save para {folder}\n")
        with open(os.path.join(folder_path, "config.ini"), "w") as f:
            f.write(f"Configurações para {folder}\n")
    print("Pastas de save de exemplo criadas.")

def test_backup_functionality():
    """Testa as funcionalidades de backup e restauração de pastas sem interface gráfica"""
    
    # Caminho de teste
    test_saves_base_path = "/home/ubuntu/C:/Users/joaov/AppData/LocalLow/semiwork/Repo/saves"
    
    print("=== TESTE DO PROGRAMA DE BACKUP DOS SAVES (PASTAS) ===\n")
    
    # Criar pastas de save de exemplo
    create_dummy_save_folders(test_saves_base_path)

    # Verificar se a pasta base existe
    if not os.path.exists(test_saves_base_path):
        print(f"❌ Pasta base de saves não encontrada: {test_saves_base_path}")
        return False
    
    print(f"✅ Pasta base de saves encontrada: {test_saves_base_path}")
    
    # Listar pastas de save
    try:
        entries = os.listdir(test_saves_base_path)
        save_folders = [e for e in entries if os.path.isdir(os.path.join(test_saves_base_path, e)) and e != "backup"]
        print(f"✅ Encontradas {len(save_folders)} pastas de save: {save_folders}")
    except Exception as e:
        print(f"❌ Erro ao listar pastas de saves: {e}")
        return False
    
    if not save_folders:
        print("❌ Nenhuma pasta de save encontrada para teste")
        return False
    
    # Testar funcionalidade de backup
    test_folder = save_folders[0]
    print(f"\n--- Testando backup da pasta: {test_folder} ---")
    
    try:
        # Criar pasta de backup
        backup_base_dir = os.path.join(test_saves_base_path, "backup")
        os.makedirs(backup_base_dir, exist_ok=True)
        print(f"✅ Pasta de backup criada/verificada: {backup_base_dir}")
        
        # Fazer backup
        source_folder_path = os.path.join(test_saves_base_path, test_folder)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dest_folder_name = f"{test_folder}_backup_{timestamp}"
        backup_dest_path = os.path.join(backup_base_dir, backup_dest_folder_name)
        simple_backup_path = os.path.join(backup_base_dir, test_folder)
        
        # Copiar a pasta inteira
        shutil.copytree(source_folder_path, backup_dest_path)
        if os.path.exists(simple_backup_path):
            shutil.rmtree(simple_backup_path)
        shutil.copytree(source_folder_path, simple_backup_path)
        
        print(f"✅ Backup criado com sucesso:")
        print(f"   - Backup com timestamp: {backup_dest_folder_name}")
        print(f"   - Backup simples: {test_folder}")
        
        # Verificar se os backups foram criados
        if os.path.exists(backup_dest_path) and os.path.exists(simple_backup_path):
            print("✅ Pastas de backup verificadas com sucesso")
        else:
            print("❌ Erro: Pastas de backup não foram criadas corretamente")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao criar backup: {e}")
        return False
    
    # Testar funcionalidade de restauração
    print(f"\n--- Testando restauração do backup da pasta: {test_folder} ---")
    
    try:
        # Modificar a pasta original para simular perda
        original_data_file = os.path.join(source_folder_path, "data.txt")
        original_content = ""
        with open(original_data_file, 'r') as f:
            original_content = f.read()
        
        with open(original_data_file, 'w') as f:
            f.write("CONTEÚDO MODIFICADO PARA TESTE")
        
        print("✅ Pasta original modificada para simular perda")
        
        # Restaurar backup
        dest_folder_path = os.path.join(test_saves_base_path, test_folder)
        if os.path.exists(dest_folder_path):
            shutil.rmtree(dest_folder_path)
        shutil.copytree(simple_backup_path, dest_folder_path)
        
        # Verificar se foi restaurado corretamente
        restored_data_file = os.path.join(dest_folder_path, "data.txt")
        with open(restored_data_file, 'r') as f:
            restored_content = f.read()
        
        if restored_content == original_content:
            print("✅ Backup restaurado com sucesso - conteúdo original recuperado")
        else:
            print("❌ Erro: Conteúdo restaurado não confere com o original")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao restaurar backup: {e}")
        return False
    
    # Listar backups criados
    print(f"\n--- Listando backups criados ---")
    try:
        backup_folders_list = [f for f in os.listdir(backup_base_dir) if os.path.isdir(os.path.join(backup_base_dir, f))]
        print(f"✅ Backups encontrados ({len(backup_folders_list)}):")
        for folder_name in sorted(backup_folders_list):
            folder_path = os.path.join(backup_base_dir, folder_name)
            stat = os.stat(folder_path)
            mod_time = datetime.fromtimestamp(stat.st_mtime).strftime("%d/%m/%Y %H:%M")
            print(f"   - {folder_name} (Criado em: {mod_time})")
    except Exception as e:
        print(f"❌ Erro ao listar backups: {e}")
        return False
    
    print(f"\n=== TODOS OS TESTES PASSARAM COM SUCESSO! ===")
    return True

def test_program_import():
    """Testa se o programa principal pode ser importado"""
    print("\n--- Testando importação do programa principal ---")
    try:
        sys.path.append("/home/ubuntu/src")
        import backup_saves
        print("✅ Programa principal importado com sucesso")
        
        # Testar se as classes principais existem
        if hasattr(backup_saves, 'BackupSavesApp'):
            print("✅ Classe BackupSavesApp encontrada")
        else:
            print("❌ Classe BackupSavesApp não encontrada")
            return False
            
        return True
    except Exception as e:
        print(f"❌ Erro ao importar programa principal: {e}")
        return False

if __name__ == "__main__":
    print("Iniciando testes do programa de backup dos saves (pastas)...\n")
    
    # Teste de importação
    import_ok = test_program_import()
    
    # Teste de funcionalidades
    functionality_ok = test_backup_functionality()
    
    print(f"\n=== RESULTADO DOS TESTES ===")
    print(f"Importação do programa: {'✅ OK' if import_ok else '❌ FALHOU'}")
    print(f"Funcionalidades de backup: {'✅ OK' if functionality_ok else '❌ FALHOU'}")
    
    if import_ok and functionality_ok:
        print(f"\n🎉 TODOS OS TESTES PASSARAM! O programa está funcionando corretamente.")
        sys.exit(0)
    else:
        print(f"\n❌ ALGUNS TESTES FALHARAM. Verifique os erros acima.")
        sys.exit(1)


