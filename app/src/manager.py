import datetime
from app.src.agendai import AgendAi


class Manager(AgendAi):

    def add_task(self):
        if self.tasks:
            self.tasks = []
        name = str(input("Nome da tarefa: "))
        description = str(input("Descrição: "))
        dalyAlarmChoise = str(input("Alarme diário(s,n): ")).lower()
        if dalyAlarmChoise == 's':
            time = str(input('Hora(H:M:S): '))
            dateTime = datetime.datetime.strptime(time, "%H:%M:%S")
            self.set_task(name, description, dateTime, dalyAlarm=True)
        else:
            date = str(input(f'Insira a data(Y-M-D): '))
            time = str(input(f'Insira a data(H:M:S): '))
            dateTime = datetime.datetime.strptime(date + " " + time, "%Y-%m-%d %H:%M:%S")
            self.set_task(name, description, dateTime)

    def verify(self):
        if not self.tasks:
            self.load_task('../data/savetask.csv')
        for task in self.tasks:
            for key, value in task.items():
                print(f'{key}: {value}\n')

    def modify_task(self):
        if not self.tasks:
            self.load_task('../data/savetask.csv')
        for index, task in enumerate(self.tasks):
            print(f'ID: {index} -> {task["Name"]}')
        choise_id = int(input('Digite o ID da tarefa que deseja modificar: '))
        to_update = None
        for index in self.tasks:
            if choise_id == self.tasks.index(index):
                to_update = index
                break
        if not to_update:
            print('ID não encontrado!!!')
            return
        print(to_update)

        while True:
            choise_modify = int(input('1 - Modificar Nome\n'
                                      '2 - Modificar descrição\n'
                                      '3 - Modificar Tarefas Data/Hora\n'
                                      '4 - Modifica o Modo(diario/modo agendado)\n'
                                      '0 - Sair/Salvar\n'
                                      'Selecione a opção: '))
            if choise_modify == 1:
                to_update['Name'] = new_name = str(input('Novo Nome: '))
            elif choise_modify == 2:
                to_update['Description'] = new_description = str(input('Nova Descrição: '))
            elif choise_modify == 3 and to_update['DalyAlarm'] == 'True':
                new_time = str(input('Novo Horario(H:M:S): '))
                to_update['DateTime'] = datetime.datetime.strptime(new_time, "%H:%M:%S")
            elif choise_modify == 3:
                new_date = str(input('Nova Data(Y-M-D): '))
                new_time = str(input('Nova Hora(H:M:S): '))
                to_update['DateTime'] = datetime.datetime.strptime(new_date + " " + new_time, "%Y-%m-%d %H:%M:%S")
            elif choise_modify == 4:
                if to_update['DalyAlarm'] == 'True':
                    modo = 'o modo "modo agendado"?'
                else:
                    modo = 'o modo para "modo diario"?'
                choise_dalyAlarm = str(input(f'Deseja alterar o alarme para {modo} (s,N): ')).lower()
                if choise_dalyAlarm == 's':
                    if to_update['DalyAlarm'] == 'True':
                        to_update['DalyAlarm'] = new_dalyAlarm = False
                    else:
                        to_update['DalyAlarm'] = new_dalyAlarm = True
            else:
                break
        self.save_task('../data/savetask.csv', mode='w')

    def delete_task(self):
        if not self.tasks:
            print('Carregando arquivo...')
            self.load_task('../data/savetask.csv')
        for index, task in enumerate(self.tasks):
            print(f'ID: {index} -> {task["Name"]}')
        choise_task_del_input = input('Escolha a Tarefa que deseja excluir: ')
        if choise_task_del_input == '':
            self.tasks = []
            return

        try:
            choise_task_del = int(choise_task_del_input)
            if choise_task_del >= 0 and choise_task_del < len(self.tasks):
                delete = self.tasks.pop(choise_task_del)

                for index, task in enumerate(self.tasks):
                    print(f'ID: {index} -> {task["Name"]}')
                self.save_task('../data/savetask.csv', 'w')

        except ValueError:
            print('Entrada Invalida!!!')
