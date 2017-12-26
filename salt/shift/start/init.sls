start_shift_service:
  cmd.run:
    - name: ./shift_manager.bash start
    - runas: {{ pillar.get('username') }}
    - cwd: {{ pillar.get('app_dir') }}
