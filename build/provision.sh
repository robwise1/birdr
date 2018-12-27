#!/usr/bin/env bash

# fix locales (sometimes perl scripts are broken if we do not do this)
export LANGUAGE="en_US.UTF-8"
echo 'LANGUAGE="en_US.UTF-8"' >> /etc/default/locale
echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale

# install python 3.7 prerequisites
apt-get install -y build-essential checkinstall
apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev
apt-get install -y libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev

# install python 3.7 from source
cd /tmp
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
tar xzf Python-3.7.0.tgz
cd Python-3.7.0
./configure --enable-optimizations
make install

# clean up after python installation
cd /tmp
rm Python-3.7.0.tgz
rm Python-3.7.0 -r

# install pip packages (for IDE autocompletion - dev_appserver.py will install them too)
python3 -m pip install -U pip
python3 -m pip install gunicorn
python3 -m pip install -r /vagrant/build/requirements.txt

# install curl
apt-get install -y curl


cd /home/vagrant

# install and configure supervisor
apt-get install -y supervisor
if ! [ -d /home/vagrant/logs ]; then
    mkdir /home/vagrant/logs
    touch /home/vagrant/logs/tmp
fi

# install postgres
sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key add -
apt-get update
apt-get install -y postgresql-9.6 postgresql-contrib-9.6 libpq-dev postgresql-server-dev-all

# make postgres accessible from the host machine
sed -i "s|#listen_addresses = 'localhost'|listen_addresses = '*'         |" /etc/postgresql/9.6/main/postgresql.conf
sed -i "s|host    all             all             127.0.0.1/32            md5|host    all             all             0.0.0.0/0            md5|" /etc/postgresql/9.6/main/pg_hba.conf
service postgresql restart

# # copy project config
# if ! [ -f /vagrant/config/env/dev.py ]; then
#     cp /vagrant/build/env.py /vagrant/config/env/dev.py
# fi

# create database and user
sudo -u postgres createdb birdr
sudo -u postgres psql -c "CREATE ROLE birdy SUPERUSER INHERIT CREATEDB LOGIN PASSWORD 'pass';"

# run migrations
cd /vagrant/project/core/
python3 manage.py migrate


# install android sdk 
sudo apt-get install unzip
mkdir /home/vagrant/android-sdk/
cd /home/vagrant/android-sdk/
sudo wget https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip
unzip sdk-tools-linux-4333796.zip 
sudo rm sdk-tools-linux-4333796.zip


# Install oracle crap - fixup repositories: this fails, but still works 
sudo apt-get install software-properties-common -y
yes | sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update 
# auto add license acceptence 
echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections
echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections
yes | sudo apt-get install oracle-java8-installer --allow-unauthenticated



# set paths 
export ANDROID_HOME=/home/vagrant/android-sdk/
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
export JAVA_HOME=$(update-alternatives --query javac | sed -n -e 's/Best: *\(.*\)\/bin\/javac/\1/p')



# sometimes space gets borked, clean up tmp/ 

# fetch android images
yes | sdkmanager "system-images;android-28;google_apis;x86"
sdkmanager "tools" "emulator" "platform-tools" "platforms;android-28" "build-tools;28.0.3" "extras;android;m2repository" "extras;google;m2repository"


# grab nvm to install node  & npm
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash
source ~/.bashrc
nvm install node

yes | npm install nativescript -g --unsafe-perm

# install nsv
npm install -g @vue/cli @vue/cli-init
