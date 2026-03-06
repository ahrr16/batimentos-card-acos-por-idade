''''O doutor Henry Jones Junior estabeleceu uma regra com seus alunos da disciplina de Arqueologia: todos os que obtiverem nota maior do que 8,5 na sua prova semestral serão convidados para uma visita de campo na América do Sul.

Nosso programa deve solicitar o e-mail e a nota do aluno, exibindo a mensagem “ENVIANDO CONVITE” caso a nota do aluno satisfaça a condição proposta.

Utilizando apenas um if simples, podemos resolver esse problema rapidamente! Basta solicitarmos a digitação dos dados, converter a nota para números reais (float) e verificar se ela atende à condição do professor Jones.

'''
# Obtemos o e-mail e a nota do aluno
email = str(input('Insira o e-mail do aluno: '))
nota = float(input('Insira a nota do aluno: '))

# Verifica se a nota é maior do que 8.5 para enviar o email
if nota > 8.5:
    print('E-mail enviado')