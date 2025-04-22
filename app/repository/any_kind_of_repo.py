# repositories/abstract.py
import psycopg2
from abc import ABC, abstractmethod


class StudentRepositoryABC(ABC):
    @abstractmethod
    def add_teacher(self, tg_id):
        pass

    @abstractmethod
    def get_teacher(self, tg_id):
        pass

    @abstractmethod
    def update_teacher(self, tg_id):
        pass

    @abstractmethod
    def del_teacher(self, tg_id):
        pass


class TeacherRepository(StudentRepositoryABC):
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="wg_forge_db",
            host="localhost",
            user="wg_forge",
            password="42a",
            port="5432"
        )
        self.cursor = self.conn.cursor()

    def add_teacher(self, tg_id, name) -> bool:
        try:
            self.cursor.execute("INSERT INTO Teacher (tg_id, name) VALUES (%s, %s)", (tg_id,name,))
            self.conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Ошибка добавления учителя: {e}")
            self.conn.rollback()
            return False

    def get_teacher(self, tg_id):
        try:
            self.cursor.execute("SELECT * FROM Teacher WHERE tg_id=%s", (tg_id,))
            return True if self.cursor.fetchone() else False
        except psycopg2.Error as e:
            print(f"Ошибка получения студента: {e}")
            return None
    
    def update_teacher(self, tg_id):
        try:
            self.cursor.execute("UPDATE Teacher SET name ='Bold' WHERE tg_id = %s", (tg_id,))
            self.conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Ошибка обновления: {e}")
            return None

    def del_teacher(self,tg_id):
        try:
            self.cursor.execute("DELETE FROM Teacher WHERE tg_id = %s", (tg_id,))
            self.conn.commit()
            return True
        except psycopg2.Error as e:
            print(f"Ошибка удаления: {e}")
            return None

    def close(self):
        self.cursor.close()
        self.conn.close()