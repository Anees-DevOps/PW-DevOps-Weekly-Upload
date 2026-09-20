#!/bin/bash

# Set backup directory
BACKUP_DIR="/var/lib/jenkins_backup"
JENKINS_DIR="/var/lib/jenkins"

# Create backup directory if not exists
mkdir -p $BACKUP_DIR

# Backup file name with timestamp
BACKUP_FILE="$BACKUP_DIR/jenkins_backup_$(date +%F_%H-%M-%S).tar.gz"

# Stop Jenkins before backup
echo "Stopping Jenkins service..."
sudo systemctl stop jenkins

# Create a backup
echo "Backing up Jenkins configuration, jobs, and plugins..."
tar -czvf $BACKUP_FILE $JENKINS_DIR

# Restart Jenkins
echo "Starting Jenkins service..."
sudo systemctl start jenkins

# Remove old backups (older than 7 days)
find $BACKUP_DIR -type f -name "jenkins_backup_*.tar.gz" -mtime +7 -exec rm {} \;

echo "Backup completed! Backup file: $BACKUP_FILE"


## How to use:
# save the script 
# make it executable with chmod +x jenkins_backup.sh, 
# run it with ./jenkins_backup.sh. 