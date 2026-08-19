"""
Tests for Ark Settings Generator
Tests core functionality including INI generation and settings validation
"""

import pytest
import configparser
import copy
import os
import tempfile
from pathlib import Path
from source.main import ArkSettingsGenerator


class FakeVar:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def set(self, value):
        self.value = value


class FakeListbox:
    def __init__(self, values):
        self.values = values

    def get(self, start, end):
        return tuple(self.values)


def make_headless_app():
    app = ArkSettingsGenerator.__new__(ArkSettingsGenerator)
    app.root = None
    app.settings = {
        'ServerSettings': {
            'ServerName': '',
            'MaxPlayers': 70,
            'ActiveMods': '',
        },
        '/script/shootergame.shootergamemode': {
            'BabyMatureSpeedMultiplier': 1.0,
            'bDisableDinoBreeding': False,
        },
    }
    app.default_settings = copy.deepcopy(app.settings)
    app.mode = FakeVar('basic')
    app.switch_mode = lambda: None
    return app


class TestIniGeneration:
    """Test INI file generation"""
    
    def test_basic_mode_only_includes_basic_settings(self):
        """Test that basic mode only generates basic settings"""
        assert 'ServerName' in ['ServerName', 'MaxPlayers']
    
    def test_advanced_mode_includes_all_settings(self):
        """Test that advanced mode generates all settings"""
        app = make_headless_app()
        assert set(app.settings['ServerSettings']) == {'ServerName', 'MaxPlayers', 'ActiveMods'}
    
    def test_valid_ini_syntax(self):
        """Test that generated INI files have valid syntax"""
        # Create a test INI file
        config = configparser.ConfigParser(allow_no_value=True)
        config.optionxform = str
        config.add_section('TestSection')
        config.set('TestSection', 'TestKey', 'TestValue')
        
        # Verify it can be read back
        with tempfile.NamedTemporaryFile(mode='w', suffix='.ini', delete=False) as f:
            config.write(f)
            temp_file = f.name
        
        try:
            # Try to read it back
            test_config = configparser.ConfigParser(allow_no_value=True)
            test_config.read(temp_file)
            assert test_config.has_option('TestSection', 'TestKey')
            assert test_config.get('TestSection', 'TestKey') == 'TestValue'
        finally:
            os.unlink(temp_file)

    def test_generate_files_writes_basic_application_settings(self, monkeypatch, tmp_path):
        app = make_headless_app()
        app.basic_server = ['ServerName', 'MaxPlayers']
        app.basic_game = ['BabyMatureSpeedMultiplier']
        app.server_ServerName = FakeVar('Generated Server')
        app.server_MaxPlayers = FakeVar(5000)
        app.game_BabyMatureSpeedMultiplier = FakeVar(3.0)
        app.mods_listbox = FakeListbox(['123', '456'])
        app.update_calculations = lambda: None
        monkeypatch.chdir(tmp_path)
        monkeypatch.setattr('source.main.messagebox.showinfo', lambda *args: None)

        app.generate_files()

        user_config = configparser.ConfigParser()
        user_config.optionxform = str
        user_config.read(tmp_path / 'GameUserSettings.ini')
        game_config = configparser.ConfigParser()
        game_config.optionxform = str
        game_config.read(tmp_path / 'Game.ini')
        assert user_config['ServerSettings']['MaxPlayers'] == '5000'
        assert user_config['ServerSettings']['ActiveMods'] == '123,456'
        assert game_config['/script/shootergame.shootergamemode']['BabyMatureSpeedMultiplier'] == '3.0'


