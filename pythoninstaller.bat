echo Running python installer now.
TITLE Python Installer
IF EXIST pyinstaller.exe DEL /F pyinstaller.exe
curl https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe -o pyinstaller.exe
echo running installer now.
pyinstaller.exe /quiet InstallAllUsers=1 PrependPath=1
del pyinstaller.exe
pip install wheel
echo python install done.
cd ..
start compiler.bat
