NETW-3032:
  pkg.installed:
    - name: arpwatch

NETW-3032-conf:
  file.managed:
    - name: /etc/arpwatch.conf
    - source: salt://harden/lynis/netw3032/arpwatch.conf
    - user: root
    - group: root
    - mode: 644
    - require:
      - pkg: NETW-3032

NETW-3032-svc:
  service.running:
    - name: arpwatch
    - enable: True
    - require:
      - pkg: NETW-3032
    - watch:
      - file: NETW-3032-conf

