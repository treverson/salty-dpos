MaxSessions:
  {% if salt['file.search']('/etc/ssh/sshd_config', 'MaxSessions') %}
  file.line:
    - name: /etc/ssh/sshd_config
    - content: "MaxSessions 2"
    - match: "MaxSessions"
    - mode: "replace"
  {% else %}
  file.append:
    - name: /etc/ssh/sshd_config
    - text: "MaxSessions 2"
  {% endif %}
