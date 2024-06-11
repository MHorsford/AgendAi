import os
import playsound
from datetime import datetime
from time import sleep
from app.dao.taskDAO import TaskDAO
import threading as th
import sqlite3


class AgendAi:
    def __init__(self):
        self.dao = TaskDAO()
        self.tasks = []
        self.mutex = th.Lock()
        self.running = False

    def loading(self):
        if not self.dao.tasks_dao:
            self.dao.load_task()
        self.tasks.clear()
        for task in self.dao.tasks_dao:
            if isinstance(task['DateTime'], str):
                task['DateTime'] = datetime.strptime(task['DateTime'], '%Y-%m-%d %H:%M:%S')
            self.tasks.append(task)

    def reloading(self):
        self.dao.load_task()
        if len(self.tasks) != len(self.dao.tasks_dao):
            print('Recarregando Tarefas...')
            self.tasks.clear()
            self.loading()

    def verification_task(self):
        self.running = True
        try:
            if not self.dao.tasks_dao:
                self.dao.load_task()
            if not self.tasks:
                self.loading()
            print('Verificando Tarefas!!!')
            while self.running:
                currentDateTime = datetime.now().replace(second=0, microsecond=0)
                for task in self.tasks:
                    if task['DateTime'].replace(second=0, microsecond=0) == currentDateTime:
                        print(f'A tarefa {task["Name"], " -> ", task["DateTime"]} foi executada!!!')
                        print('Alarme Disparado!!!')
                        self.sound_alert()
                    if (task['DalyAlarm'] and task['DateTime'].time().replace(second=0, microsecond=0)
                            == currentDateTime.time()):
                        print(f'A tarefa {task["Name"], " -> ", task["DateTime"].time()} foi executada!!!')
                        print('Alarme Disparado!!!')
                        self.sound_alert()
                    print(f'Hora atual -> {currentDateTime}')
                    print(task['Name'], ' -> ', task['DateTime'])
                    sleep(1)
                if self.running is False:
                    break
        except ValueError:
            pass

    def stop(self):
        print('Verificação de Tarefas Encerrada!!!')
        self.running = False

    def sound_alert(self):
        sound_file = os.path.join('../assets/sound/music1.mp3')
        playsound.playsound(sound_file)


if __name__ == '__main__':
    pass
