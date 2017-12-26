download_new_lwf_manager:
  file.managed:
    - name: {{ pillar.get('app_dir') }}/lwf_manager.bash
    - source:  https://raw.githubusercontent.com/ShiftNrg/lwf/master/lwf_manager.bash
    - user: {{ pillar.get('username') }}
    - group: {{ pillar.get('username') }}
    - mode: 700
    - skip_verify: True
    - replace: True

start_lwf_service:
  cmd.run:
    - name: ./lwf_manager.bash update_client
    - runas: {{ pillar.get('username') }}
    - cwd: {{ pillar.get('app_dir') }}
