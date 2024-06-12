#!/usr/bin/env python3
""" A Python script that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    Generate statistics about Nginx logs in MongoDB.

    Args:
        mongo_collection: A pymongo collection object representing 'logs.nginx'.

    Prints:
        - Total number of logs.
        - Number of logs for each HTTP method: GET, POST, PUT, PATCH, DELETE.
        - Number of logs where method=GET and path=/status.
    """
    # Count total logs
    total_logs = mongo_collection.count_documents({})

    # Count logs by method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: mongo_collection.count_documents({"method": method}) for method in methods}

    # Count logs where method=GET and path=/status
    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})

    # Print results
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"    method {method}: {count}")
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Call log_stats function with the collection
    log_stats(collection)