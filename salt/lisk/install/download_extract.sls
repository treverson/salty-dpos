lisk-Linux-x86_64:
  archive.extracted:
    - name: /opt/lisk/
    {% if grains['liskenv'] == 'test' and grains['cpuarch'] == 'x86_64' %}
    - source: https://downloads.lisk.io/lisk/test/lisk-Linux-x86_64.tar.gz
    - source_hash: https://downloads.lisk.io/lisk/test/lisk-Linux-x86_64.tar.gz.SHA256
    - if_missing: /opt/lisk/lisk-Linux-x86_64/
    {% elif grains['liskenv'] == 'main' and grains['cpuarch'] == 'x86_64' %}
    - source: https://downloads.lisk.io/lisk/main/lisk-Linux-x86_64.tar.gz
    - source_hash: https://downloads.lisk.io/lisk/main/lisk-Linux-x86_64.tar.gz.SHA256
    - if_missing: /opt/lisk/lisk-Linux-x86_64/
    {% endif %}
    - archive_format: tar
    - tar_options: z
    - user: {{ pillar['username'] }}
    - group: {{ pillar['group'] }}
