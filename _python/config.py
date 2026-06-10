import time
def register_sec(sec):
    global sec
    if not sec:
        sec = [0] * 64
    while True:
        # Wait for the system to process the current transaction
        time.sleep(1)
        if sec[sec.index(i) + 2] == 0:
            break