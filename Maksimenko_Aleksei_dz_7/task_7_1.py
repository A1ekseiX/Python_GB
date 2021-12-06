import os

try:
    ROOT = os.path.dirname(__file__)
    dir_name = 'my_project'
    file_path = [os.path.join(dir_name, "settings"), os.path.join(dir_name, "mainapp"),
                 os.path.join(dir_name, "adminapp"), os.path.join(dir_name, "authapp")]
    for file in file_path:
        os.makedirs(os.path.join(ROOT, file))
except FileExistsError:
    print('Files already exist')
