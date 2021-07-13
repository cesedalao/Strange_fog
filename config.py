import time

import logging.handlers

import os


def test_log():
    logger = logging.getLogger()

    logger.setLevel(logging.INFO)

    sh = logging.StreamHandler()

    BAseDir = os.path.dirname(os.path.abspath(__file__))

    log_file = BAseDir + './Log/qw-{}.log'.format(time.strftime('%Y%m%d - %H%M%S'))

    fl = logging.handlers.TimedRotatingFileHandler(log_file,
                                                   when='midnight',
                                                   interval=1,
                                                   backupCount=3,
                                                   encoding='UTF-8')

    fmt = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]''[%(levelname)s][%(message)s]'

    fortter = logging.Formatter(fmt)

    sh.setFormatter(fortter)
    fl.setFormatter(fortter)

    logger.addHandler(sh)
    logger.addHandler(fl)



