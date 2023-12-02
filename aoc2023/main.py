from aoc2023 import day1

def main() -> None:
    with open("inputs/day1/part1.txt", "r") as f:
        day1_input = f.readlines()

    print("day1-part1:", day1.part1(day1_input))
    print("day1-part2:", day1.part2(day1_input))


if __name__ == "__main__":
    main()
