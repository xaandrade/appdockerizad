from kafka import KafkaProducer
import time

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda mensaje: mensaje.encode('utf-8')
)

while True:
    mensaje = input("Escribe un mensaje: ")
    producer.send('grupo-majo', mensaje)
    producer.flush()
    print("Mensaje enviado:", mensaje)