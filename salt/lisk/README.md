## Lisk Installation / coldstart / stop / start / remove
<pre>
<b>Install the lisk application on the dpos-delegate1 minion</b>
sudo salt dpos-delegate1 state.sls lisk.install

<b>Coldstart the lisk application on the dpos-delegate1 minion</b>
sudo salt dpos-delegate1 state.sls lisk.coldstart

<b>Install the lisk application on all minions</b>
sudo salt \* state.sls lisk.install

<b>Stop the lisk service on the dpos-delegate1 minion</b>
sudo salt dpos-delegate1 state.sls lisk.stop

<b>Start the lisk service on the dpos-delegate1 minion</b>
sudo salt dpos-delegate1 state.sls lisk.start

<b>Remove the lisk application from the dpos-delegate1 minion</b>
sudo salt dpos-delegate1 state.sls lisk.remove
</pre> 
