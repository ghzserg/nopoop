# (C) 2025 ghzserg https://github.com/ghzserg/zmod/
import csv
import os
import re
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Использование: python script.py <файл_перевода.csv>")
        return

    translate_file = sys.argv[1]
    lang_dir = os.path.splitext(translate_file)[0]

    os.makedirs(f"../%s" % (lang_dir), exist_ok=True)

    translations = {}
    with open(translate_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if len(row) >= 2:
                original = row[0].strip()
                translated = row[1].strip()
                translations[original] = translated

    pattern = re.compile(r'(===)(.*?)(===)')

    def translate_line(line):
        def replace_match(match):
            original_text = match.group(2).strip()
            translated_text = translations.get(original_text, original_text)
            return f"{translated_text}"

        return pattern.sub(replace_match, line)

    for cfg_file in Path('../').glob('*.cfg'):
        with open(cfg_file, 'r', encoding='utf-8') as f_in:
            lines = f_in.readlines()

        translated_lines = []
        for line in lines:
            translated_line = translate_line(line)
            translated_lines.append(translated_line)

        output_path = f"../%s/%s" % (Path(lang_dir), cfg_file.name)
        with open(output_path, 'w', encoding='utf-8') as f_out:
            f_out.writelines(translated_lines)

    print(f"Переведено файлов: {len(list(Path('..').glob('*.cfg')))} в каталог '{lang_dir}'")

if __name__ == "__main__":
    main()
