import sys
import json

final_dict = dict()
with open('users.csv', 'r', encoding='utf-8') as file_1, \
        open('hobby.csv', 'r', encoding='utf-8') as file_2:
    for element1 in file_1:
        element2 = file_2.readline().strip()
        if not element2:
            element2 = None
        if element1 not in final_dict:
            final_dict[element1.strip()] = element2
    content = file_2.read()
    if content:
        sys.exit(1)

with open('result.json', 'w', encoding='utf-8') as final_result:
    dict_as_string = json.dumps(final_dict, ensure_ascii=False)
    final_result.write(dict_as_string)
with open('result.json', 'r', encoding='utf-8') as file:
    content = file.read()
    result = json.loads(content)
print(result)
