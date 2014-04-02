#!/bin/sh

printf "Content-type: text/plain\n\n"

chown www-data 755 /var/www/cgi-bin
chmod 755 /var/www/cgi-bin

echo "hello" > newfile

date
ls -l date.cgi
## date.txt is a hard link to date.cgi
