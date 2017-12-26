Port:
  {% if salt['file.search']('/etc/ssh/sshd_config', 'Port') %}
  file.line:
    - name: /etc/ssh/sshd_config
    - content: Port {{ pillar.get('SSH-7408-default-port', '22') }}
    - match: "Port"
    - mode: "replace"
  {% else %}
  file.append:
    - name: /etc/ssh/sshd_config
    - text: Port {{ pillar.get('SSH-7408-default-port', '22') }}
  {% endif %}
