@echo off
:start
cls

set python_ver=3.11

python ./get-pip.py

cd \
cd \python%python_ver%\Scripts\
pip install time
pip install os
pip install colorama
pip install pystyle
pip install dhooks
pip install ctypes
pip install requests
pip install discord_webhook
pip install json
pip install random
pip install argparse
pip install selenium
pip install datetime
pip install googlesearch-python

pause
exit