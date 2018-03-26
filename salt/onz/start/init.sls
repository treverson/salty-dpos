start_onz_service:
  cmd.run:
    - name: ./onz_manager.bash start
    - runas: {{ pillar.get('username') }}
    - cwd: {{ pillar.get('app_dir') }}
