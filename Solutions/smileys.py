def count_smileys(arr):
    smileys = [":)", ":-)", ":D", ";)", ";-)", ";D", ";-D"] 
    return sum([arr.count(smile) for smile in smileys])

print(count_smileys([":)", ":)", ';]', ':*', ':-)']))
