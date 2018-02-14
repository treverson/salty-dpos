add_visudo_for_install:
  file.managed:
    - name: /etc/sudoers.d/91-customsudo
    - user: root
    - group: root
    - mode: 0440
    - template: jinja
    - source: salt://harden/sudo/files/91-customsudo

