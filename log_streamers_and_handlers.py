import logging
logger = logging.getLogger(__name__)

stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')
#creating handlers

stream_h.setLevel(logging.ERROR)
file_h.setLevel(logging.INFO)
#setting levels for stream and file handlers.

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)
#setting formatters.

logger.addHandler(stream_h)
logger.addHandler(file_h)
#adding the handler to my logger object.

logger.critical("emergency!")
logger.error("error")
