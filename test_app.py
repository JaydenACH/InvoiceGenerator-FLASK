from backendprocess import showcurrency, provide_defprojid, getcurrbyid


def test_showcurrency():
    results = showcurrency()
    assert len(results[0]) == 5
    
    
def test_provide_defprojid():
    assert provide_defprojid() == "PRJ00003"
    
    
def test_getcurrbyid():
    assert getcurrbyid(2) == "MYR"