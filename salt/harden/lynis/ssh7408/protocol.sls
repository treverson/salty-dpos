Protocol:
  {% if salt['file.search']('/etc/ssh/sshd_config', 'Protocol') %}
  file.line:
    - name: /etc/ssh/sshd_config
    - content: "Protocol 2"
    - match: "Protocol"
    - mode: "replace"
  {% else %}
  file.append:
    - name: /etc/ssh/sshd_config
    - text: "Protocol 2"
  {% endif %}
