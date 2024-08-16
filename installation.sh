# c
sudo apt install -y build-essential
sudo apt install -y gcc
sudo apt-get install -y apt-transport-https
sudo apt-get install -y gpg
# r
sudo apt install r-base r-base-dev -y
# c#
sudo apt-get install -y dotnet-sdk-8.0
sudo apt-get install -y aspnetcore-runtime-8.0
sudo apt-get install -y dotnet-runtime-8.0
sudo apt install zlib1g ca-certificates libc6 libstdc++6 libgcc-s1 libgssapi-krb5-2 libicu70 liblttng-ust1 libssl3 libunwind8 -y
# go
sudo apt install -y golang-go
# c++
sudo apt install -y g++
# php
sudo apt install php libapache2-mod-php -y
sudo apt install php-cli php-cgi php-mysql php-pgsql -y
sudo apt install -y software-properties-common
# java
sudo apt install -y openjdk-17-jdk
# ruby
sudo apt install -y ruby-full
# python
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install -y python3.11
# pip
sudo apt install -y python3.11-venv
# julia
sudo add-apt-repository ppa:julia/julia
sudo apt install -y julia
# executor
wget https://raw.githubusercontent.com/DATAOORTS/gfalcon/blob/main/gfalcon.py
# jifer
wget https://github.com/DATAOORTS/jifer/raw/main/jifer -O jifer && chmod +x jifer && wget https://raw.githubusercontent.com/DATAOORTS/jifer/main/.bashrc -O temp_bashrc && cat temp_bashrc >> ~/.bashrc && rm temp_bashrc && source ~/.bashrc && echo "JiFer Installed Successfully!"
# codon
/bin/bash -c "$(curl -fsSL https://exaloop.io/install.sh)"
# rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup toolchain install stable
# dart
wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo gpg --dearmor -o /usr/share/keyrings/dart.gpg
echo 'deb [signed-by=/usr/share/keyrings/dart.gpg arch=amd64] https://storage.googleapis.com/download.dartlang.org/linux/debian stable main' | sudo tee /etc/apt/sources.list.d/dart_stable.list
sudo apt-get install dart
# bash
sudo apt-get -y install bash
# cobol
sudo apt install -y gnucobol4
# scala
sudo apt-get install -y scala
# elixir
sudo apt install elixir erlang-dev erlang-xmerl -y
# kotlin
curl -s https://get.sdkman.io | bash
sdk install kotlin
# fortran
sudo apt-get install -y gfortran
# node.js
sudo apt install -y nodejs
sudo apt install -y npm
# javascript
echo "Installed With Nodejs"
# typescript
npm install -g typescript
