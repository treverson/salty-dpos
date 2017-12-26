BANN-7126:
  file.managed:
    - name: /etc/issue
    - source: salt://harden/lynis/bann7126/issue
    - user: root
    - group: root
    - mode: 644

