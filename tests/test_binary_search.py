from binary_search.binary_search import BinarySearch

def test_found():
    assert BinarySearch().search([-1,0,3,5,9,12], 9) == 4

def test_not_found():
    assert BinarySearch().search([-1,0,3,5,9,12], 2) == -1

def test_single_element_found():
    assert BinarySearch().search([2], 2) == 0

def test_single_element_not_found():
    assert BinarySearch().search([2], 3) == -1

def test_first_element_found():
    assert BinarySearch().search([2, 3, 4], 2) == 0

def test_last_element_found():
    assert BinarySearch().search([2, 3, 4], 4) == 2