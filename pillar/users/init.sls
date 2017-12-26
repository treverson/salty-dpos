{% if grains.get('liskenv') %}
username: liskadmin
group: liskadmin
forger_name: liska
{% elif grains.get('arkenv') %}
username: arkadmin
group: arkadmin
forger_name: slasheks
{% elif grains.get('shiftenv') %}
username: shiftadmin
group: shiftadmin
forger_name: slasheks
{% elif grains.get('oxyenv') %}
username: oxyadmin
group: oxyadmin
forger_name: slasheks
{% elif grains.get('lwfenv') %}
username: lwfadmin
group: lwfadmin
forger_name: slasheks
{% endif %}
