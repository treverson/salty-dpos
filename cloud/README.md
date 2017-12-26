##### Install salt-cloud
```
sudo apt install salt-cloud
```

##### Edit /etc/salt/cloud to include the following default minion config
```
minion:
  master: <master-ip-addr>
  mine_functions:
    external_ip:
      - mine_function: network.interface_ip
      - eth0
    internal_ip:
      - mine_function: network.interface_ip
      - eth1
```
##### Create a key that will be used to login post creation by salt-ssh
##### to bootstrap salt
```
sudo mkdir -m 700 /etc/salt/pki/cloud
sudo ssh-keygen -t rsa -N "" -f /etc/salt/pki/cloud/do.pem
sudo chmod 600 /etc/salt/pki/cloud/do.pem
```

##### Create the cloud conf directory
```
sudo mkdir -p /etc/salt/cloud.providers.d
```

##### Edit the digital_ocean configuration file to include
##### the token and the key
##### https://www.digitalocean.com/community/tutorials/how-to-use-the-digitalocean-api-v2
sudo vi /etc/salt/cloud.providers.d/do.conf
```
do:
  driver: digital_ocean
  personal_access_token: <do_access_token_see_link_above>
  ssh_key_file: /etc/salt/pki/cloud/do.pem
  ssh_key_names: do-bootstrap
  script: bootstrap-salt      
```

##### Edit the base conf profiles as you see fit
##### this example has ubuntu 16.04x64, 1gb size ($10) with no private networking
##### or ipv6
sudo vi /etc/salt/cloud.profiles.d/base-crypto.conf
```
base-crypto:                                                                                                                                       
  provider: do
  image: ubuntu-16-04-x64
  size: 1gb
  location: nyc3
  private_networking: False
  ipv6: False

lisk-main:
  extends: base-crypto
  minion:
    grains:
      liskenv: main

lisk-test:
  extends: base-crypto
  minion:
    grains:
      liskenv: test

shift-main:
  extends: base-crypto
  minion:
    grains:
      shiftenv: main

ark-main:
  extends: base-crypto
  minion:
    grains:
      arkenv: main
```

##### To see all the available options you can use the following commands
<pre>
<b>List all sizes available</b>
sudo salt-cloud --list-sizes do

<b>List all images available</b>
sudo salt-cloud --list-images do

<b>List all profiles available</b>
sudo salt-cloud --list-profiles do
</pre>

##### Finally, create a droplet based on the profile outlined in base-crypto.conf
```
sudo salt-cloud -p lisk-main lisk-do-test
```

