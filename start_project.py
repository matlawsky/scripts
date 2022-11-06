# Script to quickly create environment for a new python project on windows
# creates folder for project, virtual environment, .gitignore and vs code python configuration
# run it with "python start_project.py -f chosen_folder_name -v chosen_virtual_environment_name -p chosen_parent_folder_path"
#
# argument 1 - projects folder (-f) (required)
# argument 2 - virtualenv name (-v) (required)
# argument 3 - path to project folder parent directory (-p) (required)


import os
import subprocess
import argparse

parser = argparse.ArgumentParser(description="create project")
parser.add_argument("-f", dest="folder", help="projects folder name", type=str)
parser.add_argument("-v", dest="venv", help="virtualenv name", type=str, required=True)
parser.add_argument("-p", dest="path", help="path to project folder parent directory", type=str, required=True)
parsed_args = parser.parse_args()

try:
    folder_name = parsed_args.folder
    venv_name = parsed_args.venv
    given_path = parsed_args.path
    if ':' in given_path:
        print(given_path)
    elif '.' in given_path[0] or '\\' in given_path[0]:
        given_path = os.path.abspath(given_path)
        print(given_path)
    else: 
        print("Unknown")


except:
    print("Wrong path")


new_path = given_path.replace('\\', '/')
parse_path_for_code = '/'.join([new_path, folder_name, venv_name, "Scripts/python.exe"])

gitignore = f'''
{venv_name}
.vscode
'''

interpreter = '''
{
  "python.defaultInterpreterPath": "%s"
}
'''%(parse_path_for_code)

commands =  f'''cd {given_path} \n
mkdir {folder_name} \n
cd {folder_name} \n
python -m venv {venv_name} \n
mkdir .vscode \n
'''

process = subprocess.Popen('cmd.exe',
                shell=False,
                universal_newlines=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                )
out, err = process.communicate(commands)

with open(f"{given_path}/{folder_name}/.gitignore", mode='x', encoding = 'utf-8') as g:
    g.write(gitignore)

with open(f"{given_path}/{folder_name}/.vscode/settings.json", mode='x', encoding = 'utf-8') as p:
    p.write(interpreter)


if out:
    print("OUTPUT")
    print(out)
if err:
    print("ERROR")
    print(err)



