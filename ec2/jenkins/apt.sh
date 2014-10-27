export DEBIAN_FRONTEND=noninteractive

apt-get -y update
apt-get -y install linux-headers-$(uname -r) build-essential git vim htop

# reboot
# sleep 60
