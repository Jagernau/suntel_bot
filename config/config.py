from dotenv import dotenv_values

config = dotenv_values(".env")

# Define the bot token
TOKEN = config["TOKEN"]
DB_USER = config["DB_USER"]
DB_PASSWORD = config["DB_PASSWORD"]
DB_HOST = config["DB_HOST"]
DB_NAME = config["DB_NAME"]
DB_PORT = config["DB_PORT"]
