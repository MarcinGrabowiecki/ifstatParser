#rsync -avz 5561876b4382ec69840000f3@wrtcron-qthon.rhcloud.com:app-root/data/netstat.bz .
bzcat netstat.bz|grep ',\|wlan0.*0000'|./proc1.py >base-jquery/out.json
