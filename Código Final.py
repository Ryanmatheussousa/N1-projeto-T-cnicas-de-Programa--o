def newRegistration():        #H1
    newStudent = input(" Insira o nome completo do novo aluno: ")
    gmailStudent = input(" Insira o Gmail do aluno: ")

    cadastroAlunos = ['Estudante'] = newStudent
    cadastroAlunos = ['Gmail'] = gmailStudent

    listaAlunos.append(cadastroAlunos)


def listStudentsRegistration():      #H2
    print("Lista de cadastros:")
    print("\n")
    print(listaAlunos)

def listStudentsAZ():   #H3
    listaAlunos.sort()
    print(listaAlunos)


def filterStudentes():   #H4
    filtrarAluno = input(" Insira o nome completo do aluno: ")

    print(listaAlunos.get(filtrarAluno, 'Contato não existente na lista' ))


def removeStudents():    #H5

    alunoRemover = input("Insira o nome do aluno que deseja remover: ")
    print(listaAlunos.pop(alunoRemover, 'Contato não encontrado na lista'))
def changeName():    #H6
    usuario = input("Insira o nome completo do usuario que deseja alterar o cadastro:")
    for usuario in cadastroAlunos:
       if (usuario["Estudante"] = Estudante):
        newGmail = input("Insira o novo Gmail:")
        Estudante("Gmail") =  newGmail
       else:
        print("Desculpe valor invalido")

def main():
    listaAlunos = []
    cadastroAlunos = {'Estudante' : 'Gmail' }

    print("Bem-vindo ao evento técnico\n")

    while repetição == sim:

    print("1 - Cadastrar Novo Aluno")
    print("2 - Lista de todos alunos cadastrados(Ordem de cadastro)")
    print("3 - Lista de todos alunos cadastrados(Ordem Alfabética)")
    print("4 - Filtrando Aluno")
    print("5 - Remover Aluno ")
    print("6 - Alterar o nome do cadastro")

    op = int(input("Insira o número correspondente a função que deseja executar: "))


    if op == 1:
        newRegistration()
    elif op < 1:
        print("Você esta inserindo um valor não correspondente a tabela!")
    elif op > 6:
        print("Você esta inserindo um valor não correspondente a tabela!")
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


    repeticao = str(input("Deseja revisar ou alterar alguma coisa?(sim ou não) "))

    while("repetição")

    if name == "main":
       main()