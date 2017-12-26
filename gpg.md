##### Full Guide

[SALT.RENDERERS.GPG](https://docs.saltstack.com/en/latest/ref/renderers/all/salt.renderers.gpg.html)

##### Update for good measure
```
sudo apt update
```

##### Change the renderer on the master
```
renderer: jinja | yaml | gpg
```

##### Create keys directory
```
sudo mkdir --mode 700 /etc/salt/gpgkeys
```

##### Install deps
```
sudo apt install python-gnupg
sudo apt install rng-tools
```

##### Entropy!!
```
sudo rngd -r /dev/urandom
```

##### Generate said keys with the options
```
sudo gpg --gen-key --homedir /etc/salt/gpgkeys/

1
4096
0
y
saltstack
[enter]
o
passphrase/passphrase

Sample output:

gpg: /etc/salt/gpgkeys//trustdb.gpg: trustdb created
gpg: key 3057C661 marked as ultimately trusted
public and secret key created and signed.
gpg: checking the trustdb
gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
pub   4096R/3057C661 2017-03-16
      Key fingerprint = F568 0D0F 8AD0 1F2A 6437  C07A 9621 EB04 3057 C661
uid                  saltstack (salt pillar encrypt)
sub   4096R/21234B79 2017-03-16
```

##### Kill entropy!
```
sudo pkill rngd
```

##### Export the public key
```
sudo gpg --homedir /etc/salt/gpgkeys --export --armor > salt-master.pub
```

##### Import the public key just to generate the message
```
gpg --import salt-master.pub
```

##### Encrypt from echo (stdin) or file (stdin)
```
echo -n "my-super-secret-password" | gpg --armor --encrypt -r saltstack
cat super-secret-password-file.key | gpg --armor --encrypt -r saltstack
```

##### grab stdout and place it in a var for pillar data
```yaml
#!yaml|gpg
secret: |
  -----BEGIN PGP MESSAGE-----
  Version: GnuPG v1

  hQIMAwatum5pUOk/AQ//Zoyij3HYy5jioo+oKB/L0hdwJD2zwhtimAWgqe0Q0r5i
  2sCi8jeXtexedO1w2+3pjYwdkx7gQKwAI872GVX5XN5m8B3/aLf+R6rdzpPMM5+R
  s4JfnCrp3iuuPtoJaG5s/q9SysbaQdS98l0M0RkFsgvzjzDzAqctivfy1Wpg9oWF
  xjGEtSGHJTK7KPOGuZNuBgYNt2QHkliLYETcdQsvg0LRY89YA21ZjzHFP91eetIE
  ofIZoaBLKbfBiCgXBgTPiW17r2Ck2Fn/UlZuozJiqJTKCXRj+isDc/LvhNDfoWsj
  UN0EGn/jx3s6Ac9IQsmy5xqlNpYFvtFI22fBIMsUmv2RTx4o0UcN7Ck5Peouvkro
  5Er+dIie9jFpLfF+rvNkUazqiwnpVC/O1xmI7c091aZCw4gPfgIjhOsQ5d8ZnH+3
  mTL/EUxQqXcusC/ELP0NLZNU7m5UNqrJe8jB8TDoXZaFat6s4gk35aypj8gTrPqC
  ov1Tx4jkF/N+YhYehZ1/7eNS+kclOAzrJNXZZyb6fplydlyXxc+d/dtzuw5Qz9aY
  2+m+82Ct+Ic8UTbfrpaBoVPGp8+kWhqEtIJPcV+Ts1RKacpDQbh6L5yO1qXmFtXe
  Ewr0FToLGKuMdQxHkSfWT28HkGcoGIpQSFDKJ+q5gvkIezvcdm/zQ04y7rohTFvS
  UwEkjPiRy+gAMqXdwzoRSP2KMJn3Wz+jdNt+XLR0z8ZJducqFgJs7mwfG1bK3HcS
  +YNXhpQnjzzO8dQM3wyYheFwxNBq89O4HUHYH6bO9lUyD5wb
  =WYaq
  -----END PGP MESSAGE-----
```

