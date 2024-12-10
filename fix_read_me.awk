#!/usr/bin/awk -f

BEGIN {
    FS="|"
}

#|status|day#-part#|time|
/\|[^|]*\|[0-9]+-[0-9]\|/ {
    #printf("%s|%s|%s|\n", $1, $2, $3)
    if ($2 ~ ".*not complete.*")
    {
        printf("|not complete|%s|NA|\n", $3)
    }
    else
    {
        n=split($3, day_part, "-")
	idx = $3
	sub("-", ",", idx)
        printf("|complete|[%s-%s](/AOC/day_%s.py#L%s)|%s|\n", day_part[1], day_part[2], day_part[1], line_number[idx], $4)
    }
}

/^def part_[12]_day_[0-9]/ {
	sub("def part_", "", $0)
	#TODO: fix this. the two lines are a stop gap for space vs no space
	sub("\(text:str\):", "", $0)
	sub("\(text: str\):", "", $0)
	split($0, day_part, "_day_")
	line_number[sprintf("%s,%s",day_part[2],day_part[1])] = FNR
}
