{% set app_dir = pillar.get('app_dir') %}
{% set working_dir = pillar.get('working_dir') %}


update config from old file:
  cmd.run:
    - name: {{app_dir}}bin/node {{app_dir}}updateConfig.js -o {{working_dir}}config.json -n {{app_dir}}config.json

