rm ~/.pip
mkdir ~/.pip
echo "[global]
index-url = https://pypi.douban.com/simple

[install]
trusted-host = pypi.douban.com
" > ~/.pip/pip.conf