download_new_onz_manager:
  file.managed:
    - name: {{ pillar.get('app_dir') }}/onz_manager.bash
    - source:  https://raw.githubusercontent.com/OnzCoin/onz/master/onz_manager.bash
    - user: {{ pillar.get('username') }}
    - group: {{ pillar.get('username') }}
    - mode: 700
    - skip_verify: True
    - replace: True

start_onz_service:
  cmd.run:
    - name: ./onz_manager.bash update_client
    - runas: {{ pillar.get('username') }}
    - cwd: {{ pillar.get('app_dir') }}
