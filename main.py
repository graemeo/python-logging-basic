import logging
from basic_logger import BasicLogger

def main():
   log_format = "%(levelname)s %(asctime)s %(name)s %(message)s"
   log_level = "INFO"

   logging.basicConfig(level=log_level, format=log_format, filename="")

   basic_logger = BasicLogger()
   basic_logger.log_me_up()


if __name__ == '__main__':
   main()
