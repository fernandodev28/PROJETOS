"""SISTEMA TO-DO LIST"""
import os

# Lista de tarefas (Tarefas pendentes e tarefas concluídas)
pendentesLista = []
concluidasLista = []

#FUNÇÕES
#Menu
def menu(nome):
    print('\n"-SISTEMA TO-DO LIST-"\n    by-MendesDev28')
    print(f'BEM-VINDO {nome}!\n')
    print('MENU\n')
    print('[1]ADICIONAR UMA TAREFA\n[2]CONCLUIR UMA TAREFA\n[3]LISTAR TAREFAS\n[4]SAIR\n')

# Adicionar tarefas novas
def adicionar():
    while True:
        print('-ADICIONAR UMA NOVA TAREFA-\n')

        print('(DIGITE SAIR PARA VOLTAR AO MENU)')
        tarefa = input('DIGITE SUA NOVA TAREFA: ').upper( ) # RECEBENDO TAREFA

        if tarefa in pendentesLista: # TAREFA JÀ ADICIONADA Á LISTA DE PENDENTES
            os.system('cls')
            print('ESSA TAREFA JÁ FOI ADICIONADA UMA VEZ.')
            continue

        if tarefa == 'SAIR': # SAINDO DA FUNÇÃO
            os.system('cls')
            print('VOLTANDO PARA O MENU. ')
            break
    
        print(f'\nVOCÊ ESTÁ ADICIONANDO ESSA TAREFA ({tarefa}) À LISTA PENDENTE.\n')
        confirm = input('DESEJA CONTINUAR?\n [S]Sim | [N]Não: ').upper() # CONFIRMANDO ADIÇÃO DE NOVA TAREFA

        if confirm == 'S': # CONFIRMAÇÃO PARA ADICIONAR TAREFA
            pendentesLista.append(tarefa)
            os.system('cls')
            print('TAREFA ADICIONADA À LISTA PENDENTES!')
            continue

        elif confirm == 'N': # CANCELANDO AÇÃO
            os.system('cls') 
            print('TAREFA NÃO ADICIONADA.')
            continue

        else: # OPÇÃO INVÁLIDA (!= S ou N)
            os.system('cls')
            print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE')
            continue

# Concluir tarefas
def concluir():
    while True:
        os.system('cls')
        print('-CONCLUIR TAREFA-\n')

        if len(pendentesLista) <= 0: # CHECANDO SE A LISTA NÃO ESTÁ VAZIA
            print('VOCE AINDA NÃO ADICIONOU NENHUMA TAREFA.')
            break

        print('TAREFAS PENDENTES-')
        for indice, i in enumerate(pendentesLista, start=1): # MOSTRANDO A LISTA DE PENDENTES PARA VISUALIZAÇÃO DO USUÁRIO 
            print(f'{indice}º  -  {i}  -  PENDENTE')

        print('\n (DIGITE SAIR PARA VOLTAR AO MENU*)')
        TaskCompleted = input('\nDIGITE A TAREFA QUE VOCÊ CONCLUIU: ').upper() # RECEBENDO TAREFA QUE SERÁ CONCLUIDA
    
        if TaskCompleted in pendentesLista:
            pendentesLista.remove(TaskCompleted) # REMOVENDO TAREFA PENDENTE
            concluidasLista.append(TaskCompleted) # ADICIONANDO TAREFA À LISTA CONCLUÌDA
            os.system('cls')
            if len(pendentesLista) <= 0: # CHECANDO SE A LISTA NÃO ESTÁ VAZIA
                print('\nVOCÊ COMPLETOU TODAS AS TAREFAS.\n')
                break

            print(f'\nA TAREFA ({TaskCompleted}) FOI MARCADA COMO CONCLUÍDA.\n')
            continue
        
        elif TaskCompleted == 'SAIR':
            os.system('cls')
            print('VOLTADO PARA O MENU.')
            break
            
