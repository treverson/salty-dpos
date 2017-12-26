lisk.sh:
  file.managed:
    - name: /opt/lisk/lisk-{{ grains['liskenv'] }}/lisk.sh
    - mode: 700
    - follow_symlinks: True