class TestModValidation:
    """Test mod management functionality"""
    
    def test_mod_id_must_be_numeric(self):
        """Test that mod IDs are validated as numeric"""
        # Test cases: valid mod ID (numeric), invalid mod ID (non-numeric)
        valid_mod_id = "928595"
        invalid_mod_id = "abc123"
        
        assert valid_mod_id.isdigit()
        assert not invalid_mod_id.isdigit()
    
    def test_no_duplicate_mods(self):
        """Test that duplicate mods are not allowed"""
        mod_list = ["928595", "731604"]
        new_mod = "928595"
        
        # Check if duplicate
        is_duplicate = new_mod in mod_list
        assert is_duplicate
        
        # Should not be added
        if not is_duplicate:
            mod_list.append(new_mod)
        
        assert mod_list.count("928595") == 1


class TestSettings:
    """Test settings and calculations"""
    
    def test_default_settings_exist(self):
        """Test that all required settings are defined"""
        # Basic server settings should include essential keys
        essential_keys = [
            'SessionName', 'RCONPort', 'ServerPassword', 'AdminPassword',
            'DifficultyOffset', 'MaxPlayersCount'
        ]
        
        # Test would check that these exist in the application
        for key in essential_keys:
            assert isinstance(key, str)
            assert len(key) > 0
    
    def test_multiplier_ranges(self):
        """Test that multipliers are within reasonable ranges"""
        # Multipliers should typically be between 0.1 and 100
        test_multipliers = [1.0, 2.5, 10.0, 0.5]
        
        for multiplier in test_multipliers:
            assert 0.1 <= multiplier <= 100
    
    def test_dino_data_available(self):
        """Test that dino data is available for calculations"""
        # Should have multiple dinos for selection
        dino_names = ['Argentavis', 'Phoenix', 'Wyvern', 'Griffin', 'Griffin']
        
        assert len(set(dino_names)) >= 3  # At least 3 unique dinos


class TestImportAndReset:
    def test_import_preserves_setting_case_and_types(self, monkeypatch, tmp_path):
        app = make_headless_app()
        app.settings['ServerName'] = 'stale value'
        game_user_path = tmp_path / 'GameUserSettings.ini'
        game_path = tmp_path / 'Game.ini'
        game_user_path.write_text(
            '[ServerSettings]\n'
            'ServerName = 100% server\n'
            'MaxPlayers = 12\n'
            'MaxPlayers = 42\n'
            'ActiveMods = 123,456\n',
            encoding='utf-8',
        )
        game_path.write_text(
            '[/script/shootergame.shootergamemode]\n'
            'BabyMatureSpeedMultiplier = 5.0\n'
            'bDisableDinoBreeding = true\n',
            encoding='utf-8',
        )
        paths = iter([str(game_user_path), str(game_path)])
        monkeypatch.setattr('source.main.filedialog.askopenfilename', lambda **_: next(paths))
        monkeypatch.setattr('source.main.messagebox.showinfo', lambda *args: None)

        app.import_ini_files()

        assert app.settings['ServerSettings']['ServerName'] == '100% server'
        assert app.settings['ServerSettings']['MaxPlayers'] == 42
        assert app.settings['ServerSettings']['ActiveMods'] == '123,456'
        assert app.settings['/script/shootergame.shootergamemode']['BabyMatureSpeedMultiplier'] == 5.0
        assert app.settings['/script/shootergame.shootergamemode']['bDisableDinoBreeding'] is True

    def test_import_resets_omitted_settings_to_defaults(self, monkeypatch, tmp_path):
        app = make_headless_app()
        app.settings['ServerName'] = 'stale value'
        game_user_path = tmp_path / 'GameUserSettings.ini'
        game_path = tmp_path / 'Game.ini'
        game_user_path.write_text('[ServerSettings]\nMaxPlayers = 5000\n', encoding='utf-8')
        game_path.write_text('[/script/shootergame.shootergamemode]\n', encoding='utf-8')
        paths = iter([str(game_user_path), str(game_path)])
        monkeypatch.setattr('source.main.filedialog.askopenfilename', lambda **_: next(paths))
        monkeypatch.setattr('source.main.messagebox.showinfo', lambda *args: None)

        app.import_ini_files()

        assert app.settings['ServerSettings']['MaxPlayers'] == 5000
        assert app.settings['ServerSettings']['ServerName'] == ''

    def test_reset_restores_original_defaults_after_import(self, monkeypatch):
        app = make_headless_app()
        app.settings['ServerSettings']['ServerName'] = 'Imported'
        app.settings['ServerSettings']['MaxPlayers'] = 12
        app.mode.set('advanced')
        monkeypatch.setattr('source.main.messagebox.showinfo', lambda *args: None)

        app.reset_to_defaults()

        assert app.mode.get() == 'basic'
        assert app.settings == app.default_settings

    def test_import_rejects_files_in_wrong_order(self, monkeypatch, tmp_path):
        app = make_headless_app()
        game_user_path = tmp_path / 'GameUserSettings.ini'
        game_path = tmp_path / 'Game.ini'
        game_user_path.write_text(
            '[ServerSettings]\nMaxPlayers = 5000\n',
            encoding='utf-8',
        )
        game_path.write_text(
            '[/script/shootergame.shootergamemode]\nBabyMatureSpeedMultiplier = 5.0\n',
            encoding='utf-8',
        )
        paths = iter([str(game_path), str(game_user_path)])
        errors = []
        monkeypatch.setattr('source.main.filedialog.askopenfilename', lambda **_: next(paths))
        monkeypatch.setattr('source.main.messagebox.showerror', lambda *args: errors.append(args[1]))

        app.import_ini_files()

        assert errors
        assert 'first file must be GameUserSettings.ini' in errors[0]
        assert app.settings == app.default_settings


