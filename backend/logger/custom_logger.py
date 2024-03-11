import datetime
import logging

class TimeFilter(logging.Filter):
    def filter(self, record):
        try:
            last = self.last
        except AttributeError:
            last = record.relativeCreated

        delta = datetime.datetime.fromtimestamp(record.relativeCreated / 1000.0) - datetime.datetime.fromtimestamp(last / 1000.0)
        record.relative = '{0:.2f}'.format(delta.seconds + delta.microseconds / 1000000.0)
        self.last = record.relativeCreated
        return True

# Specify a logger name
logger = logging.getLogger("my_logger")

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(fmt="%(asctime)s (%(relative)ss) %(message)s"))
console_handler.addFilter(TimeFilter())
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)

logger.info("Logger initialized")