#https://cisofy.com/controls/SSH-7408/

include:
  - harden.lynis.ssh7408.agent_forwarding
  - harden.lynis.ssh7408.default_port
  - harden.lynis.ssh7408.log_level
  - harden.lynis.ssh7408.max_auth_tries
  - harden.lynis.ssh7408.max_sessions
  - harden.lynis.ssh7408.permit_empty_pw
  - harden.lynis.ssh7408.permit_root_login
  - harden.lynis.ssh7408.protocol
  - harden.lynis.ssh7408.tcp_forwarding
  - harden.lynis.ssh7408.tcp_keepalive
  - harden.lynis.ssh7408.x11_forwarding

restart_ssh:
  service.running:
    - name: ssh
    - reload: True
    - order: last
    - watch:
      - file: /etc/ssh/sshd_config
