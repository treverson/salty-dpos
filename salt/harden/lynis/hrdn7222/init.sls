#TODO add checks for the files

{% set compilers = ['/usr/bin/as','/usr/bin/gcc','/usr/bin/g++'] %}
{% for compiler in compilers %}
HRDN-7222-{{ compiler }}:
  file.managed:
    - name: {{compiler}}
    - user: root
    - group: root
    - mode: 500
    - replace: False
    - create: False
{% endfor %}
