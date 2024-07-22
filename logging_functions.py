import logging
import time
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
# Now also debug messages will get logged with a different format.
logging.debug('Debug message')
# This would log to a file instead of the console.
# logging.basicConfig(level=logging.DEBUG, filename='app.log')
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")

#debug, info, warning, error, crictical is the hierarchy of the logging functions. So if we setlevel to debug, it can print messages of level debug and above. 
import helper
#removed logging.info message to import info message from m.py
