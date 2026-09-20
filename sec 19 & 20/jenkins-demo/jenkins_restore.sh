#!/bin/bash

# Set backup directory
BACKUP_DIR="/var/lib/jenkins_backup"
JENKINS_DIR="/var/lib/jenkins"

# List available backups
echo "Available backups:"
ls -lh $BACKUP_DIR

# Ask for the backup file to restore
read -p "Enter the full path of the backup file to restore: " BACKUP_FILE

# Check if file exists
if [ ! -f "$BACKUP_FILE" ]; then
    echo "Backup file not found!"
    exit 1
fi

# Stop Jenkins before restoring
echo "Stopping Jenkins service..."
sudo systemctl stop jenkins

# Restore the backup
echo "Restoring backup from $BACKUP_FILE..."
tar -xzvf $BACKUP_FILE -C /

# Start Jenkins
echo "Starting Jenkins service..."
sudo systemctl start jenkins

echo "Jenkins restore completed!"
