#!/bin/bash

# Define an array of tools to check and install
tools=("git" "bash" "python3")

# Function to install a tool
install_tool() {
    local tool=$1  # Tool name passed as argument
    
    echo "$tool is not installed. Installing $tool..."
    
    # Check for macOS or Linux and install accordingly
    if [[ "$(uname)" == "Darwin" ]]; then
        brew install $tool
    elif [[ "$(uname)" == "Linux" ]]; then
        sudo apt update
        sudo apt install -y $tool
    else
        echo "Unsupported OS. Cannot install $tool."
        return 1
    fi
    
    # Verify installation
    if command -v $tool &> /dev/null; then
        echo "$tool has been installed successfully."
    else
        echo "Failed to install $tool. Please check your system or package manager."
    fi
}

# Loop through each tool in the tools array
for tool in "${tools[@]}"; do
    if command -v $tool &> /dev/null; then
        echo "$tool is already installed."
    else
        install_tool $tool  # Call the function to install the tool
    fi
done

# Final completion message
echo "Installation check complete."
