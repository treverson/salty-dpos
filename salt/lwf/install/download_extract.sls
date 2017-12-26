check_for_install_dir:
  file.directory:
    - name: {{ pillar.get('app_dir') }}
    - user: {{ pillar.get('username') }}
    - group: {{ pillar.get('username') }}
    - dir_mode: 755
    - makedirs: True

clone_shift_from_git:
  git.latest:
    - name: https://github.com/lwfcoin/lwf-node.git
    - user: {{ pillar.get('username') }}
    - target: {{ pillar.get('app_dir') }}
    {% if grains.get('lwfenv') == 'main' %}
    - rev: master
    - branch: master
    {% elif grains.get('lwfenv') == 'test' %}
    - rev: testnet
    - branch: testnet
    {% endif %}
    - require:
      - check_for_install_dir

