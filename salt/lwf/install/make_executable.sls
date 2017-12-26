make_lwf_manager_executable:
  file.managed:
    - name: {{ pillar.get('app_dir') }}/lwf_manager.bash
    - mode: 700
    - follow_symlinks: True
