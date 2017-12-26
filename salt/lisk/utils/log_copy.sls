old_logs:
  file.copy:
    - name: /opt/lisk/lisk.log
    - source: /opt/lisk/lisk-Linux-x86_64/logs/lisk.log
    - user: {{ pillar['username'] }}
    - group: {{ pillar['group'] }}
    - force: True

