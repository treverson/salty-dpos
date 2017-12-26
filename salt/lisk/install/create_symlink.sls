create lisk symlink:
  file.symlink:
    {% if grains['liskenv'] == 'main' %}
    - name: /opt/lisk/lisk-main
    {% elif grains['liskenv'] == 'test' %}
    - name: /opt/lisk/lisk-test
    {% endif %}
    - target: /opt/lisk/lisk-Linux-x86_64
    - user: {{ pillar['username'] }}
    - group: {{ pillar['group'] }}
    - force: True
