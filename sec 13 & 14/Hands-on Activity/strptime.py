Code::
from datetime import datetime
 
# Step 1: Get the current system time
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
 
# Step 2: Create a system status message
status_message = f"System Check: {formatted_time} - Everything is running smoothly."
 
# Step 3: Write the log message to a file
log_file = "/Users/moalamnm/Desktop/system_status.log"
with open(log_file, "a") as file:
	file.write(status_message + "\n")
 
print(f"Log saved to {log_file}")
