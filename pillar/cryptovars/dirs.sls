{% if grains.get('liskenv') == 'main' %}
working_dir: /opt/lisk/
app_dir: /opt/lisk/lisk-Linux-x86_64/
app_port: 8000
snapshot_url: https://snapshot.lisknode.io
snapshot_service_main: -u https://snapshot.lisknode.io
install_script: https://downloads.lisk.io/lisk/main/installLisk.sh
{% elif grains.get('liskenv') == 'test' %}
working_dir: /opt/lisk/
app_dir: /opt/lisk/lisk-Linux-x86_64/
app_port: 7000
snapshot_url: https://testnet-snapshot.lisknode.io
snapshot_service_test: -u https://testnet-snapshot.lisknode.io
install_script: https://downloads.lisk.io/lisk/test/installLisk.sh
{% elif grains.get('shiftenv') == 'main' %}
working_dir: /opt/shift
app_dir: /opt/shift/shift-main/
app_port: 9305
{% elif grains.get('shiftenv') == 'test' %}
working_dir: /opt/shift
app_dir: /opt/shift/shift-test/
app_port: 9405
{% elif grains.get('oxyenv') == 'main' %}
working_dir: /opt/oxy
app_dir: /opt/oxy/oxy-main/
app_port: 10000
snapshot_url: https://downloads.oxycoin.io/snapshots/master
{% elif grains.get('oxyenv') == 'test' %}
working_dir: /opt/oxy
app_dir: /opt/oxy/oxy-test/
app_port: 9998
snapshot_url: https://downloads.oxycoin.io/snapshots/testnet
{% elif grains.get('lwfenv') == 'main' %}
working_dir: /opt/lwf
app_dir: /opt/lwf/lwf-main/
app_port: 5556
snapshot_url: https://downloads.lwf.io/snapshots/master
{% elif grains.get('lwfenv') == 'test' %}
working_dir: /opt/lwf
app_dir: /opt/lwf/lwf-test/
app_port: 5555
snapshot_url: https://downloads.lwf.io/snapshots/testnet
{% elif grains.get('cryptoenv') == 'test' %}
working_dir: /opt/lwf
app_dir: /opt/lwf/lwf-test/
app_port: 5555
{% endif %}
