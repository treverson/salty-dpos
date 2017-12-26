TCPKeepAlive:
  {% if salt['file.search']('/etc/ssh/sshd_config', 'TCPKeepAlive') %}
  file.line:
    - name: /etc/ssh/sshd_config
    - content: "TCPKeepAlive no"
    - match: "TCPKeepAlive"
    - mode: "replace"
  {% else %}
  file.append:
    - name: /etc/ssh/sshd_config
    - text: "TCPKeepAlive no"
  {% endif %}
