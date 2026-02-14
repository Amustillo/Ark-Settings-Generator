# Changelog

Created by **Amustillo** for the Ark: Survival Ascended community

All notable changes to Ark Settings Generator will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-02-13

### Added
- **Enhanced Tab Interface**: Selected tabs are now visually larger (font size 13, padding 20x10) while unselected tabs are smaller (font size 9, padding 10x5) for better visual hierarchy
- **Decimal Thousands Display**: All slider values and entry boxes now display in 3-decimal format (e.g., "1.000" instead of "1.0") for precision
  - Slider labels show formatted values
  - Entry boxes show formatted values and accept manual input
  - Both stay synchronized when either is changed
- **Numeric-Only Validation**: All numeric entry fields now enforce number-only input, preventing text entry errors
- **INI File Import**: New "Import INI Files" button allows uploading existing GameUserSettings.ini and Game.ini files to populate settings automatically
- **Interactive Tooltips**: Hover over any setting label (marked with ℹ️ icon) to see a tooltip with the full description
- **Right-Click Paste for Mods**: Right-click in the mod entry field to quickly paste mod codes from clipboard

### Changed
- Setting labels now display with ℹ️ icon to indicate tooltip availability
- Entry boxes now maintain decimal thousands formatting for consistency
- Improved user experience with visual feedback throughout the interface
- Enhanced accessibility with validation preventing invalid inputs

### Technical
- Added `ToolTip` class for dynamic tooltip rendering
- Added `format_slider_value()` method for consistent decimal formatting across sliders and entry boxes
- Added `validate_numeric_only()` method for input validation
- Added `import_ini_files()` method for configuration import
- Added `show_mod_context_menu()` and `paste_to_mod_entry()` for right-click functionality
- Updated tab styling to support dynamic sizing based on selection state
- Implemented dual StringVar system for synchronized display between slider labels and entry boxes

## [1.0.3] - 2026-02-13

### Fixed
- **File Location Display in EXE**: Fixed issue where EXE wasn't showing file paths correctly
  - Changed from `os.path.abspath()` to `os.getcwd()` for more reliable directory detection
  - Updated all EXE locations (root, dist, and source/dist)
  - Now correctly displays working directory and full file paths when running as executable

## [1.0.2] - 2026-02-13

### Fixed
- **File Location Display**: Improved success message to show complete absolute file paths
  - Now displays full directory path where INI files are saved
  - Shows complete paths for both GameUserSettings.ini and Game.ini
  - Fixed issue where path might not display correctly in certain scenarios

## [1.0.1] - 2026-02-13

### Added
- **File Location Notification**: Success dialog now displays the full directory path where INI files are saved
  - Shows complete file path for easy file location
  - Lists both generated files (GameUserSettings.ini and Game.ini)
  - Improved user experience for finding generated configuration files

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
  - ACTIVE EVENT dropdown shows all 18 available events
  - ✅ All events currently marked as working
  - Status indicators for user clarity (✅ working, ⏰ planned)
  - Comprehensive event support:
    - ✅ None (No active event)
    - ✅ WinterWonderland (Winter holiday event with cosmetics)
    - ✅ WinterWonderland2-7 (Multi-year winter events)
    - ✅ Easter (Eggcellent Adventure - egg hunt themed)
    - ✅ SummerBash (Summer vacation themed)
    - ✅ FearEvolved (Halloween spooky creatures themed)
    - ✅ TurkeyTrial (Thanksgiving event)
    - ✅ LoveEvolved (Valentine breeding event bonuses)
    - ✅ Birthday (Anniversary/Birthday celebration bonuses)
    - ✅ EvolutionEvent (Creature variant spawns)
    - ✅ ExtraLife (Charity event bonuses)
    - ✅ ARKaeology (Artifact discovery event)
    - ✅ ARKdependenceDay (July 4th themed event)
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
