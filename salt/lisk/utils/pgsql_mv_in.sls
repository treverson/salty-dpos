copy_data_in:
  cmd.run:
    - name: mv /opt/lisk/data /opt/lisk/lisk-Linux-x86_64/pgsql/data
    - user: {{ pillar['username'] }}
    - cwd: {{ pillar['app_dir'] }}
