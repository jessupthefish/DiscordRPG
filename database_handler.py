import sqlite3
from copy import deepcopy

conn = sqlite3.connect('game.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS characters
    (user_id TEXT PRIMARY KEY, character_dict TEXT)''')
conn.commit()


class RPGDatabase:

    @staticmethod
    def save_to_db(self):
        player_dict = deepcopy(vars(self))
        if self.battling is not None:
            player_dict["battling"] = deepcopy(vars(self.battling))

        character_str = str(player_dict)

        cursor.execute("INSERT OR REPLACE INTO characters (user_id, character_dict) VALUES (?, ?)",
                       (self.user_id, character_str))
        conn.commit()

    @staticmethod
    def load_from_db(user_id, cls):
        cursor.execute("SELECT character_dict FROM characters WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()

        if row:
            player_dict = eval(row[0])
            new_player = cls()
            for key, value in player_dict.items():
                setattr(new_player, key, value)

            return new_player

        return None
