#### Requirements:
```
all:
in pillar_override/init.sls
{{ if grains.get('lwfenv') == 'main' }}
app_dir: /path/to/install
username: username_to_run
{{ if grains.get('lwfenv') == 'main' }}
{{ endif }}

mainnet:
sudo salt 'lwf-delegate2' grains.setval lwfenv main

testnet:
sudo salt 'test-lwf-delegate2' grains.setval lwfenv test
```

#### INSTALL

```
sudo salt 'test-lwf-delegate2' state.apply lwf.install
```

#### STOP

```
sudo salt 'test-lwf-delegate2' state.apply lwf.stop
test-lwf-delegate2:
----------
          ID: stop_lwf_service
    Function: cmd.run
        Name: ./lwf_manager.bash stop
      Result: True
     Comment: Command "./lwf_manager.bash stop" run 
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
                  Stopping Shift... OK

Summary for test-lwf-delegate2
------------
Succeeded: 1 (changed=1)
Failed:    0   
------------
Total states run:     1   
Total run time:   3.788 s
```

#### START
```
sudo salt 'test-lwf-delegate2' state.apply lwf.start

test-lwf-delegate2:
----------
          ID: start_lwf_service
    Function: cmd.run
        Name: ./lwf_manager.bash start
      Result: True
     Comment: Command "./lwf_manager.bash start" run 
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
                  Starting Shift... OK
                  Block height =  571823

Summary for test-lwf-delegate2
------------
Succeeded: 1 (changed=1)
Failed:    0   
------------
Total states run:     1   
Total run time:   3.434 s
```


#### REBUILD

```
sudo salt 'test-lwf-delegate2' state.apply lwf.rebuild

test-lwf-delegate2:
----------
          ID: add_visudo_for_install
    Function: file.managed
        Name: /etc/sudoers.d/91-lwfadmin
      Result: True
     Comment: File /etc/sudoers.d/91-lwfadmin is in the correct state
     Started: 19:24:43.864514
    Duration: 85.921 ms
     Changes:   
----------
          ID: rebuild_db
    Function: cmd.run
        Name: echo "y" | ./lwf_manager.bash rebuild
      Result: True
     Comment: Command "echo "y" | ./lwf_manager.bash rebuild" run
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
                  Stopping Shift... OK
                  √ Postgresql database created successfully.
                  Download a recent, verified snapshot? ([y]/n): √ Downloading blockchain.db.gz from https://downloads.lwfnrg.org/snapshot/test
                  √ Blockchain snapshot downloaded successfully.
                  Restoring blockchain with blockchain.db.gz
                  √ Blockchain restored successfully.
                  Starting Shift... OK
                  Block height =  562974
----------
          ID: remove_visudo_after
    Function: file.absent
        Name: /etc/sudoers.d/91-lwfadmin
      Result: True
     Comment: Removed file /etc/sudoers.d/91-lwfadmin
     Started: 19:25:24.069390
    Duration: 4.313 ms
     Changes:   
              ----------
              removed:
                  /etc/sudoers.d/91-lwfadmin

Summary for test-lwf-delegate2
------------
Succeeded: 3 (changed=2)
Failed:    0
------------
Total states run:     3
Total run time:  40.204 s
```


