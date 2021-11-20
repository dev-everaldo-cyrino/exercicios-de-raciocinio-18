n = float(input('massa da substancia em gramas: '))
meiavida = n
tempo = 0
while meiavida >= 0.05:
    meiavida *= 0.5
    tempo +=50
print('para q a substancia de massa {}g atinja 0.05g , levou {:.0f}s'.format(n,tempo))