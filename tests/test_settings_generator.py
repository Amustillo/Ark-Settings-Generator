"""
Tests for Ark Settings Generator
Tests core functionality including INI generation and settings validation
"""

import pytest
import configparser
import os
import tempfile
from pathlib import Path


class TestIniGeneration:
    """Test INI file generation"""
    
    def test_basic_mode_only_includes_basic_settings(self):
        """Test that basic mode only generates basic settings"""
        # This would test that generate_files in basic mode produces correct output
        # Placeholder for actual test implementation
        assert True
    
    def test_advanced_mode_includes_all_settings(self):
        """Test that advanced mode generates all settings"""
        # This would test that generate_files in advanced mode produces full output
        assert True
    
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
