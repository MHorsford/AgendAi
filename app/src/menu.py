from app.src.manager import Manager
import os


def select_option():
    choise = str(input('1 - Adicionar uma tarefa\n'
                       '2 - Verificar tarefas\n'
                       '3 - Modificar uma tarefa\n'
                       '4 - Excluir uma tarefa\n'
                       '5 - Inicie\n'
                       '0 - Sair/Salvar\n'
                       'Selecione a opção: '))
    return choise


taskManage = Manager()
file = os.path.isfile('../data/savetask.csv')
if not file:
    taskManage.save_task('../data/savetask.csv')

while True:

    choise = select_option()

    if choise == '1':
        taskManage.add_task()
        taskManage.save_task('../data/savetask.csv')
    elif choise == '2':
        taskManage.verify()
    elif choise == '3':
        taskManage.modify_task()
    elif choise == '4':
        taskManage.delete_task()
    elif choise == '5':
        taskManage.alarm_shot()
    elif choise == '0':
        break