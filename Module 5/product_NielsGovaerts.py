def times(int1, int2):
    assert isinstance(int1,int) and isinstance(int2,int)
    assert int2 >= 0


    assert int1 == 1*int1
    product = int1
    assert product == 1*int1
    count = 1
    assert product == count*int1

    while not count == int2:
        assert product == count*int1 and count < int2
        assert product + int1 == (count+1)*int1
        product = product + int1
        assert product == (count+1)*int1        
        count += 1
        assert product == count*int1

    assert product == count*int1 and count == int2
    assert product == int1*int2
    return product
        
        
