reino = input()
tipo = input()
come_oque = input()

if reino == 'vertebrado' and tipo == 'ave':
    print('aguia') if come_oque == 'carnivoro' else print('pomba')
elif reino == 'vertebrado' and tipo == 'mamifero':
    print('homem') if come_oque == 'onivoro' else print('vaca')

if reino == 'invertebrado' and tipo == 'inseto':
    print('pulga') if come_oque == 'hematofago' else print('lagarta')
elif reino == 'invertebrado' and tipo == 'anelideo':
    print('sanguessuga') if come_oque == 'hematofago' else print('minhoca')
