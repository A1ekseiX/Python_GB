import os

ROOT = os.path.dirname(__file__)
information = os.path.join(ROOT, 'content')

my_dict = {0: 0, 10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0, 1000000: 0}
keys = [0, 10, 100, 1000, 10000, 100000, 1000000]
for root, dirs, files in os.walk(information):
    for file in files:
        f_size = os.stat(os.path.join(root, file)).st_size
        if f_size == 0:
            result[0] += 1
            continue
        for i, key in enumerate(keys):
            if i == len(keys) - 1:
                break
            if key < f_size <= keys[i + 1]:
                result[keys[i + 1]] += 1
                break
print(my_dict)
