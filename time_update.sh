#!/usr/bin/bash

# echo all input to the readme function to README.md
echo > .README.md
readme () { echo -e $@ >> .README.md; }

# echo is used here to clear the file and rewrite it
echo "# Advent Of Code 2024" > README.md
echo "------" >> README.md


echo "|status|day|time to complete|" >> README.md
echo  "|:-|:-|:-|" >> README.md


readme
for day in {1..25};
do
    readme "|$(/usr/bin/time -f "|$day-1|%E|" ./aoc_2024.py $day -1 -o 2>&1 )"
    readme "|$(/usr/bin/time -f "|$day-2|%E|" ./aoc_2024.py $day -2 -o 2>&1 )"
done


./fix_read_me.awk AOC/*.py .README.md >> README.md
rm .README.md
