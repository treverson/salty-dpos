#### Requirements:
```
all:
in pillar_override/init.sls
{{ if grains.get('onzenv') == 'main' }}
app_dir: /path/to/install
username: username_to_run
{{ if grains.get('onzenv') == 'main' }}
{{ endif }}

mainnet:
sudo salt 'onz-delegate2' grains.setval onzenv main

testnet:
sudo salt 'test-onz-delegate2' grains.setval onzenv test
```

#### INSTALL

```
sudo salt 'test-onz-delegate2' state.apply onz.install
```

#### STOP

```
sudo salt 'test-onz-delegate2' state.apply onz.stop
test-onz-delegate2:
----------
          ID: stop_onz_service
    Function: cmd.run
        Name: ./onz_manager.bash stop
      Result: True
     Comment: Command "./onz_manager.bash stop" run 
     Started: 19:37:10.585936
    Duration: 3787.558 ms
     Changes:   
              ----------
              pid:
                  14664
              retcode:
                  0   
              stderr:
              stdout:
                  Stopping onz... OK

Summary for test-onz-delegate2
------------
Succeeded: 1 (changed=1)
Failed:    0   
------------
Total states run:     1   
Total run time:   3.788 s
```

#### START
```
sudo salt 'test-onz-delegate2' state.apply onz.start

test-onz-delegate2:
----------
          ID: start_onz_service
    Function: cmd.run
        Name: ./onz_manager.bash start
      Result: True
     Comment: Command "./onz_manager.bash start" run 
     Started: 19:37:18.881159
    Duration: 3434.149 ms
     Changes:   
              ----------
              pid:
                  14728
              retcode:
                  0   
              stderr:
              stdout:
                  Starting onz... OK
                  Block height =  571823

Summary for test-onz-delegate2
------------
Succeeded: 1 (changed=1)
Failed:    0   
------------
Total states run:     1   
Total run time:   3.434 s
```


#### REBUILD

```
sudo salt 'test-onz-delegate2' state.apply onz.rebuild

test-onz-delegate2:
----------
          ID: add_visudo_for_install
    Function: file.managed
        Name: /etc/sudoers.d/91-onzadmin
      Result: True
     Comment: File /etc/sudoers.d/91-onzadmin is in the correct state
     Started: 19:24:43.864514
    Duration: 85.921 ms
     Changes:   
----------
          ID: rebuild_db
    Function: cmd.run
        Name: echo "y" | ./onz_manager.bash rebuild
      Result: True
     Comment: Command "echo "y" | ./onz_manager.bash rebuild" run
     Started: 19:24:43.953447
    Duration: 40113.906 ms
     Changes:   
              ----------
              pid:
                  13715
              retcode:
                  0
              stderr:
                  
                  ########                                                                  11.8%
                  ####################                                                      28.3%
                  ###############################                                           43.9%
                  #############################################                             63.2%
                  ############################################################              84.2%
                  ######################################################################## 100.0%
              stdout:
                  Stopping onz... OK
                  √ Postgresql database created successfully.
                  Download a recent, verified snapshot? ([y]/n): √ Downloading blockchain.db.gz from https://downloads.onznrg.org/snapshot/test
                  √ Blockchain snapshot downloaded successfully.
                  Restoring blockchain with blockchain.db.gz
                  √ Blockchain restored successfully.
                  Starting onz... OK
                  Block height =  562974
----------
          ID: remove_visudo_after
    Function: file.absent
        Name: /etc/sudoers.d/91-onzadmin
      Result: True
     Comment: Removed file /etc/sudoers.d/91-onzadmin
     Started: 19:25:24.069390
    Duration: 4.313 ms
     Changes:   
              ----------
              removed:
                  /etc/sudoers.d/91-onzadmin

Summary for test-onz-delegate2
------------
Succeeded: 3 (changed=2)
Failed:    0
------------
Total states run:     3
Total run time:  40.204 s
```


