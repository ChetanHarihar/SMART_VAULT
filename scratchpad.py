from services.mqtt_functions import connect_mqtt, handle_publish
from settings.config import *

mqtt_client = connect_mqtt(mqtt_server=MQTT_SERVER, mqtt_port=MQTT_PORT)

handle_publish(client=mqtt_client, topic='mqtt/test', message="test msg")