# Плагины в Zmod

Любой пользователь может создать и подключить свой плагин к **zmod**.

Пример плагина: https://github.com/ghzserg/nopoop
(Во всех примерах ниже используется имя `nopoop` — замените его на имя вашего плагина.)

---

## Добавление плагина

В файле
```mod_data/user.moonraker.conf```
добавьте секцию:

```ini
[update_manager nopoop]
type: git_repo
channel: dev
path: /root/printer_data/config/mod_data/plugins/nopoop
origin: https://github.com/ghzserg/nopoop.git
is_system_service: False
primary_branch: master
```

- **Путь к плагину**: `/root/printer_data/config/mod_data/plugins/nopoop`
- **Источник**: `https://github.com/ghzserg/nopoop.git`

> Стабильные плагины могут быть включены в поставку zmod, но обновляются и управляются их авторами.

---

## Управление плагином

**Включить плагин:**
```gcode
ENABLE_PLUGIN name=nopoop
```
— скачает плагин и перезапустит Klipper при успехе.

**Выключить плагин:**
```gcode
DISABLE_PLUGIN name=nopoop
```

---

## Структура плагина

### Скрипт установки

После вызова `ENABLE_PLUGIN`, будет автоматически вызыван файл install.sh

После вызова `DISABLE_PLUGIN`, будет автоматически вызыван файл uninstall.sh

### Одноязычный плагин
Должен содержать файл:
```
nopoop.cfg
```
В нём — весь функционал.

### Многоязычный плагин
Файлы размещаются в подкаталогах по языкам:
```
en/nopoop.cfg
ru/nopoop.cfg
de/nopoop.cfg
...
```

Все строки вывода должны быть экранированы, например:
```gcode
RESPOND PREFIX="info" MSG="===Cutting the filament==="
```

---

#### Перевод

Переводы хранятся в каталоге `translate/` в файлах вида `de.csv`:

```csv
Cutting the filament;Filament schneiden
```

Формат:
```
Английская фраза;Перевод на нужный язык
```

Чтобы сгенерировать языковые файлы, выполните:
```bash
./Make.sh
```
Скрипт создаст нужные каталоги и `.cfg`-файлы.
