AUTH-9328-login.defs:
  file.replace:
    - name: /etc/login.defs
    - pattern: (UMASK\t\t)(\d+)
    - repl: UMASK\t\t{{ pillar.get('AUTH-9328-logindefs', '027') }}

AUTH-9328-init.d/rc:
  file.replace:
    - name: /etc/init.d/rc
    - pattern: (umask )(\d+)
    - repl: umask {{ pillar.get('AUTH-9328-initdrc', '027') }}

