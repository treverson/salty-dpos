X11Forwarding:
  {% if salt['file.search']('/etc/ssh/sshd_config', 'X11Forwarding') %}
  file.line:
    - name: /etc/ssh/sshd_config
    - content: "X11Forwarding no"
    - match: "X11Forwarding"
    - mode: "replace"
  {% else %}
  file.append:
    - name: /etc/ssh/sshd_config
    - text: "X11Forwarding no"
  {% endif %}
