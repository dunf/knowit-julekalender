#!/bin/bash

sum=0
a=0
b=1
c=0
while [[ $(($sum+$c)) -lt 4000000000 ]]; do
	c=$(($b+$a))
	if [[ $(($c%2)) -eq 0 ]]; then
		sum=$(($sum+$c))
	fi
	a=$b
	b=$c
done 
echo "Solution: $sum"
