import datetime
import time
import random
from meter import Meter

if __name__ == "__main__":
    generator = Meter(queue="powerValues")
    #random value between 0 and 9000 in a continuous way along with a timestamp
    while True:
        message = str(random.randint(0,9000)) + " " +str(datetime.datetime.now())
        generator.publish(message)
        time.sleep(2)


