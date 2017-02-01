FROM python:3.4-slim

MAINTAINER Masood Ahmed "masood.ahmed@galepartners.com"

EXPOSE 8000

ENV HOME /root
ENV APP_HOME /application/
ENV C_FORCE_ROOT=true

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential \
        apt-transport-https \
        ca-certificates \
        git

# Clean up APT and bundler when done.
RUN rm -rf /usr/share/doc \
           /usr/share/man \
           /usr/share/groff \
           /usr/share/info \
           /usr/share/lintian \
           /usr/share/linda \
           /usr/share/locale/ \
           /var/cache/man

# Clean up APT when done.
RUN apt-get clean
RUN apt-get autoclean
RUN apt-get autoremove
RUN rm -rf /var/lib/apt/lists/* \
           /tmp/* \
           /var/tmp/*

RUN mkdir -p $HOME/.ssh
ADD id_rsa $HOME/.ssh/id_rsa
RUN chmod 600 $HOME/.ssh/id_rsa && chmod 700 $HOME/.ssh
RUN ssh-keyscan github.com >> $HOME/.ssh/known_hosts

RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

ADD ./src/requirements/base.txt $APP_HOME
ADD ./src/requirements/dev.txt $APP_HOME
ADD ./src/requirements/prod.txt $APP_HOME

RUN mkdir $APP_HOME/requirements
ADD ./src/requirements/* $APP_HOME/requirements/

RUN pip install -r dev.txt

RUN rm -rf requirements
RUN rm -rf requirements.txt

ADD package.json $APP_HOME
RUN npm install

RUN rm -rf id_rsa
RUN rm -rf $HOME/.ssh

ADD . $APP_HOME
