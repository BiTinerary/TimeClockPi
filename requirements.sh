apt-get install python-dev -y
apt-get install python-pip -y
pip install --upgrade pip
pip install setuptools

cd OPi.GPIO
pip install .
cd ..

cd SPI-Py
pip install .
cd ..

python triggerRead.py