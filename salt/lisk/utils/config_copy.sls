copy_old_config:
  file.copy:
    - name: /opt/lisk/config.json
    - source: /opt/lisk/lisk-Linux-x86_64/config.json
    - user: {{ pillar['username'] }}
    - group: {{ pillar['group'] }}
    - force: True
