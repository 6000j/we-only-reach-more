import numpy as np
import hexy as hx
import hexutils as hu

def test_get_hex_line():
    expected = [
            (0, 0, 0),
            (0, -1, 1),
            (-1, 0, 1),
            (-1, -1, 2),
            ]
    start = np.array([0, 0, 0])
    end = np.array([-1, -1, 2])
    print(hu.get_hex_line(start, end, supercover=True))
    print(expected);
    assert(
        hu.get_hex_line(start, end, supercover=True).sort() == expected.sort());

if __name__ == "__main__":
    test_get_hex_line()