add_visudo_for_install:
  file.managed:
    - name: /etc/sudoers.d/91-onzadmin
    - user: root
    - group: root
    - mode: 0440
    - source: salt://onz/files/91-onzadmin

onz_manager_install:
  cmd.run:
    - name: ./onz_manager.bash install
    - runas: {{ pillar.get('username') }}
    - cwd: {{ pillar.get('app_dir') }}
    - require:
      - add_visudo_for_install

remove_visudo_after:
  file.absent:
    - name: /etc/sudoers.d/91-onzadmin
    - require:
      - onz_manager_install

