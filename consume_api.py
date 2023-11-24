import requests
import json
import time

def send_to_redis(data):
    # Lógica para enviar datos a Redis
    pass

def send_to_kafka(data):
    # Lógica para enviar datos a Kafka
    pass

def main():
    with open("ratings.dat", "r") as file:
        for line in file:
            # Procesa cada línea del archivo "ratings.dat"
            data = line.strip().split("::")
            user_id, movie_id, rating, timestamp = data
            
            # Envía los datos a Redis
            send_to_redis({"user_id": user_id, "movie_id": movie_id, "rating": rating, "timestamp": timestamp})
            
            # Envía los datos a Kafka
            send_to_kafka({"user_id": user_id, "movie_id": movie_id, "rating": rating, "timestamp": timestamp})

            time.sleep(0.1)  # Añade un pequeño retraso si es necesario

if __name__ == "__main__":
    main()
