@echo off
del killos.py
del launcher.bat
del requirements.txt
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/killos.py -O
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/requirements.txt -O
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/launcher.bat -O
pip install -r requirements.txt
del requirements.txt
