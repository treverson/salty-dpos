ssh_user_group:
  group.present:
    - name: {{ pillar['group'] }}

ssh_user:
  user.present:
    - name: {{ pillar['username'] }}
    - fullname: CryptoAdmin
    - shell: /bin/bash
    - home: /home/{{ pillar['username'] }}
    {% if pillar.get('shadow_hash') %}
    - password: {{ pillar['shadow_hash'] }}
    {% endif %}
    - groups:
      - {{ pillar['group'] }}

