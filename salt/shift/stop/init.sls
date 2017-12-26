stop_shift_service:
  cmd.run:
    - name: ./shift_manager.bash stop
    - runas: {{ pillar.get('username') }}
    - cwd: {{ pillar.get('app_dir') }}
