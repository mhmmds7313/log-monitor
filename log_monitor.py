# log_monitor.py
import re
import argparse
from collections import Counter

def parse_log(file_path):
    """
    Scan each line of the given log file for failed login attempts.
    Extract IP addresses from lines containing 'Failed password'.
    Return a Counter mapping each IP to its number of failures.
    """
    # Regex matches lines like: "Failed password for user from 192.168.1.100 port 22 ssh2"
    pattern = re.compile(r'Failed password .* from ([\d\.]+)')
    counts = Counter()

    try:
        with open(file_path, "r") as f:
            for line in f:
                match = pattern.search(line)
                if match:
                    ip = match.group(1)
                    counts[ip] += 1
    except FileNotFoundError:
        print(f"[!] Log file not found: {file_path}")
        return None

    return counts

def main():
    parser = argparse.ArgumentParser(
        description="Log Monitor: Count failed SSH login attempts by IP"
    )
    parser.add_argument(
        "logfile",
        help="Path to the log file to analyze (e.g., /var/log/auth.log)"
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=5,
        help="Only show IPs with at least this many failures (default=5)"
    )
    args = parser.parse_args()

    result = parse_log(args.logfile)
    if result is None:
        return

    print("\n🔍 Failed Login Attempts Summary:")
    print("---------------------------------")
    for ip, count in result.items():
        if count >= args.threshold:
            print(f"  {ip}: {count} failed attempts")
    print("")

if __name__ == "__main__":
    main()
