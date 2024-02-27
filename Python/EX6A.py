from collections import Counter
def count(string):
    return dict(Counter(string))
b=count('bccbrrbvv')
print(b)