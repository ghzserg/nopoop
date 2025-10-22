#!/bin/sh

[ -f /opt/config/mod_data/filament.json ] && cp /opt/config/mod_data/filament.json /opt/config/mod_data/filament.json.save && echo "Old file filament.json saved us filament.json.save"
cp filament.json /opt/config/mod_data/filament.json && echo "New file filament.json installed"
echo "Plugin Nopoop installed"
