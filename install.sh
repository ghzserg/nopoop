#!/bin/sh

[ -f /opt/config/mod_data/filament.json ] && cp /opt/config/mod_data/filament.json /opt/config/mod_data/filament.json.save && echo "Old file filament.json saved us filament.json.save"
cp filament.json /opt/config/mod_data/filament.json && echo "New file filament.json installed"
echo "SAVE_ZMOD_DATA use_trash_on_print=0" >/tmp/printer
echo "Plugin Nopoop installed"
echo "DISPLAY_OFF" >/tmp/printer
