# main.py

from log_monitor import read_log_file
from threat_detector import detect_brute_force
from alert import print_alerts

def main():
    log_lines = read_log_file("logs/sample_auth.log")
    alerts = detect_brute_force(log_lines)
    print_alerts(alerts)

if __name__ == "__main__":
    main()
