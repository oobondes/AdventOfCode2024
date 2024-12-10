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

#
#/^def part_1_day_1\(/ {
	#line_number["1,1"] = FNR
#}
#
#/^def part_2_day_1\(/ {
	#line_number["1,2"] = FNR
#}
#
#/^def part_1_day_2\(/ {
	#line_number["2,1"] = FNR
#}
#
#/^def part_2_day_2\(/ {
	#line_number["2,2"] = FNR
#}
#
#/^def part_1_day_3\(/ {
	#line_number["3,1"] = FNR
#}
#
#/^def part_2_day_3\(/ {
	#line_number["3,2"] = FNR
#}
#
#/^def part_1_day_4\(/ {
	#line_number["4,1"] = FNR
#}
#
#/^def part_2_day_4\(/ {
	#line_number["4,2"] = FNR
#}
#
#/^def part_1_day_5\(/ {
	#line_number["5,1"] = FNR
#}
#
#/^def part_2_day_5\(/ {
	#line_number["5,2"] = FNR
#}
#
#/^def part_1_day_6\(/ {
	#line_number["6,1"] = FNR
#}
#
#/^def part_2_day_6\(/ {
	#line_number["6,2"] = FNR
#}
#
#/^def part_1_day_7\(/ {
	#line_number["7,1"] = FNR
#}
#
#/^def part_2_day_7\(/ {
	#line_number["7,2"] = FNR
#}
#
#/^def part_1_day_8\(/ {
	#line_number["8,1"] = FNR
#}
#
#/^def part_2_day_8\(/ {
	#line_number["8,2"] = FNR
#}
#
#/^def part_1_day_9\(/ {
	#line_number["9,1"] = FNR
#}
#
#/^def part_2_day_9\(/ {
	#line_number["9,2"] = FNR
#}
#
#/^def part_1_day_10\(/ {
	#line_number["10,1"] = FNR
#}
#
#/^def part_2_day_10\(/ {
	#line_number["10,2"] = FNR
#}
#
#/^def part_1_day_11\(/ {
	#line_number["11,1"] = FNR
#}
#
#/^def part_2_day_11\(/ {
	#line_number["11,2"] = FNR
#}
#
#/^def part_1_day_12\(/ {
	#line_number["12,1"] = FNR
#}
#
#/^def part_2_day_12\(/ {
	#line_number["12,2"] = FNR
#}
#
#/^def part_1_day_13\(/ {
	#line_number["13,1"] = FNR
#}
#
#/^def part_2_day_13\(/ {
	#line_number["13,2"] = FNR
#}
#
#/^def part_1_day_14\(/ {
	#line_number["14,1"] = FNR
#}
#
#/^def part_2_day_14\(/ {
	#line_number["14,2"] = FNR
#}
#
#/^def part_1_day_15\(/ {
	#line_number["15,1"] = FNR
#}
#
#/^def part_2_day_15\(/ {
	#line_number["15,2"] = FNR
#}
#
#/^def part_1_day_16\(/ {
	#line_number["16,1"] = FNR
#}
#
#/^def part_2_day_16\(/ {
	#line_number["16,2"] = FNR
#}
#
#/^def part_1_day_17\(/ {
	#line_number["17,1"] = FNR
#}
#
#/^def part_2_day_17\(/ {
	#line_number["17,2"] = FNR
#}
#
#/^def part_1_day_18\(/ {
	#line_number["18,1"] = FNR
#}
#
#/^def part_2_day_18\(/ {
	#line_number["18,2"] = FNR
#}
#
#/^def part_1_day_19\(/ {
	#line_number["19,1"] = FNR
#}
#
#/^def part_2_day_19\(/ {
	#line_number["19,2"] = FNR
#}
#
#/^def part_1_day_20\(/ {
	#line_number["20,1"] = FNR
#}
#
#/^def part_2_day_20\(/ {
	#line_number["20,2"] = FNR
#}
#
#/^def part_1_day_21\(/ {
	#line_number["21,1"] = FNR
#}
#
#/^def part_2_day_21\(/ {
	#line_number["21,2"] = FNR
#}
#
#/^def part_1_day_22\(/ {
	#line_number["22,1"] = FNR
#}
#
#/^def part_2_day_22\(/ {
	#line_number["22,2"] = FNR
#}
#
#/^def part_1_day_23\(/ {
	#line_number["23,1"] = FNR
#}
#
#/^def part_2_day_23\(/ {
	#line_number["23,2"] = FNR
#}
#
#/^def part_1_day_24\(/ {
	#line_number["24,1"] = FNR
#}
#
#/^def part_2_day_24\(/ {
	#line_number["24,2"] = FNR
#}
#
#/^def part_1_day_25\(/ {
	#line_number["25,1"] = FNR
#}
#
#/^def part_2_day_25\(/ {
	#line_number["25,2"] = FNR
#}
