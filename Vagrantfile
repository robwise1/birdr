# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
    config.vm.box = "debian/stretch64"
    config.vm.synced_folder ".", "/vagrant", type: "virtualbox"

    config.vm.network :forwarded_port, guest: 8000, host: 8000 # Default web server.
    config.vm.network :forwarded_port, guest: 8001, host: 8001 # Open for debugging sessions.
    config.vm.network :forwarded_port, guest: 1080, host: 8002 # Mail catcher UI.
    config.vm.network :forwarded_port, guest: 5432, host: 8003 # PostgreSQL port for external connections.
    
    config.vm.provision :shell, path: "build/provision.sh"
    config.vm.provision :shell, path: "build/boot.sh", run: "always"

    config.vm.provider "virtualbox" do |vb|
        vb.memory = "1024"
    end
end