#!/bin/bash

# Check and install Git
tool="git"
if command -v $tool &> /dev/null; then
    echo "$tool is already installed."
else
    echo "$tool is not installed. Installing $tool..."

    # Check if the system is macOS
    if [[ "$(uname)" == "Darwin" ]]; then
        # Install Git using Homebrew for macOS
        brew install $tool
    elif [[ "$(uname)" == "Linux" ]]; then
        # Install Git using apt for Debian/Ubuntu
        sudo apt update
        sudo apt install -y $tool
    else
        echo "Unsupported OS. Cannot install $tool."
    fi

    # Verify if Git was installed successfully
    if command -v $tool &> /dev/null; then
        echo "$tool has been installed successfully."
    else
        echo "Failed to install $tool. Please check your system or package manager."
    fi
fi

# Check and install Python3
tool="python3"
if command -v $tool &> /dev/null; then
    echo "$tool is already installed."
else
    echo "$tool is not installed. Installing $tool..."

    # Check if the system is macOS
    if [[ "$(uname)" == "Darwin" ]]; then
        # Install Python3 using Homebrew for macOS
        brew install $tool
    elif [[ "$(uname)" == "Linux" ]]; then
        # Install Python3 using apt for Debian/Ubuntu
        sudo apt update
        sudo apt install -y $tool
    else
        echo "Unsupported OS. Cannot install $tool."
    fi

    # Verify if Python3 was installed successfully
    if command -v $tool &> /dev/null; then
        echo "$tool has been installed successfully."
    else
        echo "Failed to install $tool. Please check your system or package manager."
    fi
fi

echo "Installation check complete."
