# DB Vars
postgres.port: 5432
postgres.host: localhost
postgres.pass: password

{% if grains.get('liskenv') and grains.get('liskenv') == 'test' %}
postgres.user: liskuser
postgres.maintenance_db: lisk_test
postgres.bins_dir: /opt/lisk/lisk-test/pgsql/bin/
{% elif grains.get('shiftenv') and grains.get('shiftenv') == 'test' %}
postgres.pass: testing
postgres.user: shift_testnet
postgres.maintenance_db: shift_db_testnet
postgres.bins_dir: /opt/shift/shift-test/pgsql/bin/
{% elif grains.get('oxyenv') and grains.get('oxyenv') == 'test' %}
postgres.user: oxycoin
postgres.maintenance_db: oxycoin_db
postgres.bins_dir: /opt/shift/oxy-test/pgsql/bin/
{% elif grains.get('lwfenv') and grains.get('lwfenv') == 'test' %}
postgres.user: lwf
postgres.maintenance_db: lwf_testnet
postgres.bins_dir: /opt/shift/lwf-test/pgsql/bin/
{% elif grains.get('liskenv') and grains.get('liskenv') == 'main' %}
postgres.user: liskuser
postgres.maintenance_db: lisk_main
postgres.bins_dir: /opt/lisk/lisk-test/pgsql/bin/
{% elif grains.get('shiftenv') and grains.get('shiftenv') == 'main' %}
postgres.pass: testing
postgres.user: shift
postgres.maintenance_db: shift_db
postgres.bins_dir: /opt/shift/shift-main/pgsql/bin/
{% elif grains.get('oxyenv') and grains.get('oxyenv') == 'main' %}
postgres.user: oxycoin
postgres.maintenance_db: oxycoin_db_main
postgres.bins_dir: /opt/oxy/oxy-main/pgsql/bin/
{% elif grains.get('lwfenv') and grains.get('lwfenv') == 'main' %}
postgres.user: lwf
postgres.maintenance_db: lwf_mainnet
postgres.bins_dir: /opt/shift/lwf-main/pgsql/bin/
{% endif %}
