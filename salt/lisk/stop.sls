stop_lisk_service:
  cmd.run:
    - name: bash lisk.sh stop
    - cwd: {{ pillar['app_dir'] }}
    - user: {{ pillar['username'] }}

