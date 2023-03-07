"""
Holds copies of our data store objects.
"""

from src.data_store import DataStore
from src.data.game_data import GameData
from src.data.line_score import LineScore

game_data  : DataStore[GameData]  = DataStore[GameData]()
line_score : DataStore[LineScore] = DataStore[LineScore]()
