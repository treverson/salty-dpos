remove_lisk_install_dir:
  file.absent:
    - name: /opt/lisk/lisk-Linux-x86_64/

remove_lisk_tar_file:
  file.absent:
    - name: /opt/lisk/lisk-Linux-x86_64.tar.gz
