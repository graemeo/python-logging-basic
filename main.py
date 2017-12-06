import logging

def main():
   logging.basicConfig(level="NOTSET", format="%(levelname)s %(asctime)s %(name)s %(message)s")
   logger = logging.getLogger(__name__)
   logger.info("hello")
   logger.debug("hello")
   logger.warning("hello")

if __name__ == '__main__':
   main()
