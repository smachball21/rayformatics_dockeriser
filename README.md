# Create Password
openssl passwd -6 -salt yourpass


# Update Password for user
echo "$SSH_USER:$SSH_PASSWORD"  | chpasswd -e
