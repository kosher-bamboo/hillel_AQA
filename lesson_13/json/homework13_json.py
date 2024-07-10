"""
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log
"""

import json
from pathlib import Path
import logging

logging.basicConfig(
    filename='json_marar.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')

path = Path("work_with_json")
# file = "login.json"

# list comprehension - create a list of files
files = [f for f in path.iterdir() if f.is_file()]

for file in files:
    with open(file, "r") as f:
        try:
            file_content = json.load(f)
            print(f"{file} is valid")
        except:
            logging.error(f"invalid json: {file}")
            pass
