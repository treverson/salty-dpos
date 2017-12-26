AllowTcpForwarding:
  {% if salt['file.search']('/etc/ssh/sshd_config', 'AllowTcpForwarding') %}
  file.line:
    - name: /etc/ssh/sshd_config
    - content: "AllowTcpForwarding no"
    - match: "AllowTcpForwarding"
    - mode: "replace"
  {% else %}
  file.append:
    - name: /etc/ssh/sshd_config
    - text: "AllowTcpForwarding no"
  {% endif %}
