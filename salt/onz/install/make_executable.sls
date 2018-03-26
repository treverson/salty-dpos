make_onz_manager_executable:
  file.managed:
    - name: {{ pillar.get('app_dir') }}/onz_manager.bash
    - mode: 700
    - follow_symlinks: True
