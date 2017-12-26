start_oxy_service:
  cmd.run:
    - name: ./oxy_manager.bash start
    - runas: {{ pillar.get('username') }}
    - cwd: {{ pillar.get('app_dir') }}
