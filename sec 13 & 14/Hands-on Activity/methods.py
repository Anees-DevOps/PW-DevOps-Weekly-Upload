# Sample configuration file content as a string
config_data = """
  [general]  
  username = admin   
  password = oldpassword123   
  [settings]
  deploy_directory = /var/www/app
  server_ip = 192.168.1.1
"""

# Step 1: Remove extra spaces around each line (strip leading/trailing spaces)
print("Step 1: Strip extra spaces around lines")
lines = config_data.strip().split("\n")  # Strip whitespace from the whole content and split into lines
for line in lines:
    print(f"'{line.strip()}'")  # Strip each line and print it

# Step 2: Split each line into key-value pairs
print("\nStep 2: Split each line into key-value pairs")
for line in lines:
    stripped_line = line.strip()  # Remove spaces
    if '=' in stripped_line:  # Check if line has a key-value pair
        key, value = stripped_line.split("=", 1)  # Split by the first equal sign
        print(f"Key: {key.strip()}, Value: {value.strip()}")  # Print key-value

# Step 3: Replace old password with a new one
print("\nStep 3: Replace old password with new one")
updated_config = config_data.replace("oldpassword123", "newpassword456")
print(updated_config)

# Step 4: Join lines back into a single string after cleaning
print("\nStep 4: Join cleaned lines back into a single string")
cleaned_lines = []
for line in lines:
    cleaned_line = line.strip()  # Clean each line
    if '=' in cleaned_line:
        key, value = cleaned_line.split("=", 1)
        cleaned_lines.append(f"{key.strip()} = {value.strip()}")  # Append cleaned key-value
    else:
        cleaned_lines.append(cleaned_line)  # Append section headers
final_config = "\n".join(cleaned_lines)  # Join lines back into a string
print(final_config)
