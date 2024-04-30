import csv
import os
from datetime import datetime
import playsound


class AgendAi:

    def __init__(self):
        self.tasks = []
        self.reTasks = set()

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

    def save_task(self, filename, mode=None):
        file_exist = os.path.isfile(filename)

        if mode is None:
            mode = 'a' if file_exist else 'w'

        with open(filename, mode, newline='') as file:
            write = csv.DictWriter(file, fieldnames=['Name', 'Description', 'DateTime', 'DalyAlarm'])
            if not file_exist or mode == 'w':
                write.writeheader()

            for task in self.tasks:
                write.writerow(task)
        self.tasks = []

    def load_task(self, filename):
        self.tasks = []
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                task = {
                    'Name': row['Name'],
                    'Description': row['Description'],
                    'DateTime': datetime.datetime.strptime(row['DateTime'], "%Y-%m-%d %H:%M:%S"),
                    'DalyAlarm': row['DalyAlarm']
                }
                self.tasks.append(task)

    def verification_task(self):
        if not self.tasks:
            self.load_task('../data/savetask.csv')
        currentDateTime = datetime.datetime.now().replace(microsecond=0)
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
    taskManage = AgendAi()

    taskManage.sound_alert()
#    while True:
#        taskManage.alarm_shot()
