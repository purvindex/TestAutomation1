import inspect
import logging
import logging.handlers

#DEBUG - Detailed information, typically of interest only when diagnosing problems.
# INFO - Confirmation that things are working as expected.
# WARNING - An indication that something unexpected happened or indicative of some problem in the near future(e.g disk apace low'). The software is still working as expected.
# ERROR - Due to a more serius problem, the software has not been able to perform some funciton.
# CRITICAL - A serious error, indicating that the program itself may be unable to continue running.

class custLogger:
    def getLogs(self,level=logging.DEBUG):
        #set class/method name from where its called ,#60,Ver
        logger_name = inspect.stack()[1][3]
        #create logger
        logger = logging.getLogger(logger_name)
        # Set the level of logger
        logger.setLevel(level)
        #logger.setLevel(logging.logLevel) # As debug is the highest level which will log all the messages Debug and above all of it
        # Create console handler or file handler and set the log level
        fileHandler = logging.FileHandler("..\\Logs\\automation.log") # For console handler ch = logging.Streamhandler()
        #ch = logging.Streamhandler()
        fileHandler.setLevel(level)
        #logger.setLevel(logLevel)
        #create formatter - how you want your logs to be formatted
        formatter = logging.Formatter ('%(asctime)s: %(levelname)s: %(module)s:-  %(funcName)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        # add formatter to console or file
        fileHandler.setFormatter(formatter) #pass the above formatter to file handler, so it will display in above format
        # add console handler to logger
        logger.addHandler(fileHandler)
        # logger.debug("Debug message")
        # logger.info("Information regarding the test case")
        # logger.warning("Test case pass but with a Warning message")
        # logger.error("Test case fail")
        # logger.critical("Important test case fail on which other test case depends")
        return logger

# cl = custLogger
# cl().getLogs()

