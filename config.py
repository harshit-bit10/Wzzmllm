from os import environ

class Config(object):
    API_ID = int(environ.get("API_ID", 27190467))
    API_HASH = environ.get("API_HASH", "ff6bc6ad2faba520f426cf04ca7f5773")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7240304290:AAGfIJUgfukO1ALuhnhZS21g980zpL57VQM")
    AUTH_USERS = list(int(x) for x in environ.get("AUTH_USERS", "6066102279 5574593875").split(" "))
    OWNER_ID = int(environ.get("OWNER_ID", 6066102279))
    CREDITS = environ.get("CREDITS", "SharkToonsIndia")  # Default value is "SharkToonsIndia"
    DOWNLOAD_DIRECTORY = environ.get("DOWNLOAD_DIRECTORY", "./downloads")
    BIN_DIRECTORY = environ.get("BIN_DIRECTORY", "./bin")
