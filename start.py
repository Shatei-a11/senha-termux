import os
os.chdir('/data/data/com.termux/files/home/senha-termux')
os.system('cp caminho /data/data/com.termux/files/usr/etc/')
os.chdir('/data/data/com.termux/files/usr/etc/')
os.system('rm -rf bash.bashrc')
os.system('mv caminho bash.bashrc')
