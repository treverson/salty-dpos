distribute_snapshot:
  file.managed:
    {% if pillar.get('liskenv') %}
    - name: /tmp/blockchain.db.gz
    - source: salt://dpos/snapshot/files/lisk-blockchain.db.gz
    {% elif pillar.get('oxyenv') %}
    - name: /tmp/blockchain.db.gz
    - source: salt://dpos/snapshot/files/oxy-blockchain.db.gz
    {% elif pillar.get('lwfenv') %}
    - name: /tmp/blockchain.db.gz
    - source: salt://dpos/snapshot/files/lwf-blockchain.db.gz
    {% endif %}
    - skip_verify: True
