# Ark Settings Generator

A modern GUI application to generate `GameUserSettings.ini` and `Game.ini` configuration files for Ark Survival Ascended servers.

## Features

- **🎮 Basic and Advanced Modes**: Choose between commonly used settings (Basic) or full server customization (Advanced)
- **🎨 Modern Dark UI**: Clean, professional interface with teal accents and improved visibility
- **📊 Real-Time Dino Calculations**: Select any dino from dropdown and see live calculations for:
  - Taming times
  - Maturation times
  - Imprinting intervals and max imprint %
  - Incubation times
  - Mating cooldowns
  - Max wild dino levels (based on difficulty)
- **🔌 Mod Management**: Easy-to-use interface for adding, removing, and reordering CurseForge mods
  - Add mods by CurseForge Mod ID
  - Reorder mods with Move Up/Down buttons
  - Built-in instructions for finding mod IDs
  - Mods persist across mode switches
- **💡 Advanced Tips**: Displays useful server configuration tips most players don't know about
  - Difficulty offset formulas
  - Performance warnings
  - Multiplier behavior insights
- **🎉 Server Events**: Easy selection of active events with status indicators
  - Choose from 18+ available Ark events (Winter Wonderland, Easter, Summer Bash, etc.)
  - Birthday/Anniversary events and special celebration bonuses
  - Evolution and Extra Life charity events
  - Clear ✅ working / ⏰ planned indicators for event availability
- **📝 Helpful Descriptions**: Each setting includes a brief description of its effects
- **📑 Tabbed Interface**: Separate tabs for Server Settings, Game Settings, and Mods
- **⚡ Optimized Performance**: Smooth scrolling and window movement even with many settings
- **🖱️ Mouse Wheel Support**: Scroll through all settings tabs with your mouse wheel
- **🎯 Mode-Specific Generation**: Generate INI files with only the settings visible in the current mode

## Quick Start

1. **Download**: Get the latest release or clone this repository
2. **Run**: Double-click `ArkSettingsGenerator.exe` (or run from source)
3. **Configure**: 
   - Select Basic or Advanced mode
   - Adjust server and game settings
   - Add mods in the Mods tab (optional)
4. **Generate**: Click "Generate INI Files" to create your config files
5. **Deploy**: Copy the generated `Game.ini` and `GameUserSettings.ini` to your Ark server's configuration folder

## Usage

### Running the Application

**From Executable:**
```
Double-click ArkSettingsGenerator.exe
```

**From Source:**
```bash
cd source
python main.py
```

### Interface Overview

- **Mode Selection**: Choose between Basic (common settings) or Advanced (all settings) at the top
- **Control Buttons**: Generate INI files or reset to defaults (visible at top)
- **Settings Tabs**: 
  - **Server Settings**: Server name, passwords, difficulty, multipliers, etc.
  - **Game Settings**: Breeding, harvesting, day/night cycle, etc.
  - **Mods**: Manage CurseForge mods with easy add/remove/reorder interface
- **Calculations Panel**: Real-time dino calculations on the right side

### Using Server Events

The **ACTIVE EVENT** dropdown in Server Settings allows you to select from 18+ available Ark events:

**Available Events:**
- No Event: `None`
- Winter Events: `WinterWonderland` (1-7 yearly versions)
- Holiday Events: `Easter` (Eggcellent Adventure), `SummerBash`, `FearEvolved`, `TurkeyTrial`, `LoveEvolved`
- Birthday/Anniversary: `Birthday` event with celebration bonuses
- Miscellaneous: `EvolutionEvent`, `ExtraLife`, `ARKaeology`, `ARKdependenceDay`

**How to Use:**
1. In Server Settings (Basic or Advanced mode), locate the **ACTIVE EVENT** dropdown
2. Click the dropdown to see all available events with status indicators
3. ✅ = Currently working and fully supported
4. ⏰ = Planned/Coming Soon (when applicable)
5. Select your desired event - the setting will update automatically

### Using Mod Management

1. Navigate to the **Mods** tab
2. Find your desired mod on [CurseForge](https://www.curseforge.com/ark-survival-ascended/mods)
3. Copy the Mod ID from the URL (e.g., `curseforge.com/.../mods/12345` → ID is `12345`)
4. Enter the Mod ID in the "Add Mod" field and click "Add Mod"
5. Use Move Up/Down buttons to reorder mods (load order matters!)
6. Mods are automatically included in generated INI files

### Mode Differences

- **Basic Mode**: Shows ~15-20 essential server settings including server name, passwords, difficulty, player limits, and key multipliers
- **Advanced Mode**: Shows 100+ settings for complete server customization
- **Mods Tab**: Always visible in both modes
- **File Generation**: Only generates settings that are visible in the current mode, but mods are always included

## File Structure

```
Ark Settings Generator/
├── .gitignore                  # Git ignore file
├── ArkSettingsGenerator.exe    # Main executable (excluded from git)
├── Game.ini                    # Generated output (excluded from git)
├── GameUserSettings.ini        # Generated output (excluded from git)
├── README.md                   # This documentation
└── source/                     # Source code
    ├── main.py                 # Main application (1500+ lines)
    ├── requirements.txt        # Python dependencies
    ├── ArkSettingsGenerator.spec # PyInstaller build config
    └── dist/                   # Build output directory
        └── ArkSettingsGenerator.exe
```

## For Developers

### Prerequisites

- Python 3.8+
- tkinter (usually included with Python)
- PyInstaller (for building executables)

### Setup Development Environment

```bash
# Clone the repository
git clone <your-repo-url>
cd "Ark Settings Generator"

# Create virtual environment (optional but recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\Activate.ps1
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
cd source
pip install -r requirements.txt
```

### Running from Source

```bash
cd source
python main.py
```

### Building Executable

```bash
cd source
python -m PyInstaller --clean --noconfirm ArkSettingsGenerator.spec
```

The executable will be created in `source/dist/ArkSettingsGenerator.exe`

### Code Structure

- **Main Application**: `source/main.py`
  - `ArkSettingsGenerator` class handles all UI and logic
  - Modern dark theme with teal accent colors
  - Optimized canvas rendering for smooth performance
  - Throttled window updates for lag-free dragging
- **Settings Data**: Embedded dictionaries with default values and descriptions
- **Real-time Calculations**: Updates on slider movement using Scale command callbacks
- **Mod Management**: ListBox-based interface with validation and reordering

## Troubleshooting

If you encounter issues:
1. Ensure you're using the latest version
2. Check that your antivirus isn't blocking the executable
3. Try running as administrator if file generation fails
4. Make sure the application has write permissions in its directory
5. Check the generated INI files for any syntax issues

## Tips for Server Configuration

The application includes advanced tips in the Settings tabs:

**Server Settings Tips:**
- DifficultyOffset formula for max dino levels
- XP multiplier effects on players and dinos
- HarvestAmount warnings for mesh issues
- TamingSpeed behavior at high values
- MaxTributeDinos for cross-server transfers

**Game Settings Tips:**
- Fast breeding configurations (10min raises)
- Mating cooldown reduction strategies
- Imprint stat scaling behavior
- MaxTamedDinos performance impact
- Common configuration mistakes to avoid

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).

**Important**: This software is provided free of charge and for non-commercial use only. Commercial use, redistribution for profit, or sale of this software is strictly prohibited.

For more details, see the [LICENSE](LICENSE) file.

## Author

**Amustillo** - Creator and maintainer of Ark Settings Generator

## Acknowledgments

- Created by Amustillo for the Ark: Survival Ascended community
- Uses Python 3 with tkinter for cross-platform compatibility
- Optimized for smooth performance even with 100+ settings