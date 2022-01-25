@ECHO OFF
del killos.exe
mkdir build
cd build
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/killos.py -O
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/requirements.txt -O
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/launcher.bat -O
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/updater.bat -O
pip install -r requirements.txt
pip install auto-py-to-exe
del requirements.txt
pyinstaller --noconfirm --onefile --console killos.py
cd dist && copy killos.exe ..\.. && cd ..\..
rmdir /Q /S build
exit