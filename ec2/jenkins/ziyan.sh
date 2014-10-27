useradd --create-home --shell /bin/bash ziyan
passwd -dl ziyan

mkdir -p /home/ziyan/.ssh
cat > /home/ziyan/.ssh/authorized_keys << EOF
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAnOVKs81FNkKUKmYoIaj1f2TMPRHUQKy3NxOURj4cVdxGWyofpl0/qdgAoPHqHxtQUgw6hlRFhXxFt5oWl72PbDcqGv2LxcoiFGcAfEZdeRFt89cwbtD6Dv8IA3DWZfTwoDlx9YE47LuPaYrSvBVkhQxBsFAMArIGolH0O5k+fMf+GZjn0ipu9g9SXyEW7TO/hqC1lKtg4jUyr4dC27VLWdBAOHtHe/iVdY3gJIekgJLGa3BtfTBMwRUTobO4s3Y8W4f9HHeAPFBjyhi8K46rpcMeVXRhIZkPsK+KEFRnXhJtGi7ejpRlRB5RcSKFvW6PLDe64OvE86jHjdUZSaFviQ== zhou@ziyan.info
EOF
chown -R ziyan:ziyan /home/ziyan
chmod -R go-w /home/ziyan/.ssh
gpasswd -a ziyan sudo

cat > /etc/sudoers.d/ziyan << EOF
ziyan ALL=(ALL) NOPASSWD:ALL
EOF

