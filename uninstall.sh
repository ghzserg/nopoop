#!/bin/sh

[ -f /opt/config/mod_data/filament.json.save ] && mv /opt/config/mod_data/filament.json.save /opt/config/mod_data/filament.json && echo "Restored file filament.json from filament.json.save"
echo "Plugin Nopoop ubinstalled"
