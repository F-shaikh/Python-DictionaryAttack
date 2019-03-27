#!/bin/bash
nc -zv 192.168.1.10 1-65535 > scanOutput 2>&1;
grep "succ" scanOutput > openPorts;
grep -E -o "[0123456789]{5}" openPorts > portNums;

python findport.py $1 $2 $3
python findpasswd.py $1 $2 $3 $4
chmod +x binary
python overflow.py $1
curl 192.168.1.10:10613 | grep -Eo "(http)://[a-zA-Z0-9./?=_-]*"
