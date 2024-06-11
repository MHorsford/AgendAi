from datetime import datetime
import sqlite3
import os


class TaskDAO:
    def __init__(self):
        self.db_path = '../data/Tasks.db'
        self.tasks_dao = []
        self.create_table()

    def create_connection(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        try:
            if not os.path.exists('../data/Tasks.db'):
                with open('../data/Tasks.db', 'w') as file:
                    pass
            cursor.execute('CREATE TABLE IF NOT EXISTS Tasks('
                           'ID INTEGER PRIMARY KEY AUTOINCREMENT,'
                           'Name TEXT,'
                           'Description TEXT,'
                           'DateTime TEXT,'
                           'DalyAlarm NUMERIC)')
        except sqlite3.Error as e:
            print(f'Não foi possivel criar a base de dados: {e}!!!')
        finally:
            conn.close()

    def load_task(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        try:
            if self.tasks_dao is not None:
                self.tasks_dao.clear()
            cursor.execute('SELECT * FROM Tasks')
            rows = cursor.fetchall()
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
            conn.close()

    def reload_task(self):
        pass

    def set_task(self, name, description, dateTime, dalyAlarm=0):
        conn = self.create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO Tasks (Name, Description, DateTime, DalyAlarm) VALUES (?, ?, ?, ?)',
                           (name, description, dateTime, dalyAlarm))
            conn.commit()

        except sqlite3.Error as e:
            print(f'Erro ao inserir a tarefa: {e}!!!')

        finally:
            self.tasks_dao.clear()
            self.load_task()
            conn.close()

    def modify_task(self, ID, **kwarg):
        conn = self.create_connection()
        cursor = conn.cursor()
        if not self.tasks_dao:
            self.load_task()
        try:
            command_sql_1 = 'UPDATE Tasks SET '
            command_sql_2 = ', '.join([f'{key} = ?' for key in kwarg.keys()])
            command_sql_3 = ' WHERE ID = ?'
            values = list(kwarg.values()) + [ID]
            sql = f'{command_sql_1}{command_sql_2}{command_sql_3}'
            cursor.execute(sql, values)
            conn.commit()
        except sqlite3.Error as e:
            print(f'Ocorreu um erro ao modificar a tarefa: {e}!!!')
        finally:
            self.tasks_dao.clear()
            self.load_task()
            conn.close()

    def del_task(self, ID):
        conn = self.create_connection()
        cursor = conn.cursor()
        if not self.tasks_dao:
            self.load_task()
        try:
            cursor.execute('DELETE FROM Tasks WHERE ID = ?', (ID,))
            conn.commit()
        except sqlite3.Error as e:
            print(f'Erro ao excluir a tarefa: {e}!!!')
        finally:
            self.tasks_dao.clear()
            self.load_task()
            conn.close()

    def get_task(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        temp_list = []
        try:
            if not self.tasks_dao:
                self.load_task()
            if temp_list:
                temp_list.clear()
            cursor.execute('SELECT * FROM Tasks')
            rows = cursor.fetchall()
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
            conn.close()


