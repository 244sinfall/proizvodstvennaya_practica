"""Sqlite support to export vote data"""
import sqlite3

from contracts.database import VoteDatabase

class SqliteVoteDatabase(VoteDatabase):
    """Sqlite support to export vote data
    path - path to db file
    query - query tu run to get data
    """
    def __init__(self, path: str, query: str) -> None:
        self.path = path
        self.query = query

    def get_data(self) -> list[tuple]:
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        res = cur.execute(self.query)
        data: list[tuple] = res.fetchall()
        return data
