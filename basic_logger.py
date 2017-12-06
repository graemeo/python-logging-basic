import logging

class BasicLogger:

   def log_me_up(self):
      logger = logging.getLogger(__name__)

      print "##############################################"

      logger.critical("Mission CRITICAL!!!! Time to panic!!")
      logger.error("Crap happens!")
      logger.warning("This is just a warning!! Take it easy...")
      logger.info("Hello world!")
      logger.debug("Well, everything you should know is now...")

      print "##############################################"
