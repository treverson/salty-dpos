download_bootstrap_script:
  file.managed:
    - name: /tmp/bootstrap-salt.sh
    - source: https://bootstrap.saltstack.com
    - user: {{ pillar.get('username') }}
    - group: {{ pillar.get('username') }}
    - mode: 700
    - skip_verify: True
    - replace: True

update_salt_minion:
  cmd.run:
    - name: bash bootstrap-salt.sh git v2016.11.6
    - cwd: /tmp
    - require:
      - cmd: download_new
