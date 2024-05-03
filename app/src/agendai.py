import csv
import os
import playsound
from datetime import datetime
from app.dao.taskDAO import TaskDAO


class AgendAi:
    def __init__(self):
        self.dao = TaskDAO()
        self.tasks = []

    def loading(self):
        for task in self.dao.tasks_dao:
            self.tasks.append(task)

    def verification_task(self):
        try:
            if not self.dao.tasks_dao:
                self.dao.load_task()
            if not self.tasks:
                self.loading()
            currentDateTime = datetime.now().replace(microsecond=0)
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
        except ValueError:
            pass

    def alarm_shot(self):
        if self.verification_task():
            self.sound_alert()

    def sound_alert(self):
        sound_file = os.path.join('../sound/music1.mp3')
        playsound.playsound(sound_file)


if __name__ == '__main__':
    ag = AgendAi()
    while True:
        ag.alarm_shot()
    pass
