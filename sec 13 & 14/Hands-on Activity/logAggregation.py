import os
import sys
from datetime import datetime
import shutil
import subprocess
import argparse
 
# Step 1: Set up the command-line argument parser
def parse_arguments():
	"""
	This function sets up and parses command-line arguments.
	It expects the user to provide a status message to log.
	"""
	parser = argparse.ArgumentParser(description="Log system status with timestamps")
	# Defining a positional argument 'status_message' that the user must pass
	parser.add_argument('status_message', type=str, help="The system status message to log")
   
	# Parse the arguments provided by the user
	return parser.parse_args()
 
# Step 2: Log the message with timestamp
def log_message(status_message):
	"""
	This function takes the status message, adds a timestamp to it,
	and appends it to the log file.
	"""
	# Get the current date and time formatted as 'YYYY-MM-DD HH:MM:SS'
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
	# Creating the log entry by combining timestamp and status message
	log_entry = f"{timestamp} - {status_message}\n"
   
	# Define the log file where we'll store messages
	log_file = "system_log.txt"
   
	# Open the log file in append mode and write the log entry
	with open(log_file, 'a') as file:
    	file.write(log_entry)
   
	# Inform the user that the message has been logged
	print(f"Log saved to {log_file}")
 
# Step 3: Create a backup of the log file
def backup_log():
	"""
	This function creates a backup of the log file in a 'backups' directory
	and compresses the backup into a tar.gz file.
	"""
	log_file = "system_log.txt"
	backup_dir = "backups"
   
	# Create the backup directory if it doesn't exist
	os.makedirs(backup_dir, exist_ok=True)
   
	# Copy the log file to the backup directory
	shutil.copy(log_file, backup_dir)
   
	# Inform the user that the log file has been backed up
	print(f"Log file backed up to {backup_dir}/{log_file}")
   
	# Compress the backup log file using the 'tar' command to create a .tar.gz file
	subprocess.run(['tar', '-czf', f'{backup_dir}/backup_log.tar.gz', os.path.join(backup_dir, log_file)])
   
	# Inform the user that the backup has been compressed
	print(f"Backup compressed to {backup_dir}/backup_log.tar.gz")
 
# Step 4: Main function to handle the flow of the program
def main():
	"""
	The main entry point of the program.
	- It parses arguments
	- Logs the message with a timestamp
	- Backs up the log file and compresses it
	"""
	# Parse the arguments passed to the script (the status message)
	args = parse_arguments()
   
	# Call the function to log the message with a timestamp
	log_message(args.status_message)
   
	# Call the function to back up the log file and compress it
	backup_log()
 
# Entry point of the program
if __name__ == "__main__":
	# Run the main function to start the script
	main()

