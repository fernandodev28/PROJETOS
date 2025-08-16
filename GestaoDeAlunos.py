"           <GESTÃO DE ALUNOS>            "
import os
" Listas "
alunos = ['ANA', 'BRUNO', 'CARLOS', 'DANIELA', 'EDUARDO', 'FERNANDA', 'GABRIEL', 'HELENA'] # LISTA TESTE
notas = [8.5, 7.0, 9.2, 6.8, 7.5, 8.0, 9.0, 6.5] # LISTA TESTE

# FUNÇÕES DE MENU, LOGIN E SENHAS:
# MENU
def menu(nome = 'Usuário'): 
    print('GESTÃO DE ALUNOS\n')
    print(f'USUÁRIO\n{nome}\n \nBEM-VINDO!')
    print('Selecione uma opção')
    print('[1] Cadastrar aluno \n[2] Consultar dados do aluno \n[3] Listar alunos \n[4] Remover aluno \n[5] Sair ')
# SENHA
def confirm_Senha(confirmSenha = 0):
    while True:
        print('"CONFIRME SUA SENHA"')
        confirmSenha = input('DIGITE SUA SENHA: ')
        if confirmSenha != senha:
            os.system('cls')
            print('Senha inválida. Tente novamente.')
            continue
        else:
            os.system('cls')
            print('Acesso liberado.')
            break           

# FUNÇÕES DAS OPÇÕES DO USUÁRIO:
# CADASTRO
def cadastroAluno():
    os.system('cls')
    while True:
        print('"CADASTRO DO ALUNO" \n(Digite "SAIR" para voltar ao menu.)\n')

        aluno = input('Digite o nome do aluno: ').upper()
        if aluno in alunos:
            print(f'Esse aluno({aluno}) já está cadastrado.')
            continue
        if aluno == 'SAIR' or aluno == 'sair':
            print(' \nVoltando para o menu.\n ')
            os.system('cls')
            break
        alunos.append(aluno)

        nota = float(input('Digite a nota do aluno: '))
        if nota < 0:
            print('A nota do aluno não pode ser negativa. Tente novamente.\n  ')
            continue     
        if nota > 10:
            print('A nota não pode ser maior que 10. Tente novamente')
            continue
        notas.append(nota)
        os.system('cls')
        print(' \nAluno cadastrado com sucesso!')
# CONSULTA DE DADOS
def consultarAluno():
    os.system('cls')
    while True:
        print('"CONSULTAR DADOS DO ALUNO""\n  \nDigite "SAIR" para voltar ao menu.\n')

        consulta = input('Digite o nome do aluno: ').upper()
        if consulta in alunos:
            matricula = alunos.index(consulta)
            os.system('cls')
            print(' \nDados do aluno:\n ')
            print(f'Nº do cadastro: {matricula} \nNome: {consulta}\nNota: {notas[matricula]}')
            continue
        elif consulta == 'SAIR':
            print('\nVoltando para o menu.\n')
            os.system('cls')
            break
        else:
            print(f'O aluno - {consulta} não está cadastrado.')
            continue
# LISTAR ALUNOS
def listarAlunos():
    os.system('cls')
    while True:
        print('"LISTA DOS ALUNOS CADASTRADOS"\n')
        print('Alunos:\n')
        
        for i in range(len(alunos)):
            print(f'| Nº {i} - {alunos[i]} - {notas[i]} ')

        confirm = input('\nVoltar ao menu?\n[S]sim | [N]não: ').upper()
        if confirm == 'N':
            continue

        elif confirm == 'S':
            os.system('cls')
            print('Voltando para o menu.\n')
            break

        else: 
            os.system('cls')
            print('Digite uma opção válida. [S] ou [N].')
# REMOVER ALUNO(S)
def removerAluno():
    os.system('cls')
    while True:
        print('"REMOVER ALUNO CADASTRADO"\n')
        
        remocao = input('Digite o nome do aluno: ')
        if remocao in alunos:
            id_remocao = alunos.index(remocao)
            alunos.pop(id_remocao)
            notas.pop(id_remocao)
            print(f'O aluno {remocao} foi removido com sucesso!')
        else:
            print(f'O aluno {remocao} não está cadastrado ou já foi removido.')
        
        confirm = input('Deseja remover mais algum aluno?\n[S]sim ou [N]não: ')
        if confirm == 'S':
            os.system('cls')
            continue
        elif confirm == 'N':
            os.system('cls')
            break
# SAIR DO SISTEMA
def sair():
    while True:
        print('"SAINDO DO SISTEMA"')
        confirm = input('\nVocê deseja sair?\n[S]sim || [N]não: ').upper()
        if confirm == 'N':
            os.system('cls')
            print('Voltando para o sistema.')
            break
        elif confirm == 'S':
            os.system('cls')
            print('Saindo do sistema...')
            return True
        else:
            os.system('cls')
            print('Digite uma opção válida.')
            continue            
# INICIO DO PROGRAMA
# LOGIN: NOME E SENHA
while True:
    print('"SISTEMA DE GESTÃO DE ALUNOS"\n')
    usuario = input('DIGITE SEU NOME COMPLETO: ').upper()
    if len(usuario.strip()) == 0:
        os.system('cls')
        print('Nome inválido.')
        continue
    else:
        break
while True:
    senha = input('DIGITE UMA SENHA: ')
    if len(senha.strip()) < 4:
        os.system('cls')
        print('Senha inválida.\nSua senha deve conter 4 dígitos ou mais.')
        continue
    else:
        confirm_Senha(senha)
        os.system('cls')
        print('LOGIN CONCLUÍDO!')
        break

# MENU E OPÇÕES DO USUÁRIO
while True:
    menu(usuario)
    opcao = input('Digite sua opção: ')

#   "CADASTRO DO ALUNO"
    if opcao == '1':
        cadastroAluno()
#   "CONSULTAR DADOS DE UM DETERMINADO ALUNO" 
    elif opcao == '2':
        consultarAluno()
#   "LISTAR ALUNOS CADASTRADOS"
    elif opcao == '3':
        listarAlunos()
#   "REMOVER ALUNO CADASTRADO"
    elif opcao == '4':
        removerAluno()
#   "SAINDO DO SISTEMA"
    elif opcao == '5':
        if sair():
            break