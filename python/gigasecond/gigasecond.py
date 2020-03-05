from datetime import datetime, timedelta

def add(moment):
    try:
        moment2 = moment + timedelta(seconds=1000000000)
    except OverflowError:
        moment2 = datetime.now
    return moment2