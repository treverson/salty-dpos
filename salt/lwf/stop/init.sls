stop_lwf_service:
  cmd.run:
    - name: ./lwf_manager.bash stop
    - runas: {{ pillar.get('username') }}
    - cwd: {{ pillar.get('app_dir') }}
