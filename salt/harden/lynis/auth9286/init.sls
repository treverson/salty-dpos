AUTH-9286-login.defs-max-age:
  file.replace:
    - name: /etc/login.defs
    - pattern: (PASS_MAX_DAYS\t)(\d+)
    - repl: PASS_MAX_DAYS\t{{ pillar.get('AUTH-9286-PASS_MAX_DAYS', '182') }}

AUTH-9286-login.defs-min-days:
  file.replace:
    - name: /etc/login.defs
    - pattern: (PASS_MIN_DAYS\t)(\d+)
    - repl: PASS_MIN_DAYS\t{{ pillar.get('AUTH-9286-PASS_MIN_DAYS', '1' }}

