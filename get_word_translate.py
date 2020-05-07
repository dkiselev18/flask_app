from db.db_connection import DatabaseConnection


def get_word_translate(word):
    word = word.lower()
    return f""" select * from get_word_translate('{word}') """


def translate(word):
    with DatabaseConnection() as conn:
        cursor = conn.cursor()
        cursor.execute(get_word_translate(word))
        return cursor.fetchall()
