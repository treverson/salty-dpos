PermitEmptyPasswords:
  {% if salt['file.search']('/etc/ssh/sshd_config', 'PermitEmptyPasswords') %}
  file.line:
    - name: /etc/ssh/sshd_config
    - content: "PermitEmptyPasswords no"
    - match: "PermitEmptyPasswords"
    - mode: "replace"
  {% else %}
  file.append:
    - name: /etc/ssh/sshd_config
    - text: "PermitEmptyPasswords no"
  {% endif %}
