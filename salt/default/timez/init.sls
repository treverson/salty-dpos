set_system_time:
  timezone.system:
  - name: {{ pillar.get('system_timezone') }}
  - utc: False
