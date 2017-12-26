admin_user_group:
  group.present:
    - name: {{ pillar['group'] }}

sudo_user_group:
  group.present:
    - name: sudo

admin_user:
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
      - sudo
    - require:
      - group: admin_user_group
      - group: sudo_user_group
