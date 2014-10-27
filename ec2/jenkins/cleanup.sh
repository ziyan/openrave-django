# cleanup
apt-get -y autoremove

# disable root
passwd -dl root
rm -rf /home/root/.ssh

# disable ubuntu
passwd -dl ubuntu
rm -rf /home/ubuntu/.ssh
rm -f /etc/sudoers.d/90-cloud-init-users

# delete ubuntu user after first boot
cp /etc/rc.local /etc/rc.local.bak
cat > /etc/rc.local << EOF
#!/bin/sh -e
rm -rf /root/.ssh

rm -rf /home/ubuntu
userdel ubuntu

mv -f /etc/rc.local.bak /etc/rc.local
EOF

exit
