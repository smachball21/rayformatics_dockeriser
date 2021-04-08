FROM debian:latest
RUN apt -yqq update && apt -yqq install ssh nano libpam-chroot rsyslog && mkdir /home/public/ && touch /home/public/DO_NOT_UPLOAD_HERE
CMD service rsyslog start && \
useradd -m $SSH_USER --home="/home/public" && \
echo "$SSH_USER:$SSH_PASSWORD" | chpasswd --encrypted && \
service ssh start && \ 
tail -f /var/log/auth.log &&  \
touch /home/public/DO_NOT_UPLOAD_HERE && \
chown -hR $SSH_USER:$SSH_USER /home/public
