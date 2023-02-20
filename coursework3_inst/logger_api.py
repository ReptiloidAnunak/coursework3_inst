import logging

logger_api = logging.getLogger("logger_api")
file_handler = logging.FileHandler("logs/api.logs")
formatter_api = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter_api)
logger_api.addHandler(file_handler)
logger_api.setLevel(logging.INFO)