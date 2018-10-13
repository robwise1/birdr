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
python3 -m pip install -r /build/requirements.txt

# install curl
apt-get install -y curl

# # install cloud sdk
# export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
# echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
# curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
# apt-get update
# apt-get install -y google-cloud-sdk google-cloud-sdk-app-engine-python google-cloud-sdk-datastore-emulator

# install cloud sql proxy
cd /home/vagrant
# wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
# chmod +x cloud_sql_proxy
# mkdir /cloudsql
# chmod 777 /cloudsql

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
sudo -u postgres createdb recordlog
sudo -u postgres psql -c "CREATE ROLE birdr SUPERUSER INHERIT CREATEDB LOGIN PASSWORD 'pass';"

# run migrations
cd /vagrant
python3 ./manage.py migrate