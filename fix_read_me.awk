#!/usr/bin/awk -f

BEGIN {
    FS="|"
}

#|status|day#-part#|time|
/\|[0-9]* ?\|[0-9]+-[0-9]\|/ {
    printf("%s|%s|%s|\n", $1, $2, $3)
    if ($2 ~ ".*not complete.*")
    {
        printf("|not complete|%s|NA|\n", $3)
    }
    else
    {
        n=split($3, day_part, "-")
        printf("|complete|(%s-%s)[/AOC/day_%s.py#L%s]|%s|\n", day_part[1], day_part[2], day_part[1], line_number["def part_"day_part[2]"_day_"day_part[1]"(text:str):"], $4)
    }
}

/^def part_[12]_day_/ {
    print NR
    line_number[$0] = NR
    }
