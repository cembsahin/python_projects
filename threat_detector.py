# threat_detector.py

import re
from collections import defaultdict


def detect_brute_force(log_lines, threshold=5):
    failed_attempts = defaultdict(int)
    alerts = []

    for line in log_lines:
        match = re.search(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)", line)
        if match:
            ip = match.group(1)
            failed_attempts[ip] += 1
            if failed_attempts[ip] == threshold:
                alerts.append(f"[ALERT] Possible brute-force from {ip}")

    return alerts
