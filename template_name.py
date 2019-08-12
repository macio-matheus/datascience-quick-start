import os

dir = f'./'
files = ['docker-compose.yml', 'README.md']
tag_old = '<project_name>'
project_name = '<project_name>'
for file_name in files:

    print(f'{dir}{file_name}')

    with open(f'{dir}{file_name}') as f:
        update_file = f.read().replace('A', 'Orange')

    with open(f'{dir}{file_name}', 'w') as f:
        f.write(update_file)
