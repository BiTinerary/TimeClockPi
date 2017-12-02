apt-get update -y
apt-get upgrade -y
apt-get install python-dev -y
apt-get install python-pip -y
pip install --upgrade pip
pip install setuptools
pip install gspread
pip install oauth2client

cd OPi.GPIO
pip install .
cd ..

cd SPI-Py
pip install .
cd ..

python triggerRead.py
