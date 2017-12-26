### Using pillar overrides

Pillar overrides provide a method, as the name suggests, to override
values set by other system values. It can also override defaults
set in jinja in other configuration options. 

For example, system timezone for the state default.timez is NewYork
to override this simply add 

`system_timezone: America/Denver`

To pillar/pillar_override/init.sls and the new value will be applied

You can also include sls files to be used by different parts of the system.
An example of this is an include clause that will add the contents of the 
file party_hashes to the pillar data.

```
include:
  - pillar_override.party_hashes
```

Where party_hashes is used by default.users to add a password to a created user
```
shadow_hash: $6$notmysalt$asd123qweasdfzxcasdqweqwdasdzxcdasdasda
```

This is to simplify overwriting default values. If you need more granular control
edit the pillar/top.sls file and target the minions based on your needs. 
