import logging
import json
from datetime import datetime
from collections import OrderedDict


class JSONFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()

    def format(self, record):
        out = OrderedDict([
            # utcnow + Z for RFC3339Nano for Promtail
            ("timestamp", datetime.utcnow().isoformat() + "Z"),
            ("thread", record.thread),
            ("level", record.levelname.lower()),
            ("message", super().format(record)),
        ])
        return json.dumps(out)


def setup_logging():
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    handler = logging.StreamHandler()
    handler.setFormatter(JSONFormatter())
    logging.root.handlers = [handler]


setup_logging()

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
