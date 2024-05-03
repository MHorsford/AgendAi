import datetime
from app.dao.taskDAO import TaskDAO


class Manager:
    def __init__(self):
        self.dao = TaskDAO()

    def add_task(self):
        try:
            name = str(input("Nome da tarefa: "))
            description = str(input("Descrição: "))
            dalyAlarmChoise = str(input("Alarme diário(s,n): ")).lower()
            if dalyAlarmChoise == 's':
                time = str(input('Hora(H:M:S): '))
                dateTime = datetime.datetime.strptime(time, "%H:%M:%S")
                self.dao.set_task(name, description, dateTime, dalyAlarm=True)
            else:
                date = str(input(f'Insira a data(Y-M-D): '))
                time = str(input(f'Insira a data(H:M:S): '))
                dateTime = datetime.datetime.strptime(date + " " + time, "%Y-%m-%d %H:%M:%S")
                self.dao.set_task(name, description, dateTime, dalyAlarm=False)
        except ValueError:
            pass

    def verify(self):
        pass

    def modify_task(self):
        choice_id = int(input('Digite o ID da tarefa que deseja modificar: '))
        try:
            for ID in self.dao.get_task():
                if choice_id == ID['ID']:
                    to_update = {}
                    while True:
                        choise_modify = int(input('1 - Modificar Nome\n'
                                                  '2 - Modificar descrição\n'
                                                  '3 - Modificar Tarefas Data/Hora\n'
                                                  '4 - Modifica o Modo(diario/modo agendado)\n'
                                                  '0 - Sair/Salvar\n'
                                                  'Selecione a opção: '))
                        if choise_modify == 1:
                            to_update['Name'] = str(input('Novo Nome: '))
                        elif choise_modify == 2:
                            to_update['Description'] = str(input('Nova Descrição: '))
                        elif choise_modify == 3 and self.dao.get_task()[choice_id - 1]['DalyAlarm']:
                            new_time = str(input('Novo Horario(H:M:S): '))
                            to_update['DateTime'] = datetime.datetime.strptime(new_time, "%H:%M:%S")
                        elif choise_modify == 3:
                            new_date = str(input('Nova Data(Y-M-D): '))
                            new_time = str(input('Nova Hora(H:M:S): '))
                            to_update['DateTime'] = datetime.datetime.strptime(new_date + " " + new_time,
                                                                               "%Y-%m-%d %H:%M:%S")
                        elif choise_modify == 4:
                            mode = 'o modo "modo agendado"?' if (self.dao.get_task()[choice_id - 1]['DalyAlarm'])\
                                                                else 'o modo "diário"?'
                            print(mode)
                            choice_alarm = str(input(f'Deseja alterar para {mode} (s/n): ')).lower()
                            if choice_alarm == 's':
                                to_update['DalyAlarm'] = False if (self.dao.get_task()[choice_id - 1]['DalyAlarm'])\
                                                                    else True
                        else:
                            break
                    self.dao.modify_task(choice_id, **to_update)
                    break
                else:
                    continue
        except ValueError:
            pass

    def delete_task(self):
        try:
            choice_id = int(input('Digite o ID da tarefa que desejas excluir: '))
            ID_tasks = [ID['ID'] for ID in self.dao.get_task()]
            if choice_id in ID_tasks:
                self.dao.del_task(choice_id)
            else:
                print('ID não encontrado!!!')
        except ValueError:
            pass
        finally:
            pass


if __name__ == '__main__':
    pass
