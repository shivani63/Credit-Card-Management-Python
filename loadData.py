import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "ccdata.json")

def loadData():
    if not os.path.exists(FILE_PATH):
        return []
    if os.path.getsize(FILE_PATH) == 0:
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)
