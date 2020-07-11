
import logging

# Default logging standards -
# And By default the logging standard is set to WARNING and above, so if we try to log debug or info it will not log that unless changed in config.

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# Log attributes -> https://docs.python.org/3/library/logging.html#logrecord-attributes

# logging.basicConfig(filename='test.log', level=logging.INFO)
logging.basicConfig(filename='test.log', level=logging.INFO,
                    format='[%(asctime)s]::[%(filename)s]::[%(funcName)s]::[%(message)s]')

logging.debug('Started Logging')
logging.info('Started Logging')
logging.warning('Started Logging')
logging.error('Started Logging')
logging.critical('Started Logging')
