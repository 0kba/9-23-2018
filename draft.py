class LineSegment:
    start = 0
    end = 0

    #constructor
    def __init__(self, start, end):
        self.start = start
        self.end  = end

    def overlap(self, other):
        if other.start > self.end or self.start > other.end:
            return False
        return True

    def __str__(self):
        return f"({self.start}, {self.end})"

def print_line_segment(line_segment):
    print(f"start: {line_segment.start} end: {line_segment.end}")

def test_overlapping(x1, y1, x2, y2):
    line1 = LineSegment(x1, y1)
    line2 = LineSegment(x2, y2)
    if line1.overlap(line2):
        return f"{line1} overlaps with {line2}"

    return f"{line1} doesn't overlap with {line2}"

def main():
    line1 = LineSegment(10,12)
    line2 = LineSegment(10,15)
    #overlapping
    #not overlapping
    #contained

    first_begin_overlapping = test_overlapping(1,5, 3,6)
    print(first_begin_overlapping)

    not_overlapping = test_overlapping(1, 5, 6 , 8)
    print(not_overlapping)

    first_contain = test_overlapping(1, 50, 3, 6)
    print(first_contain)

    second_contain = test_overlapping( 3, 6 , 1 , 50)
    print(second_contain)

    second_begin_overlapping = test_overlapping( 3, 6 , 1 ,5)
    print(second_begin_overlapping)

    similar = test_overlapping(1,3, 1, 3)
    print(similar)

    zero = test_overlapping(0,0,0,0)
    print(zero)

    negative_overlapping = test_overlapping(-3,-1,-2,1)
    print(negative_overlapping)

    negative_nonoverlapping = test_overlapping(-2,-1,-6,-4)
    print(negative_nonoverlapping)

    print_line_segment(line1)
    print_line_segment(line2)

    is_overlapping = line1.overlap(line2)
    if is_overlapping:
        print(f"{line1} overlaps with {line2}")
    else:
        print(f"{line1} doesn't overlap with {line2}")

if __name__ == '__main__':
    main()



