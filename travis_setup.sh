sudo apt-get update
sudo apt-get install -y ntpdate
sudo ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
sudo ntpdate a.ntp.br
