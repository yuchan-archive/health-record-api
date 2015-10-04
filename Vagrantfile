# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
curl -L https://github.com/docker/compose/releases/download/1.4.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
SCRIPT

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision "docker"
  config.vm.provision "shell", inline: $script
end
