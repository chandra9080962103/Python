import logging
logger = logging.getLogger(__name__)
logger.propagate = False
#this statement ensures nothing from this file is being propagated to other files.
logger.info("hello world")
