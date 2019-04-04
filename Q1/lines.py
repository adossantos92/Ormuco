def overlap(line1, line2):
    assert len(line1) == 2 and len(line2) == 2

    min_line1, max_line1 = sorted(line1)
    min_line2, max_line2 = sorted(line2)

    # If minimum of line1 superior to minimum of line2, invert lines
    if min_line2 > min_line1:
        min_line1, min_line2 = min_line2, min_line1
        max_line1, max_line2 = max_line2, max_line1

    return (min_line2 <= min_line1 <= max_line2) or (min_line2 <= max_line1 <= max_line2)


if __name__ == '__main__':
    print(overlap((0,1), (2,3)))
    print(overlap((0,2), (1,3)))
    print(overlap((0,3), (1,2)))
    print(overlap((1,3), (0,2)))
    print(overlap((2,3), (0,1)))