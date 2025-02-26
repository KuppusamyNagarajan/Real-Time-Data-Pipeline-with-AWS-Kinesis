# Real-Time Data Pipeline with AWS Kinesis
This project processes real-time IoT data using AWS Kinesis, Lambda, S3, and QuickSight.

## Steps
1️⃣ Sensor data is sent to **Kinesis Data Stream**.  
2️⃣ AWS **Lambda** processes and stores data in **S3**.  
3️⃣ QuickSight visualizes real-time data.  

## Files Included
- `send_data_to_kinesis.py` → Script to send data  
- `lambda_processor.py` → Lambda function  
- `manifest.json` → S3 manifest file  
- `sample_sensor_data.json` → Example sensor data  

## How to Run
1. Deploy Lambda with the given script.
2. Run `send_data_to_kinesis.py` to stream data.
3. Connect S3 data to QuickSight.
4. Create a dashboard!
