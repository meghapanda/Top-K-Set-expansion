#!/bin/bash
x=`wc -l ./listseed_set.txt`
echo $x
y=` echo $x | awk '{print $1}'`

for i in `seq 1 $y` ; do
  z=`head -n $i ./listseed_set.txt | tail -n 1`
  # coment as and when how ever needed
  python -m memory_profiler ./imp.py "$z"  >> ./Tested/improved/ad_1/improved"$i".txt
  python -m memory_profiler ./improved_2.py "$z"  >> ./Tested/improved/ad_1/improved"$i".txt
  python -m memory_profiler ./seisa1.py "$z"  >> ./Tested/improved/ad_1/improved"$i".txt
  echo $i
done;
