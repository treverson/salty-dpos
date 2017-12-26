BANN-7130:
  file.managed:
    - name: /etc/issue.net
    - source: salt://harden/lynis/bann7130/issue.net
    - user: root
    - group: root
    - mode: 644

BANN-7130-ssh-update:
  file.replace:
    - name: /etc/ssh/sshd_config
    - pattern: (#Banner /etc/issue.net)
    - repl: Banner /etc/issue.net
    - require:
      - file: BANN-7130
