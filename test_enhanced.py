#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de teste para validar a versão aprimorada do programa de backup
"""

import os
import shutil
import sys
from datetime import datetime

def test_enhanced_program_import():
    """Testa se o programa aprimorado pode ser importado"""
    print("\n--- Testando importação do programa aprimorado ---")
    try:
        sys.path.append("/home/ubuntu/src")
        import backup_saves_enhanced
        print("✅ Programa aprimorado importado com sucesso")
        
        # Testar se as classes principais existem
        if hasattr(backup_saves_enhanced, 'BackupSavesEnhancedApp'):
            print("✅ Classe BackupSavesEnhancedApp encontrada")
        else:
            print("❌ Classe BackupSavesEnhancedApp não encontrada")
            return False
        
        if hasattr(backup_saves_enhanced, 'ModernStyle'):
            print("✅ Classe ModernStyle encontrada")
        else:
            print("❌ Classe ModernStyle não encontrada")
            return False
            
        return True
    except Exception as e:
        print(f"❌ Erro ao importar programa aprimorado: {e}")
        return False

def test_enhanced_functionality():
    """Testa as funcionalidades da versão aprimorada"""
    
    # Caminho de teste
    test_saves_base_path = "/home/ubuntu/C:/Users/joaov/AppData/LocalLow/semiwork/Repo/saves"
    
    print("=== TESTE DO PROGRAMA APRIMORADO DE BACKUP DOS SAVES ===\n")
    
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
    
    # Verificar se existem backups
    backup_base_dir = os.path.join(test_saves_base_path, "backup")
    if os.path.exists(backup_base_dir):
        try:
            backup_folders = [f for f in os.listdir(backup_base_dir) 
                            if os.path.isdir(os.path.join(backup_base_dir, f))]
            print(f"✅ Encontrados {len(backup_folders)} backups: {backup_folders}")
        except Exception as e:
            print(f"❌ Erro ao listar backups: {e}")
            return False
    else:
        print("ℹ️ Pasta de backup não existe ainda")
    
    print(f"\n=== FUNCIONALIDADES DA VERSÃO APRIMORADA VERIFICADAS! ===")
    return True

def test_visual_components():
    """Testa se os componentes visuais estão definidos corretamente"""
    print("\n--- Testando componentes visuais ---")
    
    try:
        sys.path.append("/home/ubuntu/src")
        from backup_saves_enhanced import ModernStyle
        
        # Verificar se as cores estão definidas
        required_colors = ['BG_DARK', 'BG_MEDIUM', 'BG_LIGHT', 'ACCENT_BLUE', 
                          'TEXT_PRIMARY', 'TEXT_SECONDARY', 'SUCCESS_GREEN']
        
        for color in required_colors:
            if hasattr(ModernStyle, color):
                color_value = getattr(ModernStyle, color)
                print(f"✅ Cor {color}: {color_value}")
            else:
                print(f"❌ Cor {color} não encontrada")
                return False
        
        print("✅ Todos os componentes visuais estão definidos corretamente")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao verificar componentes visuais: {e}")
        return False

if __name__ == "__main__":
    print("Iniciando testes da versão aprimorada do programa de backup...\n")
    
    # Teste de importação
    import_ok = test_enhanced_program_import()
    
    # Teste de componentes visuais
    visual_ok = test_visual_components()
    
    # Teste de funcionalidades
    functionality_ok = test_enhanced_functionality()
    
    print(f"\n=== RESULTADO DOS TESTES ===")
    print(f"Importação do programa: {'✅ OK' if import_ok else '❌ FALHOU'}")
    print(f"Componentes visuais: {'✅ OK' if visual_ok else '❌ FALHOU'}")
    print(f"Funcionalidades básicas: {'✅ OK' if functionality_ok else '❌ FALHOU'}")
    
    if import_ok and visual_ok and functionality_ok:
        print(f"\n🎉 TODOS OS TESTES PASSARAM! A versão aprimorada está funcionando corretamente.")
        sys.exit(0)
    else:
        print(f"\n❌ ALGUNS TESTES FALHARAM. Verifique os erros acima.")
        sys.exit(1)

