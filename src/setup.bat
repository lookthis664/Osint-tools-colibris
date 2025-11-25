@echo off


:start
cls

set python_ver=3.11
python ./get-pip.py

cd \
cd \python%python_ver%\Scripts\
python -m pip install colorama playwright BeautifulSoup requests bs4
python -m playwright install


pause
exit
