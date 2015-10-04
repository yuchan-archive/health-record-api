# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
curl -L https://github.com/docker/compose/releases/download/1.4.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
SCRIPT

Vagrant.configure(2) do |config|
  config.vm.box = 'phusion/ubuntu-14.04-amd64'
  config.vm.provision 'docker'
  config.vm.provision 'shell', inline: $script
  config.vm.synced_folder 'src/', '/src/'
  config.vm.synced_folder '.', '/vagrant', disabled: true
  config.vm.network 'forwarded_port', guest: 3000, host: 3000
end
