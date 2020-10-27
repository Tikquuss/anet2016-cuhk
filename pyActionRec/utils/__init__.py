import logging
import sys

import os
sys.path.append(os.path.join(os.environ['ANET_HOME'], "pyActionRec", "utils"))

from media_files import *

_formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)d - [%(levelname)s] %(message)s')
_ch = logging.StreamHandler()
_ch.setLevel(logging.DEBUG)
_ch.setFormatter(_formatter)

def get_logger(debug=False):
    logger = logging.getLogger("pyActionRec")
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    logger.addHandler(_ch)
    return logger
