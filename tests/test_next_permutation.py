from arrays.next_permutation import NextPermutation


def test_next_permutation_basic():
    solver = NextPermutation()

    nums = [1, 2, 3]
    solver.nextPermutation(nums)

    assert nums == [1, 3, 2]


def test_next_permutation_descending():
    solver = NextPermutation()

    nums = [3, 2, 1]
    solver.nextPermutation(nums)

    assert nums == [1, 2, 3]


def test_next_permutation_duplicate_values():
    solver = NextPermutation()

    nums = [1, 1, 5]
    solver.nextPermutation(nums)

    assert nums == [1, 5, 1]


def test_next_permutation_complex_case():
    solver = NextPermutation()

    nums = [1, 6, 4, 5, 3, 2]
    solver.nextPermutation(nums)

    assert nums == [1, 6, 5, 2, 3, 4]


def test_next_permutation_single_element():
    solver = NextPermutation()

    nums = [1]
    solver.nextPermutation(nums)

    assert nums == [1]