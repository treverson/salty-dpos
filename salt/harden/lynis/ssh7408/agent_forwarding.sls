AllowAgentForwarding:
  {% if salt['file.search']('/etc/ssh/sshd_config', 'AllowAgentForwarding') %}
  file.line:
    - name: /etc/ssh/sshd_config
    - content: "AllowAgentForwarding no"
    - match: "AllowAgentForwarding"
    - mode: "replace"
  {% else %}
  file.append:
    - name: /etc/ssh/sshd_config
    - text: "AllowAgentForwarding no"
  {% endif %}
