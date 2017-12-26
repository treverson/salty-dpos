install_ssh:
  pkg.latest:
    - name: ssh

start_ssh:
  service.running:
    - name: ssh
    - enable: True
    - require:
      - pkg: install_ssh
    - watch:
      - file: sshd_conf

sshd_conf:
  file.managed:
    - name: /etc/ssh/sshd_config
    - source: salt://default/ssh/files/sshd_config
    - user: root
    - group: root
    - mode: 644

rename_authkey_file:
  file.rename:
    - name: /home/{{ pillar.get('username') }}/.ssh/authorized_keys
    - source: /root/.ssh/authorized_keys
    - makedirs: True
    - require:
      - file: sshd_conf

set_authkey_perms:
  file.managed:
    - name: /home/{{ pillar.get('username') }}/.ssh/authorized_keys
    - user: {{ pillar.get('username') }}
    - group: {{ pillar.get('username') }}
    - mode: 600
    - require:
      - file: rename_authkey_file
    
