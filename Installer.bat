@echo off
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/killos.py -O
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/requirements.txt -O
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/launcher.bat -O
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/updater.bat -O
pip install -r requirements.txt
del requirements.txt
del Installer.bat
