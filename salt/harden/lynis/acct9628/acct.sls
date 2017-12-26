ACCT-9628-acct:
  pkg.installed:
    - name: acct

ACCT-9628-svc:
  service.running:
    - name: acct
    - enable: True
    - require:
      - pkg: ACCT-9628-acct
