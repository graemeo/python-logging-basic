import logging
import argparse
from basic_logger import BasicLogger

def main():
   parser = argparse.ArgumentParser(description="")
   parser.add_argument("-l", "--loglevel", default="info", required=True, help="Log level setting - can either be notset, debug, critical, warning, error or info")
   args = parser.parse_args()

   log_format = "%(levelname)s %(asctime)s %(name)s %(message)s"
   log_level = args.loglevel.upper()

   logging.basicConfig(level=log_level, format=log_format)

   basic_logger = BasicLogger()
   basic_logger.log_me_up()


if __name__ == '__main__':
   main()
