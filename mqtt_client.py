import paho.mqtt.client as mqtt
from servo_motor import open_door

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("dse/open")
    
def on_message(client, userdata, msg):
    print("Received message:", msg)
    open_door()

def send_message(client, topic, message):
    print("Sending message to topic:", topic)
    client.publish(topic, message)

def connect_mqtt():
    broker_url = "ecd8950746cc4cbe99f19f8a4d3a2f23.s1.eu.hivemq.cloud"
    broker_port = 8883

    client = mqtt.Client()
    client.username_pw_set("ordozgoite", "TestPassword123?")
    client.on_connect = on_connect
    client.on_message = on_message
    client.tls_set()
    client.connect(broker_url, broker_port)
    client.loop_start()

    return client
