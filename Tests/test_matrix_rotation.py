from Solutions.matrix_rotation import rotate


def test_rotation():
    assert rotate([['a']*4, ['b']*4, ['c']*4, ['d']*4]) == (
        [
            ['d', 'c', 'b', 'a'],
            ['d', 'c', 'b', 'a'],
            ['d', 'c', 'b', 'a'],
            ['d', 'c', 'b', 'a']
        ]
    )
