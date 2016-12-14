#!/bin/bash

x=0
y=0
wget http://pastebin.com/raw/BZrAMcN2 -O file && echo " " >> file
while read line; do
	distance=$(echo $line | awk '{print $2}')
	direction=$(echo $line | awk '{print $4}')
	case "$direction" in
		north* )
			((y+=$distance)) ;;
		south* )
			((y-=$distance)) ;;
		west* )
			((x+=$distance)) ;;
		east* )
			((x-=$distance)) ;;
	esac
done < file
echo "$y, $x"







