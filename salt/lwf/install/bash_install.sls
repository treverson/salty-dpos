add_visudo_for_install:
  file.managed:
    - name: /etc/sudoers.d/91-lwfadmin
    - user: root
    - group: root
    - mode: 0440
    - source: salt://lwf/files/91-lwfadmin

lwf_manager_install:
  cmd.run:
    - name: ./lwf_manager.bash install
    - runas: {{ pillar.get('username') }}
    - cwd: {{ pillar.get('app_dir') }}
    - require:
      - add_visudo_for_install

remove_visudo_after:
  file.absent:
    - name: /etc/sudoers.d/91-lwfadmin
    - require:
      - lwf_manager_install

