#!/bin/bash
for i in {1.254}
do
echo -e "192.168.1.$i\tnode$i" > myhosts
done
