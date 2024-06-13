import os
import signal
import time
import subprocess


# @PrivateFileTg # Set the path to the script you want to restart
script_to_restart = "m.py"

def restart_script():
    # @PrivateFileTg # Run the script
    print("😁😁😁😁😁😁.....")
    process = subprocess.Popen(["python3", script_to_restart], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def main():
    process = restart_script()
    while True:
        time.sleep(480)  # @PrivateFileTg # Sleep for 30 seconds
        # @PrivateFileTg # Send Ctrl+C signal to the process
        process.send_signal(signal.SIGINT)
        # @PrivateFileTg # Wait for the process to terminate
        process.wait()
        # @PrivateFileTg # Restart the script
        process = restart_script()

if __name__ == "__main__":
    main()