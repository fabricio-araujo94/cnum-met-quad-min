import sympy
from func import printMatrix

def continuo():
  x = sympy.Symbol('x')

  f = sympy.parse_expr(str(input('Digite a função f: ')))

  g = [] # Funções

  # Obtenção das funções
  while True:
    temp = str(input(f'Digite a função g: '))
    g.append(sympy.parse_expr(temp))

    print()
    print('[0] -- Parar')
    print('[N] -- Continuar')
    opcao = int(input('Escolha: '))
    print()

    if opcao == 0:
      break


  # limites da integral
  inf = float(input('Limite inferior da integral: '))
  sup = float(input('Limite superior da integral: '))

  # valores da matriz A
  a = []
  tam = len(g)

  for i in range(0, tam):
    temp = []
    for j in range(0, tam):
      temp.append(sympy.integrate(g[i] * g[j], (x, inf, sup)))

    a.append(temp)

  # valores da matriz B
  b = []
  for i in range(0, tam):
    b.append(sympy.integrate(f * g[i], (x, inf, sup)))

  # criação das matrizes
  A = sympy.Matrix(a)
  B = sympy.Matrix(b)

  print('----------------  MATRIZES -------------------------')

  print('--- A ---')
  printMatrix(A, len(g))

  print('--- B ---')
  printMatrix(B, len(g))

  print('----------------  RESOLUÇÃO -------------------------')
  eq = A.solve(B)
  printMatrix(eq, len(g))

  # Formulação da reta φ
  formula = ''

  for i in range(0, len(eq)):
    formula += str(round(eq[i], 2) * g[i])

    if i == len(eq) - 1:
      break

    if eq[i + 1] > 0:
      formula += ' + '
    else:
      formula += ' '

  formula = sympy.parse_expr(formula)

  print('----------------  Equação da Reta -------------------------')

  print(formula)
