import psutil, time, datetime, os

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('C:\\').percent
disk_free_gb = round(psutil.disk_usage('C:\\').free / (1024**3), 2)

# Ping check
ping_status = "UP" if os.system("ping -n 2 8.8.8.8 > nul") == 0 else "DOWN"

log_entry = f"{timestamp} | CPU: {cpu}% | RAM Used: {ram}% | Disk Used: {disk}% (Free {disk_free_gb} GB) | Ping: {ping_status}\n"

with open("health.log", "a") as f:
    f.write(log_entry)
print(log_entry)

# Ticket logic
if cpu > 80:
    with open("ticket.log", "a") as f:
        f.write(f"{timestamp} | TICKET-001 | P1 | CPU High {cpu}%\n")
if ram > 85:
    with open("ticket.log", "a") as f:
        f.write(f"{timestamp} | TICKET-002 | P1 | RAM High {ram}%\n")
if disk_free_gb < 10:
    with open("ticket.log", "a") as f:
        f.write(f"{timestamp} | TICKET-003 | P2 | Disk Low {disk_free_gb} GB\n")
if ping_status == "DOWN":
    with open("ticket.log", "a") as f:
        f.write(f"{timestamp} | TICKET-004 | P1-CRITICAL | Network DOWN\n")