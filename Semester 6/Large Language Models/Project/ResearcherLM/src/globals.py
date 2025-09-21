"""
Module: Globals
"""
import json
import os
import logging


class Global:
    """
    Stores global configuration parameters.

    Methods:
    - init(config_path)
    """
    config = {}

    @staticmethod
    def init(config_path):
        """Initializes global configuration from a JSON file."""
        with open(config_path, 'r', encoding='utf-8') as config_file:
            Global.config = json.loads(config_file.read())
            for key in Global.config:
                if key in os.environ:
                    if Global.is_json(os.environ[key]):
                        Global.config[key] = json.loads(os.environ[key])
                    else:
                        if os.environ[key] == "\"\"":
                            Global.config[key] = ""
                        elif os.environ[key].isnumeric():
                            Global.config[key] = int(os.environ[key])
                        else:
                            Global.config[key] = os.environ[key]

            # extra initialization

    @staticmethod
    def get_logger(name):
        """Gets the logger"""
        log = logging.getLogger(name)
        if len(log.handlers) > 0:
            return log
        log.setLevel(Global.config['LOG_LEVEL'])
        lsh = logging.StreamHandler()
        log_format = ('%(levelname) -5s %(asctime)s [%(thread)d] \
    	%(name) -5s %(funcName) -5s %(lineno) -5d: %(message)s')    # pylint: disable=superfluous-parens
        lsh.setFormatter(logging.Formatter(log_format))
        log.addHandler(lsh)
        log.propagate = False
        return log

    @staticmethod
    def is_json(myjson):
        """Checks if its a JSON file."""
        try:
            json.loads(myjson)
        except Exception:
            return False
        return True
