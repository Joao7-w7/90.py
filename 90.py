aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = '\033[4;32mAprovado\033[m'
elif 5 <= aluno['media'] < 7:
    aluno['situaçâo'] = '\033[4;33mRecuperação\033[m'
else:
    aluno['situação'] = '\033[4;31mReprovado\033[m'
print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} e igual a {v}')