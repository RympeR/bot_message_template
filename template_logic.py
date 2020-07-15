import random
import json
import re
from string import Template

with open('dictionary.json', 'r') as f:
    text = f.read()

JSON_ITEMS = json.loads(text)
PATTERN = r'\$(\w+)'

def add_template(template):
    with open('templates.txt', 'a', encoding='utf-8') as f:
        f.write(template + '\n')


def create_message(amount:int, templates: list):
    amount = amount // len(templates)
    result = []
    for template in templates:
        template_ = Template(template)
        for _ in range(amount):
            vars = re.findall(PATTERN, template)
            vars = {name: random.choice(JSON_ITEMS[name]) for name in vars}
            mess = template_.safe_substitute(vars)
            k = 0
            while k < 6000:
                with open('unique_messages.txt', 'r+', encoding='utf-8') as f:
                    text = f.readlines()
                    text = [row.replace('\n', '') for row in text]
                    if mess in text:
                        k+=1
                        # print(mess, ' In file')
                        vars = {name: random.choice(JSON_ITEMS[name])
                            for name in vars}
                        mess = template_.safe_substitute(vars)
                        continue
                    else:
                        f.write(mess + '\n')
                        with open('messages.txt', 'a+',
                            encoding='utf-8') as message:
                            message.write(mess + '\n')
                        result.append(mess)
                        break
    return result
