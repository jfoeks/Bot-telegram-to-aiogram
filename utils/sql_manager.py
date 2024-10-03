import sqlite3
import os


class UserId:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.db_path = os.path.join(BASE_DIR, 'base', 'user_id.db')

    def create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE
            )
            ''')
            conn.commit()

    def get_all_user_id(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT user_id FROM users')
            user_ids = cursor.fetchall()
            return [user_id[0] for user_id in user_ids]

    def delete_user_id(self, user_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            DELETE FROM users WHERE user_id = ?
            ''', (user_id,))
            conn.commit()

    def get_user_id(self, user_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                INSERT OR IGNORE INTO users (user_id) 
                VALUES (?)
                ''', (user_id,))
                conn.commit()
            except Exception as e:
                print(f"Error: {e}")
class ImagePhoto:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.db_path = os.path.join(BASE_DIR, 'base', 'image.db')
        self.create_table_image()  # Создаем таблицу при инициализации

    def create_table_image(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS image_user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image TEXT UNIQUE
            )
            ''')
            conn.commit()

    def get_image_all(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT image FROM image_user')

            # Извлекаем все записи
            image_data = cursor.fetchall()
            return [image[0] for image in image_data]

    def create_image(self, image):
        for existing_image in self.get_image_all():
            self.delete_image(existing_image)

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                INSERT OR IGNORE INTO image_user (image) 
                VALUES (?)
                ''', (image,))
                conn.commit()
            except Exception as e:
                print(f"Error while inserting image: {e}")

    def delete_image(self, image):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            DELETE FROM image_user WHERE image = ?
            ''', (image,))
            conn.commit()


USER = UserId()
IMAGE = ImagePhoto()
