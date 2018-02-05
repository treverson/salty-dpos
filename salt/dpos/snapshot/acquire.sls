{% set file_path = '/tmp/' %}

{% if pillar.get('liskenv') %}
  {% set file_name = 'lisk-blockchain.db.gz' %}
{% elif pillar.get('oxyenv') %}
  {% set file_name = 'oxy-blockchain.db.gz' %}
{% elif pillar.get('lwfenv') %}
  {% set file_name = 'lwf-blockchain.db.gz' %}
{% endif %}

download_blockchain_snapshot:
  file.managed:
    - name: {{ file_path }}{{ file_name }}
    {% if pillar.get('liskenv') == 'main' %}
    - source: https://snapshot.lisknode.io/blockchain.db.gz
    {% elif pillar.get('liskenv') == 'test' %}
    - source: https://testnet-snapshot.lisknode.io/blockchain.db.gz
    {% elif pillar.get('oxyenv') == 'main' %}
    - source: https://downloads.oxycoin.io/snapshots/master/latest
    {% elif pillar.get('oxyenv') == 'test' %}
    - source: https://downloads.oxycoin.io/snapshots/testnet/latest
    {% elif pillar.get('lwfenv') == 'main' %}
    - source: https://downloads.lwf.io/snapshots/master/latest
    {% elif pillar.get('lwfenv') == 'test' %}
    - source: https://downloads.lwf.io/snapshots/testnet/latest
    {% endif %}
    - user: {{ pillar.get('username') }}
    - group: {{ pillar.get('username') }}
    - mode: 600
    - skip_verify: True
    - replace: True

symlink_snapshot:                                            
  file.symlink:
    - name: {{ pillar.get('salt_dir') }}salt/dpos/snapshot/files/{{ file_name }}
    - target: {{ file_path }}{{ file_name }}
