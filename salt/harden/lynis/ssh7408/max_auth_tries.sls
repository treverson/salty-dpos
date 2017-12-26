MaxAuthTries:
  {% if salt['file.search']('/etc/ssh/sshd_config', 'MaxAuthTries') %}
  file.line:
    - name: /etc/ssh/sshd_config
    - content: "MaxAuthTries 2"
    - match: "MaxAuthTries"
    - mode: "replace"
  {% else %}
  file.append:
    - name: /etc/ssh/sshd_config
    - text: "MaxAuthTries 2"
  {% endif %}
