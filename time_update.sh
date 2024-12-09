#!/usr/bin/bash

# echo all input to the readme function to README.md
readme () { echo -e $@ >> README.md; }

# echo is used here to clear the file and rewrite it
echo "# Advent Of Code 2024" > README.md
echo "------" >> README.md

readme

readme "|status|day|time to complete|"
readme "|:-|:-|:-|"

for day in {1..25};
do
    readme "|$(/usr/bin/time -f "|$day-1|%E|" ./aoc_2024.py $day -1 -o 2>&1 )"
    readme "|$(/usr/bin/time -f "|$day-2|%E|" ./aoc_2024.py $day -2 -o 2>&1 )"
done

# mark incomplete days as "not complete"
sed -i  "s/^|day [0-9]* part [12]* not complete |\([^|]*\)|\([^|]*\)|$/|not complete|\1|NA|/" README.md
# mark complete days as "complete" and create a link to the solution
sed -i  "s/^|[^n][^|]*|\([0-9]*\)-\([12]\)|\([0-9\.:]*\)|$/|complete|[\1-\2](AOC\/day_\1.py)|\3|/" README.md