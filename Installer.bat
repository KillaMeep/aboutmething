@echo off
mkdir killos
cd killos
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/killos.py -O
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/requirements.txt -O
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/launcher.bat -O
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/updater.bat -O
pip install -r requirements.txt
del requirements.txt
cd ..
START /B CMD.EXE /D /C "PING.EXE -n 5 127.0.0.1 && DEL Installer.bat"