# Listar tarefas
def listar():
    while True:
        print('-LISTAR TAREFAS-\n')

        if len(pendentesLista) <= 0 and len(concluidasLista) <= 0: # CHECA SE TODAS AS LISTAS ESTÃO VAZIAS
            print('VOCÊ AINDA NÃO ADICIONOU NENHUMA TAREFA.\n')
            break

        print('[P]PENDENTES\n[C]CONCLUÍDAS\n[T]TODAS\n[S]SAIR')
        confirm = input('VOCE DESEJA LISTAR: ').upper()

        if confirm == 'P': # LISTA PENDENTE
            os.system('cls')
            print('-TAREFAS PENDENTES-')

            if len(pendentesLista) <= 0: # CONDIÇÃO DAS LISTAS VAZIAS
                os.system('cls')
                print('\nESSA LISTA ESTÁ VAZIA.')
                continue

            for indice1, i in enumerate(pendentesLista, start= 1): # EXIBIÇÃO DA LISTA      
                print(f'{indice1}º  -  {i}  -  PENDENTE\n-------------------------')
            continue
        
        elif confirm == 'C': # LISTA CONCLUÍDA
            os.system('cls')
            print('-TAREFAS CONCLUÍDAS-')

            if len(concluidasLista) <= 0: # CONDIÇÃO: LISTA VAZIA
                print('\nESSA LISTA ESTÁ VAZIA.')
                continue
            
            for indice2, i in enumerate(concluidasLista, start=1): # EXIBIÇÃO DA LISTA
                print(f'{indice2}º  -  {i}  -  CONCLUÍDA\n-------------------------')
            continue
        
        elif confirm == 'T': # TODAS AS LISTAS
            os.system('cls')
            print('-TAREFAS PENDENTES-')
            if len(pendentesLista) <= 0: # CONDIÇÃO LISTA VAZIA
                print('===LISTA VAZIA===\n\n')

            else:
                for indice1, i in enumerate(pendentesLista, start=1): # EXIBIÇÃO DA LISTA | PENDENTES
                    print(f'{indice1}º  -  {i}  -  PENDENTE\n-------------------------')

            print('\n-TAREFAS CONCLUÍDAS-')
            if len(concluidasLista) <= 0: # CONDIÇÃO LISTA VAZIA
                print('===LISTA VAZIA===\n\n')

            else:
                for indice2, i in enumerate(concluidasLista, start=1): # EXIBIÇÃO DA LISTA | CONCLUÍDAS
                    print(f'{indice2}º  -  {i}  -  CONCLUÍDA\n-------------------------')
        elif confirm == 'S':
            os.system('cls')
            print('VOLTANDO PARA O MENU.\n')
            break
        
        else:
            os.system('cls')
            print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.\n') # OPÇÃO INVÁLIDA
            continue

# Sair do Sistema
def sair():
    while True:
        print('-SAIR DO SISTEMA-\n')
        confirm = input('DESEJA SAIR?\n[S]SIM | [N]NÃO: ').upper() # CONFIRMAÇÃO PARA SAIR

        if confirm == 'S': # CONFIRMANDO PARA SAIR
            os.system('cls')
            print('SAINDO DO SISTEMA')
            while True:
                print('DIGITE SAIR PARA VOLTAR')
                confirmUsuario = input('\nDIGITE SEU NOME DE USUÁRIO: ').upper()

                if confirmUsuario != usuario: # CONDIÇÃO INVÁLIDA PARA SAIR.
                    os.system('cls')
                    print('INFORMAÇÃO INVÁLIDA.')
                    continue

                else:
                    print(f'VOLTE SEMPRE {usuario}!') # SAINDO...
                    return True    

        elif confirm == 'N': # CANCELANDO AÇÃO
            return False
        
        else: # OPÇÃO INVÁLIDA
            print('OPÇÃO INVÁLIDA.')
            return False

# LOGIN
while True:
    print('-LOGIN-\n')
    usuario = input('DIGITE SEU NOME: ').upper()
    confirmUsuario = input('CONFIRME SEU NOME DE USUÁRIO: ').upper()

    if confirmUsuario == usuario:
        os.system('cls')
        ('LOGIN FEITO COM SUCESSO!\n')
        break
    else: 
        os.system('cls')
        print('USUÁRIO INCORRETO. TENTE NOVAMENTE\n')
        continue

# INICIO SISTEMA
while True: 
    menu(confirmUsuario)
    escolha = input('DIGITE SUA ESCOLHA: ')
    os.system('cls')

    if escolha == '1': # ADICIONANDO TAREFAS
        adicionar()
        continue

    elif escolha == '2': # CONCLUIR UMA TAREFA
        concluir()
        continue
        
    elif escolha == '3': # LISTAR TAREFAS (PENDENTES E CONCLUÍDAS)
        listar()
        continue
    
    elif escolha == '4': # SAINDO DO SISTEMA 
        if sair():
            break

    else: # OPÇÃO INVÁLIDA
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
        continue