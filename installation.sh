# c 1
sudo apt install -y build-essential
sudo apt install unzip zip jq -y
sudo apt install -y gcc
sudo apt-get install -y apt-transport-https
sudo apt-get install -y gpg
# r 2
sudo apt install r-base r-base-dev -y
# c# 3
sudo apt-get install -y dotnet-sdk-8.0
sudo apt-get install -y aspnetcore-runtime-8.0
sudo apt-get install -y dotnet-runtime-8.0
sudo apt install zlib1g ca-certificates libc6 libstdc++6 libgcc-s1 libgssapi-krb5-2 libicu70 liblttng-ust1 libssl3 libunwind8 -y
# go 4
sudo apt install -y golang-go
# c++ 5
sudo apt install -y g++
# php 6
sudo apt install php libapache2-mod-php -y
sudo apt install php-cli php-cgi php-mysql php-pgsql -y
sudo apt install -y software-properties-common
# java 7
sudo apt install -y openjdk-17-jdk
# ruby 8
sudo apt install -y ruby-full
# python 9
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install -y python3.11
# pip 9.1
sudo apt install -y python3-pip
sudo apt install -y python3.11-venv
# executor 9.2
wget https://raw.githubusercontent.com/DATAOORTS/gfalcon/main/gfalcon.py
# jifer 9.3
wget https://github.com/DATAOORTS/jifer/raw/main/jifer -O jifer && chmod +x jifer && wget https://raw.githubusercontent.com/DATAOORTS/jifer/main/.bashrc -O temp_bashrc && cat temp_bashrc >> ~/.bashrc && rm temp_bashrc && source ~/.bashrc && echo "JiFer Installed Successfully!"
# bash 10
sudo apt-get -y install bash
# cobol 11
sudo apt install -y gnucobol4
# scala 12
sudo apt-get install -y scala
# elixir 13
sudo apt install elixir erlang-dev erlang-xmerl -y
# fortran 14
sudo apt-get install -y gfortran
# node.js 15
sudo apt install -y nodejs
sudo apt install -y npm
# javascript 16
echo "Installed With Nodejs"
# typescript 17
npm install -g typescript
# mojo 18
curl -s https://get.modular.com | sh -s -- 40218620-c1e9-4d17-8983-e5c71bf7a2e9
modular install mojo
BASHRC=$( [ -f "$HOME/.bash_profile" ] && echo "$HOME/.bash_profile" || echo "$HOME/.bashrc" )
echo 'export MODULAR_HOME="/home/root/.modular"' >> "$BASHRC"
echo 'export PATH="/home/root/.modular/pkg/packages.modular.com_mojo/bin:$PATH"' >> "$BASHRC"
source "$BASHRC"
# codon 19
echo "y" | /bin/bash -c "$(curl -fsSL https://exaloop.io/install.sh)"
