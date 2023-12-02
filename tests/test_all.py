from aoc2023 import day1

def test_day1_part1() -> None:
    part1_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

    assert day1.part1(part1_input.split("\n")) == 142

def test_day1_part2() -> None:
    part2_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
6sevengsmxeightfive5seven"""

    assert day1.part2(part2_input.split("\n")) == 348
