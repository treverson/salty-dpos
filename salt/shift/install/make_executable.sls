make_shift_manager_executable:
  file.managed:
    - name: {{ pillar.get('app_dir') }}/shift_manager.bash
    - mode: 700
    - follow_symlinks: True
