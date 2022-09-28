import sqlite3


class BotDB:

    def __init__(self, db_file):
        """Инициализация соединения с БД

        Args:
            db_file {string} -- путь к файлу БД
        """
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def close(self):
        """Закрытие соединения с БД"""
        self.conn.close()

    def user_exists(self, user_id):
        """Проверяем, есть ли пользователь в БД

        Args:
            user_id (integer): ID пользователя в Telegram

        Returns:
            True/False (bool): ``True``, если переданный``user_id`` найден в БД
        """
        result = self.cursor.execute(
            "SELECT id FROM users WHERE user_id = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        result = self.cursor.execute(
            "SELECT id FROM users WHERE user_id = ?", (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):
        """Добавление пользователя в БД

        Args:
            user_id (integer): ID пользователя в Telegram
        """
        self.cursor.execute('INSERT OR IGNORE INTO users (user_id) VALUES (?)',
                   (user_id))
        self.conn.commit()

    def record(self, user_id):
        pass
