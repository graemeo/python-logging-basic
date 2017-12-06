import logging
from basic_logger import BasicLogger

def main():
   log_format = "%(levelname)s %(asctime)s %(name)s %(message)s"

   logging.basicConfig(level="NOTSET", format=log_format)

   BasicLogger()

if __name__ == '__main__':
   main()
