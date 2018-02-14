cryptoadmin_user_group:
  group.present:
    - name: {{ pillar['admin_group'] }}

cryptoadmin_user:
  user.present:
    - name: {{ pillar['admin_name'] }}
    - fullname: CryptoAdmin
    - shell: /bin/bash
    - home: /home/{{ pillar['admin_name'] }}
    {% if pillar.get('admin_shadow_hash') %}
    - password: {{ pillar['admin_shadow_hash'] }}
    {% endif %}
    - groups:
      - {{ pillar['admin_group'] }}
