import boto3
import json
import random
import time
from datetime import datetime

# Initialize Kinesis client
kinesis_client = boto3.client("kinesis", region_name="us-east-1")

# Function to generate random IoT sensor data
def generate_sensor_data():
    return {
        "device_id": random.choice(["sensor_01", "sensor_02", "sensor_03"]),
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(30, 80), 2),
        "status": random.choice(["Active", "Idle", "Error"]),
        "timestamp": datetime.utcnow().isoformat(),
        "location": random.choice(["Warehouse-1", "Warehouse-2", "Factory-1"])
    }

# Send multiple records to Kinesis
for _ in range(50):  # Sends 50 records
    sensor_data = generate_sensor_data()
    
    response = kinesis_client.put_record(
        StreamName="real-time-data-stream",
        Data=json.dumps(sensor_data),
        PartitionKey=sensor_data["device_id"]
    )
    
    print(f"Sent: {sensor_data}")
    time.sleep(1)  # 1-second delay between records
