import os
import shutil

root_direction = os.path.join(os.path.dirname(__file__), 'my_project')
dir_location = os.path.join(os.path.dirname(__file__), 'my_project', 'templates')

if not os.path.exists(dir_location):
    os.makedirs(dir_location)

for root, dirs, files in os.walk(root_direction):
    if root.count('templates'):
        for _dir in dirs:
            if not os.path.exists(os.path.join(dir_location, _dir)):
                os.makedirs(os.path.join(dir_location, _dir))
        for file in files:
            source_file = os.path.join(root, file)
            dir_file = os.path.join(dir_location, os.path.basename(root))
            if not os.path.dirname(source_file) == dir_file:
                shutil.copy(source_file, dir_file)
