FROM debian:latest
RUN apt -yqq update && apt -yqq install ssh nano libpam-chroot rsyslog && mkdir /home/public/ && touch /home/public/DO_NOT_UPLOAD_HERE
RUN apt install -yqq composer nodejs yarn 
RUN apt-get update && apt-get install -y php7.3-fpm php7.3-cli php7.3-common php7.3-curl php7.3-mbstring php7.3-mysql php7.3-xml php7.3-intl php7.3-gd php7.3-zip php7.3-redis php7.3-igbinary
RUN cd /home/public/ && composer global require laravel/installer
RUN composer create-project --prefer-dist laravel/laravel /home/public/public_html/project
RUN mv /home/public/public_html/project/* /home/public/public_html/ 
RUN cd /home/public/public_html/project && find . -name . -o -exec sh -c 'mv -- "$@" "$0"' /home/public/public_html/ {} + -type d -prune
RUN rm -rf /home/public/public_html/project/
CMD service rsyslog start && \
useradd -m $SSH_USER --home="/home/public" && \
echo "$SSH_USER:$SSH_PASSWORD" | chpasswd --encrypted && \
service ssh start && \ 
tail -f /var/log/auth.log &&  \
touch /home/public/DO_NOT_UPLOAD_HERE && \
chown -hR $SSH_USER:$SSH_USER /home/public
