def newRegistration():              #H1
    newStudent = input(" Insira o nome completo do novo aluno: ")
    gmailStudent = input(" Insira o Gmail do aluno: ")

    cadastroAlunos = ['Estudante'] = newStudent
    cadastroAlunos = ['Gmail'] = gmailStudent

    intlistaAlunos.append(cadastroAlunos)


def listStudentsRegistration():      #H2
    listStudentsAZ

def listStudentsAZ():   #H3
    listaAlunos.sort()
    print(listaAlunos)


def filterStudentes():   #H4
    filtrarAluno = input(" Insira o nome completo do aluno: ")
    if filtrarAluno == true: 
        print(filtrarAluno in listaAlunos)

    print(listaAlunos.get(filtrarAluno, 'Contato não existente na lista, olha o golpe!'))


def removeStudents():    #H5

    alunoRemover = input("Insira o nome do aluno que deseja remover: ")
    print(listaAlunos.pop(alunoRemover, 'Contato não encontrado na lista'))

def changeName():    #H6
    listStudentsRegistration

def main():
    listaAlunos = []
    cadastroAlunos = {'Estudante' : 'Gmail' 

    print("Bem-vindo ao evento técnico\n")

    #Criar um laço de repetição

    print("1 - Cadastrar Novo Aluno")
    print("2 - Lista de todos alunos cadastrados(Ordem de cadastro)")
    print("3 - Lista de todos alunos cadastrados(Ordem Alfabética)")
    print("4 - Filtrando Aluno")
    print("5 - Remover Aluno ")
    print("6 - Alterar o nome do cadastro")

    op = int(input("Insira o número correspondente a função que deseja executar: "))

    if op >= 1 or <= 6:
        if op == 1:
            newRegistration()
        elif op == 2:
            listStudentsRegistration()
        elif op == 3:
            listStudentsAZ()
        elif op == 4:
            filterStudentes()
        elif op == 5:
            removeStudents()
        else:
            changeName()
    else:
        print("ERROR!! Você esta inserindo um valor não correspondente a lista!")


    #Criar um laço de repetição



if name == "main":
    main()