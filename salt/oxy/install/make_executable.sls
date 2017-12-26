make_oxy_manager_executable:
  file.managed:
    - name: {{ pillar.get('app_dir') }}/oxy_manager.bash
    - mode: 700
    - follow_symlinks: True
