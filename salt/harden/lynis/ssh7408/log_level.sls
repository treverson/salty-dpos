LogLevel:
  {% if salt['file.search']('/etc/ssh/sshd_config', 'LogLevel') %}
  file.line:
    - name: /etc/ssh/sshd_config
    - content: "LogLevel VERBOSE"
    - match: "LogLevel"
    - mode: "replace"
  {% else %}
  file.append:
    - name: /etc/ssh/sshd_config
    - text: "LogLevel VERBOSE"
  {% endif %}
