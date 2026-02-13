# Changelog

Created by **Amustillo** for the Ark: Survival Ascended community

All notable changes to Ark Settings Generator will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-13

### Added
- **Initial Release**: Full-featured Ark Survival Ascended settings generator
- **Dual Modes**: Basic mode for common settings, Advanced mode for full customization
- **Real-Time Calculations**: Live dino taming, maturation, imprinting, and incubation calculations
  - Supported Dinos (all with working calculations):
    - ✅ Argentavis
    - ✅ Rex
    - ✅ Spino
    - ✅ Giga
    - ✅ Titanosaur
    - ✅ Megalodon
    - ✅ Mosasaurus
    - ✅ Plesiosaur
    - ✅ Therizino
    - ✅ Thylacoleo
  - Dropdown status indicators for working/planned dinos
- **Dino Calculator Features**:
  - Dropdown menu shows availability status for each dino
  - ✅ Working dinos show instant calculations
  - ⏰ Planned dinos display as "coming soon"
  - Color-coded indicators for user clarity
- **Server Events Manager**:
  - ACTIVE EVENT dropdown shows all 13 available events
  - ✅ All events currently marked as working
  - Status indicators for user clarity (✅ working, ⏰ planned)
  - Supported events:
    - ✅ None (No active event)
    - ✅ WinterWonderland (Winter holiday event with cosmetics)
    - ✅ Easter (Easter egg hunt themed event)
    - ✅ SummerBash (Summer vacation themed event)
    - ✅ FearEvolved (Halloween spooky creatures event)
    - ✅ TurkeyTrial (Thanksgiving turkey challenges)
    - ✅ LoveEvolved (Valentine breeding event bonuses)
    - ✅ WinterWonderland2-7 (Multi-year winter events)
- **Mod Management System**:
  - Add/remove mods by CurseForge Mod ID
  - Reorder mods (Move Up/Down functionality)
  - Clear all mods at once
  - Built-in instructions for finding mod IDs
  - Mods persist across mode switches
  - Automatic inclusion in generated INI files
- **Modern UI**:
  - Dark theme with teal accents
  - 1400x1000 responsive window
  - Tabbed interface (Server Settings, Game Settings, Mods)
  - Descriptive tooltips for all settings
- **Advanced Features**:
  - Mouse wheel scrolling in all tabs
  - Real-time value updates on slider movement
  - Mode-specific INI generation (only visible settings saved)
  - Reset to Defaults functionality
- **Performance Optimizations**:
  - Throttled window updates during dragging
  - Non-blocking UI calculations
  - Efficient canvas rendering
  - Canvas scroll region management
- **Settings Coverage**:
  - 15+ essential settings in Basic mode
  - 100+ settings in Advanced mode
  - Helpful descriptions for each setting
  - Advanced tips for experienced server admins
- **INI Generation**:
  - Generates GameUserSettings.ini
  - Generates Game.ini
  - Error handling with user feedback
  - Proper formatting and syntax

### Technical
- Python 3.8+ compatibility
- tkinter GUI framework
- configparser for INI file management
- PyInstaller support for standalone executable
- MIT License (open source)
- Comprehensive README documentation

## [Unreleased]

### Planned Features
- Configuration import (read existing INI files)
- Profile saving/loading
- Server presets (PvE/PvP templates)
- More dino types for calculations
- Settings validation and warnings
- Cross-platform installer
- Web-based version

---

## Legend
- **Added**: For new features
- **Changed**: For changes in existing functionality
- **Deprecated**: For soon-to-be removed features
- **Removed**: For now removed features
- **Fixed**: For any bug fixes
- **Security**: In case of vulnerabilities
