from selenium import webdriver
import logging

logging.basicConfig(filename="test.log",
                    level=logging.DEBUG,
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt="%m %d %y %I:%M:%S %p")

#logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)

logging.debug("This is debug")
logging.info("This is info")
logging.warning("This is warning")
logging.error("This is error")
logging.critical("This is critical")