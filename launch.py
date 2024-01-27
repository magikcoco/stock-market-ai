import sys
import os
import subprocess

def in_venv():
    return sys.prefix != sys.base_prefix

def enter_venv():
    print("Not in virtual environment. Attmepting to switch...")
    virtual_env_path = "./venv/"
    virtual_env_python = os.path.join(virtual_env_path, "bin", "python3")
    os.execl(virtual_env_python, virtual_env_python, *sys.argv)
     
def launch():
    print("Running: ", __file__)
    if in_venv():
        print("In virtual environment: ", sys.prefix)
        subprocess.run([sys.executable, os.path.join(os.getcwd(), 'stock-ticker-list.py')])
        exit()
    else:
        enter_venv()

launch()