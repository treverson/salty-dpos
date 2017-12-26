### Hardening tasks based on Lynis recommendations
<pre>
<b>Apply all the changes from the harden lynis category</b>
sudo salt 'node1' state.apply harden.lynis

<b>Apply all the changes from a category</b>
sudo salt 'node1' state.apply harden.lynis.ssh7408

<b>Apply just one change from a category</b>
sudo salt 'node1' state.apply harden.lynis.ssh7408.max_sessions
</pre>

---

