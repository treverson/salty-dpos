add_visudo_for_install:
  file.managed:
    - name: /etc/sudoers.d/91-lwfadmin
    - user: root
    - group: root
    - mode: 0440
    - source: salt://lwf/files/91-lwfadmin

rebuild_db:
  cmd.run:
    - name: echo "y" | ./lwf_manager.bash rebuild
    - runas: {{ pillar.get('username') }}
    - cwd: {{ pillar.get('app_dir') }}
    - require:
      - add_visudo_for_install

remove_visudo_after:
  file.absent:
    - name: /etc/sudoers.d/91-lwfadmin
    - require:
      - rebuild_db

