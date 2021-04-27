FROM debian:latest
RUN ln -snf /usr/share/zoneinfo/"Europe/Paris" /etc/localtime && echo "Europe/Paris" > /etc/timezone
RUN apt -yqq update && apt -yqq upgrade && apt -yqq install mariadb-client mariadb-server wget tar software-properties-common yarn composer gnupg gnupg1 gnupg2
RUN wget -q https://packages.sury.org/php/apt.gpg -O- | apt-key add -
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/php.list
RUN apt -yqq install php php-cgi php-mysqli php-pear php-mbstring libapache2-mod-php php-common php-phpseclib php-mysql php-curl
ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]
