from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'grupo-majo',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    group_id=None,
    value_deserializer=lambda mensaje: mensaje.decode('utf-8')
)

print("Esperando mensajes...")

for mensaje in consumer:
    print("Mensaje recibido:", mensaje.value)