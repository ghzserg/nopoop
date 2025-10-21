# Plugins in Zmod

Any user can create their own plugin and integrate it into **zmod**.

Plugin example: https://github.com/ghzserg/nopoop  
(Throughout the examples below, the plugin name `nopoop` is used — replace it with your own plugin name as needed.)

---

## Adding a Plugin

In the file  
```mod_data/user.moonraker.conf```  
add the following section:

```ini
[update_manager nopoop]
type: git_repo
channel: dev
path: /root/printer_data/config/mod_data/plugins/nopoop
origin: https://github.com/ghzserg/nopoop.git
is_system_service: False
primary_branch: master
```

- **Plugin path**: `/root/printer_data/config/mod_data/plugins/nopoop`
- **Source URL**: `https://github.com/ghzserg/nopoop.git`

> Stable plugins may be included in the zmod distribution, but they are updated and maintained by their respective authors.

---

## Plugin Structure

### Single-language plugin  
Must contain a file:  
```
nopoop.cfg
```
All functionality resides in this file.

### Multi-language plugin  
Language-specific files are placed in subdirectories:  
```
en/nopoop.cfg
ru/nopoop.cfg
de/nopoop.cfg
...
```

All output messages must be escaped, for example:  
```gcode
RESPOND PREFIX="info" MSG="===Cutting the filament==="
```

---

## Translations

Translations are stored in the `translate/` directory in files like `de.csv`:

```csv
Cutting the filament;Filament schneiden
```

Format:  
```
English phrase;Translated phrase
```

To generate language files, run:
```bash
./Make.sh
```
This script will create the required directories and `.cfg` files.

---

## Plugin Management

**Enable plugin:**
```gcode
ENABLE_PLUGIN name=nopoop
```
— Downloads the plugin and restarts Klipper if successful.

**Disable plugin:**
```gcode
DISABLE_PLUGIN name=nopoop
```