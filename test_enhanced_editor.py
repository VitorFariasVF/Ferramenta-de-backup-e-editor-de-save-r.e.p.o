#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de teste para a versão aprimorada do programa de backup com editor de saves
"""

import os
import json
import tempfile
from save_editor_core import SaveEditorCore

def test_save_editor_core():
    """Testa as funcionalidades do SaveEditorCore"""
    print("🧪 Testando SaveEditorCore...")
    
    # Criar dados de teste
    test_data = {
        "playerNames": {"value": {"player1": "TestPlayer"}},
        "dictionaryOfDictionaries": {
            "value": {
                "playerHealth": {"player1": 100},
                "playerUpgradeHealth": {"player1": 5},
                "playerUpgradeStamina": {"player1": 3},
                "playerUpgradeExtraJump": {"player1": 1},
                "playerUpgradeLaunch": {"player1": 2},
                "playerUpgradeMapPlayerCount": {"player1": 1},
                "playerUpgradeSpeed": {"player1": 4},
                "playerUpgradeStrength": {"player1": 3},
                "playerUpgradeRange": {"player1": 2},
                "playerUpgradeThrow": {"player1": 1},
                "runStats": {
                    "level": 5,
                    "currency": 1000,
                    "lives": 3,
                    "chargingStationCharge": 100,
                    "totalHaul": 500
                }
            }
        },
        "teamName": {"value": "TestTeam"}
    }
    
    # Criar arquivo temporário
    with tempfile.NamedTemporaryFile(mode='w', suffix='.es3', delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Instanciar o editor
        editor = SaveEditorCore()
        
        # Teste 1: Criptografar dados
        print("  ✓ Testando criptografia...")
        json_str = json.dumps(test_data)
        success = editor.encrypt_es3(json_str.encode('utf-8'), temp_path)
        assert success, "Falha na criptografia"
        print("    ✅ Criptografia funcionando")
        
        # Teste 2: Descriptografar dados
        print("  ✓ Testando descriptografia...")
        success, message = editor.open_save_file(temp_path)
        assert success, f"Falha na descriptografia: {message}"
        print("    ✅ Descriptografia funcionando")
        
        # Teste 3: Obter dados dos jogadores
        print("  ✓ Testando obtenção de dados dos jogadores...")
        players = editor.get_player_data()
        assert len(players) == 1, "Número incorreto de jogadores"
        assert players[0]["name"] == "TestPlayer", "Nome do jogador incorreto"
        assert players[0]["health"] == 100, "Vida do jogador incorreta"
        print("    ✅ Dados dos jogadores obtidos corretamente")
        
        # Teste 4: Obter dados do mundo
        print("  ✓ Testando obtenção de dados do mundo...")
        world_data = editor.get_world_data()
        assert world_data["level"] == 5, "Nível incorreto"
        assert world_data["currency"] == 1000, "Moeda incorreta"
        assert world_data["team_name"] == "TestTeam", "Nome da equipe incorreto"
        print("    ✅ Dados do mundo obtidos corretamente")
        
        # Teste 5: Atualizar dados do jogador
        print("  ✓ Testando atualização de dados do jogador...")
        new_upgrades = {
            "health": 10,
            "stamina": 8,
            "extra_jump": 3,
            "launch": 5,
            "map_player_count": 2,
            "speed": 7,
            "strength": 6,
            "range": 4,
            "throw": 3
        }
        success = editor.update_player_data("player1", 150, new_upgrades)
        assert success, "Falha na atualização dos dados do jogador"
        
        # Verificar se os dados foram atualizados
        players = editor.get_player_data()
        assert players[0]["health"] == 150, "Vida do jogador não foi atualizada"
        assert players[0]["upgrades"]["health"] == 10, "Upgrade de vida não foi atualizado"
        print("    ✅ Dados do jogador atualizados corretamente")
        
        # Teste 6: Atualizar dados do mundo
        print("  ✓ Testando atualização de dados do mundo...")
        new_world_data = {
            "level": 10,
            "currency": 2000,
            "lives": 5,
            "charging_station": 200,
            "total_haul": 1000,
            "team_name": "NewTestTeam"
        }
        success = editor.update_world_data(new_world_data)
        assert success, "Falha na atualização dos dados do mundo"
        
        # Verificar se os dados foram atualizados
        world_data = editor.get_world_data()
        assert world_data["level"] == 10, "Nível não foi atualizado"
        assert world_data["currency"] == 2000, "Moeda não foi atualizada"
        assert world_data["team_name"] == "NewTestTeam", "Nome da equipe não foi atualizado"
        print("    ✅ Dados do mundo atualizados corretamente")
        
        # Teste 7: Salvar arquivo
        print("  ✓ Testando salvamento de arquivo...")
        success, message = editor.save_file(temp_path)
        assert success, f"Falha no salvamento: {message}"
        print("    ✅ Arquivo salvo corretamente")
        
        # Teste 8: Validação de dados
        print("  ✓ Testando validação de dados...")
        
        # Validação de dados do jogador
        valid, message = editor.validate_player_data("player1", 150, new_upgrades)
        assert valid, f"Validação de dados do jogador falhou: {message}"
        
        # Validação de dados inválidos do jogador
        valid, message = editor.validate_player_data("player1", -10, new_upgrades)
        assert not valid, "Validação deveria ter falhado para vida negativa"
        
        # Validação de dados do mundo
        valid, message = editor.validate_world_data(new_world_data)
        assert valid, f"Validação de dados do mundo falhou: {message}"
        
        # Validação de dados inválidos do mundo
        invalid_world_data = new_world_data.copy()
        invalid_world_data["level"] = -1
        valid, message = editor.validate_world_data(invalid_world_data)
        assert not valid, "Validação deveria ter falhado para nível negativo"
        
        print("    ✅ Validação de dados funcionando corretamente")
        
        print("✅ Todos os testes do SaveEditorCore passaram!")
        return True
        
    except Exception as e:
        print(f"❌ Erro durante os testes: {str(e)}")
        return False
        
    finally:
        # Limpar arquivo temporário
        if os.path.exists(temp_path):
            os.unlink(temp_path)

def test_translations():
    """Testa se as traduções foram carregadas corretamente"""
    print("🧪 Testando traduções...")
    
    try:
        translations_file = os.path.join(os.path.dirname(__file__), 'translations.json')
        
        if not os.path.exists(translations_file):
            print(f"❌ Arquivo de traduções não encontrado: {translations_file}")
            return False
            
        with open(translations_file, 'r', encoding='utf-8') as f:
            translations = json.load(f)
            
        # Verificar se todos os idiomas estão presentes
        expected_languages = ["pt", "en", "fr", "zh", "ja"]
        for lang in expected_languages:
            assert lang in translations, f"Idioma {lang} não encontrado"
            
        # Verificar se as novas chaves do editor estão presentes
        editor_keys = [
            "edit_save", "save_editor_title", "world_data", "players_data",
            "raw_json", "save_changes", "cancel", "team_name", "level",
            "currency", "lives", "health", "stamina"
        ]
        
        for lang in expected_languages:
            for key in editor_keys:
                assert key in translations[lang], f"Chave {key} não encontrada no idioma {lang}"
                
        print("✅ Todas as traduções estão corretas!")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar traduções: {str(e)}")
        return False

def main():
    """Função principal de teste"""
    print("🚀 Iniciando testes da versão aprimorada com editor...")
    print("=" * 60)
    
    # Teste 1: SaveEditorCore
    test1_passed = test_save_editor_core()
    print()
    
    # Teste 2: Traduções
    test2_passed = test_translations()
    print()
    
    # Resumo dos testes
    print("=" * 60)
    print("📊 RESUMO DOS TESTES:")
    print(f"  SaveEditorCore: {'✅ PASSOU' if test1_passed else '❌ FALHOU'}")
    print(f"  Traduções: {'✅ PASSOU' if test2_passed else '❌ FALHOU'}")
    
    if test1_passed and test2_passed:
        print("\n🎉 TODOS OS TESTES PASSARAM! A versão aprimorada está funcionando corretamente.")
        return True
    else:
        print("\n❌ ALGUNS TESTES FALHARAM. Verifique os erros acima.")
        return False

if __name__ == "__main__":
    main()

