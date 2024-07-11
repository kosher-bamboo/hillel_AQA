"""
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і
повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
"""

import xml.etree.ElementTree as ET
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')


def search_in_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()

    for group in root.findall('group'):
        timing_exbytes = group.find('timingExbytes')
        if timing_exbytes is not None:
            incoming = timing_exbytes.find('incoming')
            if incoming is not None:
                logging.info(f"group: {group.find('number').text}, incoming: {incoming.text}")
            else:
                logging.info(f"group: {group.find('number').text}, incoming: Не знайдено")
    return incoming


search_in_xml("groups.xml")
