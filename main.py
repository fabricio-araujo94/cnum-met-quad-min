# Para o funcionamento do código, é necessário instalar
# o mpmath ( pip install mpmath )
# e o sympy ( pip install sympy )
# respectivamente.

from disc import discreto
from cont import continuo

while True:
    print('--------- Menu ----------')
    print()
    print('[1] -- Caso Discreto')
    print('[2] -- Caso Contínuo')
    print()
    esc = int(input('Escolha: '))

    if esc == 1:
        discreto()
    elif esc == 2:
        continuo()
    else:
        print()
        print('Digite uma opção válida')
        continue
    break

print('-------------------------')
print()