import pandas as pd
import openpyxl as np
import csv


tabela =  pd.read_csv("notas.csv", sep=",")
m1 = (7.0 + 7.0)/2
m2 = (3.0 + 1.0)/2
m3 = (9.0 + 4.0)/2
m4 = (10.0 + 6.0)/2

media_geral = (m1+m2+m3+m4)/4

falta1 = 1.0
falta2 = 7.0
falta3 = 2.0
falta4 = 9.0

if falta1 > 5 or m1 < 7:
    status1 = ('reprovado')
else:
    status1 = ('aprovado')

if  falta2 > 5 or m2 < 7:
        status2 = ('reprovado')
else:
         status2 = ('aprovado')

if  falta3 > 5 or m3 < 7:
        status3 = ('reprovado')
else:
         status3 = ('aprovado')

if  falta4 > 5 or m4 < 7:
        status4 = ('reprovado')
else:
         status4 = ('aprovado')
print('  ')
print('-----------------RESULTADO----------------')
print('=> A média geral da turma é {:.3f} ou {:.1f};'.format(media_geral, media_geral))

maior = 0
if m2 > m1 and m2 > m3 and m2 > m4:
    maior = m2
    print(f'=> O aluno2 possui a maior média => {maior}')
elif m3 > m1 and m3 > m2 and m3 > m4:
    maior = m3
    print(f'=> O aluno3 possui a maior média => {maior}')
elif m4 > m1 and m4 > m2 and m4 > m3:
    maior = m4
    print(f'=> O aluno4 possui a maior média => {maior}')
else:
    maior = m1
    print(f'=> O aluno1 possui a maior média => {maior}')
print('  ')

pd.set_option('display.precision', 1)

valor_média = [m1, m2, m3, m4]  
status = [status1, status2, status3, status4]     
tabela.insert(loc=4, column='média', value=valor_média)
tabela.insert(loc=5, column='situação', value=status)

print(tabela)

tabela.to_csv("alunos_situacao.csv")
print(' ')
print('Dataframe foi salva no arquivo => alunos_situacao.csv')