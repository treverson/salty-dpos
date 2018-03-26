check_for_install_dir:
  file.directory:
    - name: {{ pillar.get('app_dir') }}
    - user: {{ pillar.get('username') }}
    - group: {{ pillar.get('username') }}
    - dir_mode: 755
    - makedirs: True

clone_onz_from_git:
  git.latest:
    - name: https://github.com/OnzCoin/onz.git
    - user: {{ pillar.get('username') }}
    - target: {{ pillar.get('app_dir') }}
    {% if grains.get('onzenv') == 'main' %}
    - rev: master
    - branch: master
    {% elif grains.get('onzenv') == 'test' %}
    - rev: testnet
    - branch: testnet
    {% endif %}
    - require:
      - check_for_install_dir

