cipher = 'UXGHI BTIWDS UGDCI UPCIPHN'
charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def check_combination(n):
    total_str = ''
    for ch in cipher:
       index = (charset.find(ch) + n) % len(charset)
       total_str += charset[ index ]
    return total_str

def combination():
    for i in range(26):
       print('{} - {}'.format(i, check_combination(i)))