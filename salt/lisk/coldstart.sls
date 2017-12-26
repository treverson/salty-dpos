coldstart_lisk_service:
  cmd.run:
    {% if grains['liskenv'] == 'test' %}
    - name: bash lisk.sh coldstart {{ pillar.get('snapshot_service_test') }}
    {% elif grains['liskenv'] == 'main' %}
    - name: bash lisk.sh coldstart {{ pillar.get('snapshot_service_main') }}
    {% endif %}
    - cwd: {{ pillar['app_dir'] }}
    - runas: {{ pillar['username'] }}
