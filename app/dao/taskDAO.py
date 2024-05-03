from datetime import datetime
import sqlite3
import os


class TaskDAO:
    def __init__(self):
        self.connect = sqlite3.connect('../data/Tasks.db')
        self.cursor = self.connect.cursor()

        self.tasks_dao = []

    def create_table(self):
        try:
            if not os.path.exists('../data/Tasks.db'):
                with open('../data/Tasks.db', 'w') as file:
                    pass
            self.cursor.execute('CREATE TABLE IF NOT EXISTS Tasks('
                                'ID INTEGER PRIMARY KEY AUTOINCREMENT,'
                                'Name TEXT,'
                                'Description TEXT,'
                                'DateTime TEXT,'
                                'DalyAlarm NUMERIC)')
        except sqlite3.Error as e:
            print(f'Não foi possivel criar a base de dados: {e}!!!')
        finally:
            pass

    def load_task(self):
        try:
            if not self.connect:
                self.connect = sqlite3.connect('../data/Tasks.db')
                self.cursor = self.connect.cursor()
            self.cursor.execute('SELECT * FROM Tasks')
            rows = self.cursor.fetchall()
            for row in rows:
                task = {
                    'ID': row[0],
                    'Name': row[1],
                    'Description': row[2],
                    'DateTime': datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S'),
                    'DalyAlarm': row[4]
                }
                self.tasks_dao.append(task)
        except sqlite3.Error as e:
            print(f'Não foi possivel carregar a base de dados: {e}')
        finally:
            pass

    def set_task(self, name, description, dateTime, dalyAlarm=False):
        try:
            if not self.connect:
                self.connect = sqlite3.connect('../data/Tasks.db')
                self.cursor = self.connect.cursor()
            self.cursor.execute('INSERT INTO Tasks (Name, Description, DateTime, DalyAlarm) VALUES (?, ?, ?, ?)',
                                (name, description, dateTime, dalyAlarm))
            self.connect.commit()
        except sqlite3.Error as e:
            print(f'Erro ao inserir a tarefa: {e}!!!')
        finally:
            pass

    def modify_task(self, ID, **kwarg):
        if not self.tasks_dao:
            self.load_task()
        if not self.connect:
            self.connect = sqlite3.connect('../data/Tasks.db')
            self.cursor = self.connect.cursor()
        try:
            command_sql_1 = 'UPDATE Tasks SET '
            command_sql_2 = ', '.join([f'{key} = ?' for key in kwarg.keys()])
            command_sql_3 = ' WHERE ID = ?'
            values = list(kwarg.values()) + [ID]
            sql = f'{command_sql_1}{command_sql_2}{command_sql_3}'
            self.cursor.execute(sql, values)
            self.connect.commit()
        except sqlite3.Error as e:
            print(f'Ocorreu um erro ao modificar a tarefa: {e}!!!')
        finally:
            pass

    def del_task(self, ID):
        if not self.tasks_dao:
            self.load_task()
        try:
            if not self.connect:
                self.connect = sqlite3.connect('../data/Tasks.db')
                self.cursor = self.connect.cursor()

            self.cursor.execute('DELETE FROM Tasks WHERE ID = ?', (ID,))
            self.connect.commit()

        except sqlite3.Error as e:
            print(f'Erro ao excluir a tarefa: {e}!!!')
        finally:
            pass

    def get_task(self):
        temp_list = []
        try:
            if not self.connect:
                self.connect = sqlite3.connect('../data/Tasks.db')
                self.cursor = self.connect.cursor()
            if temp_list:
                temp_list.clear()

            self.cursor.execute('SELECT * FROM Tasks')
            rows = self.cursor.fetchall()
            for row in rows:
                task = {
                    'ID': row[0],
                    'Name': row[1],
                    'Description': row[2],
                    'DateTime': row[3],
                    'DalyAlarm': row[4]
                }
                temp_list.append(task)
            return temp_list
        except sqlite3.Error as e:
            print(f'Erro ao buscar as tarefas: {e}!!!')
        finally:
            pass


if __name__ == '__main__':
    pass
