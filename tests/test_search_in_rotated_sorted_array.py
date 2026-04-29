from binary_search.search_in_rotated_sorted_array import SearchInRotatedSortedArray


def test_search_rotated():
    sol = SearchInRotatedSortedArray()
    assert sol.search([4,5,6,7,0,1,2], 0) == 4
    assert sol.search([4,5,6,7,0,1,2], 3) == -1
    assert sol.search([1], 0) == -1