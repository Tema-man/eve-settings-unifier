# EVE Online Settings Unifier

A Python utility for unifying EVE Online game settings across multiple characters.

## Overview

This script helps EVE Online players synchronize settings between different characters by copying settings files from a source character to all other character configuration files. It automatically backs up existing settings before making changes and supports both user-level and character-level settings.

## Features

- 🔄 **Automatic Settings Sync**: Copy settings from one source character to all others
- 💾 **Automatic Backups**: Creates `.bak` files before overwriting existing settings
- 👤 **Multi-Character Support**: Handles both user and character-specific settings
- 🛡️ **Safe Operations**: Validates file types and skips already processed files
- ⚙️ **Flexible Configuration**: Use command line arguments, environment variables, or `.env` file for convenience

## Requirements

- Python 3.6+
- EVE Online client installed

## Installation

1. Clone this repository:
   ```bash
   git clone git@github.com:Tema-man/eve-settings-unifier.git
   cd eve-settings-unifier
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. The script uses only Python standard library modules, so no additional packages are required.

## Configuration

### Option 1: Command Line Arguments (Recommended)
You can run the script directly with command line arguments without any configuration files:

```bash
python unite_settings.py --path "path/to/eve/settings" --source_user_id "12345" --source_char_id "67890"
```

### Option 2: Environment File (Optional)
For convenience, you can create a `.env` file to save your preferences between usages:

1. Create a `.env` file in the project directory:
   ```env
   SOURCE_CHAR_ID=your_source_character_id
   SOURCE_USER_ID=your_source_user_id
   EVE_PATH="path_to_your_eve_settings_folder"
   ```

2. The script will automatically read these values when run without arguments.

### Finding Your Settings Path

The EVE Online settings are typically located at:
- **Windows**: `%LOCALAPPDATA%\CCP\EVE\[installation_folder]\settings_Default`
- **macOS**: `~/Library/Preferences/EVE Online Preferences/p_drive/Local Settings/Application Data/CCP/EVE/[installation_folder]/settings_Default`
- **Linux**: `~/.eve/wineenv/drive_c/users/[username]/Local Settings/Application Data/CCP/EVE/[installation_folder]/settings_Default`

### Finding Character and User IDs

Character and User IDs can be found in the filenames of your existing settings files:
- User settings: `core_user_[USER_ID].dat`
- Character settings: `core_char_[CHARACTER_ID].dat`

## Usage

### Command Line Arguments

```bash
python unite_settings.py --path "path/to/eve/settings" --source_user_id "12345" --source_char_id "67890"
```

**Arguments:**
- `--path`: Path to EVE Online settings directory
- `--source_user_id`: User ID of the source character whose settings to copy
- `--source_char_id`: Character ID of the source character whose settings to copy

### Environment Variables (Alternative)

If you prefer to use environment variables instead of command line arguments, you can set them in your shell:

```bash
# Windows PowerShell
$env:SOURCE_USER_ID="12345"
$env:SOURCE_CHAR_ID="67890"
$env:EVE_PATH="C:\path\to\eve\settings"
python unite_settings.py

# Linux/macOS
export SOURCE_USER_ID="12345"
export SOURCE_CHAR_ID="67890" 
export EVE_PATH="/path/to/eve/settings"
python unite_settings.py
```

## How It Works

1. **Scans** the specified EVE settings directory for `.dat` files
2. **Identifies** user and character setting files by their naming convention
3. **Creates backups** of existing settings files (adds `.bak` extension)
4. **Copies** settings from the source character/user files to all other character/user files
5. **Skips** files that have already been processed (contain `__` in filename)

## File Types Processed

- `core_user_*.dat` - User-level settings (UI preferences, shortcuts, etc.)
- `core_char_*.dat` - Character-specific settings (overview settings, chat channels, etc.)

## Safety Features

- **Automatic Backups**: Original files are backed up before any changes
- **File Validation**: Only processes `.dat` files with correct naming patterns
- **Skip Protection**: Avoids processing already modified files
- **Non-destructive**: Original source files are never modified

## Example Output

```
Backing up core_user_98765432.dat to core_user_98765432.dat.bak
Copying core_user_12345.dat as core_user_98765432.dat
Backing up core_char_11111111.dat to core_char_11111111.dat.bak
Copying core_char_67890.dat as core_char_11111111.dat
```

## Warning

⚠️ **Important**: Always backup your EVE Online settings folder before running this script. While the script creates automatic backups, having an additional manual backup is recommended.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is not affiliated with or endorsed by CCP Games. EVE Online is a trademark of CCP hf. Use this tool at your own risk and always backup your settings before making changes.

## Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/eve-settings-unifier/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide relevant details including your operating system and EVE Online installation path