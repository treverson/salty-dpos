copy_data_out:
  cmd.run:
    - name: mv /opt/lisk/lisk-Linux-x86_64/pgsql/data /opt/lisk/data
    - user: {{ pillar['username'] }}
    - cwd: {{ pillar['app_dir'] }}
