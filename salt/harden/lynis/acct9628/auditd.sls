ACCT-9628-auditd:
  pkg.installed:
    - name: auditd

ACCT-9628-audispd-plugins:
  pkg.installed:
    - name: audispd-plugins
    - require:
      - pkg: ACCT-9628-auditd

ACCT-9628-auditd-svc:
  service.running:
    - name: auditd
    - enable: True
    - require:
      - pkg: ACCT-9628-auditd
      - pkg: ACCT-9628-audispd-plugins
    - watch:
      - file: ACCT-9628-auditd-conf

ACCT-9628-auditd-conf:
  file.managed:
    - name: /etc/audit/audit.rules
    - source: salt://harden/lynis/acct9628/files/audit.rules
    - user: root
    - group: root
    - mode: 640
    - template: jinja

