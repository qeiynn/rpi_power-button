#! /bin/sh

sudo systemctl stop hostap &&

#comment lines 61-63
sudo sed -i '61,63 s/^/#/' /etc/dhcpcd.conf

#uncomment lines 61-63 WARNING: ALSO REMOVES SPACES
sudo sed -i "61,63 s/# *//" /etc/dhcpcd.conf
