import pandas as pd
import random
from datetime import datetime, timedelta

# Parameters
num_records = 1000  # Number of log entries
start_time = datetime.now() - timedelta(hours=1)  # Start time
time_interval = 1  # Time interval in seconds

# Helper Functions
def generate_ip():
    """Generate a random IPv4 address."""
    return '.'.join(map(str, (random.randint(1, 255) for _ in range(4))))

def generate_error():
    """Generate a random error type and its corresponding code."""
    errors = {
        "Authentication Failed": 1001,
        "File Not Found": 1002,
        "Connection Timeout": 1003,
        "Disk Space Low": 1004,
        "Memory Usage High": 1005,
        "Service Restarted": 1006,
        "Configuration Error": 1007,
        "Unexpected Error": 1008
    }
    error_type, error_code = random.choice(list(errors.items()))
    return error_type, error_code

def generate_logs():
    """Generate synthetic log data."""
    timestamps = [start_time + timedelta(seconds=i * time_interval) for i in range(num_records)]
    error_levels = random.choices(['INFO', 'WARN', 'ERROR', 'CRITICAL'], weights=[0.6, 0.2, 0.15, 0.05], k=num_records)
    source_ips = [generate_ip() for _ in range(num_records)]
    error_types_and_codes = [generate_error() for _ in range(num_records)]
    error_types = [et[0] for et in error_types_and_codes]
    error_codes = [et[1] for et in error_types_and_codes]

    return {
        "date": [ts.strftime("%Y-%m-%d") for ts in timestamps],  # Format as string
        "time": [ts.strftime("%H:%M:%S") for ts in timestamps],  # Format as string
        "error_level": error_levels,
        "error_type": error_types,
        "error_code": error_codes,
        "ip_address": source_ips
    }

# Generate the data
log_data = generate_logs()
df = pd.DataFrame(log_data)

# Save to a CSV file
csv_file = "C:/mnt/data/router_telemetry_data.csv"
df.to_csv(csv_file, index=False)

print(f"Synthetic error log file saved to {csv_file}")
