from arrays.product_except_self import ProductExceptSelf


def test_product_except_self():
    sol = ProductExceptSelf()
    assert sol.productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert sol.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]