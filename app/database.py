import sqlite3
from sqlite3 import Error
from datetime import datetime
import time

FILE = "mtgcards.db"
CARDS_TABLE = "Cards"
PRICE_HISTORY_TABLE = "PriceHistory"

class Database:
    def __init__(self):
        self.conn = None

        try:
            self.conn = sqlite3.connect(FILE)
        except Error as e:
            print(e)
        
        self.cursor = self.conn.cursor()
        self._create_card_table()
        self._create_price_table()

    def close(self):
        self.conn.close()

    def _create_card_table(self):
        query = f"""CREATE TABLE IF NOT EXISTS {CARDS_TABLE}
                    (name TEXT PRIMARY KEY, quantity INTEGER)"""
        self.cursor.execute(query)
        self.conn.commit()

    def _create_price_table(self):
        query = f"""CREATE TABLE IF NOT EXISTS {PRICE_HISTORY_TABLE}
                    (cardName TEXT, price REAL, date DATETIME, FOREIGN KEY(cardName) REFERENCES {CARDS_TABLE}(name))"""
        self.cursor.execute(query)
        self.conn.commit()

    def get_all_cards(self, limit=100, name=None):
        if not name:
            query = f"SELECT * FROM {CARDS_TABLE}"
            self.cursor.execute(query)
        else:
            query = f"SELECT * FROM {CARDS_TABLE} WHERE NAME LIKE %?%"
            self.cursor.execute(query, (name,))

        result = self.cursor.fetchall()
        results = []

        for res in sorted(result, key=lambda x: x[2], reverse=True)[:limit]:
            name, quantity = res
            data = {"name":name, "quantity":quantity}
            results.append(data)

    def get_cards_by_name(self, name, limit=10):
        return self.get_all_cards(limit, name)

    def get_price_history(self, name, limit=10):
        query = f"SELECT * FROM {PRICE_HISTORY_TABLE} WHERE CARDNAME = ?"
        self.cursor.execute(query, (name,))

        result = self.cursor.fetchall()
        results = []

        for res in sorted(result, key=lambda x: x[3], reverse=True)[:limit]:
            cardName, price, date = res
            data = {"cardName":cardName, "price":price, "date":str(date)}
            results.append(data)

    def save_card(self, name, quantity):
        query = f"INSERT INTO {CARDS_TABLE} VALUES (?, ?)"
        self.cursor.execute(query, (name, quantity))
        self.conn.commit()

    def save_price(self, cardName, price):
        query = f"INSERT INTO {PRICE_HISTORY_TABLE} VALUES (?, ?, ?)"
        self.cursor.execute(query, (cardName, price, datetime.now()))
        self.conn.commit()
