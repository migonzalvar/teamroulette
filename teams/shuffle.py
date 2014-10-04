def bind_teams(teams):
    matches = [teams[i]+teams[-i-1] for i in range(len(teams) // 2)]
    return matches


def test():
    teams = 'abcd'
    assert bind_teams(teams) == ['ad', 'bc']
    teams = 'abcxyz'
    assert bind_teams(teams) == ['az', 'by', 'cx']

test()