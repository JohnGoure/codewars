from DailyProgrammer.PyThreeSum import PythagoreanThreeSum as PYTHA

def test_120():
    assert PYTHA().findAll(120) == [
                                    [20, 48, 52], 
                                    [24, 45, 51], 
                                    [30, 40, 50]]

def test_fast_120():
    assert PYTHA().findAllFaster(120) == [
                                    [20, 48, 52], 
                                    [24, 45, 51], 
                                    [30, 40, 50]]
