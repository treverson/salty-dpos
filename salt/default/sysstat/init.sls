install_sysstat:
  pkg.latest:
    - name: sysstat

start_sysstat:
  service.running:
    - name: sysstat
    - enable: True
    - require:
      - pkg: install_sysstat
    - watch:
      - file: sysstat_conf

sysstat_conf:
  file.managed:
    - name: /etc/default/sysstat
    - source: salt://default/sysstat/files/sysstat
    - user: root
    - group: root
    - mode: 644
