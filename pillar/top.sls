base:
  '*':
    - users
    - cryptovars
    - systemvars
    - pillar_override
  # Scheduled Jobs
  'G@stage:1':
    - sched_jobs.stage1_pkgupgrd
  'G@stage:2':
    - sched_jobs.stage2_pkgupgrd

