# cli.py

import subprocess

def run_tests():
    print("Running API tests with pytest...")
    subprocess.run(["pytest", "test_jsonplaceholder.py", "-v"])

if __name__ == "__main__":
    run_tests()
