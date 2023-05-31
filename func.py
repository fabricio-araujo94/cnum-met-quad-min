def printMatrix(A, tam):
  for i in range(0, tam):
    for j in A.row(i):
      print(f'{j:.2f}', ' ', end='')
    print()