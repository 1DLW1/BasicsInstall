import subprocess, time

commands = ['sudo apt update && sudo apt upgrade', 'sudo apt install build-essential','sudo apt install git', 'sudo apt install vscode', 'sudo ufw enable'
            ,'sudo apt-get install selinux-basics selinux-policy-default', ]

for command in commands:
    time.sleep(1)
    subprocess.run(command, shell=True)
print('\nInstalation success!')