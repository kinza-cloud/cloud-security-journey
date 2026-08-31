# This script simulates a simple AWS Lambda function
event = input("Enter event type (s3_upload, api_call, scheduled): ")
name = input("Enter your name: ")

print("\n Lambda Function Triggered")
print("Event Type:", event)
print("Triggered By:", name)
print("Status: Function executed successfully.")
print("Timestamp: 2026-08-31 10:00 AM")
