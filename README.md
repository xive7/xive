rm -rf pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests

rm -rf xive
git clone https://github.com/xive7/xive.git
cd xive
chmod 777 xive
./xive
