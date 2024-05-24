from app.src.manager import Manager
from app.src.agendai import AgendAi
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
agendai = AgendAi()
file = os.path.isfile('../data/Tasks.db')
if not file:
    taskManage.dao.create_table()
while True:
    choise = select_option()
    if choise == '1':
        taskManage.add_task()
    elif choise == '2':
        taskManage.verify()
    elif choise == '3':
        taskManage.modify_task()
    elif choise == '4':
        taskManage.delete_task()
    elif choise == '5':
        agendai.loading()
        while True:
            agendai.alarm_shot()
    elif choise == '0':
        break
