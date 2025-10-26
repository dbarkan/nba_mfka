# nba_schedule_stub.py
from datetime import datetime

def main():
    now = datetime.now()
    print("Current date and time:")
    print(now.strftime("%A, %B %d, %Y %I:%M %p"))

if __name__ == "__main__":
    main()
