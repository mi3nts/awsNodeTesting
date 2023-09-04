import time
import paho.mqtt.client as mqtt
import ssl
import json
# import thread


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


client = mqtt.Client()
client.on_connect = on_connect
client.tls_set(ca_certs='../certs/AmazonRootCA1.pem',
               certfile='../certs/b9bda2587a2e0d95b12f6051cbe320073f539fbb3a809f4937b9fac3f9078e87-certificate.pem.crt', \
               keyfile ='../certs/b9bda2587a2e0d95b12f6051cbe320073f539fbb3a809f4937b9fac3f9078e87-private.pem.key', \
               tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect("a1sy4v3syxrxsq-ats.iot.us-east-1.amazonaws.com", 8883, 60) #Taken from REST API endpoint - Use your own. 


def main():
    print("Awesome its running")
    client.publish("device/data", payload="Hello from BinaryUpdates!!" , qos=0, retain=False)
    time.sleep(5)


if __name__ == '__main__':
    # mqtt_client = mqttClient.Client()
    while True:
        main()


# client.loop_forever()