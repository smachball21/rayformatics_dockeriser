FROM debian:latest 
RUN apt-get update 
RUN apt-get install -y software-properties-common ca-certificates apt-transport-https dirmngr curl wget git zip 
RUN wget -q https://packages.sury.org/php/apt.gpg -O- | apt-key add - 
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/php.list 
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y php7.4-fpm php7.4-cli php7.4-common php7.4-curl php7.4-mbstring php7.4-mysql php7.4-xml php7.4-intl php7.4-gd php7.4-zip php7.4-redis php7.4-igbinary
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php composer-setup.php --install-dir=/usr/bin --filename=composer
RUN php -r "unlink('composer-setup.php');"
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xF1656F24C74CD1D8
RUN add-apt-repository 'deb [arch=amd64] http://mariadb.mirror.liquidtelecom.com/repo/10.4/debian buster main/'
RUN apt-get -y update
RUN apt-get install -y mariadb-server
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt -yqq update
RUN apt install -yqq yarn
RUN apt -yqq update && apt -yqq install ssh nano libpam-chroot rsyslog && mkdir /home/public/ && touch /home/public/DO_NOT_UPLOAD_HERE
RUN apt install -yqq composer yarn curl
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - && apt-get -yqq install nodejs
CMD service rsyslog start && \
useradd -m $SSH_USER --home="/home/public" && \
echo "$SSH_USER:$SSH_PASSWORD" | chpasswd --encrypted && \
service ssh start && \
tail -f /var/log/auth.log &&  \
touch /home/public/DO_NOT_UPLOAD_HERE && \
chown -hR $SSH_USER:$SSH_USER /home/public
