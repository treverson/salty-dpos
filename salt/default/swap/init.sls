{% set swap_file = '/swapfile' %}
{% if grains['mem_total'] < 2048 %}
  {% set swap = '2G' %}
{% elif grains['mem_total'] > 2048 %}
  {% set swap = '3G' %}
{% endif %}

configure_swap:
  cmd.run:
    - name: |
        fallocate -l {{swap}} {{swap_file}}
        chmod 600 {{swap_file}}
        mkswap {{swap_file}}
        swapon {{swap_file}}
    - creates: {{swap_file}}

/etc/fstab:
  file.append:
    - text: |
        {{swap_file}} none swap sw 0 0
    - require:
      - cmd: configure_swap

/etc/sysctl.conf:
  file.append:
    - text: |
        vm.swappiness=10
        vm.vfs_cache_pressure=5
    - require:
      - cmd: configure_swap

