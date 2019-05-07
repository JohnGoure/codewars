from Solutions.Delimiter_Matching import Matching

def test_matching():
    assert Matching().match('y[a{(bc)}d]e') == True

def test_bracket_matching():
    assert Matching().match('[[]]]') == False

def test_brace_matching():
    assert Matching().match('{[]}}') == False

def test_curve_brace():
    assert Matching().match('(()))))') == False
