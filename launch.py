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
    #TODO: handle error when venv does not exist by creating one
    #TODO: handle permission error as fatal
     
def launch():
    print("Running: ", __file__)
    if in_venv():
        print("In virtual environment: ", sys.prefix)
        subprocess.run([sys.executable, os.path.join(os.getcwd(), 'stock-ticker-list.py')])
        exit()
    else:
        enter_venv()

launch()

#TODO: Check dependencies of all scripts, install missing modules (prompt user for permission if the script didnt create its own virtual environment)
#TODO: Check if the correct version of python is running. If not, offer user to install it.
#TODO: Flags for enabling/disabling venv check, version check, module check, and turn them off by default