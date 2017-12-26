#download_new_lisk_installer:
#  file.managed:
#    - name: {{ pillar.get('working_dir') }}installLisk.sh
#    {% if grains['liskenv'] == 'main' %}
#    - source: https://downloads.lisk.io/lisk/main/installLisk.sh
#    {% elif grains['liskenv'] == 'test' %}
#    - source: https://downloads.lisk.io/lisk/test/installLisk.sh
#    {% endif %}
#    - user: {{ pillar.get('username') }}
#    - group: {{ pillar.get('username') }}
#    - mode: 700
#    - skip_verify: True
#    - replace: True
#
#update_lisk:
#  cmd.run:
#    {% if grains['liskenv'] == 'main' %}
#    - name: {{ pillar.get('working_dir') }}installLisk.sh upgrade -r main -d {{ pillar.get('working_dir') }}
#    {% elif grains['liskenv'] == 'test' %}
#    - name: {{ pillar.get('working_dir') }}installLisk.sh upgrade -r test -d {{ pillar.get('working_dir') }}
#    {% endif %}

# STOP LISK 
# Move data dir to /opt/lisk
# Move config file to /opt/lisk
# Move back to /opt/lisk/lisk-Linux/data
# Update config with node utility

include:                                                                                                                                             
  - lisk.stop
  - lisk.utils.config_copy
  - lisk.utils.log_copy
  - lisk.utils.pgsql_mv_out
  - lisk.remove
  - lisk.install
  - lisk.utils.pgsql_mv_in


