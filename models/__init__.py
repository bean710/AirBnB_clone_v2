#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
import os
from models.user import User
from models.state import State
from models.review import Review
from models.city import City
from models.place import Place

storage = None

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
