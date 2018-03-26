stop_onz_service:
  cmd.run:
    - name: ./onz_manager.bash stop
    - runas: {{ pillar.get('username') }}
    - cwd: {{ pillar.get('app_dir') }}
