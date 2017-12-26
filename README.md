# Table of contents


* [Installation Method 1: Master & Minion](#master-and-minion-installation)
  * [Detailed Guide: Master & Minion](#master-and-minion-installation-detailed)
* [Installation Method 2: Master-less Minion](#masterless-minion-installation)
  * [Detailed Guide: Master-less minion](#masterless-minion-installation-detailed.md)
* [Installation Method 3: Salt SSH Minions](#salt-ssh-minion-installation)
  * [Detailed Guide: Salt SSH minions](#salt-ssh-installation-detailed.md)
* [Minion Bootstrap Guide](#minion-bootstrap-guide)
  * [Detailed Bootstrap Guide](#minion-bootstrap-guide-detailed)
* [Minion Hardening Guide](#minion-hardening-guide)
  * [Detailed Hardening Guide](#minion-hardening-guide-detailed)
* [Salty DPOS Node Management](#salty-dpos-node-management )
  * [Salty DPOS GET Execution Module](#salty-dpos-get-execution-module)
    * [Quick Reference Guide](#salty-dpos-get-quick-reference-guide)
    * [Detailed Guide](#salty-dpos-get-detailed-guide)
  * [Salty DPOS POST Execution Module](#salty-dpos-post-execution-module)
    * [Quick Reference Guide](#salty-dpos-post-quick-reference-guide)
    * [Detailed Guide](#salty-dpos-post-detailed-guide)
  * [Cryptoadmin Execution Module](#cryptoadmin-execution-module)
    * [Quick Reference Guide](#cryptoadmin-quick-reference-guide)
    * [Detailed Guide](#cryptoadmin-detailed-guide)
  * [dposrun runner Module](#dposrun-runner-module)
    * [Quick Reference Guide](#dposrun-quick-reference-guide)
    * [Detailed Guide](#dposrun-detailed-guide)

# Master and Minion Installation

Warning (ONE TIME SETUP - kinda :p)
This step is to setup a master and minion infrastructure please make sure
you understand what that means

On the master:

Install salt-master and salt-minion on the master
```
sudo apt install salt-master salt-minion
```

OR

Install salt with bootstrap script [Official salt script](https://docs.saltstack.com/en/latest/topics/tutorials/salt_bootstrap.html)

Create an iptables chain for saltstack comminucation
blocking all traffic other than the accepted minions from the master

```
iptables -N saltstack
iptables -A saltstack --src <node1 ip address> -j ACCEPT
iptables -A saltstack --src <node2 ip address> -j ACCEPT
iptables -A saltstack -i lo -p tcp -m multiport --dports 4505,4506 -j ACCEPT
iptables -A saltstack -j DROP 
iptables -I INPUT -p tcp -m multiport --dport 4505,4506 -j saltstack
```

```
wget -O bootstrap-salt.sh https://bootstrap.saltstack.com
sudo sh bootstrap-salt.sh -M -A <master ip or domain name> stable
```

On the MINION:

Install salt-minion on the minion nodes
```
sudo apt install salt-minion
```
OR

Install salt with bootstrap script [Official salt script](https://docs.saltstack.com/en/latest/topics/tutorials/salt_bootstrap.html)

```
wget -O bootstrap-salt.sh https://bootstrap.saltstack.com
sudo sh bootstrap-salt.sh -A <salt master ip address or domain name> stable
```

On the MASTER
Accept minion keys

```
salt-key -a minion1 -y
salt-key -a minion2 -y
salt-key -a minion3 -y
```

Add grains for crypto platform targeting
```
salt 'target' grains.setval liskenv main
or
salt 'target' grains.setval oxyenv main
or
salt 'target' grains.setval shiftenv main
```

ISSUES

Change master address on the /etc/salt/minion
```
sudo sed -i 's/#master: salt/master: <master_ip_address_or_domain_name>/g' /etc/salt/minion
```

## Master and Minion Installation Detailed


For a detailed setup please follow this link:
[LINK](master-and-minion-installation-detailed.md)


# Masterless Minion Installation

Warning (ONE TIME SETUP - kinda :D)
This section will walk you through installing salt without a master please make sure
you understand what that means.
If you completed the steps in the previous section there is no need to do this. 

[Reference](https://docs.saltstack.com/en/latest/topics/tutorials/quickstart.html)

Install salt from repo
```
sudo apt install salt-minion
```

OR

Install salt-minion with bootstrap script [Official salt script](https://docs.saltstack.com/en/latest/topics/tutorials/salt_bootstrap.html)

```
wget -O bootstrap-salt.sh https://bootstrap.saltstack.com
sudo sh bootstrap-salt.sh stable
```

Clone this repo and change directory
```
git clone https://github.com/slasheks/dpos-saltstack.git
cd dpos-saltstack
```

Make the minion service masterless and restart the service:
```
sudo sed -i 's/#file_client: remote/file_client: local/g' /etc/salt/minion
sudo systemctl restart salt-minion
```

Set the environment by changing the grain target in the minion config file

For LSK testnet:
```
sed -i 's/env: test/liskenv: test/g' minion
```

For LSK mainnet:
```
sed -i 's/env: test/liskenv: main/g' minion
```

For OXY testnet:
```
sed -i 's/env: test/oxyenv: test/g' minion
```

For OXY mainnet:
```
sed -i 's/env: test/oxyenv: main/g' minion
```

For LWF testnet:
```
sed -i 's/env: test/lwfenv: test/g' minion
```

For LWF testnet:
```
sed -i 's/env: test/lwfenv: main/g' minion
```

For SHIFT:
```
sed -i 's/env: test/shiftenv: test/g' minion
```

For SHIFT:
```
sed -i 's/env: test/shiftenv: main/g' minion
```

Finally you can use salty-dpos
```
sudo salt-call --local cryptoadmin.status
local:
    -
    pid:
        8932
    retcode:
        0
    stderr:
    stdout:
        √ Lisk is running as PID: 1862
        Current Block Height:  4002813
```

# Masterless Minion Installation Detailed

For a detailed setup please follow this link:
[LINK](masterless-minion-installation-detailed.md)

# Salt SSH Minion Installation

Warning (ONE TIME SETUP - kinda :D)
This section will walk you through installing salt without a master please make sure
you understand what that means.
If you completed the steps in the previous section there is no need to do this. 

[Reference](https://docs.saltstack.com/en/latest/topics/tutorials/quickstart.html)

COMING SOON-ish

# Salt SSH Minion Installation Detailed

For a detailed setup please follow this link:
[LINK](salt-ssh-installation-detailed.md) (coming soon-ish)


# Minion Bootstrap Guide


Once one of the above steps is complete you can "bootstrap" a minion with 
defaults that will be used by


Install and manage above dependencies on the dpos-delegate1 minion
```
sudo salt 'dpos-delegate1' state.highstate
```

WARNING if you ran the step above there is no need to do the ones below
this is only used if you do not want to configure all the defaults

Add swap based on available memory
```
sudo salt 'dpos-delegate1' state.sls default.swap
```

Install package dependencies on the dpos-delegate1 minion
```
sudo salt 'dpos-delegate1' state.sls default.packages
```

Install python dependencies on the dpos-delegate1 minion
```
sudo salt 'dpos-delegate1' state.sls default.python
```

Manage sysstat and dependencies on the dpos-delegate1 minion
```
sudo salt 'dpos-delegate1' state.sls default.sysstat
```

Add management user to dpos-delegate1 minion
```
sudo salt 'dpos-delegate1' state.sls default.users
```

Set the timezone from pillar data
```
sudo salt 'dpos-delegate1' state.sls default.timez
```

Manage ssh and dependencies on the dpos-delegate1 minion
```
sudo salt 'dpos-delegate1' state.sls default.ssh
```

# Minion Hardening Guide

The hardening guide uses multiple industry standards, makes them salty, ready and available
to be applied to your nodes. 

[Hardening Readme](salt/harden/README.md)

## Minion Hardening Guide Detailed

[Lynis](salt/harden/lynis/README.md)

# Salty DPOS Node Management

DPOS execution modules (lisk/oxy/lwf/shift) (BETA)

## Salty DPOS GET Execution Module

### Salty DPOS GET Quick Reference Guide

GET sync information from the target API
```
salt 'dpos-delegate1' salty_dpos_get.sync
```

GET height information from the target API
```
salt 'dpos-delegate1' salty_dpos_get.height
```

GET status information from the dpos API
```
salt 'dpos-delegate1' salty_dpos_get.status
```

GET consensus information from the target API
```
salt 'dpos-delegate1' salty_dpos_get.consensus
```

GET peer version information from the dpos API
```
salt 'dpos-delegate1' salty_dpos_get.version
```

GET peers information from the dpos API
```
salt 'dpos-delegate1' salty_dpos_get.peer_list
```

GET forging status based on a username
```
salt 'dpos-delegate1' salty_dpos_get.forging_status slasheks
```

GET network height (NOTE: This is an internal query of the DB)
```
salt 'dpos-delegate1' salty_dpos_get.network_height
```

GET the difference between the heights in the DB and your node
```
salt 'dpos-delegate1' salty_dpos_get.height_diff
```

GET True if the node has consensus > 80 and height difference of < 1
```
salt 'dpos-delegate1' salty_dpos_get.failover_candidate
```

GET delegate information based on delegate name
```
salt 'dpos-delegate1' salty_dpos_get.delegate slasheks
```

GET forged blocks based on delegate name
```
salt 'dpos-delegate1' salty_dpos_get.forged_blocks slasheks
```

GET the last forged block based on delegate name
```
salt 'dpos-delegate1' salty_dpos_get.last_forged_block slasheks
```

### Salty DPOS GET Detailed guide

[LINK](salt/_modules/salty-dpos-get-detailed-guide.md)


## Salty DPOS POST execution module

Requirements:
  pillar:
    secret: <forging delegate passphrase>

To protect your passphrase in pillar data (data at rest) please follow
the following guide: [GPG encrypted pillar data](gpg.md)

### Salty DPOS POST Quick Reference Guide

Enable forging on a node based on delegate name
```
salt 'dpos-delegate1' salty_dpos_post.enable_forging
```

Disable forging on a node based on delegate name
```
salt 'dpos-delegate1' salty_dpos_post.disable_forging
```

### Salty DPOS POST Detailed Guide

[LINK](salt/_modules/salty-dpos-post-detailed-guide.md)

## Cryptoadmin Execution Module

(using the shell tool provided by the platform)

### Cryptoadmin Quick Reference Guide

Get the help messages from the platform shell tool
```
salt 'dpos-delegate1' cryptoadmin.help
```

Rebuild the dpos database
```
salt 'dpos-delegate1' cryptoadmin.rebuild
```

Reload the dpos crypto platform process
```
salt 'dpos-delegate1' cryptoadmin.reload
```

Start the dpos crypto platform process
```
salt 'dpos-delegate1' cryptoadmin.start
```

Get the status of the process
```
salt 'dpos-delegate1' cryptoadmin.status
```

Stop the dpos platform process
```
salt 'dpos-delegate1' cryptoadmin.stop
```


### Cryptoadmin Detailed Guide

[LINK](salt/_modules/cryptoadmin-detailed-guide.md)

## dposrun runner Module

Run commands from the master with visibility of the whole infrastructure

Requirements:

  pillar:
    # For enable/disable forging:
    secret: <forging delegate passphrase>
    # For notify slack api key
    slack_api: <slack api key>

### dposrun Quick Reference Guide

Notify via slack if last block was generated more than 20m ago
```
salt-run dposrun.missed_block_notify lisk slasheks
```

Notify via slack if delegate is not forging
```
salt-run dposrun.forge_notify lisk slasheks
```

Check if a delegate is forging based on DPOS system and delegate name
```
salt-run dposrun.is_forging lisk slasheks
```

Enable delegate forging based on DPOS system
```
salt-run dposrun.enable_forging lisk slasheks
```

Disable delegate forging based on DPOS system and delegate name
```
salt-run dposrun.disable_forging lisk slasheks
```

### dposrun Detailed Guide

[LINK](salt/_runners/dposrun-detailed-guide.md)

