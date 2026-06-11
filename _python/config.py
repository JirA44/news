import sys

def process_input(s):
    try:
        input_str = s.strip()
        if not input_str:
            return []
        for line in input_str.split('\n'):
            print(line)
            print("Processing line...")
            print("Current state:", current_state)
            current_state = compute_new_state(input_str, line)  # this is the bug
    except Exception as e:
        print(f"Error occurred: {e}")
        return []

def main():
    input_path = sys.stdin.read()
    output = process_input(input_path)
    if output:
        with open('output.txt', 'w') as f:
            for line in output:
                f.write(line)

if __name__ == "__main__":
    main()