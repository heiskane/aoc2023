DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part1() -> int:
    with open("inputs/day1/part1.txt", "r") as f:
        data = f.readlines()

    result = 0
    for line in data:
        first = next(i for i in line if i.isdigit())
        last = next(i for i in reversed(line) if i.isdigit())
        result += int(first + last)

    return result


def part2() -> int:
    with open("inputs/day1/part1.txt", "r") as f:
        data = f.readlines()

    result = 0
    numbers = list(DIGITS.keys()) + list(DIGITS.values())
    for line in data:
        first = None
        last = None
        for num in numbers:
            if line.find(num) < 0:
                continue
            if first is None or line.find(num) < first[1]:
                first = (num, line.find(num))
            if last is None or line.rfind(num) > last[1]:
                last = (num, line.rfind(num))

        assert first is not None, line
        assert last is not None, line

        if first[0] in DIGITS.keys():
            first = DIGITS[first[0]]
        else:
            first = first[0]

        if last[0] in DIGITS.keys():
            last = DIGITS[last[0]]
        else:
            last = last[0]

        result += int(first + last)

    return result


def main() -> None:
    assert part1() == 54634
    assert part2() == 53855


if __name__ == "__main__":
    main()
