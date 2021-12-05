import sys
import subprocess
import platform
import os

# implement pip as a subprocess:
print("Installing python packages")
subprocess.check_call([sys.executable, '-m', 'pip3', 'install',
'-r', 'requirements.txt'])

export_path = "PYTHONPATH=" + os.cwd()
os_name = platform.system()
if os_name == 'Darwin':
    subprocess.check_call(['export', 'LC_ALL=en_US.UTF-8'])
    subprocess.check_call(['export', 'LANG=en_us.UTF-8'])
