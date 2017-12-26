start_lwf_service:
  cmd.run:
    - name: ./lwf_manager.bash start
    - runas: {{ pillar.get('username') }}
    - cwd: {{ pillar.get('app_dir') }}
