from Solutions.Delimiter_Matching import Matching


def test_matching():
    assert Matching().match('y[a{(bc)}d]e') is True


def test_bracket_matching():
    assert Matching().match('[[]]]') is False


def test_brace_matching():
    assert Matching().match('{[]}}') is False


def test_curve_brace():
    assert Matching().match('(()))))') is False
