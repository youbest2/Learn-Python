## Start python
1. Open powershell from windows menu ( py --version)
2. py -m pip --version

## List all installed packages
py -m pip freeze

## Clear PIP catch 
py -m pip cache purge


## Install over proxy
py -m pip --proxy=Ab-proxy-special.patcon.com:8080 install numpy

py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade pip


## How to install .whl
1. Download whl to any_drive
2. Open powershell as admin and change path to any_drive 
   PS C:\> Set-Location -Path C:\Users\eja1kor\Downloads ->  Set-Location -Path any_drive
py -m pip --proxy=Ab-proxy-special.patcon.com:8080 install TA_Lib-0.4.21-cp37-cp37m-win_amd64.whl
Processing c:\users\eja1kor\downloads\ta_lib-0.4.21-cp37-cp37m-win_amd64.whl
Installing collected packages: TA-Lib
Successfully installed TA-Lib-0.4.21
