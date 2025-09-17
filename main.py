import requests
import random
import time

def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

url = "http://google.com"  # Replace with the target URL

while True:
    ip = generate_random_ip()
    headers = {'X-Forwarded-For': ip}
    response = requests.get(url, headers=headers)
    print(f"Request sent from IP: {ip} - Status Code: {response.status_code}")
    time.sleep(1)  # Adjust the sleep time as necessary
