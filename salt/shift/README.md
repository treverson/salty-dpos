#### Requirements:
```
all:
in pillar_override/init.sls
{{ if grains.get('shiftenv') == 'main' }}
app_dir: /path/to/install
username: username_to_run
{{ if grains.get('shiftenv') == 'main' }}
{{ endif }}

mainnet:
sudo salt 'shift-delegate2' grains.setval shiftenv main

testnet:
sudo salt 'test-shift-delegate2' grains.setval shiftenv test
```

#### INSTALL

```
sudo salt 'test-shift-delegate2' state.apply shift.install
```

#### STOP

```
sudo salt 'test-shift-delegate2' state.apply shift.stop
test-shift-delegate2:
----------
          ID: stop_shift_service
    Function: cmd.run
        Name: ./shift_manager.bash stop
      Result: True
     Comment: Command "./shift_manager.bash stop" run 
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

Summary for test-shift-delegate2
------------
Succeeded: 1 (changed=1)
Failed:    0   
------------
Total states run:     1   
Total run time:   3.788 s
```

#### START
```
sudo salt 'test-shift-delegate2' state.apply shift.start

test-shift-delegate2:
----------
          ID: start_shift_service
    Function: cmd.run
        Name: ./shift_manager.bash start
      Result: True
     Comment: Command "./shift_manager.bash start" run 
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

Summary for test-shift-delegate2
------------
Succeeded: 1 (changed=1)
Failed:    0   
------------
Total states run:     1   
Total run time:   3.434 s
```


#### REBUILD

```
sudo salt 'test-shift-delegate2' state.apply shift.rebuild

test-shift-delegate2:
----------
          ID: add_visudo_for_install
    Function: file.managed
        Name: /etc/sudoers.d/91-shiftadmin
      Result: True
     Comment: File /etc/sudoers.d/91-shiftadmin is in the correct state
     Started: 19:24:43.864514
    Duration: 85.921 ms
     Changes:   
----------
          ID: rebuild_db
    Function: cmd.run
        Name: echo "y" | ./shift_manager.bash rebuild
      Result: True
     Comment: Command "echo "y" | ./shift_manager.bash rebuild" run
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
                  Download a recent, verified snapshot? ([y]/n): √ Downloading blockchain.db.gz from https://downloads.shiftnrg.org/snapshot/test
                  √ Blockchain snapshot downloaded successfully.
                  Restoring blockchain with blockchain.db.gz
                  √ Blockchain restored successfully.
                  Starting Shift... OK
                  Block height =  562974
----------
          ID: remove_visudo_after
    Function: file.absent
        Name: /etc/sudoers.d/91-shiftadmin
      Result: True
     Comment: Removed file /etc/sudoers.d/91-shiftadmin
     Started: 19:25:24.069390
    Duration: 4.313 ms
     Changes:   
              ----------
              removed:
                  /etc/sudoers.d/91-shiftadmin

Summary for test-shift-delegate2
------------
Succeeded: 3 (changed=2)
Failed:    0
------------
Total states run:     3
Total run time:  40.204 s
```


