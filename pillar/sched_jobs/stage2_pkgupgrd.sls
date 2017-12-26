
schedule:
  update_packages:
    function: pkg.upgrade
    maxrunning: 1
    cron: '0 14 * * *'
