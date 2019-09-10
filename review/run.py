from app import tsla
from app import controller
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, "data", "tsla.db")

tsla.dbpath = DBPATH
controller.run()