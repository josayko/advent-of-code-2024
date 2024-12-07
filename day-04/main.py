def parse_input(filename: str):
    with open(filename) as f:
        return f.read().split()


def check_row(x: int, y: int, grid: list[str]) -> bool:
    if len(grid[y]) - x < 4:
        return False
    if grid[y][x + 1] == "M" and grid[y][x + 2] == "A" and grid[y][x + 3] == "S":
        return True
    return False


def check_bottom_right(x: int, y: int, grid: list[str]) -> bool:
    if len(grid) - y < 4 or len(grid[y]) - x < 4:
        return False
    if (
        grid[y + 1][x + 1] == "M"
        and grid[y + 2][x + 2] == "A"
        and grid[y + 3][x + 3] == "S"
    ):
        return True
    return False


def check_bottom(x: int, y: int, grid: list[str]) -> bool:
    if len(grid) - y < 4:
        return False
    if grid[y + 1][x] == "M" and grid[y + 2][x] == "A" and grid[y + 3][x] == "S":
        return True
    return False


def check_bottom_left(x: int, y: int, grid: list[str]) -> bool:
    if x < 3 or len(grid) - y < 4:
        return False
    if (
        grid[y + 1][x - 1] == "M"
        and grid[y + 2][x - 2] == "A"
        and grid[y + 3][x - 3] == "S"
    ):
        return True
    return False


def check_reverse_row(x: int, y: int, grid: list[str]) -> bool:
    if x < 3:
        return False
    if grid[y][x - 1] == "M" and grid[y][x - 2] == "A" and grid[y][x - 3] == "S":
        return True
    return False


def check_top_left(x: int, y: int, grid: list[str]) -> bool:
    if x < 3 or y < 3:
        return False
    if (
        grid[y - 1][x - 1] == "M"
        and grid[y - 2][x - 2] == "A"
        and grid[y - 3][x - 3] == "S"
    ):
        return True
    return False


def check_top(x: int, y: int, grid: list[str]) -> bool:
    if y < 3:
        return False
    if grid[y - 1][x] == "M" and grid[y - 2][x] == "A" and grid[y - 3][x] == "S":
        return True
    return False


def check_top_right(x: int, y: int, grid: list[str]) -> bool:
    if y < 3 or len(grid[y]) - x < 4:
        return False
    if (
        grid[y - 1][x + 1] == "M"
        and grid[y - 2][x + 2] == "A"
        and grid[y - 3][x + 3] == "S"
    ):
        return True
    return False


def search_xmas(x: int, y: int, grid: list[str]) -> int:
    return (
        check_row(x, y, grid)
        + check_bottom_right(x, y, grid)
        + check_bottom(x, y, grid)
        + check_bottom_left(x, y, grid)
        + check_reverse_row(x, y, grid)
        + check_top_left(x, y, grid)
        + check_top(x, y, grid)
        + check_top_right(x, y, grid)
    )


def search_xmas2(x: int, y: int, grid: list[str]) -> int:
    if y < 1 or len(grid[y]) - x < 2 or x < 1 or len(grid) - y < 2:
        return False
    first_word = "".join(
        [
            grid[y - 1][x - 1],
            grid[y][x],
            grid[y + 1][x + 1],
        ]
    )
    second_word = "".join(
        [
            grid[y - 1][x + 1],
            grid[y][x],
            grid[y + 1][x - 1],
        ]
    )
    if (first_word == "MAS" or first_word == "SAM") and (
        second_word == "MAS" or second_word == "SAM"
    ):
        return True
    return False


def main():
    grid = parse_input("day-04/input.txt")
    total_count = 0
    total_count2 = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "X":
                total_count += search_xmas(x, y, grid)
            if grid[y][x] == "A":
                total_count2 += search_xmas2(x, y, grid)

    print(f"Puzzle One - count: {total_count}")
    print(f"Puzzle Two - count2: {total_count2}")
    return


if __name__ == "__main__":
    main()
