#!/bin/sh

[ -f /opt/config/mod_data/filament.json.save ] && mv /opt/config/mod_data/filament.json.save /opt/config/mod_data/filament.json && echo "Restored file filament.json from filament.json.save"
echo "SAVE_ZMOD_DATA use_trash_on_print=1" >/tmp/printer
echo "Plugin Nopoop ubinstalled"
