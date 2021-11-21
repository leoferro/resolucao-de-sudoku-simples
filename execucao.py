from sudoku import Tabela

from PIL import Image

# creating a object
im = Image.open('sdk.jpeg')
print('Abbrindo imagem do sudoku de exemplo')

im.show()

#------------------------------ TESTES -----------------------------------------------------
t1 = Tabela()

#Para teste adicionar cada celula com atribuir_valor(linha, coluna, valor)

t1.atribuir_valor(0,2,5)
t1.atribuir_valor(0,4,3)
t1.atribuir_valor(0,6,7)
t1.atribuir_valor(0,8,2)

t1.atribuir_valor(1,0,6)
t1.atribuir_valor(1,2,9)
t1.atribuir_valor(1,8,8)

t1.atribuir_valor(2,3,1)

t1.atribuir_valor(3,6,6)

t1.atribuir_valor(4,0,3)
t1.atribuir_valor(4,1,5)
t1.atribuir_valor(4,3,7)
t1.atribuir_valor(4,4,4)
t1.atribuir_valor(4,5,9)
t1.atribuir_valor(4,6,8)
t1.atribuir_valor(4,8,1)

t1.atribuir_valor(5,3,2)
t1.atribuir_valor(5,5,5)
t1.atribuir_valor(5,7,3)
t1.atribuir_valor(5,8,4)

t1.atribuir_valor(6,1,4)
t1.atribuir_valor(6,2,8)
t1.atribuir_valor(6,3,6)
t1.atribuir_valor(6,5,1)
t1.atribuir_valor(6,6,2)

t1.atribuir_valor(7,1,6)
t1.atribuir_valor(7,5,7)
t1.atribuir_valor(7,7,8)
t1.atribuir_valor(7,8,9)

t1.atribuir_valor(8,1,9)
t1.atribuir_valor(8,2,7)
t1.atribuir_valor(8,4,5)
t1.atribuir_valor(8,5,3)
t1.atribuir_valor(8,6,4)

t1.repeticao()