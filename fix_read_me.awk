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
    # make key "day,part" and set that key to the line number
    key = $0
    sub(/_day_/, ",", key)
    gsub(/[^0-9,]/, "", key)
    split(key, part_day, ",")
    key=sprintf("%s,%s", part_day[2], part_day[1])
	line_number[key] = FNR
}
