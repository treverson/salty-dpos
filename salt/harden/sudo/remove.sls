remove_visudo_after:
  file.absent:
    - name: /etc/sudoers.d/91-customsudo

