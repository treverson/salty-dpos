add_visudo_for_install:
  file.managed:
    - name: /etc/sudoers.d/91-shiftadmin
    - user: root
    - group: root
    - mode: 0440
    - source: salt://shift/files/91-shiftadmin

rebuild_db:
  cmd.run:
    - name: echo "y" | ./shift_manager.bash rebuild
    - runas: {{ pillar.get('username') }}
    - cwd: {{ pillar.get('app_dir') }}
    - require:
      - add_visudo_for_install

remove_visudo_after:
  file.absent:
    - name: /etc/sudoers.d/91-shiftadmin
    - require:
      - rebuild_db

