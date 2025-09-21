"""
Module: Main
"""
from ingestion.globals import Global
from chatbot import ChatBot

if __name__ == "__main__":
    Global.init('config/config.json')
    _log = Global.get_logger(__name__)
    _log.info('Global instance created')
    chat_bot = ChatBot()
    chat_bot.launch_bot()
