#from leetcode_practice.garrison_exercises.rotate_image.rotate_image import Solution
"""
import pathlib
filepath = pathlib.Path(__file__).absolute() # gets the path of the current file
"""

import sys
from typing import List

from .rotate_image import *

def test_size4_matrix() -> None:
    input_matrix: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    output_matrix: List[List[int]] = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert(Solution.rotate(input_matrix) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

