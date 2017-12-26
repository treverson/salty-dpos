
{% set ip_address = salt['grains.get']('ip4_interfaces:eth0')[0] %}

{% if salt['grains.get']('liskenv') %}
  {% set crypto = "lisk" %}
{% elif salt['grains.get']('shiftenv') %}
  {% set crypto = "shift" %}
{% elif salt['grains.get']('oxyenv') %}
  {% set crypto = "oxy" %}
{% elif salt['grains.get']('lwfenv') %}
  {% set crypto = "lwf" %}
{% endif %}

create_self_signed_cert:
  cmd.run:
    - name: openssl req -subj '/CN={{ ip_address }} /O={{ crypto }}delegate./C=US' -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout {{ crypto }}.key -out {{ crypto }}.crt
    - cwd: {{ salt['pillar.get']('working_dir') }}
