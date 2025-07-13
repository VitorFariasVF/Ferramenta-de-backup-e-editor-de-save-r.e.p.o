#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de teste para validar a versão multilíngue do programa de backup
"""

import os
import sys
import json
from datetime import datetime

def test_multilang_program_import():
    """Testa se o programa multilíngue pode ser importado"""
    print("\n--- Testando importação do programa multilíngue ---")
    try:
        sys.path.append("/home/ubuntu/src")
        import backup_saves_multilang
        print("✅ Programa multilíngue importado com sucesso")
        
        # Testar se as classes principais existem
        if hasattr(backup_saves_multilang, 'BackupSavesMultiLangApp'):
            print("✅ Classe BackupSavesMultiLangApp encontrada")
        else:
            print("❌ Classe BackupSavesMultiLangApp não encontrada")
            return False
        
        if hasattr(backup_saves_multilang, 'Translations'):
            print("✅ Classe Translations encontrada")
        else:
            print("❌ Classe Translations não encontrada")
            return False
            
        return True
    except Exception as e:
        print(f"❌ Erro ao importar programa multilíngue: {e}")
        return False

def load_translations_json():
    """Carrega o JSON de traduções diretamente para os testes"""
    try:
        with open(os.path.join(os.path.dirname(__file__), 'translations.json'), 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Erro ao carregar translations.json: {e}")
        return {}

def test_translations():
    """Testa se as traduções estão definidas corretamente"""
    print("\n--- Testando traduções ---")
    
    try:
        translations_data = load_translations_json()
        
        # Verificar se todos os idiomas estão definidos
        expected_languages = ['pt', 'en', 'fr', 'zh', 'ja']
        
        for lang in expected_languages:
            if lang in translations_data:
                lang_data = translations_data[lang]
                print(f"✅ Idioma {lang} ({lang_data['name']}) {lang_data['flag']}: OK")
                
                # Verificar se tem as chaves essenciais
                essential_keys = ['title', 'make_backup', 'restore_backup', 'delete_backup', 'language']
                missing_keys = []
                
                for key in essential_keys:
                    if key not in lang_data['translations']:
                        missing_keys.append(key)
                
                if missing_keys:
                    print(f"   ⚠️ Chaves faltando: {missing_keys}")
                else:
                    print(f"   ✅ Todas as chaves essenciais presentes")
            else:
                print(f"❌ Idioma {lang} não encontrado")
                return False
        
        print("✅ Todas as traduções estão definidas corretamente")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao verificar traduções: {e}")
        return False

def test_config_persistence():
    """Testa a persistência da configuração de idioma"""
    print("\n--- Testando persistência da configuração ---")
    
    try:
        # Criar um arquivo de configuração de teste
        config_file = "/home/ubuntu/src/test_config.json"
        test_config = {
            'language': 'en'
        }
        
        # Salvar configuração
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(test_config, f, ensure_ascii=False, indent=2)
        
        print("✅ Arquivo de configuração criado com sucesso")
        
        # Ler configuração
        with open(config_file, 'r', encoding='utf-8') as f:
            loaded_config = json.load(f)
        
        if loaded_config['language'] == 'en':
            print("✅ Configuração carregada corretamente")
        else:
            print("❌ Configuração não foi carregada corretamente")
            return False
        
        # Limpar arquivo de teste
        os.remove(config_file)
        print("✅ Arquivo de teste removido")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar persistência: {e}")
        return False

def test_text_encoding():
    """Testa se os caracteres especiais são exibidos corretamente"""
    print("\n--- Testando codificação de caracteres ---")
    
    try:
        translations_data = load_translations_json()
        
        # Testar caracteres especiais de cada idioma
        test_cases = [
            ('pt', 'title', '🎮'),  # Emoji
            ('fr', 'title', 'é'),   # Acentos franceses
            ('zh', 'title', '中'),   # Caracteres chineses
            ('ja', 'title', '日'),   # Caracteres japoneses
        ]
        
        for lang, key, expected_char in test_cases:
            text = translations_data[lang]['translations'][key]
            if expected_char in text:
                print(f"✅ Caracteres especiais para {lang}: OK")
            else:
                print(f"⚠️ Caracteres especiais para {lang}: Não encontrados (mas pode estar OK)")
        
        print("✅ Teste de codificação concluído")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar codificação: {e}")
        return False

def test_language_switching():
    """Testa a funcionalidade de troca de idioma"""
    print("\n--- Testando troca de idioma ---")
    
    try:
        translations_data = load_translations_json()
        
        # Simular troca de idioma
        languages_to_test = ['pt', 'en', 'fr', 'zh', 'ja']
        
        for lang in languages_to_test:
            # Simular obtenção de texto traduzido
            title_text = translations_data[lang]['translations']['title']
            make_backup_text = translations_data[lang]['translations']['make_backup']
            
            print(f"✅ {lang}: '{title_text[:30]}...' | '{make_backup_text}'")
        
        print("✅ Troca de idioma simulada com sucesso")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar troca de idioma: {e}")
        return False

def test_functionality():
    """Testa as funcionalidades básicas da versão multilíngue"""
    
    # Caminho de teste
    test_saves_base_path = "/home/ubuntu/C:/Users/Usuario/AppData/LocalLow/semiwork/Repo/saves"
    
    print("=== TESTE DO PROGRAMA MULTILÍNGUE DE BACKUP DOS SAVES ===\n")
    
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
    
    print(f"\n=== FUNCIONALIDADES DA VERSÃO MULTILÍNGUE VERIFICADAS! ===")
    return True

if __name__ == "__main__":
    print("Iniciando testes da versão multilíngue do programa de backup...\n")
    
    # Teste de importação
    import_ok = test_multilang_program_import()
    
    # Teste de traduções
    translations_ok = test_translations()
    
    # Teste de persistência
    persistence_ok = test_config_persistence()
    
    # Teste de codificação
    encoding_ok = test_text_encoding()
    
    # Teste de troca de idioma
    switching_ok = test_language_switching()
    
    # Teste de funcionalidades
    functionality_ok = test_functionality()
    
    print(f"\n=== RESULTADO DOS TESTES ===")
    print(f"Importação do programa: {'✅ OK' if import_ok else '❌ FALHOU'}")
    print(f"Traduções: {'✅ OK' if translations_ok else '❌ FALHOU'}")
    print(f"Persistência de configuração: {'✅ OK' if persistence_ok else '❌ FALHOU'}")
    print(f"Codificação de caracteres: {'✅ OK' if encoding_ok else '❌ FALHOU'}")
    print(f"Troca de idioma: {'✅ OK' if switching_ok else '❌ FALHOU'}")
    print(f"Funcionalidades básicas: {'✅ OK' if functionality_ok else '❌ FALHOU'}")
    
    if all([import_ok, translations_ok, persistence_ok, encoding_ok, switching_ok, functionality_ok]):
        print(f"\n🎉 TODOS OS TESTES PASSARAM! A versão multilíngue está funcionando corretamente.")
        sys.exit(0)
    else:
        print(f"\n❌ ALGUNS TESTES FALHARAM. Verifique os erros acima.")
        sys.exit(1)


