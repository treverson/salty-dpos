remove lisk symlink:
  file.absent:
    - name: /opt/lisk/lisk-{{ grains['liskenv'] }}

