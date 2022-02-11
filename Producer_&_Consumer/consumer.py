import random
from meter import Meter


def on_message_recevied(ch, method, properties, body):
    #convert it into its original type
    received = body.decode('utf-8')
    #the meter value 
    meter_value = int(received.split(" ")[0])
    #The pv_power_value is the random value created (between 1 and 10) by the PV simulator.
    pv_power_value = random.randint(1, 10)
    final_power_value = meter_value + pv_power_value
    print("The final power value is: {}".format(final_power_value))
    #The second received value is the date
    print(received.split(" ")[1])
    #The third received value is the timestamp
    print("Received at: {}".format(received.split(" ")[2]))
    #Write the values
    with open('file_text', 'a') as f:
        f.write("%s,%s,%s,%s,%s\n" % (str(meter_value), str(pv_power_value), str(final_power_value), received.split(" ")[1], received.split(" ")[2]))
    
if __name__ == "__main__":
    #connection to the broker and the queue
    generator = Meter(queue="powerValues")

    #It allows to consume the values 
    while True:
        generator.basic_consumer('powerValues', on_message_recevied, True)
    
    




