import csv
import os
import playsound
from datetime import datetime
from app.dao.taskDAO import TaskDAO


class AgendAi:
    def __init__(self):
        self.dao = TaskDAO()
        self.tasks = []

    def set_task(self, name, description, dateTime, dalyAlarm=False):
        if dateTime is None and dalyAlarm is None:
            ValueError('É necessario fornecer valores para DateTime ou DalyTime.')
        if dateTime is not None and dalyAlarm is not None:
            ValueError('Apenas um dos parâmetros pode ser declarado.')

        self.tasks.append({
            'Name': name,
            'Description': description,
            'DateTime': dateTime,
            'DalyAlarm': True if dalyAlarm else False
        })


    def loading(self):
        for task in self.dao.tasks_dao:
            self.tasks.append(task)

    def verification_task(self):
        if not self.tasks:
            self.dao.load_task()
        currentDateTime = datetime.now().replace(microsecond=0)
        print(currentDateTime)
        for task in self.tasks:
            if task['DateTime'] == currentDateTime:
                print(f'A tarefa {task["Name"], " -> ", task["DateTime"]} foi executada!!!')
                print('Alarme Disparado!!!')
                return True
            if task['DalyAlarm'] and task['DateTime'].time() == currentDateTime.time():
                print(f'A tarefa {task["Name"], " -> ", task["DateTime"]} foi executada!!!')
                print('Alarme Disparado!!!')
                return True
            print(f'Hora atual -> {currentDateTime}')
            print(task['Name'], ' -> ', task['DateTime'])
            print('Verificando Tarefa...')
        return False

    def alarm_shot(self):
        if self.verification_task():
            self.sound_alert()

    def sound_alert(self):
        sound_file = os.path.join('../sound/music1.mp3')
        playsound.playsound(sound_file)


if __name__ == '__main__':
    pass
