download_new_shift_manager:
  file.managed:
    - name: {{ pillar.get('app_dir') }}/shift_manager.bash
    - source:  https://raw.githubusercontent.com/ShiftNrg/shift/master/shift_manager.bash
    - user: {{ pillar.get('username') }}
    - group: {{ pillar.get('username') }}
    - mode: 700
    - skip_verify: True
    - replace: True

start_shift_service:
  cmd.run:
    - name: ./shift_manager.bash update_client
    - runas: {{ pillar.get('username') }}
    - cwd: {{ pillar.get('app_dir') }}