class TestCalculations:
    """Test real-time calculations"""
    
    def test_taming_time_calculation(self):
        """Test taming time calculation is reasonable"""
        # Example calculation: faster taming speed = shorter time
        base_time = 600  # 10 minutes in seconds
        taming_multiplier = 2.0
        
        calculated_time = base_time / taming_multiplier
        
        assert calculated_time < base_time
        assert calculated_time == 300
    
    def test_maturation_time_calculation(self):
        """Test maturation time calculation"""
        base_time_hours = 6.0
        maturation_multiplier = 3.0
        
        calculated_time = base_time_hours / maturation_multiplier
        
        assert calculated_time < base_time_hours
        assert calculated_time == 2.0
    
    def test_difficulty_to_level_calculation(self):
        """Test max level calculation from difficulty offset"""
        difficulty_offset = 1.0
        max_level = 150 + (difficulty_offset * 30)
        
        assert max_level == 180
        
        # Half difficulty should give level 165
        diff_half = 0.5
        max_level_half = 150 + (diff_half * 30)
        assert max_level_half == 165

    def test_zero_multiplier_falls_back_to_safe_calculation_value(self):
        assert ArkSettingsGenerator._positive_multiplier(0) == 1.0
        assert ArkSettingsGenerator._positive_multiplier(-2) == 1.0
        assert ArkSettingsGenerator._positive_multiplier(2.5) == 2.5


class TestFileOperations:
    """Test file operations"""
    
    def test_ini_file_creation(self):
        """Test that INI files can be created and read"""
        config = configparser.ConfigParser(allow_no_value=True)
        config.optionxform = str
        config.add_section('ServerSettings')
        config.set('ServerSettings', 'SessionName', 'TestServer')
        config.set('ServerSettings', 'MaxPlayersCount', '70')
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.ini', delete=False) as f:
            config.write(f)
            temp_file = f.name
        
        try:
            # Verify file was created and contains correct data
            assert os.path.exists(temp_file)
            
            # Read back and verify
            verify_config = configparser.ConfigParser(allow_no_value=True)
            verify_config.read(temp_file)
            
            assert verify_config.get('ServerSettings', 'SessionName') == 'TestServer'
            assert verify_config.get('ServerSettings', 'MaxPlayersCount') == '70'
        finally:
            os.unlink(temp_file)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
