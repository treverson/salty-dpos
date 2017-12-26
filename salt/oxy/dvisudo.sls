add_visudo_for_install:
  file.managed:
    - name: /etc/sudoers.d/91-oxyadmin
    - user: root
    - group: root
    - mode: 0440
    - source: salt://oxy/files/91-oxyadmin

#remove_visudo_after:
#  file.absent:
#    - name: /etc/sudoers.d/91-oxyadmin
#    - require:
#      - oxy_manager_install
#
