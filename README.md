

# 📜 Log Monitor

A simple Python-based log analysis tool that scans for SSH “Failed password” entries and summarizes failed login attempts by IP address.

---

## 🔧 Usage

1. **Clone or download** this repository.
2. **Run** the script against a log file (e.g., `/var/log/auth.log` on Linux or a sample file).

```bash
python3 log_monitor.py <path_to_log_file> --threshold <number>

python3 log_monitor.py sample_auth.log --threshold 2


🔍 Failed Login Attempts Summary:
---------------------------------
  192.168.1.10: 3 failed attempts
  10.0.0.5: 2 failed attempts


🧠 What I Learned

How to parse log files with regular expressions (re module)
Counting occurrences per IP with collections.Counter
Building an incident-detection-like tool for failed login analysis
Packaging Python scripts for straightforward CLI usage

👤 Author

Mohammad Akib Shaikh
Cybersecurity Analyst

## Next Steps
- Building a self-hosted Wazuh SIEM lab to replicate these alerts locally
- Completing Phishing Email Analysis (Email Header Forensics, IOC Extraction)
- Contributing detection rules to Sigma repository
