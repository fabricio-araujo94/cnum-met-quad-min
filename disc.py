import sympy
from func import printMatrix

def discreto():
  x = sympy.Symbol('x')

  g = []  # funções

  # adição das funções
  while True:
    temp = str(input(f'Digite a função: '))
    g.append(sympy.parse_expr(temp))

    print()
    print('[0] -- Parar')
    print('[N] -- Continuar')
    opcao = int(input('Escolha: '))
    print()

    if opcao == 0:
      break


  # Valores de x
  valor_x = []

  print('------------ valores de x --------------------')

  # Adição dos valores de x
  while True:
    valor_x.append(float(input('Digite os valores: ')))

    print()
    print('[0] -- Parar')
    print('[N] -- Continuar')
    opcao = int(input('Escolha: '))
    print()

    if opcao == 0:
      break

  # Valores de y/f(x)
  valor_y = []

  print('------------ valores de y --------------------')

  for i in range(0, len(valor_x)):
    valor_y.append(float(input('Digite os valores: ')))

  print('----------------------------------------------')

  """
  Set de número para o caso de pouco tempo
  valor_x = [-1.00, -0.75, -0.60, -0.50, -0.30, 0.00, 0.20, 0.40, 0.50, 0.70, 1.00]
  valor_y = [2.05, 1.15, 0.45, 0.40, 0.50, 0.00, 0.20, 0.60, 0.51, 1.20, 2.05]
  """

  # cálculo dos vetores
  v = []
  tamEx = len(g)
  tamIn = len(valor_x)

  for i in range(0, tamEx):
    temp = []
    for j in range(0, tamIn):
      temp.append(g[i].evalf(subs={x: valor_x[j]}))
    v.append(temp)

  V = sympy.Matrix(v)

  tam = len(g)
  print(tam)

  # valores da matriz A
  a = []
  for i in range(0, tam):
    temp = []
    for j in range(0, tam):
      temp.append(V.row(i).dot(V.row(j)))

    a.append(temp)

  # Criação do vetor y
  y = sympy.Matrix(valor_y)

  # valores da matriz B
  b = []
  for i in range(0, tam):
    b.append(y.dot(V.row(i)))

  # criação das matrizes
  A = sympy.Matrix(a)
  B = sympy.Matrix(b)

  print('----------------  MATRIZES -------------------------')
  
  print('--- A  ---')
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
