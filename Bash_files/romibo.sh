#udpate the CHIP
sudo apt-get update

#install python
sudo apt-get install python

#install mosquitto & clients
sudo apt-get install mosquitto
sudo apt-get install mosquitto-clients

#install espeak
sudo apt-get install espeak

#install git
sudo apt-get install git-all

#install pip
sudo apt-get install python-pip

#install paho-mqtt
pip install paho-mqtt

#install tkinter
sudo apt-get install python-tk

#install CHIP_IO
sudo apt-get install git build-essential python-dev flex bison chip-dt-overlays -y
git clone git://github.com/xtacocorex/CHIP_IO.git
cd CHIP_IO
sudo python setup.py install
cd

#install MQTT for wifi connection
sudo apt-get install dnsmasq 
cd /home/chip/Romibo-V8/wifi
sudo cp access_point.conf /etc/dnsmasq.d
sudo cp interfaces /etc/network
cd /
sudo /etc/init.d/dnsmasq restart 
cd /home/chip/Romibo-V8/wifi
sudo cp hostapd.conf /etc
cd /
sudo hostapd /etc/hostapd.conf 
cd /home/chip/Romibo-V8/wifi
sudo cp systemd.service /lib/systemd/system 
cd /
sudo update-rc.d hostapd disable 
sudo systemctl daemon-reload 
sudo systemctl enable systemd
sudo systemctl start systemd
systemctl status systemd

#install unclutter to remove mouse pointer
sudo apt-get install unclutter

#write cronjobs for running script on startup
(sudo crontab -l; echo "@reboot sh /home/chip/Romibo-V8/Bash_files/launcher1.sh > /home/chip/Romibo-V8/logs/cronlog 2>&1";) | sudo crontab -
(sudo crontab -l; echo "@reboot sh /home/chip/Romibo-V8/Bash_files/launcher2.sh > /home/chip/Romibo-V8/logs/cronlog2 2>&1";) | sudo crontab -
(sudo crontab -l; echo "@reboot sh /home/chip/Romibo-V8/Bash_files/launcher3.sh > /home/chip/Romibo-V8/logs/cronlog3 2>&1";) | sudo crontab -
