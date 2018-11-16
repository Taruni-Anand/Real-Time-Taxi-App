"""
    Add all project related settings here!
"""

import os
from pathlib import Path

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = Path("{}/data/".format(PROJECT_DIR))

SPARK_CONFIGURE_INPUT = "spark.mongodb.input.uri"

# Database setting
DB_HOST = "localhost:27017"
DB_NAME = "taxi"
