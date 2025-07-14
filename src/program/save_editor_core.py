#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo Core do Editor de Saves R.E.P.O
Adaptado do repositório: https://github.com/seregonwar/R.E.P.O-Save-Editor

Este módulo contém as funcionalidades essenciais para:
- Descriptografar arquivos .es3 do jogo R.E.P.O
- Editar dados de jogadores e mundo
- Criptografar e salvar os arquivos modificados
"""

import json
import gzip
import os
from typing import Dict, List, Optional, Tuple
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import HMAC, SHA1


class SaveEditorCore:
    """Classe principal para edição de saves do jogo R.E.P.O"""
    
    def __init__(self):
        self.json_data = None
        self.password = "Why would you want to cheat?... :o It's no fun. :') :'D"
    
    def decrypt_es3(self, file_path: str) -> bytes:
        """
        Descriptografa um arquivo .es3 do jogo R.E.P.O
        
        Args:
            file_path: Caminho para o arquivo .es3
            
        Returns:
            bytes: Dados descriptografados
            
        Raises:
            Exception: Se houver erro na descriptografia
        """
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

        # Extrair o IV (primeiros 16 bytes)
        iv = encrypted_data[:16]
        encrypted_data = encrypted_data[16:]

        # Derivar a chave usando PBKDF2
        key = PBKDF2(self.password, iv, dkLen=16, count=100, 
                     prf=lambda p, s: HMAC.new(p, s, SHA1).digest())

        # Descriptografar os dados usando AES-128-CBC
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        # Verificar se os dados estão comprimidos com GZip
        if decrypted_data[:2] == b'\x1f\x8b':  # Número mágico do GZip
            decrypted_data = gzip.decompress(decrypted_data)

        return decrypted_data
    
    def encrypt_es3(self, data: bytes, output_file: str, should_gzip: bool = False) -> bool:
        """
        Criptografa dados e salva em um arquivo .es3
        
        Args:
            data: Dados para criptografar
            output_file: Caminho onde salvar o arquivo
            should_gzip: Se deve comprimir com gzip antes de criptografar
            
        Returns:
            bool: True se salvou com sucesso, False caso contrário
        """
        try:
            # Comprimir os dados se necessário
            if should_gzip:
                data = gzip.compress(data)

            # Gerar um IV aleatório
            iv = os.urandom(16)

            # Derivar a chave usando PBKDF2
            key = PBKDF2(self.password, iv, dkLen=16, count=100,
                         prf=lambda p, s: HMAC.new(p, s, SHA1).digest())

            # Criptografar os dados usando AES-128-CBC
            cipher = AES.new(key, AES.MODE_CBC, iv)
            encrypted_data = cipher.encrypt(pad(data, AES.block_size))

            # Adicionar o IV no início dos dados criptografados
            result = iv + encrypted_data
            
            # Salvar o resultado no arquivo
            with open(output_file, 'wb') as f:
                f.write(result)
                
            return True
        except Exception as e:
            print(f"Erro durante a criptografia ou salvamento: {str(e)}")
            return False
    
    def open_save_file(self, file_path: str) -> Tuple[bool, str]:
        """
        Abre e decodifica um arquivo de save
        
        Args:
            file_path: Caminho para o arquivo .es3
            
        Returns:
            Tuple[bool, str]: (sucesso, mensagem)
        """
        try:
            decrypted_data = self.decrypt_es3(file_path)
            self.json_data = json.loads(decrypted_data.decode('utf-8'))
            return True, "Arquivo aberto com sucesso"
        except Exception as e:
            return False, f"Erro ao abrir o arquivo: {str(e)}"
    
    def save_file(self, file_path: str) -> Tuple[bool, str]:
        """
        Salva e codifica os dados no arquivo de save
        
        Args:
            file_path: Caminho onde salvar o arquivo
            
        Returns:
            Tuple[bool, str]: (sucesso, mensagem)
        """
        if not self.json_data:
            return False, "Nenhum dado para salvar"
            
        try:
            json_str = json.dumps(self.json_data, indent=4)
            success = self.encrypt_es3(json_str.encode('utf-8'), file_path)
            if success:
                return True, "Arquivo salvo com sucesso"
            else:
                return False, "Erro ao salvar o arquivo"
        except Exception as e:
            return False, f"Erro ao salvar o arquivo: {str(e)}"
    
    def get_player_data(self) -> List[Dict]:
        """
        Obtém os dados dos jogadores do save
        
        Returns:
            List[Dict]: Lista com dados de cada jogador
        """
        players = []
        if not self.json_data:
            return players
            
        try:
            player_names = self.json_data["playerNames"]["value"]
            dictionaries = self.json_data["dictionaryOfDictionaries"]["value"]
            
            for player_id, player_name in player_names.items():
                player_health = dictionaries["playerHealth"][player_id]
                players.append({
                    "id": player_id,
                    "name": player_name,
                    "health": player_health,
                    "upgrades": {
                        "health": dictionaries["playerUpgradeHealth"][player_id],
                        "stamina": dictionaries["playerUpgradeStamina"][player_id],
                        "extra_jump": dictionaries["playerUpgradeExtraJump"][player_id],
                        "launch": dictionaries["playerUpgradeLaunch"][player_id],
                        "map_player_count": dictionaries["playerUpgradeMapPlayerCount"][player_id],
                        "speed": dictionaries["playerUpgradeSpeed"][player_id],
                        "strength": dictionaries["playerUpgradeStrength"][player_id],
                        "range": dictionaries["playerUpgradeRange"][player_id],
                        "throw": dictionaries["playerUpgradeThrow"][player_id]
                    }
                })
        except KeyError as e:
            print(f"Erro ao acessar dados do jogador: {e}")
            
        return players
    
    def get_world_data(self) -> Dict:
        """
        Obtém os dados do mundo do save
        
        Returns:
            Dict: Dados do mundo (nível, moeda, vidas, etc.)
        """
        if not self.json_data:
            return {}
            
        try:
            run_stats = self.json_data["dictionaryOfDictionaries"]["value"]["runStats"]
            return {
                "level": run_stats["level"],
                "currency": run_stats["currency"],
                "lives": run_stats["lives"],
                "charging_station": run_stats["chargingStationCharge"],
                "total_haul": run_stats["totalHaul"],
                "team_name": self.json_data["teamName"]["value"]
            }
        except KeyError as e:
            print(f"Erro ao acessar dados do mundo: {e}")
            return {}
    
    def update_player_data(self, player_id: str, health: int, upgrades: Dict) -> bool:
        """
        Atualiza os dados de um jogador
        
        Args:
            player_id: ID do jogador
            health: Nova vida do jogador
            upgrades: Dicionário com upgrades do jogador
            
        Returns:
            bool: True se atualizou com sucesso
        """
        if not self.json_data:
            return False
            
        try:
            dictionaries = self.json_data["dictionaryOfDictionaries"]["value"]
            dictionaries["playerHealth"][player_id] = health
            dictionaries["playerUpgradeHealth"][player_id] = upgrades["health"]
            dictionaries["playerUpgradeStamina"][player_id] = upgrades["stamina"]
            dictionaries["playerUpgradeExtraJump"][player_id] = upgrades["extra_jump"]
            dictionaries["playerUpgradeLaunch"][player_id] = upgrades["launch"]
            dictionaries["playerUpgradeMapPlayerCount"][player_id] = upgrades["map_player_count"]
            dictionaries["playerUpgradeSpeed"][player_id] = upgrades["speed"]
            dictionaries["playerUpgradeStrength"][player_id] = upgrades["strength"]
            dictionaries["playerUpgradeRange"][player_id] = upgrades["range"]
            dictionaries["playerUpgradeThrow"][player_id] = upgrades["throw"]
            return True
        except KeyError as e:
            print(f"Erro ao atualizar dados do jogador: {e}")
            return False
    
    def update_world_data(self, data: Dict) -> bool:
        """
        Atualiza os dados do mundo
        
        Args:
            data: Dicionário com novos dados do mundo
            
        Returns:
            bool: True se atualizou com sucesso
        """
        if not self.json_data:
            return False
            
        try:
            run_stats = self.json_data["dictionaryOfDictionaries"]["value"]["runStats"]
            run_stats["level"] = data["level"]
            run_stats["currency"] = data["currency"]
            run_stats["lives"] = data["lives"]
            run_stats["chargingStationCharge"] = data["charging_station"]
            run_stats["totalHaul"] = data["total_haul"]
            self.json_data["teamName"]["value"] = data["team_name"]
            return True
        except KeyError as e:
            print(f"Erro ao atualizar dados do mundo: {e}")
            return False
    
    def get_file_info(self) -> Dict:
        """
        Obtém informações básicas sobre o arquivo carregado
        
        Returns:
            Dict: Informações do arquivo (nome da equipe, número de jogadores, etc.)
        """
        if not self.json_data:
            return {}
            
        try:
            return {
                "team_name": self.json_data["teamName"]["value"],
                "player_count": len(self.json_data["playerNames"]["value"]),
                "level": self.json_data["dictionaryOfDictionaries"]["value"]["runStats"]["level"],
                "currency": self.json_data["dictionaryOfDictionaries"]["value"]["runStats"]["currency"],
                "lives": self.json_data["dictionaryOfDictionaries"]["value"]["runStats"]["lives"]
            }
        except KeyError as e:
            print(f"Erro ao obter informações do arquivo: {e}")
            return {}
    
    def is_file_loaded(self) -> bool:
        """
        Verifica se um arquivo foi carregado
        
        Returns:
            bool: True se há um arquivo carregado
        """
        return bool(self.json_data)
    
    def validate_player_data(self, player_id: str, health: int, upgrades: Dict) -> Tuple[bool, str]:
        """
        Valida os dados de um jogador antes da atualização
        
        Args:
            player_id: ID do jogador
            health: Vida do jogador
            upgrades: Upgrades do jogador
            
        Returns:
            Tuple[bool, str]: (válido, mensagem)
        """
        if not self.json_data:
            return False, "Nenhum arquivo carregado"
            
        if player_id not in self.json_data["playerNames"]["value"]:
            return False, f"ID do jogador inválido: {player_id}"
            
        if not isinstance(health, int) or health < 0 or health > 200:
            return False, "A vida deve ser um número inteiro entre 0 e 200"
            
        for key, value in upgrades.items():
            if not isinstance(value, int) or value < 0:
                return False, f"O upgrade {key} deve ser um número inteiro não negativo"
                
        return True, "Dados válidos"
    
    def validate_world_data(self, data: Dict) -> Tuple[bool, str]:
        """
        Valida os dados do mundo antes da atualização
        
        Args:
            data: Dados do mundo
            
        Returns:
            Tuple[bool, str]: (válido, mensagem)
        """
        if not self.json_data:
            return False, "Nenhum arquivo carregado"
            
        required_fields = ["level", "currency", "lives", "charging_station", "total_haul", "team_name"]
        for field in required_fields:
            if field not in data:
                return False, f"Campo obrigatório: {field}"
                
        if not isinstance(data["level"], int) or data["level"] < 1:
            return False, "O nível deve ser um número inteiro positivo"
            
        if not isinstance(data["currency"], int) or data["currency"] < 0:
            return False, "A moeda deve ser um número inteiro não negativo"
            
        if not isinstance(data["lives"], int) or data["lives"] < 0:
            return False, "As vidas devem ser um número inteiro não negativo"
            
        if not isinstance(data["charging_station"], int) or data["charging_station"] < 0:
            return False, "A carga da estação deve ser um número inteiro não negativo"
            
        if not isinstance(data["total_haul"], int) or data["total_haul"] < 0:
            return False, "O total de carga deve ser um número inteiro não negativo"
            
        if not isinstance(data["team_name"], str) or not data["team_name"]:
            return False, "O nome da equipe não pode estar vazio"
            
        return True, "Dados válidos"

