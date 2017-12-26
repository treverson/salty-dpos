check_lisk_dir:
  file.directory:
    - name: /opt/lisk
    - user: {{ pillar['username'] }}
    - group: {{ pillar['group'] }}
    - dir_mode: 755
    
