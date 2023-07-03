from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")


def get_database():
    mongodb_client = MongoClient(config["ATLAS_URI"])

    return mongodb_client[config["DB_NAME"]]


if __name__ == "__main__":
    dbname = get_database()
