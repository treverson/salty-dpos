PermitRootLogin:
  {% if salt['file.search']('/etc/ssh/sshd_config', 'PermitRootLogin') %}
  file.line:
    - name: /etc/ssh/sshd_config
    - content: "PermitRootLogin no"
    - match: "PermitRootLogin yes"
    - mode: "replace"
  {% else %}
  file.append:
    - name: /etc/ssh/sshd_config
    - text: "PermitRootLogin no"
  {% endif %}
