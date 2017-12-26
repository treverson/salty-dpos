start_lisk_service:
  cmd.run:
    - name: bash lisk.sh start
    - cwd: {{ pillar['app_dir'] }}
    - user: {{ pillar['username'] }}
