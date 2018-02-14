salt-restart:
  file.managed:
    - name: /usr/local/bin/restart_salt_minion
    - source: salt://harden/sudo/files/restart_salt_minion
    - user: root
    - group: root
    - mode: 700
