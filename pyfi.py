limit = 'qweasdzxc'
print({x: ord(x) % 32 for x in limit.lower()})

alphabet = 'abcdefghijklmnopqrstuvwxyz'

print({x: alphabet.index(x) + 1 for x in limit})
