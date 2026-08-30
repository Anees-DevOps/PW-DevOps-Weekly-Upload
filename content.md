SEC:03_SAT


🖥️ Lesson: Introduction to the Linux Terminal

1️⃣ Analogy: The Terminal as Your "Control Room"
Imagine your computer is like a large factory.


The Graphical User Interface (GUI) (icons, windows, mouse clicks) is like walking around the factory and pressing buttons one by one.


The Terminal is like the control room — from one place, you can control everything with precise instructions.


System Administrators & DevOps engineers prefer the control room (terminal) because it’s faster, more powerful, and can be automated.



2️⃣ Concept: Why the Terminal Matters
Linux servers (used in cloud, DevOps, production systems) often don’t have GUIs.


Terminal = direct communication with the OS.


Every DevOps engineer needs it because:


Cloud servers are accessed via SSH → terminal only.


Automation (scripts, Ansible, CI/CD) runs terminal commands.


Faster & more flexible than GUI.



3️⃣ Hands-On Commands
🔹 Navigating & Listing
pwd           # Show where you are
ls            # List files
ls -l         # Detailed view
ls -a         # Show hidden files

🔹 Moving Around
cd folder_name   # Go into folder
cd ..            # Go back one step
cd /             # Go to root
cd ~             # Go to home

🔹 Managing Files & Directories
mkdir myfolder          # Create folder
rm file.txt             # Delete file
rm -r folder_name       # Delete folder
cp file.txt backup.txt  # Copy file
cp -r folder1 folder2   # Copy folder

🔹 Viewing & Searching Files
cat file.txt               # Print entire file
less file.txt              # Scroll through file
grep "error" logfile.txt   # Search for "error"
grep -i "error" logfile.txt   # Case-insensitive
grep -r "password" /etc    # Recursive search


4️⃣ Industry Use Cases
System Admins → move around servers with cd, pwd, ls.


DevOps engineers → debug errors using grep in logs.


Developers → quickly check config files with cat, less.


Automation → create/delete/copy folders in CI/CD pipelines.



5️⃣ Mini Activity for Students (with Answers ✅)
📝 Activity Steps
Check where you are

 pwd
 ✅ Output: Shows current directory (e.g., /home/student).


Create a folder devops_practice

 mkdir devops_practice


Move into it

 cd devops_practice


Create a file notes.txt with text

 echo "Hello DevOps" > notes.txt


Copy notes.txt to backup.txt

 cp notes.txt backup.txt


List files

 ls -l
 ✅ Output: Shows notes.txt and backup.txt.


View contents of notes.txt

 cat notes.txt
 ✅ Output:

 Hello DevOps


Add more lines

 echo "Learning Linux" >> notes.txt
 Now notes.txt contains:

 Hello DevOps
Learning Linux


Search for the word "Linux"

 grep "Linux" notes.txt
 ✅ Output:

 Learning Linux



🌟 Challenge Exercise
Task:
Create a folder projects.


Inside it, create file1.txt, file2.txt, file3.txt with different text.


Search which file contains the word "cloud".


Solution:
mkdir projects
cd projects

echo "This is file one" > file1.txt
echo "DevOps runs in the cloud" > file2.txt
echo "Linux is awesome" > file3.txt

grep "cloud" *.txt

✅ Output:
file2.txt:DevOps runs in the cloud

👉 Now u see how grep can pinpoint which file contains important text, just like scanning logs for errors in real systems.

👥 Lesson: Linux Users and Groups
1️⃣ Analogy: Users & Groups as "Residents in a Building"
Think of a Linux system as a large apartment building:


Each user = a resident with their own apartment (home directory).


Each group = a family or team (a set of users with shared access).


Example:


A company server may have developers, testers, and admins.


Developers should only edit code, testers access test files, admins control everything.


Linux uses users & groups to ensure security and proper permissions.



2️⃣ Concept: Why Users & Groups Matter
Users: Identify people or processes on the system.


Each has a username, user ID (UID), and a home directory.


Groups: Collections of users to manage permissions easily.


Instead of giving file permissions to 50 individual users, you just give it to a group.


Why important in DevOps/System Administration:


Security: Prevents unauthorized access.


Collaboration: Team members share resources via groups.


Separation: Developers, QA, Ops can be isolated.



3️⃣ Hands-On Commands

Here’s a clean comparison table for User & Group Management across Ubuntu/Debian, RHEL, macOS:
macOS:
Action
Command (macOS dscl)
Create user
sudo dscl . -create /Users/alice
Set shell
sudo dscl . -create /Users/alice UserShell /bin/bash
Set UID
sudo dscl . -create /Users/alice UniqueID "510"
Set primary GID
sudo dscl . -create /Users/alice PrimaryGroupID 20
Set home dir
sudo dscl . -create /Users/alice NFSHomeDirectory /Users/alice
Set password
sudo dscl . -passwd /Users/alice password123
Add to group
sudo dscl . -append /Groups/staff GroupMembership alice
Delete user
sudo dscl . -delete /Users/alice
Notes
Very verbose compared to Linux. Normally you don’t create users this way — use Linux VM or WSL instead.

Ubuntu/Debian, RHEL:
Action
Ubuntu/Debian
RHEL
Create user
sudo adduser alice
sudo useradd alice
Set password
Done interactively with adduser
sudo passwd alice
Add to group
sudo usermod -aG developers alice
sudo usermod -aG developers alice
Delete user
sudo deluser alice
sudo userdel alice
Notes
adduser is more user-friendly than useradd.
Similar to Debian, but uses useradd.


🔹 User Management
# Create a new user
sudo adduser alice

# Modify a user (e.g., add to a group)
sudo usermod -aG developers alice

# Delete a user
sudo deluser alice

🔹 Group Management
# Create a group
sudo groupadd developers

# Rename/modify a group
sudo groupmod -n devteam developers

# Delete a group
sudo groupdel devteam

🔹 Managing Group Memberships
# Add user to group
sudo usermod -aG groupname username

# Check group memberships
groups alice

# Change a user’s primary group
sudo usermod -g groupname username


4️⃣ Industry Use Cases
Cloud servers → DevOps engineers create separate users for security.


Project teams → Developers in one group, QA in another, admins in sudo group.


Access control → Database admins only access DB files, not application code.


Auditing → Easy to track which user did what on the system.



5️⃣ Mini Activity for Students (with Answers ✅)
1) Create a group devops_team
Linux / WSL (Ubuntu/Debian)

 sudo groupadd devops_team

macOS

 # simplest
sudo dseditgroup -o create devops_team

# (optional) set a specific GID if you need one
# sudo dscl . -create /Groups/devops_team
# sudo dscl . -create /Groups/devops_team PrimaryGroupID 505


2) Create a user john and add him to devops_team
Linux / WSL (Ubuntu/Debian)

 sudo adduser john
sudo usermod -aG devops_team john

macOS

 # create user (recommended tool on modern macOS)
sudo sysadminctl -addUser john -password 'StrongPass123' -home /Users/john -shell /bin/bash

# add to group
sudo dseditgroup -o edit -a john -t user devops_team

tip (macOS): you can also build a user with dscl attribute-by-attribute, but sysadminctl is shorter and safer.

3) Check John’s group memberships
Linux / WSL

 groups john
# or
id john

macOS

 groups john
# or
id john


4) Rename group devops_team → cloud_team
Linux / WSL

 sudo groupmod -n cloud_team devops_team

macOS

 # change the record name of the group
sudo dscl . -change /Groups/devops_team RecordName devops_team cloud_team


5) Remove user john from the system
Linux / WSL (Ubuntu/Debian)

 sudo deluser john           # keeps home by default on Debian/Ubuntu
# (optional) remove home too:
# sudo deluser --remove-home john
 (on RHEL/CentOS you’d use sudo userdel john and optionally remove /home/john)


macOS

 # delete user but KEEP the home folder
sudo sysadminctl -deleteUser john -keepHome

# delete user AND remove the home folder (careful!)
# sudo sysadminctl -deleteUser john

quick notes you’ll care about
WSL behaves like Linux (Ubuntu) for these commands. Everything in the “Linux / WSL” column works the same inside your WSL distro.


macOS doesn’t have adduser/deluser/groupadd/groupmod/systemctl. You use:


Users: sysadminctl (or dscl)


Groups: dseditgroup (or dscl)


To test switching to the new account:


Linux/WSL: su - john or sudo -iu john


macOS: su - john (only after setting a password and if the account isn’t disabled)

🌟 Challenge Exercise
Task:
Create a group projectX.


Add two users (alice and bob).


Make alice’s primary group projectX.


Verify memberships.


Solution:
sudo groupadd projectX
sudo adduser alice
sudo adduser bob
sudo usermod -aG projectX bob
sudo usermod -g projectX alice

groups alice
groups bob

✅ Expected Output:
alice : projectX
bob   : bob projectX

👉 Here, Alice belongs primarily to projectX, while Bob has it as a secondary group.

📦 Lesson: Package Managers & Basic System Administration

1️⃣ Analogy: Package Managers as "App Stores for Linux"
On your phone, you don’t download apps manually from websites—you use the App Store or Play Store.


In Linux, package managers are like app stores:


They download software from official repositories.


They automatically install required dependencies.


They make updating and removing software easy.


Different Linux families have different "app stores":


Debian/Ubuntu → apt


Red Hat/CentOS/Fedora → yum or dnf



2️⃣ Concept: Why Package Managers & Services Matter
Package Managers: Tools to install, update, and remove software.


Systemd & systemctl: Manage system services (e.g., web servers, databases).


Important because:


You can set up environments quickly.


You keep software up to date with security patches.


You control system services like nginx, mysql, or docker.



3️⃣ Hands-On Commands
Perfect 👍 Let’s build a package management comparison table for Ubuntu/Debian, RHEL/CentOS/Fedora, WSL (Windows Subsystem for Linux), and macOS.

📊 Package Management Commands
Action
Ubuntu/Debian (APT)
RHEL/CentOS/Fedora (YUM/DNF)
WSL (depends on distro)
macOS (Homebrew)
Update package list
sudo apt update
sudo yum update -y sudo dnf update -y
Same as chosen distro (e.g., Ubuntu → apt update)
brew update
Upgrade installed packages
sudo apt upgrade -y
sudo yum update -y sudo dnf upgrade -y
Same as distro (Ubuntu → apt upgrade)
brew upgrade
Install software
sudo apt install nginx -y
sudo yum install nginx -y sudo dnf install nginx -y
Same as distro (e.g., apt install nginx)
brew install nginx
Remove software
sudo apt remove nginx -y
sudo yum remove nginx -y sudo dnf remove nginx -y
Same as distro
brew uninstall nginx
Remove incl. config
sudo apt purge nginx -y
N/A (configs not purged separately)
Same as distro
Must manually remove configs (e.g., /usr/local/etc/)
Notes
APT manages .deb packages.
YUM (older), DNF (modern). Manages .rpm.
WSL mirrors native distro tools.
Homebrew is community-driven; must be installed separately.


⚡ Key takeaways:
WSL: just uses whatever Linux distro you installed (Ubuntu → apt, Fedora → dnf, etc.).


macOS: no native package manager like Linux; Homebrew (brew) is the de facto standard.

🔹 Managing Services with systemctl

Linux:
 systemctl start nginx, systemctl status nginx, systemctl enable nginx


macOS:
 macOS doesn’t use systemd. It uses launchctl or Homebrew’s brew services.
 
Example:

 brew services start nginx
brew services stop nginx
brew services list
 👉 So you can’t practice systemctl directly on macOS. For that, you need Linux or WSL.


# Start a service
sudo systemctl start nginx

# Stop a service
sudo systemctl stop nginx

# Restart a service
sudo systemctl restart nginx

# Enable service on boot
sudo systemctl enable nginx

# Disable service from starting on boot
sudo systemctl disable nginx

# Check status
sudo systemctl status nginx


4️⃣ Industry Use Cases
Web server setup → Install & manage Apache/Nginx with apt or yum.


CI/CD servers → Install Jenkins, Docker, Kubernetes tools via package managers.


Security → Keep packages updated (apt upgrade, dnf update).


Service management → Ensure critical services (databases, monitoring agents) restart automatically on boot.



5️⃣ Mini Activity for Students (with Answers ✅)
📝 Activity Steps
Update package repositories

 sudo apt update         # Debian/Ubuntu
# or
sudo yum update -y      # RHEL/CentOS


Install Nginx web server

 sudo apt install nginx -y      # Debian/Ubuntu
sudo yum install nginx -y      # RHEL/CentOS


Check if the service is running

 systemctl status nginx
 ✅ Output (snippet):

 Active: active (running)


Stop and start the service

 sudo systemctl stop nginx
sudo systemctl start nginx


Enable it to run at boot

 sudo systemctl enable nginx


Remove the package

 sudo apt remove nginx -y     # Debian/Ubuntu
sudo yum remove nginx -y     # RHEL/CentOS



🌟 Challenge Exercise
Task:
Install apache2 (Debian/Ubuntu) or httpd (RHEL).


Start the service.


Check if it’s running by visiting http://localhost in a browser.


Then stop and disable it.


Solution:
# Debian/Ubuntu
sudo apt install apache2 -y
sudo systemctl start apache2
systemctl status apache2

# RHEL/CentOS
sudo yum install httpd -y
sudo systemctl start httpd
systemctl status httpd

✅ Expected Results:
Visiting http://localhost → shows the Apache test page.


systemctl status → service should be active.


After stopping & disabling:

 Active: inactive (dead)

🔐 Lesson: File Permissions & Ownership in Linux

1️⃣ Analogy: House with Rooms and Keys
Imagine a house with rooms (files/directories).


Each room has:


Owner (the person who owns the room).


Group (a family/friends circle with access).


Others (strangers/visitors).


Each can have three kinds of keys:


Read (r) → permission to look inside (read contents).


Write (w) → permission to change things.


Execute (x) → permission to enter and use (for directories or programs).



2️⃣ Concept: Linux File Permissions
Every file/directory has permissions for owner, group, others.


Shown when running ls -l:

 -rw-r--r-- 1 alice devs  1234 Aug 30 file.txt
 Breakdown:


-rw-r--r-- → permissions (owner = rw, group = r, others = r).


alice → file owner.


devs → group.


🔹 Numeric (Octal) Format
Permissions are also expressed as numbers:


Read (r) = 4


Write (w) = 2


Execute (x) = 1


Add them up:


7 = rwx


6 = rw-


5 = r-x


4 = r--


Example:
chmod 755 file.sh → Owner = rwx (7), Group = r-x (5), Others = r-x (5).



3️⃣ Hands-On Commands
🔹 Viewing Permissions
ls -l file.txt

🔹 Changing Permissions with chmod
# Give owner execute permission
chmod u+x file.sh

# Remove write permission from others
chmod o-w file.txt

# Using numeric mode
chmod 644 file.txt   # Owner: rw-, Group: r--, Others: r--
chmod 755 script.sh  # Owner: rwx, Group: r-x, Others: r-x

🔹 Ownership with chown
# Change owner
sudo chown bob file.txt

# Change owner and group
sudo chown bob:devs file.txt

🔹 Default Permissions with umask
umask        # Check current mask (e.g., 0022)
umask 0027   # Set new default (no access for others)

👉 Example:
With umask 0022, new files get 644 (rw-r--r--) and directories 755.


With umask 0027, new files get 640 (rw-r-----) and directories 750.



4️⃣ Industry Use Cases
Security: Ensure sensitive files (like SSH keys) are only readable by the owner (chmod 600 id_rsa).
chmod 600 file

Format: [ OWNER ] [ GROUP ] [ OTHERS ]

First digit (6) → Owner permissions


6 = 4 (read) + 2 (write) = rw-


✅ Owner can read & write


❌ No execute permission


Second digit (0) → Group permissions


0 = ---


❌ Group has no access


Third digit (0) → Others (everyone else)


0 = ---


❌ No access for others



Collaboration: Developers in the same group can share project files (chown user:devs).


Web servers: Web files must be readable by the webserver user (chmod 644 index.html).


Automation: Scripts must be executable (chmod +x deploy.sh).



5️⃣ Mini Activity for Students (with Answers ✅)
📝 Activity Steps
Create a file report.txt and check permissions

 touch report.txt
ls -l report.txt
 ✅ Output example:

 -rw-r--r-- 1 student student 0 Aug 30 report.txt


Change permissions so only the owner can read and write

 chmod 600 report.txt
ls -l report.txt
 ✅ Output:

 -rw------- 1 student student 0 Aug 30 report.txt


Make a script executable

 echo 'echo "Hello DevOps"' > hello.sh
chmod 755 hello.sh
./hello.sh
 ✅ Output:

 Hello DevOps


Change owner of a file to another user (e.g., bob)

 sudo chown bob report.txt
ls -l report.txt
 ✅ Output:

 -rw------- 1 bob student 0 Aug 30 report.txt


Check umask and predict default permissions

 umask
 ✅ If umask = 0022:


New files → 644 (rw-r--r--)


New dirs → 755 (rwxr-xr-x)



🌟 Challenge Exercise
Task:
Create a directory project_dir.


Inside it, create a file secret.txt.


Set it so only the owner can read/write, no one else has access.


Verify with ls -l.


Solution:
mkdir project_dir
touch project_dir/secret.txt
chmod 600 project_dir/secret.txt
ls -l project_dir/secret.txt

✅ Expected Output:
-rw------- 1 student student 0 Aug 30 project_dir/secret.txt


💽 Lesson: Disk Usage & Storage Management in Linux
1️⃣ Analogy: Disk Space as a Bookshelf
Think of your disk as a bookshelf.


df tells you how much space is left on the whole shelf.


du tells you how much space each book or section takes.


If the shelf gets full, you need to:


Rearrange (clean up old books).


Move some to another shelf (archive/migrate).


Buy a bigger shelf (add new disk/volume).



2️⃣ Concept: Disk Usage Tools
df (disk free) → Shows available and used disk space on the system.


du (disk usage) → Shows how much space files/directories take.


Why important:


Servers crash if disks fill up.


Logs, temp files, or old backups often eat space.


Storage monitoring is a core DevOps duty.



3️⃣ Hands-On Commands
🔹 Checking File System Usage with df
df -h

-h = human-readable (MB/GB).
 ✅ Example Output:


Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   25G   22G  54% /
tmpfs           2.0G     0  2.0G   0% /dev/shm

🔹 Checking Directory Sizes with du
# Size of current directory
du -sh .

# Size of all subdirectories
du -sh *  

# Find top space consumers (example: top 5)
du -ah /var | sort -rh | head -n 5

✅ Example Output:
1.2G /var/log
800M /var/cache
500M /var/tmp


4️⃣ Practical Tips for Clearing Space
Logs: Clear or rotate large logs.

But journalctl (Linux logs) doesn’t exist on macOS.
sudo journalctl --vacuum-size=200M

👉 macOS uses log show instead:
log show --predicate 'eventMessage contains "error"' --info


 sudo journalctl --vacuum-size=200M
sudo truncate -s 0 /var/log/large.log


Package cache:

 sudo apt clean        # Debian/Ubuntu
sudo yum clean all    # RHEL/CentOS


Old files: Find and remove unused large files.

 find / -type f -size +500M


Temp files:

 rm -rf /tmp/*


Move/archive data: Transfer old backups to cloud storage.



5️⃣ Industry Use Cases
CI/CD servers: Build artifacts/logs fill up space quickly.


Web servers: Log files in /var/log can grow huge.


Cloud servers: AWS/GCP disks cost money — optimize usage.


Monitoring: Tools like Prometheus/Grafana monitor disk usage continuously.



6️⃣ Mini Activity for Students (with Answers ✅)
📝 Activity Steps
Check disk usage

 df -h
 ✅ Output (example):

 Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        30G   15G   14G  52% /


Check how much space /var is using

 du -sh /var
 ✅ Output:

 2.3G    /var


List all directories under /var with their sizes

 du -sh /var/*
 ✅ Output:

 1.2G /var/log
800M /var/cache
300M /var/tmp


Find top 5 biggest files under /var/log

 du -ah /var/log | sort -rh | head -n 5
 ✅ Output:

 600M /var/log/syslog.1
400M /var/log/kern.log
200M /var/log/auth.log
50M  /var/log/dpkg.log
30M  /var/log/apt/history.log



🌟 Challenge Exercise
Task:
Check the biggest directory inside /home.


Find files larger than 100MB.


Suggest what to delete.


Solution:
du -sh /home/*
find /home -type f -size +100M

✅ Example Output:
2.0G /home/student/videos
/home/student/videos/ubuntu.iso (1.5G)

👉 Suggestion: Move ubuntu.iso to external storage or delete if not needed.
👉 We learnt how to diagnose disk space issues — a daily job for DevOps engineers.




SEC:04_SUN

⏰ Lesson: Cron Jobs & Background Processes (with OS Differences)

1️⃣ Analogy: Robots & Assistants
Imagine you have a robot assistant that waters your plants every day at 6 AM.


You don’t have to wake up early — the robot just does it automatically.


In Linux/macOS:


Cron jobs = robots that run tasks automatically at scheduled times.


Background processes = assistants who keep working while you do other things.





2️⃣ Concept: Why Cron Jobs & Background Processes Matter
Cron Jobs: Automate repetitive tasks (backups, log cleanup, monitoring).


🔹 Foreground vs Background
Foreground process → runs and occupies your terminal (you can’t type anything until it finishes).


Background process → runs behind the scenes, freeing your terminal for other commands.

[1] 12345
[1] → Job number (the shell’s reference for this background task)


12345 → Process ID (PID)


3️⃣ Hands-On Commands (with OS Differences)
🔹 Cron Jobs

Action
Ubuntu/Debian
RHEL/CentOS
macOS
Open crontab editor
crontab -e
crontab -e
crontab -e
List cron jobs
crontab -l
crontab -l
crontab -l
Remove all cron jobs
crontab -r
crontab -r
crontab -r
Cron service mgmt
sudo systemctl status cron
sudo systemctl status crond
No systemctl (cron runs by default, or use launchd)


📌 Note for macOS:
macOS supports cron, but Apple prefers launchd for scheduling.


Example launchd plist: /Library/LaunchDaemons/com.user.task.plist.


For learning → cron works fine.



Crontab Format Reminder:
* * * * * command
| | | | |
| | | | └── Day of week (0-6, Sun=0)
| | | └──── Month (1-12)
| | └────── Day of month (1-31)
| └──────── Hour (0-23)
└────────── Minute (0-59)

Example entries:
# Run every day at midnight
0 0 * * * /home/user/backup.sh

	So for 0 0 * * *:
0 (minute) → at 0th minute → :00


0 (hour) → at 0th hour → midnight


* (day of month) → any day of the month


* (month) → any month


* (day of week) → any day of the week


👉 Together: Run every day, at 00:00 (midnight).


# Run every 5 minutes
*/5 * * * * /home/user/check.sh

# Run at 8 AM on Mondays
0 8 * * 1 /home/user/weekly_report.sh


🔹 Background Processes
Action
Command (all OS: Ubuntu/RHEL/macOS)
Run in background
ping google.com > pinglog.txt &
List jobs
jobs
Bring job foreground
fg %1
Resume stopped job in background
bg %1
Kill a process
kill <PID> (get PID via ps or jobs -l)

📌 Note:
On macOS, ping runs indefinitely by default. Add -c 5 to limit it:

 ping -c 5 google.com > pinglog.txt &



4️⃣ Industry Use Cases
DevOps: Automated backups, log rotation, health checks.


Monitoring: Run scripts every 5 min for server checks.


Deployments: Scheduled deployments at low-traffic hours.


Background Processes: Run web servers, simulations, data processing jobs without blocking terminal.



5️⃣ Mini Activity for Students (with Answers ✅)
📝 Activity Steps
Create a simple script to log date
echo 'date >> /home/aneesh/Desktop/pw_cron.log' > ~/mycron.sh   # Linux
# OR
echo 'date >> /Users/aneesh/Desktop/pw_cron.log' > ~/mycron.sh  # macOS


chmod +x ~/mycron.sh

Schedule it to run every minute


crontab -e

Add this line:
* * * * * /Users/moalamnm/mycron.sh       # macOS
* * * * * /home/moalamnm/mycron.sh        # Ubuntu/RHEL

3. Run the script: 

~/mycron.sh

4. Wait 2–3 minutes and check the log


cat ~/Desktop/pw_cron.log


✅ Output:
Sat Aug 30 09:01:01 IST 2025
Sat Aug 30 09:02:01 IST 2025
Sat Aug 30 09:03:01 IST 2025

Key Tip: Always use absolute paths inside cron (both for scripts and log files), otherwise cron won’t know where to write.

Run a background process


# Ubuntu/RHEL
ping google.com > pinglog.txt &

# macOS (limit to 5 pings)
ping -c 5 google.com > pinglog.txt &

Check jobs:
jobs

✅ Output:
[1]+  Running   ping google.com > pinglog.txt &

Bring to foreground, then stop it


fg %1
CTRL+C


🌟 Challenge Exercise
Task:
Write a script that saves disk usage (df -h) to a log file.


Schedule it every 5 minutes.


Verify multiple log entries appear.


Solution:
# Script
echo 'df -h >> /tmp/disk_report.log' > ~/diskcheck.sh
chmod +x ~/diskcheck.sh

# Add to crontab
crontab -e

Add line:
*/5 * * * * /Users/student/diskcheck.sh    # macOS
*/5 * * * * /home/student/diskcheck.sh     # Ubuntu/RHEL

✅ Check log after 10 mins:
cat /tmp/disk_report.log


🔑 Key Difference Summary:
Cron service name: cron (Ubuntu) vs crond (RHEL) vs no systemctl on macOS.


File paths: /home/user/... (Linux) vs /Users/user/... (macOS).


Ping behavior: infinite by default on Linux, finite with -c on macOS.


Advanced macOS: prefer launchd for production jobs, but cron is okay for practice.



🖥️ Lesson: Debugging CPU & Memory Issues in Linux

1️⃣ Analogy – "Traffic on a Highway" 🚗
Think of your server as a highway:


CPU = number of lanes available.


Memory (RAM) = fuel tanks of cars; if cars run out, they stall.


Disk I/O = toll booths that cars must pass.


If too many cars try to pass, or if some cars never leave (memory leaks), traffic jams happen.


👉 Debugging tools = traffic cameras that show where the jam is.

2️⃣ Concept – Why Debugging is Needed
Heap Memory Issues: Memory leaks, unoptimized apps consuming RAM → system slows down or OOM (Out of Memory) kills processes.


CPU Issues: One rogue process consuming 100% CPU can slow the server.


I/O Issues: Slow disk reads/writes → bottleneck.


DevOps needs visibility into these resources to quickly triage problems.

3️⃣ Hands-On Tools
🔹 top (default monitoring tool)
Shows CPU, memory, and processes.
top

Press M → sort by memory.


Press P → sort by CPU usage.


Press q → quit.



🔹 htop (improved top)
More user-friendly, color-coded, interactive.


Install first:


Ubuntu/Debian → sudo apt install htop


RHEL/CentOS → sudo yum install htop or sudo dnf install htop


macOS → brew install htop (needs Homebrew)


Run:

 htop



🔹 vmstat (virtual memory statistics)
vmstat 2 5

Updates every 2 seconds, 5 times.


Shows CPU idle time, memory free, swap usage, and processes waiting.


macOS does have its own vm_stat (note the underscore), but the output format is very different:
vm_stat 2

👉 prints memory statistics every 2 seconds.s

🔹 iostat (I/O statistics – part of sysstat package)
iostat -xz 2 5

For Mac:
 iostat -d -w 2 5



Updates every 2 seconds, 5 times.


Shows CPU usage + disk read/write throughput.


Install:
Ubuntu/Debian → sudo apt install sysstat


RHEL/CentOS → sudo yum install sysstat or sudo dnf install sysstat


macOS → brew install sysstat (not default)



4️⃣ OS Differences (Quick Reference)
Tool
Ubuntu/Debian 🟢
RHEL/CentOS 🔴
macOS 🍎
top
✅ Default
✅ Default
✅ Default (top looks different but works)
htop
sudo apt install htop
sudo yum/dnf install htop
brew install htop
vmstat
✅ Default
✅ Default
✅ Default
iostat
sudo apt install sysstat
sudo yum/dnf install sysstat
brew install sysstat


5️⃣ Industry Use Cases
Debugging high CPU on app servers.


Finding memory leaks in long-running microservices.


Identifying disk I/O bottlenecks in databases.


Using tools inside containers/VMs to tune performance.



6️⃣ Mini Activity (with Answers ✅)
📝 Activity Steps
Run top and identify the process consuming the most CPU.


Answer: In top, the %CPU column shows usage. The highest value = the culprit.


Install htop and sort processes by memory.


Answer: Press F6 in htop to change sort column → choose %MEM.


Use vmstat 2 3. Interpret the id column.


Answer: id = CPU idle %. If it’s very low (<10%), CPU is heavily used.


Run iostat -xz 2 3. Look at %util.


Answer: %util near 100% means your disk is fully busy (I/O bottleneck).


Kill a CPU-hogging process.


Run:

 kill -9 <PID>


Answer: Process disappears from top or htop.



7️⃣ Key Takeaway
top/htop → Find which process is the hog.


vmstat → Check CPU vs memory balance.


iostat → See if the disk is the bottleneck.


With these, DevOps engineers gain visibility + control to troubleshoot servers fast.



how to think like a DevOps engineer?
System slow? 
   ↓
Check CPU with top/htop
   ├─ One process high CPU → kill/optimize it
   └─ All processes high CPU → need more CPU scaling
   ↓
Check Memory with top/vmstat
   ├─ Swap being used? → add RAM or fix leaks
   └─ Memory hog process? → restart/kill it
   ↓
Check Disk with iostat
   ├─ %util ~100% → disk bottleneck, use faster disks
   └─ Low %util → disk OK, check network/app level


⚙️ Module: Process Management in Linux
1️⃣ Analogy – "Office Workers and a Manager"
Think of your system as a big office:
Each process = a worker doing a task.


The CPU = their working hours.


Priority (nice/renice) = how urgently the boss assigns them work.


ps/top/htop = the attendance register + CCTV camera.


kill = firing a worker who is misbehaving or stuck.


👉 As a sysadmin/DevOps engineer, you are the manager deciding which tasks (processes) get priority.

2️⃣ Concepts
Process: A running instance of a program.


PID (Process ID): A unique number assigned to every process.


PPID (Parent PID): The process that started another process.


Foreground process: Runs actively in terminal.


Background process: Runs behind the scenes.


Priority (niceness): Determines scheduling preference.



3️⃣ Commands
🔹 ps – list processes
ps aux

a → all users


u → show user/owner


x → include processes without terminal


Key columns:
PID → Process ID


%CPU / %MEM → usage


STAT → state (R = running, S = sleeping, Z = zombie)


COMMAND → the program name


✅ OS differences:
Ubuntu/RHEL/macOS → ps aux works everywhere.


On macOS, ps -ef shows slightly different format (but still useful).



🔹 top / htop – real-time monitoring
top:

 top


P → sort by CPU


M → sort by memory


htop (colorful, interactive):


Install:


Ubuntu: sudo apt install htop


RHEL: sudo yum install htop or sudo dnf install htop


macOS: brew install htop



🔹 nice and renice – adjust priorities
Nice values range: -20 (highest priority) to +19 (lowest priority).


Start a program with lower priority:

 nice -n 10 myprogram


Change priority of a running process:

 renice -n 5 -p <PID>


✅ OS differences:
Works the same in Ubuntu, RHEL, macOS.


On macOS, root access may be needed for lowering nice values.



🔹 kill – terminate processes
Kill by PID:

 kill <PID>


Stronger kill:

 kill -9 <PID>


Kill by process name:

 pkill <name>


Interactive selection:

 top → press k → enter PID → signal 9


✅ OS differences:
kill and pkill exist on Ubuntu/RHEL/macOS.


macOS pkill works but syntax slightly stricter.



4️⃣ Industry Use Cases
Detecting & killing rogue processes hogging CPU.


Adjusting priority for background tasks (e.g., backups should run at low priority).


Monitoring microservices or containers using top/htop.


Debugging zombie processes (stuck processes not releasing resources).



5️⃣ Mini Activity (with Answers ✅)
📝 Activity Steps
List all running processes with ps aux.


Answer: Output shows all processes with PID, CPU, MEM usage.


Find your terminal’s shell PID.

 echo $$


Answer: Returns PID of your current shell, visible in ps.


Start a background process:

 yes > /dev/null &


Find its PID in ps aux or top.


Answer: PID visible with high CPU in %CPU column.


Use renice to lower its priority:

 renice -n 15 -p <PID>


Answer: renice confirms new priority. CPU usage may drop.


Kill the background process.

 kill -9 <PID>


Answer: Process disappears from top or ps aux.



6️⃣ Key Takeaway
ps → snapshot of processes.


top/htop → real-time monitoring.


nice/renice → adjust priority.


kill → terminate processes.
 👉 Process management is about visibility + control of system resources.


real-world troubleshooting scenarios - know when to use each command — not just how.
🛠️ Process Management – Troubleshooting Scenarios
1️⃣ Scenario: Process is Eating All CPU
Symptom: System is laggy, fans spinning, commands slow.


Diagnosis:

 top
 → One process shows %CPU near 100.


Fix:

 kill <PID>
# if stubborn
kill -9 <PID>

✅ Industry relevance: Happens often when a web server or script enters an infinite loop.

2️⃣ Scenario: Background Task Slowing Down System
Symptom: You start a backup or large script → your apps become slow.


Diagnosis:

 ps -u <username>
top

Fix: Lower its priority so it doesn’t fight with critical processes.

 renice -n 15 -p <PID>

If starting new:

 nice -n 15 mybackup.sh &

✅ Industry relevance: Backups, log rotations, or data imports often run with low priority.

3️⃣ Scenario: Process Is Frozen (Unresponsive App)
Symptom: You open an app (e.g., text editor) → it hangs.


Diagnosis:

 ps aux | grep <appname>

Fix: Terminate it.

 kill <PID>
kill -9 <PID>  # if needed

✅ Industry relevance: Same as killing stuck web servers, Jenkins jobs, or container processes.

4️⃣ Scenario: Too Many “Zombie” Processes
Symptom: ps aux shows processes with STAT = Z.


Cause: Parent process hasn’t cleaned up child processes.


Fix: Kill/restart the parent process.

 ps -o ppid= -p <zombie_pid>
kill <parent_pid>

✅ Industry relevance: Zombies can slowly eat up system resources.

5️⃣ Scenario: Find Which Process Uses a File or Port
Symptom: You try to bind to a port but it says "already in use".


Fix:

 lsof -i :8080
kill <PID>
 Or for files:

 lsof /path/to/file

✅ Industry relevance: Common when deploying web apps — e.g., port 80 already used by Apache when you try to run Nginx.

6️⃣ Scenario: Need to Monitor Processes Continuously
Symptom: System randomly spikes in load.


Fix: Run htop for a live dashboard.

 htop

Filter by user or process name for clarity.


✅ Industry relevance: DevOps engineers often keep htop running on production servers during incidents.

🌐 Module: Networking Tools in Linux

1️⃣ Analogy – "The Postal System"
Your computer = a house.


IP address = house address (where to deliver letters).


Ping = sending a postcard to check if house exists.


Traceroute = showing the path your letter takes via different post offices.


Netstat/ss = list of doors/windows (ports) open in your house.


Nslookup = looking up someone’s house address in the directory (DNS).


👉 Networking tools = your postal inspectors to check addresses, routes, and open doors.

2️⃣ Concepts Covered
Interfaces & IPs → identify your machine on the network.


Connectivity testing → ensure communication works.


Socket statistics → see open ports & connections.


Routing paths → see how packets travel across the internet.


DNS resolution → map hostnames to IP addresses.



3️⃣ Commands & OS Differences
🔹 ifconfig / ip → Interface management
Check IP address and network interfaces:

 ifconfig
ip addr show


✅ Differences:
Ubuntu: ifconfig may not be installed by default → sudo apt install net-tools.


RHEL: Same, ifconfig in net-tools. Modern tool is ip.


macOS: ifconfig works, but no ip command.



🔹 ping → Test connectivity
Test reachability:

 ping google.com


Stop with Ctrl + C.


✅ Differences:
Ubuntu/RHEL: Continuous ping until stopped.


macOS: By default stops after sending a few packets unless -c option is used (e.g., ping -c 4 google.com).



🔹 netstat / ss → Socket statistics
Show active ports & connections:

 netstat -tulnp    # TCP/UDP listening
ss -tulnp


✅ Differences:
Ubuntu: netstat requires sudo apt install net-tools; ss is modern alternative.


RHEL: Same (ss built-in).


macOS: netstat -an works, but ss is unavailable.



🔹 traceroute → Trace network path
Show hops (routers) between you and a destination:

 traceroute google.com


✅ Differences:
Ubuntu/RHEL: May need install → sudo apt install traceroute or sudo yum install traceroute.


macOS: Built-in traceroute.



🔹 nslookup → DNS queries
Find IP of domain:

 nslookup google.com


Reverse lookup:

 nslookup 8.8.8.8


✅ Differences:
Works the same in Ubuntu, RHEL, macOS.


Alternative: dig (more detailed, often preinstalled in Linux).



4️⃣ Industry Use Cases
DevOps troubleshooting → check if app server is reachable (ping, traceroute).


Port checks → see if DB/web service is listening (ss, netstat).


DNS issues → confirm if domain resolves (nslookup, dig).


Cloud setups → check private IPs in AWS/Azure VM (ip addr).



5️⃣ Mini Activity (with Answers ✅)
Find your system’s IP address.


Answer:


Ubuntu/RHEL → ip addr show → look for inet under your interface (like 192.168.x.x).


macOS → ifconfig → look for inet.


Test connectivity to google.com with 4 pings.

 ping -c 4 google.com


Answer: Should show 4 responses with latency (ms).


Check which ports are listening on your machine.

 ss -tulnp


Answer: Lists services like SSH (22), web server (80/443).


Run a traceroute to google.com.

 traceroute google.com


Answer: Shows multiple hops (routers) from local network → ISP → Google servers.


Find the IP of openai.com.

 nslookup openai.com


Answer: Returns one or more IP addresses.



6️⃣ Troubleshooting Scenarios
Site unreachable?
 → Ping the IP. If works but domain fails → DNS issue.


Slow connection?
 → Use traceroute to see where delays happen.


App not connecting to DB?
 → Check with ss if DB is listening on correct port.


Server has no internet?
 → Check ip addr for valid IP and ping 8.8.8.8 to confirm connectivity.



🌟 Key Takeaway
ifconfig/ip → who am I on the network?


ping → can I reach someone?


netstat/ss → which doors are open?


traceroute → how do I get there?


nslookup → where is that house?


👉 Networking tools = your diagnostic toolbox for connectivity & DNS issues.

📖 Networking Tools Cheat Sheet 
(Ubuntu vs RHEL vs macOS)
Tool
Purpose
Ubuntu/Debian 🟢
RHEL/CentOS 🔴
macOS 🍎
ifconfig
Show IP/network interfaces
Not preinstalled → sudo apt install net-tools Run: ifconfig
Not preinstalled → sudo yum install net-tools Run: ifconfig
Built-in Run: ifconfig
ip
Modern replacement for ifconfig
ip addr show
ip addr show
❌ Not available
ping
Test connectivity
Continuous until stopped Example: ping google.com
Same as Ubuntu
Sends finite packets by default (use ping -c 4 google.com for 4 packets)
netstat
Show sockets, ports, connections
Needs net-tools Example: netstat -tulnp
Needs net-tools Example: netstat -tulnp
Built-in Example: netstat -an
ss
Modern socket statistics
Built-in Example: ss -tulnp
Built-in Example: ss -tulnp
❌ Not available
traceroute
Trace packet path to host
Install: sudo apt install traceroute Run: traceroute google.com
Install: sudo yum install traceroute Run: traceroute google.com
Built-in Run: traceroute google.com
nslookup
DNS lookup
Built-in Example: nslookup google.com
Built-in Example: nslookup google.com
Built-in Example: nslookup google.com
dig (alt to nslookup)
Advanced DNS lookup
sudo apt install dnsutils Example: dig google.com
sudo yum install bind-utils Example: dig google.com
❌ Not available by default (install via brew install bind)



🔥 Module: Linux Firewalls (iptables & firewalld)

1️⃣ Analogy – "The Security Guard at the Gate"
Your server = building


iptables/firewalld = security guard


Rules decide:


✅ Allow → e.g., visitors on the guest list (HTTP traffic on port 80)


❌ Block/Reject → deny unwanted visitors (bad IPs)


👉 Firewalls are traffic cops deciding who can enter/leave your system.

2️⃣ Concepts Covered
iptables → older, rule-based firewall.


firewalld → newer, zone-based (friendlier on RHEL).


ufw → simple wrapper on iptables (Ubuntu).


macOS → uses pf (Packet Filter), but we’ll highlight alternatives for mac users.



3️⃣ OS Differences
OS
Default Firewall Tool
Ubuntu/Debian 🟢
ufw (simplified iptables) + iptables available
RHEL/CentOS 🔴
firewalld (default) + iptables available
macOS 🍎
No iptables/firewalld → uses pf (Packet Filter). Students can follow logic but need Linux VM/Docker for real practice.


5️⃣ Industry Use Cases
Web server → Allow HTTP (80), HTTPS (443), block everything else.


Database server → Allow only internal traffic from app servers.


Cloud VM security → Combine Linux firewall + Cloud provider rules.


Zero-trust principle → "Default deny, allow only needed."



6️⃣ Mini Activities (with Answers ✅)
🔹 1. Check Firewall Rules
Task
Ubuntu
RHEL
macOS
Expected Output
Check firewall rules
sudo ufw status or sudo iptables -L -v -n
sudo firewall-cmd --list-all
sudo pfctl -sr
List of rules, policies (accept/drop)


🔹 2. Allow only SSH (22), block everything else
⚠️ Warning: Can lock you out if on SSH!
Task
Ubuntu (iptables)
RHEL (firewalld)
macOS (pf.conf)
Expected Output
Allow only SSH (22)
bash<br>sudo iptables -P INPUT DROP<br>sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
bash<br>sudo firewall-cmd --set-default-zone=drop<br>sudo firewall-cmd --zone=public --add-service=ssh --permanent<br>sudo firewall-cmd --reload
In /etc/pf.conf add:<br>block in all<br>pass in proto tcp from any to any port 22<br>Reload: sudo pfctl -f /etc/pf.conf && sudo pfctl -e
Only port 22 open, all other ports blocked


🔹 3. Open HTTP (80) Permanently
Task
Ubuntu
RHEL
macOS
Expected Output
Open HTTP (80)
sudo ufw allow http
bash<br>sudo firewall-cmd --zone=public --add-service=http --permanent<br>sudo firewall-cmd --reload
Add to /etc/pf.conf:pass in proto tcp from any to any port 80Reload with sudo pfctl -f /etc/pf.conf
Port 80 open for web server traffic


🔹 4. Block IP 203.0.113.5
Task
Ubuntu (iptables)
RHEL (firewalld)
macOS (pf.conf)
Expected Output
Block IP 203.0.113.5
sudo iptables -A INPUT -s 203.0.113.5 -j DROP
bash<br>sudo firewall-cmd --permanent --add-rich-rule="rule family=ipv4 source address=203.0.113.5 drop"<br>sudo firewall-cmd --reload
Add to /etc/pf.conf:block drop in quick from 203.0.113.5 to anyReload with sudo pfctl -f /etc/pf.conf
Traffic from 203.0.113.5 blocked


🔹 5. Verify Which Ports Are Open
Task
Ubuntu
RHEL
macOS
Expected Output
Verify open ports
sudo ufw status OR sudo iptables -L -n -v
sudo firewall-cmd --list-ports --list-services
`sudo lsof -i -nP
grep LISTENORnetstat -anv


7️⃣ Key Takeaways
🟢 Ubuntu → ufw (easy) or iptables (manual).


🔴 RHEL → firewalld (zones).


🍎 macOS → pf (separate, not same syntax).


Industry best practice → Default deny, allow only what you need.



🌐 Module: Network Traffic Analysis & Monitoring

1️⃣ Analogy – “Listening to Conversations at a Party”
Imagine a network like a party 🎉.


Each guest = a device.


Each conversation = network traffic (packets).


Tools like tcpdump, iftop, nload = eavesdropping (to understand who’s talking, how much, and about what).



2️⃣ Key Tools We’ll Use
tcpdump → Capture & analyze packets (like Wireshark in terminal).


iftop → Monitor bandwidth usage per connection (like top but for network).


nload → See overall incoming/outgoing traffic as simple graphs.



3️⃣ OS Differences
Tool
Ubuntu/Debian 🟢
RHEL/CentOS 🔴
macOS 🍎
tcpdump
sudo apt install tcpdump
sudo yum install tcpdump or sudo dnf install tcpdump
Pre-installed (tcpdump)
iftop
sudo apt install iftop
sudo yum install iftop
Requires brew: brew install iftop
nload
sudo apt install nload
sudo yum install nload
brew install nload


4️⃣ Hands-on Commands
🔹 1. Interface Names
OS
Common Interface Names
Example Command
Linux
eth0, ens33, wlan0 (varies by distro and network setup)
sudo tcpdump -i eth0
macOS
en0 (Ethernet), en1 (Wi-Fi)
sudo tcpdump -i en0

👉 On macOS, you can list interfaces with:
ifconfig -l


🔹 2. Using tcpdump
Task
Linux Command
macOS Command
Notes
Capture all packets
sudo tcpdump -i eth0
sudo tcpdump -i en0
Ctrl+C to stop
Capture only HTTP (port 80)
sudo tcpdump -i eth0 port 80
sudo tcpdump -i en0 port 80
Useful for web traffic
Save packets to file
sudo tcpdump -i eth0 -w capture.pcap
sudo tcpdump -i en0 -w capture.pcap
File can be opened in Wireshark
Read saved file
tcpdump -r capture.pcap
Same on macOS
Works cross-platform


🔹 3. Using iftop
⚠️ Note: iftop is not pre-installed on macOS; you’ll need Homebrew:
brew install iftop

Task
Linux Command
macOS Command
Notes
Start monitoring
sudo iftop -i eth0
sudo iftop -i en0
Shows live bandwidth per connection
Navigation
Same on both
Same on both
t = toggle display, arrows = scroll, q = quit


🔹 4. Using nload
⚠️ Note: nload is Linux-only; on macOS, you can install via Homebrew:
brew install nload

Task
Linux Command
macOS Command
Notes
Monitor traffic
sudo nload eth0
sudo nload en0
Two graphs: Incoming & Outgoing
Usage
Same on both
Same on both
Easy to detect spikes in usage


✅ Now the differences are clear:
Interface names (eth0 vs en0)


Some tools need Homebrew on macOS (iftop, nload)


Commands otherwise behave the same

5️⃣ Practical Examples
Check what happens when you open Google in your browser:


Run: sudo tcpdump -i eth0 port 443


Then open https://www.google.com


See packets being exchanged!


Find which process is using high bandwidth:


Run: sudo iftop -i eth0


Watch which IPs are sending/receiving the most data.


Monitor network spikes while downloading a large file:


Run: sudo nload eth0


Start a file download → see the graph shoot up 📈.



6️⃣ Mini Activities (with Answers ✅)
Capture only ICMP (ping) packets:

 sudo tcpdump -i eth0 icmp
 ✅ When you run ping google.com in another terminal, you’ll see ICMP traffic.


Log 100 packets into a file and analyze later:

 sudo tcpdump -i eth0 -c 100 -w test.pcap
tcpdump -r test.pcap


Find your system’s top bandwidth consumer in real-time:


Run: sudo iftop -i eth0
 ✅ The IP with the highest bandwidth usage will be at the top.


Monitor traffic rate changes:


Run: sudo nload eth0


Start playing a YouTube video.
 ✅ Incoming traffic graph will rise steadily.


Check DNS queries when visiting a new website:

 sudo tcpdump -i eth0 port 53
 ✅ You’ll see your machine asking DNS servers to resolve the domain.



7️⃣ Key Takeaways
tcpdump → fine-grained packet capture (deep inspection).


iftop → shows “who’s using bandwidth.”


nload → shows “how much bandwidth is used overall.”


DevOps engineers use these tools for:


Debugging slow apps.


Detecting unusual outbound traffic (possible malware).


Capacity planning & monitoring.




---


SEC:05_SAT

⚙️ Module: CPU & Memory Monitoring in Linux & macOS

1️⃣ Analogy – “Health Check of a Person”
CPU = brain 🧠 (thinking power).


Memory (RAM) = short-term memory 📒.


Swap = scratch paper when RAM is full.


Tools like top, htop, free/vm_stat = doctors checking vitals.



2️⃣ Tools Overview
top → real-time system & process monitoring.


htop → enhanced top (colorful, interactive).


free/vm_stat → memory + swap usage snapshot.



3️⃣ OS Differences
Tool
Ubuntu/Debian 🟢
RHEL/CentOS 🔴
macOS 🍎
top
Pre-installed, interactive shortcuts (Shift+P, Shift+M)
Same as Ubuntu
Pre-installed, BUT no interactive shortcuts — use flags (-o)
htop
sudo apt install htop
sudo yum install htop or sudo dnf install htop
brew install htop
free
Pre-installed
Pre-installed
❌ Not available. Use vm_stat or `top -l 1


4️⃣ Hands-On Commands
🔹 Monitoring with top
🟢🔴 Linux:

 top


Shift + P → sort by CPU


Shift + M → sort by memory


k → kill a process


q → quit


🍎 macOS:

 top -o cpu     # sort by CPU
top -o rsize   # sort by memory (resident memory)


No interactive sorting keys.


Use Ctrl+C to stop.



🔹 Monitoring with htop
Run:

 htop


Interactive (Linux-like on all OS).


Arrow keys to scroll, F6 to change sorting, F9 to kill process.



🔹 Checking Memory
🟢🔴 Linux:

 free -h


Mem: line = RAM usage.


Swap: line = swap usage.


🍎 macOS alternatives:

 vm_stat
# OR
top -l 1 | grep PhysMem


vm_stat shows memory pages (multiply by 4096 bytes).


top -l 1 gives a one-time snapshot (like Linux free).



5️⃣ Interpreting Output
top/htop:


%CPU → CPU usage per process.


%MEM / rsize → memory usage.


load average → 1, 5, 15 min system load (compare to CPU cores).


free/vm_stat:


available → memory free for apps.


High swap used = system struggling with RAM.



6️⃣ Practical Examples
Check which process is hogging CPU


Linux: top → press Shift+P.


macOS: top -o cpu.


Check memory usage trend


Linux: free -h.


macOS: top -l 1 | grep PhysMem.


Simulate high CPU usage

 yes > /dev/null &
top     # or htop


See the yes process consuming CPU.


Kill with kill %1.



7️⃣ Mini Activities (with Answers ✅)
Sort processes by CPU usage.


🟢🔴 Linux → run top, press Shift+P.


🍎 macOS → run top -o cpu.


Sort processes by memory usage.


🟢🔴 Linux → run top, press Shift+M.


🍎 macOS → run top -o rsize.


Check available memory in human-readable format.


🟢🔴 Linux → free -h.


🍎 macOS → top -l 1 | grep PhysMem.


Install and run htop for a colorful view.


🟢 Ubuntu → sudo apt install htop && htop


🔴 RHEL → sudo yum install htop && htop


🍎 macOS → brew install htop && htop


Explain what “load average: 6.00” means on a 4-core CPU.


✅ The system is overloaded (6 > 4).



8️⃣ Key Takeaways
Linux top = interactive shortcuts.


macOS top = use -o flags for sorting.


htop works the same everywhere — great for demos.


free (Linux) vs vm_stat/top (macOS) → different tools, same purpose.


DevOps engineers rely on these tools daily for quick performance diagnosis.



🖥️ Module: System Load, CPU Usage & Performance Metrics (Linux vs macOS)
1️⃣ Analogy – “Office Workload & Employees”
System = an office 🏢.


CPU cores = employees 👩‍💻👨‍💻.


Load average = tasks waiting for employees.


4 employees, 2 tasks → relaxed.


4 employees, 8 tasks → overloaded.


Context switching = employees constantly interrupted.


CPU usage states = what employees spend time on:


user → real work for clients.


system → office admin work.


idle → no tasks, chilling.


iowait → waiting on supplies (disk/network).



2️⃣ Checking Number of CPU Cores
OS
Command
Example Output
🟢 Ubuntu/Debian
nproc
4 (means 4 cores)
🔴 RHEL/CentOS
nproc
8
🍎 macOS
sysctl -n hw.ncpu
8

👉 Always compare load average to CPU cores.
 E.g., load avg 6.0 on a 4-core CPU = overloaded.

3️⃣ Load Average
Definition: Average number of processes waiting for CPU/I/O over 1, 5, 15 minutes.


Commands:


🟢🔴 Linux:

 uptime
top


🍎 macOS:

 uptime
top -l 1


Example:

 load average: 0.25, 0.50, 0.75
 → Lightly loaded system.

4️⃣ Context Switching
Definition: CPU switching from one process to another.


Too many = wasted cycles (like workers constantly interrupted).


Commands:


🟢🔴 Linux:

 vmstat 1 5
 → Look at cs column.


🍎 macOS:


No direct cs metric in vm_stat.


Use dtrace or install sysstat via Homebrew if needed:

 brew install sysstat
mpstat 1

5️⃣ CPU Usage Breakdown
State
Meaning
us
User processes (apps)
sy
System (kernel work)
id
Idle (free CPU)
wa
I/O wait (disk/network)
st
Steal time (in VMs, hypervisor overhead)


Commands:


🟢🔴 Linux:

 mpstat 1


🍎 macOS:

 top -l 1 | grep "CPU usage"
 Example:

 CPU usage: 25.00% user, 15.00% sys, 0.00% idle



6️⃣ I/O Wait
Definition: CPU idle but waiting on I/O (disk/network).


High %wa = disk/network bottleneck.


Commands:


🟢🔴 Linux:

 iostat -x 1 5 
 Look at await and %util.


🍎 macOS:

 brew install sysstat
iostat -w 1



7️⃣ Mini Activities (with Answers ✅)
Find out how many CPU cores your machine has.


🟢🔴 Linux → nproc


🍎 macOS → sysctl -n hw.ncpu


If load avg is 6.00 on a 2-core CPU, what does it mean?
 ✅ 2 tasks are running, 4 are waiting → overloaded.


Run vmstat 1 5 (Linux). Which column shows context switches?
 ✅ cs column.


Check CPU usage breakdown.


🟢🔴 Linux → mpstat 1


🍎 macOS → top -l 1 | grep "CPU usage"


How do you detect disk bottleneck?
 ✅ Look at %wa in top (Linux) or high iostat values.



8️⃣ Key Takeaways
Always compare load average with CPU cores.


Context switching too high → CPU is busy switching, not working.


CPU breakdown shows whether load is from apps, OS, or I/O.


I/O wait = silent bottleneck (disk/network).


macOS lacks some Linux commands → use sysctl, vm_stat, brew install sysstat for Linux-like monitoring.




⚙️ Module: Terminating & Prioritizing Processes (Linux vs macOS)
1️⃣ Analogy – “Office Rules”
Kill = firing an employee 👋.


Nice value = who gets coffee first ☕ (CPU priority).


Renice = HR reassigning priority later.


Some tasks (like backups) can be “polite” → high nice value.


Others (like serving customers) must be urgent → low nice value.



2️⃣ Terminating Processes
Using kill
Find PID (Process ID):

 ps aux | grep process_name


Kill it:

 kill <PID>       # gentle termination (SIGTERM)
kill -9 <PID>    # force kill (SIGKILL)


Using htop (easier)
Run: htop


Navigate to process with arrow keys


Press F9 → kill


👉 OS Differences:
OS
Command Availability
🟢 Ubuntu / 🔴 RHEL
ps, kill, htop all available (htop install: apt / yum)
🍎 macOS
ps, kill available by default; htop via brew install htop


3️⃣ Adjusting Process Priorities
Nice Values
Range: -20 (highest priority) → +19 (lowest priority)


Default: 0


Lower = more CPU, Higher = less CPU



Starting a Process with Nice
Example (start with lower priority):

 nice -n 10 yes > /dev/null &


Check nice value in top/htop under NI column.



Changing Priority with Renice
Find PID:

 ps aux | grep yes


Adjust priority:

 renice -n -5 -p <PID>


Verify:


🟢🔴 Linux → top or htop (NI column)


🍎 macOS → top -o cpu (shows NI values too)



4️⃣ OS Differences in Priority Commands
Command
Ubuntu/Debian 🟢
RHEL/CentOS 🔴
macOS 🍎
nice
Built-in
Built-in
Built-in
renice
Built-in
Built-in
Built-in
Viewing NI
top (Shift+P/M to sort) or htop
Same as Ubuntu
top -o cpu (NI column shown)

👉 Good news: nice and renice work the same across all OS ✅.
 The only difference is how students view NI values (Linux top/htop vs macOS top -o cpu).

🔹 Difference:
nice → used when starting a new process.
renice → used to change priority of an existing process (PID).

🔹 Key point:
renice changes the scheduler preference.
It won’t make the process hog CPU or auto-bubble to the top of the top/htop list unless it’s actively consuming resources.


5️⃣ Practical Examples
Start a CPU hog with low priority (nice 15):

 nice -n 15 yes > /dev/null &
 → Won’t slow down the system much.


Start a process with high priority (-5):

 sudo nice -n -5 yes > /dev/null &
 → Requires sudo, since lowering nice needs root.


Change running process priority:

 renice -n 5 -p <PID>
 → Makes process more polite.


Verify new priority:


Linux: top → check NI column.


macOS: top -o cpu → check NI column.



6️⃣ Mini Activities (with Answers ✅)
Start a process with nice value 10. How do you confirm it?


Run: nice -n 10 yes > /dev/null &


Linux: top → NI column = 10


macOS: top -o cpu → NI column = 10


Change the nice value of the above process to -5.


Find PID: ps aux | grep yes


Run: sudo renice -n -5 -p <PID>


Verify in top/htop.


Why is sudo needed for negative nice values?
 ✅ Because giving more priority (-5, -10, etc.) can affect system stability, only root can boost priority.


Kill the process started earlier.


kill -9 <PID> or in htop press F9.


Explain: If one process has NI=15 and another NI=-10, which one gets more CPU?
 ✅ The NI=-10 process (lower nice = higher priority).



7️⃣ Key Takeaways
kill and htop help terminate runaway processes.


nice sets priority at process start, renice changes it later.


Lower nice = higher priority (more CPU share).


sudo required for boosting priority above normal.


Works the same on Linux & macOS, only difference is viewing NI values in top.



Exercise for Students : Exercise: Linux_System_Optimization




SEC:06_SUN


Advanced System Optimization and Resource Allocation in Linux


Prometheus & Grafana installation

From old notes ….

Advanced: System optimization mechanisms
 
Index:
·      
Intro & setup: Prometheus & Grafana
·      
understanding data visualization tools.
·      
Advanced Optimization Mechanisms
·      
Deep dive into Offloading & CPU affinity
·      
Tuning Kernel Parameters (sysctl)
·      
Disk partition strategies
 
 
Using sar (System Activity Report):
 
sar (System Activity Report):
 sar is a command-line tool that collects and reports system activity information, like CPU, memory, disk I/O, and more. It helps in monitoring system performance over time, either in
real-time or from historical logs. By providing data on how the system is performing,
it helps system administrators identify performance bottlenecks.



 Analogy:
 Think of sar as a fitness tracker for your system. Just as a fitness tracker records your daily steps, heart rate, and calories burned, sar tracks your system’s activity—how much CPU,
memory, and disk your system is using. It gives you a snapshot of the system’s
health.



 



 



Prometheus:


 Prometheus is a monitoring tool designed for
long-term metrics collection. It collects time-series data and allows you to
monitor your system over weeks, months, or even years. It’s typically
paired with Grafana for data visualization. Prometheus can also trigger alerts
when predefined conditions (like resource exhaustion) are met.





 Analogy:


 Imagine Prometheus as a weather station that
collects long-term data. It doesn’t just tell you today’s temperature but
tracks the climate over months and years, so you can predict patterns (like
forecasting a storm). This helps you anticipate issues before they occur.









Commands: sar, glances.
 
Feature
Sar
Glances
Purpose
Long-term system activity reporting
 
Real-time system monitoring
 
data
Historical (stored data from past hours/days)
 
Live, real-time stats
 
metrics
CPU, memory, disk, network, etc. (historical)
 
CPU, memory, disk, network, load, processes, etc. (live)
 
configuration
Requires setup for logging historical data
 
No setup needed, real-time monitoring out-of-the-box
 
usage
Good for analyzing trends and performance over time
 
Best for immediate monitoring and troubleshooting
 
User interface
Text-based (command-line reports)
 
Interactive (text-based, but more user-friendly)
 


Then Prometheus & Grafana setup --
 
Grafana:
 
Grafana is an open-source platform for monitoring and observability, primarily used for visualizing time-series data from different sources like Prometheus.
It provides dashboards that allow you to monitor system metrics, application performance, and infrastructure health through customizable graphs, charts, and alerts.
Key Features of Grafana:
Dashboards: Grafana provides a rich set of visualizations such as graphs, charts, and tables.
Data Sources: It can connect to various databases and services, including Prometheus, InfluxDB, Elasticsearch, etc.
Alerting: Allows setting up alerts based on specific conditions, such as if a metric exceeds a threshold.
Annotations: Allows you to add markers to graphs for better understanding of system events.
Feature
Grafana
Prometheus
Purpose

Visualization and Dashboarding








Metrics collection and monitoring








Role in Monitoring








Visualizes time-series data from sources like Prometheus








Collects and stores metrics for monitoring








Data Storage








Doesn't store data, only visualizes data from other sources








Stores time-series data in its own database








Alerting








Can set up visual alerts on the dashboard








Built-in alerting with Prometheus Alertmanager








Use Case








Displays metrics, logs, and application data in a readable format







Monitors servers, applications, or systems by scraping metrics from targets
 

 
Summary:
Grafana is used for visualizing data, creating dashboards, and providing insights through graphs and charts. It can pull data from Prometheus and other sources.
Prometheus is used for monitoring and storing time-series data, primarily for metrics collection from systems and services, and it can trigger alerts when certain thresholds are crossed.
In DevOps, these tools are often used together:
Prometheus collects and stores the metrics, Grafana visualizes those metrics in an easy-to-read dashboard for better operational insights.
They are essential in observability, helping DevOps teams to proactively monitor, manage, and optimize system performance, detect issues early, and ensure uptime.
Optimizing CPU Usage (Offloading Workloads, Balancing Resources)
Concepts & Theory:
CPU Optimization:
 Optimizing CPU usage is about ensuring that the system’s CPU is being used efficiently. When the CPU is overloaded, performance degrades.
2 Techniques : CPU affinity & offloading tasks.

 Analogy:
 Optimizing CPU usage is like balancing traffic at an intersection. If too many cars (tasks) try to go through at the same time, traffic jams occur. Offloading tasks or balancing them across lanes (cores) ensures smooth flow.




CPU Affinity:
 
Analogy:
 Binding a process to a CPU core is like assigning a task to a specific worker in a factory. If the same worker handles a task repeatedly, they get better and faster over time, without the inefficiency of switching workers.
 

CPU affinity (also known as CPU Pinning) involves binding a process to a specific CPU core, allowing the process to always run on the same core. This can optimize performance, as the core becomes more familiar with the process's data.

 
Why Use CPU Affinity (CPU Pinning)?
Performance Optimization: When running high-performance applications, controlling CPU affinity can ensure the process uses specific cores and improve the execution speed.
Preventing Overload: If some cores are overloaded with too many processes, binding certain critical processes to specific cores ensures that they don't get mixed up with other tasks.
Real-Time Systems: For applications requiring low-latency and predictable performance, binding processes to specific cores can be crucial in avoiding sudden resource conflicts.



Hands-On Practical:
1. 	View CPU Usage with top or htop:
2. 	Set CPU Affinity (CPU Pinning):
o  
Command: taskset -c 0,1 <pid>
o   Sample Usage: taskset -cp 0,1 <pid_of_python_process>
Description: This binds a process to specific CPU cores (e.g., core 0 and 1, can be 1,2,3 also not limited to using 2 cores).
What to observe:
After running the command, use top to check the CPU
utilization. The process should primarily run on CPU cores 0 and 1 (instead of
being distributed across all cores).
Note: “taskset” command doesn’t run in mac, only for linux distro’s. Can use cpuset but it requires few dependencies.
 
Task Offloading:
Analogy:
 Offloading is like sending heavy lifting to a forklift instead of having people do it by hand. The forklift (GPU) can handle large loads (complex computations) much faster than people (CPU).

 The process of shifting work from one resource (like a CPU or system) to another resource (like another CPU, system, or external device) to improve performance or avoid overloading a specific resource. Can free up the CPU and increase system performance.

 Why Do We Offload Tasks?
To free up resources: By offloading tasks, you free up the main CPU (or resource) to focus on other important tasks.
Better performance: Using dedicated resources (e.g., GPUs for graphics) can greatly improve the speed and efficiency of specific operations.
Scalability: You can offload tasks to more powerful systems to scale your workload without overburdening a single system.
·   	Used-cases:
·   	Offload
file transfer to remote server using scp
·   	Offload
file storage to AWS S3
·   	Offload
HTTP requests to multiple backend servers via a load balancer
 
Task offloading Vs CPU Affinity:
 
Aspect

CPU Affinity








Task Offloading







Definition

Binds a process / task to a specific CPU core to control where it executes.








Moves a task to another resource (like a GPU, external server, or cloud) to offload the processing.







Focus

Local optimization—focuses on distributing tasks across CPU cores.








Global optimization—focuses on moving tasks to specialized resources like GPUs or remote servers.








Primary Resource








Affects only the CPU cores (restricting task execution to specific cores).








Can involve multiple resources: CPU, GPU, cloud, or external servers.








Main Use Case








Managing CPU load and ensuring a task runs efficiently on a specified core.








Offloading compute-heavy tasks to specialized hardware (e.g., GPUs) or distributed systems.







Cost

No cost, since you're only using the existing CPU cores.








May involve additional cost (e.g., using cloud resources, paying for GPU usage, etc.).







Complexity

Simpler, as it only involves setting CPU affinity via tools like taskset.







More complex, as it often involves setting up distributed systems or external resources (like cloud computing or GPUs).
 
Example

Binding a web server process to specific CPU cores using taskset.








Moving a machine learning model training task to a GPU.








 
In Summary:
CPU Affinity: Best when you want to optimize local resources (CPU cores) on a single machine without external dependencies. Task Offloading: Best when the task demands specialized resources (e.g., GPU, cloud) or when you want to offload workloads to distributed systems to scale.
 
Tuning Kernel Parameters (sysctl) for Networking and Resource Allocation

What Are Kernel Parameters? (Settings in a mobile)
So far we have only watched how a networking is run & how swap space is utilized by system via few linux commands…..but there is a way where we can go behind the scenes and make few modifications to the system….after all we are the owners to our systems right!
Kernel parameters control how the Linux kernel behaves in areas like networking, memory management, file systems, etc. These parameters are important because they determine how the system interacts with hardware and manages system resources.
Why Change Kernel Parameters?
Kernel parameters allow you to tune your system for better performance. For instance:
You may need to adjust networking parameters if your system is handling many simultaneous connections.
You may tweak memory settings if your system is running out of memory and using swap too often.
Real-Time Changes with sysctl
The sysctl command lets you change kernel parameters without rebooting. If you make changes directly in system files (e.g., /etc/sysctl.conf), they will require reboots, but sysctl allows for immediate testing and changes.

Example:
Networking parameters like net.ipv4.tcp_max_syn_backlog decide how many incoming network connections the system can handle at once.
Memory parameters like vm.swappiness control how the system uses swap space when RAM is full.
 
1. Networking Parameter: net.ipv4.tcp_max_syn_backlog
This kernel parameter controls how many TCP connections can be queued before the system rejects new requests.
Analogy: This is like a waiting room for incoming clients. If the room is full (queue is maxed), new clients (TCP connections) will be rejected. By increasing the room's capacity, more clients can wait, improving service.
2. Memory Parameter: vm.swappiness
This parameter controls how the system uses swap space when the RAM is full.
Analogy: Think of RAM as your office desk, and swap as an external storage locker. If the desk is too full, you start storing things in the locker. Lowering vm.swappiness means you prefer to keep things on your desk (RAM) rather than moving them to the locker (swap space).

Hands-On Practical:
1. Viewing Current Kernel Parameters
Command:
sysctl -a
Description: Displays all current kernel parameters.
What to observe: This will list many system parameters, including networking and memory settings. Look for net.ipv4.tcp_max_syn_backlog and vm.swappiness.
Note: These names might diff as per the kernel versions and disabled or renamed by configuration settings.
Example:
·   	net.ipv4.tcp_max_syn_backlog = 128
·   	vm.swappiness = 60
·   	To filter only above 2 parameters: “sysctl -n net.ipv4.tcp_max_syn_backlog” & “sysctl -n vm.swappiness”. [-n flag will act as a filter here!]
2. Modifying Kernel Parameters
Command:
sysctl -w net.ipv4.tcp_max_syn_backlog=1024
·   	Description: Changes the maximum TCP connection queue to 1024.
·   	What to observe: After running the command, verify if the change took place.
Check Current Value:
sysctl net.ipv4.tcp_max_syn_backlog
Expected Output:
o   net.ipv4.tcp_max_syn_backlog = 1024
3. Making Changes Persistent
Changes made using sysctl -w are temporary and will be lost after a reboot. To make them permanent:
Command: Open /etc/sysctl.conf file and add the changes.
sudo nano /etc/sysctl.conf
Add the following lines:
net.ipv4.tcp_max_syn_backlog = 1024
vm.swappiness = 10
Save the file:
Press CTRL + O to save.
Press Enter to confirm the filename.
Press CTRL + X to exit.
Command to apply changes immediately:
sudo sysctl -p
·   	Description: This will reload the configuration from /etc/sysctl.conf and apply the changes permanently.
·   	What to observe: After running this command, verify that the changes were applied successfully:
·   	sysctl net.ipv4.tcp_max_syn_backlog
·   	sysctl vm.swappiness
You should now see the updated values even after a reboot.

Key Commands Recap:
View Parameters: Use sysctl -a to see all current kernel parameters.
Modify Parameters: Use sysctl -w to change specific parameters temporarily.
Verify Changes: Use sysctl <parameter> to check if changes were applied.
Make Persistent: Edit /etc/sysctl.conf for permanent changes.
Apply Permanently: Use sudo sysctl -p to reload and apply persistent changes.
 
 
Disk Partitioning Strategies for Read-heavy vs. Write-heavy Workloads

Concepts & Theory:
 
Analogy: Think of partitioning a disk like organizing a bookshelf. If you have different types of books (data), you'd organize them in separate sections. For novels (read-heavy), you want easy access, and for textbooks (write-heavy), you want large & flexible shelves for frequent use.
 
1. 	Disk Partitioning: Disk partitioning is the process of dividing a disk into separate sections (partitions) to better manage and optimize different kinds of data or workloads, like read-heavy (lots of data retrieval) or write-heavy (lots of data writing) tasks.
 
2. 	Read-heavy Workloads:
o   Analogy: A read-heavy workload is like having a fast, easy-to-access bookshelf (SSD). Just like grabbing books quickly from the shelf, an SSD allows fast data retrieval.
 
o   Definition: These tasks often need to retrieve large amounts of data quickly. SSDs (Solid-State Drives) are ideal because they offer faster read speeds than traditional HDDs (Hard Disk Drives).
 
3. 	Write-heavy Workloads:
o   Analogy: A write-heavy workload is like constantly writing in a notebook. Over time, the pages get filled. If you write too quickly, the notebook will wear out. RAID setups act like a notebook with extra pages that get replaced quickly, providing durability and speed.
 
o   Definition: These tasks frequently modify or add data (e.g., databases or logs). To handle heavy writing, like  Storing large amounts of data or backups in the cloud.
o   they are often used for speed and data safety
Mounting: (A fundamental concept related to disks)
Analogy: Imagine your computer's hard drive is like a bookshelf (storage device). When you "mount" a bookshelf, you're essentially placing it somewhere (in your living room, or in a specific corner) so you can access the books (data) stored on it.
 
Definition: The process of making a disk or partition accessible by attaching it to the existing file system at a specific location.
 
In Simple Terms: Mounting is the process of connecting or linking a storage device (like a hard drive or USB) to the existing operating system so that the data on it becomes usable by your system.
 

Hands-On Practical: Cant execute as it might affect our system so just observe!
1. Viewing Disk Partitions
Command:
Lsblk might not be available by default sudo apt install util-linux
For mac diskutil list
·   	Description: This command lists all block devices and their partitions. It shows you the disks available and their associated partitions.
·   	What to Observe:
Look for devices like /dev/sda or /dev/sdb.
Observe partitions like /dev/sda1, /dev/sdb1, etc.
Check the mount points to ensure disks are being used properly.
Example Output:
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda  	8:0	0   50G  0 disk
├─sda1   8:1	0   50G  0 part /mnt
 
Breakdown:
sda is the disk itself (50GB).
sda1 is a partition on the sda disk (also 50GB).
MOUNTPOINT for sda1 is /mnt, meaning that sda1 is mounted at /mnt.
 
2. Creating Partitions Using fdisk
Command:
sudo fdisk /dev/sda
·   	Description: Opens the fdisk utility to partition the /dev/sda disk. From here, you can create, delete, or modify partitions.
·   	What to Observe: After entering fdisk, you'll be able to interactively create a new partition (follow on-screen prompts).
After creating a new partition, run lsblk again to confirm the new partition is visible.
Sample steps in fdisk:
2.          	Type n to create a new partition.
Follow the prompts to set partition type, start and end sectors.
Type w to save and write the changes.
3. Mounting Partitions
Command:
sudo mount /dev/sda1 /mnt
·   	Description: Mounts the newly created partition /dev/sda1 to the /mnt directory. This makes the partition accessible through /mnt for storing files or using the disk space.
·   	What to Observe:
Use the df -h command to check if the partition is mounted and available.
The df command shows the disk space usage and confirms if the partition has been mounted correctly.
Command to check mounted partitions:
df -h
Expected Output:
Filesystem  	Size  Used Avail Use% Mounted on
/dev/sda1   	50G   4G   46G   8%  /mnt

Summary:
Step
Action
Command
Description
1. View Partitions
List available disks and partitions
lsblk
Displays all disks and partitions, showing mount points and sizes.
2. Create Partition
Use fdisk to partition a disk
sudo fdisk /dev/sda
Opens fdisk to partition /dev/sda. Create a new partition interactively.
3. Mount Partition
Mount a partition to a directory
sudo mount /dev/sda1 /mnt
Mounts the newly created partition at /mnt for use.
4. Check Mounts
Verify the disk is mounted correctly
df -h
Verifies that the partition is mounted and shows available space.


Key Takeaways:
Partitioning is useful for optimizing disk performance for read-heavy or write-heavy tasks. The fdisk and mount commands help in creating partitions and making them accessible.

 


---

INDEX ::
Sat
Sun
Bash Intro, use-cases, Ex: GitHub remote connection.
Foreground & background processes - diff, commands & activity.
Structure of bash: Shebang line, assigning variables, command body & comments.
Command substitution & process substitution.
File handling: [cp, rm, touch, echo], 
File compression: [tar]
Loops (for, while, until)
String Manipulation: Awk, sed, grep
Conditionals (if, else, elif)
Small activities on - awk, sed, grep
Small activities on: [for, if, else, elif, while].
Automation scenarios
Functions and its types with activities
Project - Updating packages
Project - Automate GITHUB repo backup via bash script using functions, if, else.


Introduction to Bash and its Structure
1. Bash Intro
What is Bash?


Bash (Bourne Again Shell) is a Unix shell and command language, commonly used for command-line interfaces, automation, and scripting.
Bash allows you to interact with the system by issuing commands directly to the shell.
Bash scripting refers to writing a sequence of commands in a text file that can be executed together as a script. It is a way to automate tasks by combining multiple Linux commands and adding logic (like loops, conditionals, and variables) into a script.
In a Bash script, you can write a sequence of Linux commands along with more advanced programming constructs, such as:
Loops: for, while
Conditionals: if, else
Functions: Custom functions to encapsulate commands
Variables: Storing and manipulating data

Key Differences: Linux & Bash
Linux Commands: Individual commands that you execute one at a time in the terminal.
Bash Scripts: A sequence of Linux commands and Bash scripting elements (loops, conditionals, functions, etc.) written in a script file to automate tasks.

Why Use Bash over Cron?
Cron is a task scheduler that allows you to run commands or scripts at specific intervals.
Bash provides a way to write scripts that can execute multiple Linux commands, making complex automation tasks possible.
By combining Bash scripting with cron, you can automate repetitive tasks, handle errors, log output, and make system maintenance more efficient, all without manual intervention.
Cron and Bash Example - Automating Backups:
Let's say you want to automatically backup files every day at 3 AM. You could write a Bash script to copy files and compress them, then schedule this script with cron.
Create the Bash script (backup.sh):
ar

#!/bin/bash
# Backup script
 
BACKUP_DIR="/home/user/backups"
SOURCE_DIR="/home/user/documents"
DATE=$(date +\%Y-\%m-\%d_\%H-\%M-\%S)
 
mkdir -p "$BACKUP_DIR/$DATE"
cp -r "$SOURCE_DIR" "$BACKUP_DIR/$DATE/"
tar -czf "$BACKUP_DIR/$DATE.tar.gz" -C "$BACKUP_DIR" "$DATE"
rm -rf "$BACKUP_DIR/$DATE"
echo "Backup completed at $DATE" >> /var/log/backup.log
Schedule it with Cron: Edit the cron file to run this script at 3 AM every day:
bash
Copy
0 3 * * * /home/user/backup.sh
This sets up an automated backup system where your Bash script is executed daily at 3 AM via cron, backing up your files and logging the results.
 


Use Cases of Bash:


File management
Automating repetitive tasks
Server administration
Running commands in remote environments (e.g., GitHub remote connections)
System backups
Real World Analogy:


Think of Bash as a personal assistant in the kitchen. If you want a sandwich, you give instructions (commands) on how to make it, and the assistant (Bash) performs the actions (gathering ingredients, assembling, etc.).
2. Structure of Bash Script
Shebang Line (#!/bin/bash):


The shebang (#!/bin/bash) is the first line of the script and tells the system to use the Bash interpreter to execute the script.
Without it, the script will be executed by the default shell (e.g., /bin/sh).
Example:

 #!/bin/bash
echo "Hello, world!"


Assigning Variables:


You can assign variables using the = sign without spaces.
Example: variable_name="value"
Bash variables are case-sensitive.
name="John"
echo $name  # Outputs: John


Command Body & Comments:


Commands are the instructions that Bash will execute.
Comments are lines that start with # and are ignored during execution.
Example:
 # This is a comment
echo "Hello World"  # This prints Hello World



Practical Activity (1 Hour) - Basic Bash Script
Let’s start by writing a simple Bash script with the necessary structure.
Steps:
Create a New Bash Script:


Open your terminal.
Create a new script using the touch command:
 touch hello_world.sh


Open the file in a text editor:
 nano hello_world.sh


Add Shebang Line:


The first line of the script tells the system which interpreter to use to run the script.
Add the following:
 #!/bin/bash


Add a Simple Echo Command:


Below the shebang line, add a command to print "Hello, World!" to the terminal.
Your script should now look like this:
 #!/bin/bash
echo "Hello, World!"


Save and Exit:


Press Ctrl + X to exit, press Y to confirm saving, and hit Enter to confirm the filename.
Make the Script Executable:


In the terminal, run the following command to make the script executable:
 chmod +x hello_world.sh


Run the Script:


Now, run the script by typing:
 ./hello_world.sh


You should see the output: Hello, World!.

Hour 2: File Handling in Bash
1. File Handling Commands
cp (copy files):


The cp command copies files or directories from one location to another.
Syntax: cp source destination
Example:

 cp file1.txt file2.txt  # Copies file1.txt to file2.txt


rm (remove files):


The rm command deletes files.
Syntax: rm filename
Example:

 rm file1.txt  # Deletes file1.txt


touch (create empty file):


The touch command creates an empty file or updates the timestamp of an existing file.
Syntax: touch filename
Example:

 touch newfile.txt  # Creates an empty file called newfile.txt


echo (print output):


The echo command is used to display a line of text or variable values.
Syntax: echo "message"
Example:

 echo "Hello, world!"  # Outputs: Hello, world!


2. File Compression 
Great question 👍 Let’s demonstrate file compression using gzip, bzip2, and tar. I’ll show you step-by-step so you can try it directly on your terminal.

🔹 1. gzip → Compress individual files
gzip compresses a single file (it replaces the original file by default).
Example:
# Create a sample file
echo "This is a test file" > file1.txt

# Compress with gzip
gzip file1.txt

# Now you’ll see file1.txt.gz and the original file1.txt is gone
ls
# file1.txt.gz

# Decompress back
gunzip file1.txt.gz
ls
# file1.txt

👉 gzip works only on single files.

🔹 2. bzip2 → Stronger compression (but slower)
Similar to gzip, but gives better compression.
# Compress file
bzip2 file1.txt
ls
# file1.txt.bz2

# Decompress back
bunzip2 file1.txt.bz2
ls
# file1.txt

👉 Use bzip2 if you need smaller file size (but slower than gzip).

🔹 3. tar → Archiving (bundling multiple files/folders)
tar is used to create an archive (like .zip but without compression unless you add flags).
Archive without compression
# Create multiple files
echo "File A" > a.txt
echo "File B" > b.txt

# Create archive
tar -cf archive.tar a.txt b.txt

# List contents
tar -tf archive.tar
# a.txt
# b.txt

# Extract archive
tar -xf archive.tar


🔹 4. tar with compression (most common)
You can combine tar with gzip or bzip2.
Using gzip (.tar.gz or .tgz)
tar -czf archive.tar.gz a.txt b.txt
# -c = create, -z = gzip, -f = filename

# Extract
tar -xzf archive.tar.gz

Using bzip2 (.tar.bz2)
tar -cjf archive.tar.bz2 a.txt b.txt
# -j = bzip2

# Extract
tar -xjf archive.tar.bz2


✅ Summary
gzip file → compress one file → .gz


bzip2 file → compress one file (smaller but slower) → .bz2


tar -cf archive.tar files... → archive multiple files (no compression)


tar -czf archive.tar.gz files... → archive + gzip compression


tar -cjf archive.tar.bz2 files... → archive + bzip2 compression



What is tar?
The tar command is used for archiving files into a single compressed file.
Syntax: tar -cf archive.tar file1 file2
-c creates a new archive
-f specifies the name of the archive
-z compresses the archive using gzip
Example:
 tar -czf archive.tar.gz file1.txt file2.txt  # Creates a gzipped tarball

Practical Activity (1 Hour) - File Operations Script
Steps:
Create the Script:


Start by creating a new file for the script:
 touch file_operations.sh


Open the file in a text editor:
 nano file_operations.sh


Copy File (cp Command):


Let’s copy an existing file to a new location using cp.
Write the following code:
 #!/bin/bash
cp file1.txt file2.txt
echo "File copied!"


Remove a File (rm Command):


After copying the file, let’s delete the original file:
 rm file1.txt
echo "Original file removed!"


Create a New File (touch Command):


Let’s create a new file:
 touch newfile.txt
echo "New file created!"


Append Text with echo:


Append text into the new file using the echo command:
 echo "Hello from Bash!" >> newfile.txt
echo "Text added to new file!"


Save and Exit:


Save and exit the script as explained in the previous activity.
Make the Script Executable:


Run the following command:
 chmod +x file_operations.sh


Run the Script:


Execute the script to test:
 ./file_operations.sh


Verify Files:


Check if the new file was created and the content was appended:
 cat newfile.txt
Hands-on Activity:

Sure! Let's break this down step by step:
Objective:
Create a folder on your Desktop.
Create a file named file1.txt inside that folder and add the text: "1st content inside first file".
Create another file named file2.txt and copy the content of file1.txt into it.
Compress the folder containing both files into a .tar.gz archive.

Step-by-Step Bash Script:
Create a directory on the Desktop.
Create file1.txt inside the directory and write content into it.
Create file2.txt and copy the content from file1.txt.
Compress the folder into a .tar.gz file.
Here's the complete Bash script to achieve that:
#!/bin/bash

# Define folder and file names
folder_name="$HOME/Desktop/my_folder"
file1="$folder_name/file1.txt"
file2="$folder_name/file2.txt"
archive_name="$HOME/Desktop/my_folder_archive.tar.gz"

# Step 1: Create a folder on Desktop
mkdir -p "$folder_name"

# Step 2: Create file1.txt and add content to it
echo "1st content inside first file" > "$file1"

# Step 3: Create file2.txt and copy content from file1.txt
cp "$file1" "$file2"

# Step 4: Compress the folder into a .tar.gz archive
tar -czf "$archive_name" -C "$HOME/Desktop" "my_folder"

# Optional: Verify the result by listing the contents
echo "Created folder and compressed it into: $archive_name"”

Explanation:
Creating a Folder:


mkdir -p "$folder_name" creates the folder on your Desktop. The -p flag ensures it doesn’t fail if the folder already exists.
Creating file1.txt and Writing Content:


echo "1st content inside first file" > "$file1" writes the string into file1.txt. If the file already exists, it overwrites it.
Creating file2.txt and Copying Content:


cp "$file1" "$file2" copies the content from file1.txt to file2.txt.
Compressing the Folder:


tar -czf "$archive_name" -C "$HOME/Desktop" "my_folder" compresses the folder into a .tar.gz archive.
-c creates a new archive.
-z compresses the archive using gzip.
-f specifies the archive filename.
-C allows you to specify the path to the folder, so you can archive it without including the full path.
How to Run the Script:
Save the script as script.sh on your Desktop or any location.
Make the script executable:
 chmod +x script.sh


Run the script:
 ./script.sh


Once the script runs successfully, you should see:
A folder named my_folder on your Desktop.
Two files, file1.txt and file2.txt, inside the folder.
A compressed archive named my_folder_archive.tar.gz on your Desktop.

Hour 3: String Manipulation with awk, sed, grep
1. awk Command
What is awk?


awk is a powerful text processing tool, often used for pattern scanning and processing.
It processes text line-by-line and is particularly useful for handling structured data, like CSV files.
Basic Syntax:

 awk '{ print $1 }' file.txt  # Prints the first column of the file
 Example:

 echo -e "Name, Age, City\nJohn, 30, New York" | awk -F, '{ print $1 }'


2. sed Command
What is sed?


sed (stream editor) is used for text manipulation, like search and replace, insertion, or deletion in files.
Basic Syntax:

 sed 's/old-text/new-text/' filename  # Replaces 'old-text' with 'new-text'
 Example:

 echo "Hello World" | sed 's/World/Everyone/'


3. grep Command
What is grep?


grep is used to search for patterns in files.
Basic Syntax:

 grep "pattern" filename  # Searches for 'pattern' in the file
 Example:

 echo "Hello World" | grep "Hello"


macOS Alternative Commands:
The usage of awk, sed, and grep on macOS is the same as on Linux, so no changes are necessary here.

Comparison of awk, sed, and grep
Command
Purpose
When to Use
Example
awk
Text processing and reporting tool, particularly for structured data.
When you need to process structured data (like CSV files) or extract specific fields from text.
awk '{print $1}' file.txt
sed
Stream editor for performing basic text transformations on an input stream (file or input).
When you need to perform search-and-replace, delete lines, or modify file contents.
sed 's/old/new/g' file.txt
grep
Search utility for searching text using regular expressions.
When you need to find patterns within files or output.
grep "pattern" file.txt


DEMO: AWK - SED - GREP

Perfect! Let’s do a practical crash course on string manipulation with awk, sed, and grep.
 I’ll keep it simple, hands-on, and comparable so you can practice directly on your terminal.

🔹 1. grep → Finding and filtering
grep is for searching patterns in text.
Example file: data.txt
apple
banana
apricot
grape
pineapple

Examples
# Find lines containing 'apple'
grep "apple" data.txt
# Output:
# apple
# pineapple

# Find lines starting with 'a'
grep "^a" data.txt
# Output:
# apple
# apricot

# Case-insensitive search
grep -i "Apple" data.txt

# Count matches
grep -c "apple" data.txt

👉 Use grep when you need pattern matching and filtering.

🔹 2. sed → Stream editing
sed is for search & replace or transforming lines.
Example file: data.txt
Hello World
Hello DevOps
Hello AWS

Examples
# Replace "Hello" with "Hi"
sed 's/Hello/Hi/' data.txt
# Output:
# Hi World
# Hi DevOps
# Hi AWS

# Replace globally in each line
sed 's/o/O/g' data.txt
# Output:
# HellO WOrld
# HellO DevOps
# HellO AWS

# Delete lines containing "DevOps"
sed '/DevOps/d' data.txt

👉 Use sed when you want substitution, deletion, or transformation.

🔹 3. awk → Text processing & field extraction
awk works great with columns of text.
Example file: employees.txt
1 John 5000
2 Alice 6000
3 Bob 4500

Examples
# Print 2nd column (names)
awk '{print $2}' employees.txt
# Output:
# John
# Alice
# Bob

# Print name and salary in a formatted way
awk '{print "Name: "$2 ", Salary: "$3}' employees.txt
# Output:
# Name: John, Salary: 5000
# Name: Alice, Salary: 6000
# Name: Bob, Salary: 4500

# Filter: print only salaries > 5000
awk '$3 > 5000 {print $2, $3}' employees.txt
# Output:
# Alice 6000

👉 Use awk when you want structured extraction, filtering, or formatting.

🔹 Putting them together
# Find employees with salary > 5000 and replace name format
awk '$3 > 5000 {print $2}' employees.txt | sed 's/Alice/ALICE/' | grep "ALICE"


✅ Quick Summary
grep → search/filter text by pattern


sed → search/replace, delete, transform text


awk → extract fields, apply conditions, format output



Example: Log File Analysis for Monitoring System Health
Scenario:
As a DevOps engineer, you might need to analyze log files (e.g., system logs, application logs) to identify errors, monitor system health, or track user activity.
For instance, you could use these tools to check if the system is running out of disk space by looking at logs for specific warnings or errors.
Commands:
Using grep to find error logs: We can use grep to find all lines containing the word ERROR in a log file and extract the relevant information.
bash
CopyEdit
grep "ERROR" /var/log/syslog
Explanation:
grep "ERROR" will search for the word ERROR in the file /var/log/syslog (a typical system log).
It will return all lines that contain the word "ERROR", which can be further processed to get more details about system failures.
Using awk to extract specific fields from the logs: Once you have found error logs using grep, you may want to extract useful information (such as the timestamp, error type, etc.). Here's an example using awk:
bash
CopyEdit
grep "ERROR" /var/log/syslog | awk '{print $1, $2, $3, $5, $6}'
Explanation:
grep "ERROR" /var/log/syslog filters out the errors from the log file.
awk '{print $1, $2, $3, $5, $6}' extracts specific columns. $1, $2, and $3 are the date and time fields, and $5, $6 might represent the error message or any relevant fields (depending on your log format).
Using sed to remove sensitive information from logs before sharing: If you need to share log files with other team members or vendors but want to mask sensitive data, you can use sed to replace sensitive information (e.g., IP addresses, usernames).
bash
CopyEdit
sed 's/[0-9]\{1,3\}\([.][0-9]\{1,3\}\)\{3\}/XXX.XXX.XXX.XXX/g' /var/log/syslog

Pattern Breakdown:
[0-9]\{1,3\}: Matches 1 to 3 digits (e.g., 192.18.9.100).
([.][0-9]\{1,3\}): Matches a dot (.) followed by 1 to 3 digits (e.g., .18, .9, .100).
\{3\}: Ensures the pattern repeats 3 times, covering all sections of the IP address.
Substitution:
The IP address (e.g., 192.18.9.100) will be replaced with XXX.XXX.XXX.XXX.
Global Flag (g):
Replaces all occurrences of IP addresses throughout the file.

This sed command will find IP addresses in the log file (assuming they follow a common pattern) and replace them with XXX.XXX.XXX.XXX.
Outcome:
The awk, grep, and sed tools are used together to analyze log files, extract key information, and protect sensitive data, which is a common use case in DevOps when working with logs.


4. Practical Activity (1 Hour) - Text Processing Script
Steps:
Create the Script:


Create a new script for string manipulation:
 touch text_processing.sh


Open the file in a text editor:
 nano text_processing.sh


Use awk to Extract Columns:


Let’s use awk to extract specific columns from a file.
Example text file (create data.txt):
 Name, Age, City
John, 30, New York
Alice, 25, Los Angeles
Bob, 35, Chicago


Add the following code to your script to extract the "Name" column:
 #!/bin/bash
awk -F, '{ print $1 }' data.txt


Use sed for String Replacement:


Let’s replace "New York" with "Boston" in the data.txt file using sed:
 sed -i 's/New York/Boston/' data.txt
echo "Replaced New York with Boston!"


Use grep to Search for a Pattern:


Use grep to search for "Alice" in the file:
 grep "Alice" data.txt
echo "Searched for Alice!"


Save and Exit:


Save and exit the script.
Make the Script Executable:


Run the following command:
 chmod +x text_processing.sh


Run the Script:


Run the script to check the output:
 ./text_processing.sh


Verify File Changes:


Verify if the changes were applied in data.txt (e.g., check the replaced string):
 cat data.txt



Automation Scenarios
A DevOps engineer uses Bash extensively for automating tasks, managing servers, deploying applications, and handling infrastructure. Below are the typical daily activities where Bash scripting plays a key role:
1. Server Setup and Configuration:
Automating Server Provisioning: DevOps engineers use Bash scripts to automate the installation and configuration of software on virtual machines (VMs), cloud instances (like EC2), or on-premise servers.
Example: A script that installs and configures a web server like Nginx or Apache on a fresh machine.
Environment Configuration: Ensuring that the server is correctly configured for development, staging, or production environments.
Example: A script to set environment variables or configure security settings on the server.

2. System Monitoring and Health Checks:
Automated System Health Checks: Checking server health, disk usage, CPU load, and memory usage regularly.
Example: A Bash script runs at regular intervals (cron jobs) to check the server's disk usage and email the DevOps team if usage exceeds a threshold.
Automated Alerts: Sending notifications or alerts based on server issues, such as high CPU usage, low disk space, or service failure.
Example: A script to monitor disk space using the df command and notify if it's near full capacity.

3. Task Automation:
Automating Repetitive Tasks: Automating frequent but simple administrative tasks such as creating new user accounts, restarting services, and rotating logs.
Example: A Bash script to automate log file rotation (like logrotate) to prevent disk space issues.
Scheduled Jobs: Scheduling cron jobs to run scripts at specified times (daily backups, system updates, etc.).
Example: Automating a script to back up files every night at midnight using a cron job.

4. Software Installation and Updates:
Automating Software Installation: Installing or upgrading software on servers using package managers (apt, yum, brew, etc.).


Example: A script to automate the installation of the latest version of Docker on all nodes in the cluster.
Patching and Updates: Regularly updating system packages and patching security vulnerabilities across all servers.


Example: A script that runs apt update and apt upgrade on Linux systems to keep them up to date.

5. Version Control and Deployment:
Git Automation: Automating code deployments, managing Git repositories, and checking out branches.
Example: A Bash script that pulls the latest code from a Git repository and deploys it to the correct environment.
Continuous Integration/Continuous Deployment (CI/CD) Pipelines: Integrating with CI/CD tools (like Jenkins, GitLab CI) to automate deployment pipelines. Bash scripts often define parts of the pipeline, like testing, building, and deploying.
Example: A deployment script that runs tests, builds a Docker image, and pushes it to a container registry like DockerHub or AWS ECR.

6. Containerization and Orchestration:
Docker Management: Automating the deployment and management of Docker containers (starting, stopping, building images, etc.).
Example: A Bash script to start a Docker container, remove old containers, or clean up unused images.
Example: Automating the process of stopping and starting Docker containers across multiple hosts with Bash.
Kubernetes Cluster Management: Bash scripts are used to manage Kubernetes clusters, perform health checks on pods, and scale applications up/down.
Example: A script to check if the pods in a Kubernetes cluster are running and healthy, and restart them if necessary.

7. Cloud Infrastructure Management:
Cloud Automation: Automating cloud resource provisioning (AWS, GCP, Azure) through command-line interfaces (CLI) or APIs using Bash.


Example: A Bash script to start/stop EC2 instances or scale auto-scaling groups.
Example: Creating and managing cloud resources like databases, load balancers, or storage using aws CLI in Bash.
Infrastructure as Code (IaC): Writing and maintaining Bash scripts that work alongside IaC tools (like Terraform or CloudFormation) to provision and manage infrastructure.


Example: A script to trigger Terraform or CloudFormation stack creation or updates.

8. Security and Compliance:
User and Permission Management: Automating the process of creating users, setting permissions, and securing system access.


Example: A script to create a new user, set up SSH keys, and restrict sudo permissions.
Firewall Configuration: Configuring firewall rules and ensuring that necessary ports are open/closed according to security requirements.


Example: A Bash script to open specific ports in the server’s firewall based on the environment.

9. Backup and Disaster Recovery:
Automating Backups: Writing scripts to back up databases, application data, or server configurations regularly.


Example: A script that backs up a database nightly and stores it in a secure S3 bucket.
Automated Restore Procedures: Creating recovery scripts to restore files or systems in case of failure.


Example: A script that automatically restores the system from backup if a critical failure is detected.

10. Logging and Troubleshooting:
Log Management: Collecting, parsing, and analyzing system logs (e.g., error logs, application logs).


Example: A Bash script that parses logs for specific errors and sends an email alert if a critical issue is found.
Error Handling in Scripts: Bash scripts handle errors gracefully and log failures or important events.


Example: A script that checks for errors after running a system command and sends an alert if it fails.

11. Networking Tasks:
Automating Network Configuration: Automating IP address configuration, network interfaces, DNS, or routing configurations.


Example: A script that sets up a static IP on a server or configures DNS settings for multiple systems.
Monitoring Network Activity: Automating the monitoring of network traffic, response times, and outages.


Example: A script to check if a server is responding to ping requests and notify the team if it's unreachable.

Bash skills are essential for any DevOps engineer as they help in automating nearly every aspect of system and application management. By automating manual processes, Bash frees up time for more strategic tasks and ensures consistency and reliability across systems.

1. Practical Activity (1 Hour) - System Backup Automation Script
Steps:
Create the Backup Script:


Create a script that automates system backups:
 touch backup_script.sh


Open the script in a text editor:
 nano backup_script.sh


Write the Backup Command Using tar:


Add the following code to your script:
 #!/bin/bash
backup_folder="/backup"
current_date=$(date +%Y-%m-%d)
tar -czf $backup_folder/backup_$current_date.tar.gz /home/user/
echo "Backup completed for $current_date!"


Save and Exit:


Save and exit the script.
Make the Script Executable:


Run the following command to make the script executable:
 chmod +x backup_script.sh


Run the Backup Script:


Execute the script:
 ./backup_script.sh


Verify Backup:


Check if the backup file has been created in the /backup directory:
 ls /backup



Hour 5: Project - Updating Packages Using Bash
1. Practical Activity (1 Hour) - Automating Package Updates
Steps:
Create the Update Script:


Create a new script that updates your system’s packages automatically:
 touch update_packages.sh


Open the script in a text editor:
 nano update_packages.sh


Write the Update Commands:


For Ubuntu/Debian-based systems:

 #!/bin/bash
echo "Updating package list..."
sudo apt update
echo "Upgrading packages..."
sudo apt upgrade -y
echo "Cleaning up..."
sudo apt autoremove -y


For CentOS/RHEL-based systems, replace the above commands with:

 sudo yum update -y


Save and Exit:


Save and exit the script.
Make the Script Executable:


Run the following command to make the script executable:
 chmod +x update_packages.sh


Run the Script:


Run the script to automatically update the packages:
 ./update_packages.sh


Verify the Updates:


Check if the system has been updated by running:
 sudo apt list --upgradable  # For Ubuntu/Debian
sudo yum check-update  # For CentOS/RHEL



SUN ::

1. Foreground & Background Processes
Theory Recap:
Foreground Process: A process that is executed directly in the terminal. It is the active process that occupies the terminal until it finishes. While it is running, you can see its output in the terminal, and you need to wait for it to finish before getting back control of the terminal.
Background Process: runs in the background, meaning it doesn't take up the terminal or block your ability to execute other commands. The process runs independently, and the terminal immediately returns control to you after starting it.
Task 1: Demonstrating Foreground & Background Processes
Step-by-Step:
Open the terminal.


Run a command in the foreground:


Example: nano somefile.txt
 This opens a file in the nano editor. You cannot do anything else in the terminal until you finish editing or exit.
Pause the foreground process:


Press Ctrl+Z to pause the process. This stops it temporarily and moves it to the background.
Run a command in the background:


Example: sleep 30 &
 The sleep command will wait for 30 seconds, but the terminal is not blocked, and you can continue typing commands while it runs in the background.
List background jobs:


Use the jobs command to see a list of background tasks.
Bring the background process to the foreground:


Use the fg command. This will bring the paused job back to the foreground. If you have multiple jobs, you may need to specify the job number (e.g., fg %1).
Kill a background process:


Use the kill command to terminate a process. Example: kill %1 (replace %1 with the job number).
Expected Output:
The terminal will show you information about the job when you run the jobs command.
After using fg, you'll return to the sleep command or whatever you were running in the background.

2. Command Substitution & Process Substitution
Theory Recap:
Command Substitution: Command substitution allows you to run a command and substitute its output into another command. The output of the command is returned and used as if it were typed in directly at that spot.
Process Substitution: Process substitution allows you to use the output of a command as if it were a file. This is useful when a command expects a file as input but you want to pass the output of another command instead.
Key Differences:
Command Substitution ($()): It substitutes the output of a command into the command line. It’s like running a command and using its output directly in another command.
Process Substitution (<(command)): It allows you to treat the output of a command as a file. This is useful when commands expect file input but you want to provide the output of a command.

Task 2: Using Command and Process Substitution
Step-by-Step:
Command Substitution:
Open the terminal.


Run a command with substitution:


Example: mkdir $(date +%Y-%m-%d)
Creates a folder named as the current date.

Process Substitution:
Run a command with process substitution:


Let’s say you want to combine the output of two commands (e.g., the result of a file listing and a date) and view them together in cat:
Command:
bash
Copy
cat <(ls) <(date)
What happens:
ls lists the files in the current directory.
date prints the current date and time.
The output of both commands is combined and displayed.

Loops in Bash
Loops in Bash allow you to execute a set of commands repeatedly. Bash supports three types of loops: for, while, and until.
1. for Loop
it is generally used for iterating over a list or a range. The for loop repeats a block of code for a specific number of times or for each item in a list or range. 
Use it When you know the exact number of iterations.
Syntax:
for item in [list]
do
  # commands
done

item: A variable that will take each value in the list, one by one.
list: A list of items that will be iterated over (it can be numbers, strings, or even files).
Example 1: Simple for Loop
This script prints numbers from 1 to 5 using a for loop.
#!/bin/bash

# Simple for loop to print numbers from 1 to 5
for i in 1 2 3 4 5
do
  echo "Number: $i"
done

Explanation:
for i in 1 2 3 4 5: This loop will iterate over the list 1 2 3 4 5, and in each iteration, the variable i will take the corresponding number from the list.
echo "Number: $i": Prints the current value of i.
Step-by-Step Instructions:
Save the script as for_loop.sh.
Give it execution permissions:
 chmod +x for_loop.sh


Run the script:
 ./for_loop.sh


Expected Output:
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
Hands-On Exercise with for loop:
Exercise 1: Print numbers from 1 to 10 using a for loop:

for i in {1..10}
do
  echo $i
done

Exercise 2: Print each word from a list using a for loop:
 
for word in "apple" "banana" "cherry" "date"
do
  echo "I love $word"
done

2. while Loop
The while loop in Bash repeats a set of commands as long as a given condition is true.
Syntax:
while [ condition ]
do
  # commands
done

condition: A condition that will be checked before each iteration. If the condition is true, the loop continues; otherwise, it exits.

Example 2: Simple while Loop
This script prints numbers from 1 to 5 using a while loop.
#!/bin/bash

# Simple while loop to print numbers from 1 to 5
i=1
while [ $i -le 5 ]
do
  echo "Number: $i"
  ((i++))  # Increment i by 1
done

Explanation:
i=1: This initializes the counter variable i to 1.
while [ $i -le 5 ]: The condition checks if i is less than or equal to 5. If true, the loop executes.
echo "Number: $i": Prints the current value of i.
((i++)): Increments i by 1 after each iteration.
Step-by-Step Instructions:
Save the script as while_loop.sh.
Give it execution permissions:
 chmod +x while_loop.sh


Run the script:
 ./while_loop.sh


Expected Output:
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5

3. until Loop
The until loop in Bash is the opposite of the while loop. It repeats the set of commands until a condition is true (i.e., the loop continues as long as the condition is false).
Syntax:
until [ condition ]
do
  # commands
done

Example 3: Simple until Loop
This script prints numbers from 1 to 5 using an until loop.
#!/bin/bash

# Simple until loop to print numbers from 1 to 5
i=1
until [ $i -gt 5 ]
do
  echo "Number: $i"
  ((i++))  # Increment i by 1
done

Explanation:
i=1: Initializes the counter variable i to 1.
until [ $i -gt 5 ]: The loop continues until i is greater than 5. The condition is checked before each iteration.
echo "Number: $i": Prints the current value of i.
((i++)): Increments i by 1 after each iteration.
Step-by-Step Instructions:
Save the script as until_loop.sh.
Give it execution permissions:
 chmod +x until_loop.sh


Run the script:
 ./until_loop.sh


Expected Output:
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
Key Differences: While vs Until
while loop:
The loop keeps running as long as the condition is true.
It stops immediately when the condition becomes false.
until loop:
The loop keeps running as long as the condition is false.
It stops immediately when the condition becomes true.

Conditionals in Bash
Conditionals in Bash allow you to execute a set of commands based on whether a condition is true or false.
1. if, else, and elif
The if statement checks if a condition is true. If it is true, it executes the commands in the if block. If not, it will either skip the if block or run an else block (if defined).
if: Executes commands if the condition is true.
else: Executes commands if the if condition is false.
elif: Allows you to check multiple conditions (else if).
Syntax:
if [ condition ]; then
  # commands if condition is true
elif [ another_condition ]; then
  # commands if another_condition is true
else
  # commands if all conditions are false
fi

Example 4: Basic if, else, elif
This script checks if a number is positive, negative, or zero.
#!/bin/bash

# Read the number from the user
echo "Enter a number:"
read number

# Check if the number is positive, negative, or zero
if [ $number -gt 0 ]; then
  echo "The number is positive."
elif [ $number -lt 0 ]; then
  echo "The number is negative."
else
  echo "The number is zero."
fi

Explanation:
if [ $number -gt 0 ]: Checks if the number is greater than zero (positive).
elif [ $number -lt 0 ]: If the number is not greater than zero, it checks if it is less than zero (negative).
else: If neither condition is true, it executes the else block (the number is zero).
Step-by-Step Instructions:
Save the script as check_number.sh.
Give it execution permissions:
 chmod +x check_number.sh


Run the script and input different numbers to check the results:
 ./check_number.sh


Example Output 1 (positive number):
Enter a number:
7
The number is positive.

Example Output 2 (negative number):
Enter a number:
-4
The number is negative.

Example Output 3 (zero):
Enter a number:
0
The number is zero.
—----------------------------------------------------------------------------------------------------------------------
Task: create 3 directories on your Desktop and place 2 empty files inside each directory, using loops + conditionals.
Script: Create Directories and Files
#!/bin/bash

# Get the Desktop path of the current user
desktop_path="$HOME/Desktop"

# Loop to create 3 directories
for i in {1..3}
do
    # Define the directory name
    dir_name="Directory_$i"
    dir_path="$desktop_path/$dir_name"
    
    # Check if the directory already exists
    if [ -d "$dir_path" ]; then      //-d checks if the given path exists and is a directory.
        echo "$dir_name already exists on the Desktop."
    else
        # Create the directory
        echo "Creating $dir_name..."
        mkdir "$dir_path"
    fi

    # Loop to create 2 files inside the directory
    for j in {1..2}
    do
        # Define the file name
        file_name="file_$j.txt"
        file_path="$dir_path/$file_name"
        
        # Check if the file already exists
        if [ -f "$file_path" ]; then      //-f checks if the given path exists and is a file.
            echo "$file_name already exists in $dir_name."
        else
            # Create the file
            echo "Creating $file_name inside $dir_name..."
            touch "$file_path"
        fi
    done
done

echo "Process complete: 3 directories and 2 files have been created on the Desktop."

Summary of What’s Happening in the Script:
Outer Loop: Creates 3 directories on the Desktop (named Directory_1, Directory_2, and Directory_3).
Directory Existence Check: Before creating a directory, the script checks if it already exists using [ -d "$dir_path" ]. If it exists, it prints a message; if not, it creates the directory using mkdir.
Inner Loop: Inside each directory, it creates 2 files (file_1.txt, file_2.txt).
File Existence Check: Before creating each file, it checks if the file already exists using [ -f "$file_path" ]. If the file exists, it prints a message; if not, it creates the file using touch.
Completion Message: Once all directories and files have been processed, it prints a final completion message.

Project:  Simplified Script for Git and Python3: Conditions
the script that checks and installs Git and Python3 as per the OS.

e


Functions in Bash: Detailed Explanation
What is a Function?
A function in Bash allows you to group a series of commands together that can be executed with a single command. This helps in reusing code, organizing your script better, and making your code more modular and easier to read and maintain. Instead of writing the same set of commands multiple times, you can define a function and call it wherever needed in the script.
Why Use Functions?
Code Reusability: You define the function once, then call it whenever you need to execute the same code.
Code Organization: Functions allow you to organize code into smaller, logical blocks.
Simplifies Scripts: Complex scripts are easier to read and maintain when divided into functions.
Basic Syntax of Functions in Bash:
The general structure of a function in Bash is as follows:
function function_name() {
  # Your commands
}

Or without the function keyword:
function_name() {
  # Your commands
}

function_name: This is the name of your function, which you will call in your script to execute it.
Commands inside the function: These are the commands that will be executed when the function is called.
You can also pass arguments to a function. These arguments are variables that can be used within the function.

Task 5: Using Functions
Here’s a breakdown of how you can practice and learn Bash functions with simple examples.
Example 1: Simple Function Definition and Call
Step 1: Define a Simple Function
Let’s start with defining a basic function. This function will print a message when called.
#!/bin/bash

# Define a simple function that prints a greeting message
greet_user() {
  echo "Hello, welcome to Bash scripting!"
}

# Call the function
greet_user

Explanation:
The function greet_user doesn’t take any arguments. It simply prints a greeting message when called.
The greet_user function is called at the end of the script, which makes it print the message.
Step 2: Run the Script
Save this script as greet.sh.
Give the script execution permissions:
 chmod +x greet.sh


Run the script:
 ./greet.sh


Expected Output:
Hello, welcome to Bash scripting!

Example 2: Function with Arguments
Now, let’s define a function that accepts arguments. This function will take a name and age and print a message including those values.
Step 1: Define a Function with Arguments
#!/bin/bash

# Define a function that accepts two arguments (name and age)
greet_with_age() {
  echo "Hello, $1! You are $2 years old."
}

# Call the function with arguments
greet_with_age "John" 25

Explanation:
$1 is a special variable in Bash that refers to the first argument passed to the function.
$2 refers to the second argument.
The greet_with_age function prints a message using the values passed to it.
When calling the function greet_with_age "John" 25, John will be passed as $1 and 25 will be passed as $2.
Step 2: Run the Script
Save the script as greet_with_age.sh.
Give it execution permissions:
 chmod +x greet_with_age.sh


Run the script:
 ./greet_with_age.sh


Expected Output:
Hello, John! You are 25 years old.

Example 3: Function with Return Value (using echo)
Bash functions can return values using the echo command. These values can then be captured in variables outside the function.
Step 1: Define a Function that Returns a Value
#!/bin/bash

#Define a function that adds two numbers
add_numbers() {
  result=$(( $1 + $2 ))  #Adding the first and second arguments
  echo $result            #Output the result to be captured
}

#Capture the returned value in a variable
sum=$(add_numbers 10 15)

#Print the result
echo "The sum is: $sum"

Explanation:
The function add_numbers takes two arguments ($1 and $2), adds them, and prints the result using echo.
The echo command in the function returns the result.
We capture this returned value using the syntax sum=$(add_numbers 10 15). This stores the value of the sum in the variable sum.
Finally, we print the result outside the function.
Step 2: Run the Script
Save the script as add_numbers.sh.
Give it execution permissions:
 chmod +x add_numbers.sh


Run the script:
 ./add_numbers.sh


Expected Output:
The sum is: 25

Example 4: Function with Conditional Logic
Now let’s make a function that uses conditional logic to check whether a number is even or odd.
Step 1: Define the Function
#!/bin/bash

#Define a function to check if a number is even or odd
check_even_odd() {
  if [ $(($1 % 2)) -eq 0 ]; then
    echo "The number $1 is even."
  else
    echo "The number $1 is odd."
  fi
}

#Call the function with a number
check_even_odd 7
Explanation:
The function check_even_odd takes a number as an argument ($1).
The if condition checks if the number is even using the modulus operator (%). The modulus operator returns the remainder when divided by 2.
If the number is divisible by 2 (i.e., remainder is 0), the number is even.
If the remainder is 1, the number is odd.
Based on this condition, the script will print either "even" or "odd".
Step 2: Run the Script
Save the script as even_odd.sh.
Give it execution permissions:
 chmod +x even_odd.sh


Run the script:
 ./even_odd.sh


Expected Output:
The number 7 is odd.

Combining Everything into One Script:
To understand how to use functions along with loops & conditionals.
Here’s an example that combines everything:
#!/bin/bash

# Function to check if a number is even or odd
check_even_odd() {
  if [ $(($1 % 2)) -eq 0 ]; then
    echo "The number $1 is even."
  else
    echo "The number $1 is odd."
  fi
}

# Function to print a greeting message
greet_user() {
  echo "Hello, welcome to Bash scripting!"
}

# Function to add two numbers
add_numbers() {
  result=$(( $1 + $2 ))
  echo $result
}

# Main program
greet_user
check_even_odd 5
sum=$(add_numbers 10 20)
echo "The sum is: $sum"

Step 1: Run the script
Save the script as combined_example.sh.
Give it execution permissions:
 chmod +x combined_example.sh


Run the script:
 ./combined_example.sh



Expected Output:
Hello, welcome to Bash scripting!
The number 5 is odd.
The sum is: 30


Key Takeaways
Functions in Bash allow for code reusability, better organization, and modularity in your scripts.
Functions can take arguments (like $1, $2), which makes them flexible.
They can also return values using echo, which can be captured outside the function.
Conditional logic (like if-else) and loops can also be used inside functions, making them even more powerful.

GitHub Repo Backup Script:
This is useful for any DevOps workflow where you want to automate backups or cloning of repositories for deployment or storage purposes.

#!/bin/bash

# Function to clone or pull the GitHub repository
backup_repo() {
    repo_url=$1
    backup_dir=$2

    # Extract the repo name from the URL
    repo_name=$(basename $repo_url .git)

    # Check if the repository already exists
    if [ -d "$backup_dir/$repo_name" ]; then
        echo "Repository already exists. Pulling the latest changes..."
        cd "$backup_dir/$repo_name" && git pull
    else
        echo "Repository does not exist. Cloning it..."
        git clone "$repo_url" "$backup_dir/$repo_name"
    fi
}

# Function to create a backup of the repository
create_backup() {
    repo_path=$1
    backup_location=$2
    timestamp=$(date +%Y%m%d%H%M%S)
    backup_name=$(basename $repo_path)
    tar -czf "$backup_location/$backup_name-$timestamp.tar.gz" -C "$repo_path" .
    echo "Backup created at $backup_location/$backup_name-$timestamp.tar.gz"
}

# Main Program
echo "Enter the GitHub repository URL to backup:"
read repo_url

# Define backup location (change this to a desired path)
# On your Mac, $HOME resolves to /Users/<your-username>

backup_dir="$HOME/git_repos"         
backup_location="$HOME/backups"

# Create directories if they do not exist
mkdir -p "$backup_dir"
mkdir -p "$backup_location"

# Backup the repository
backup_repo "$repo_url" "$backup_dir"

# Create a compressed backup of the repository
create_backup "$backup_dir/$(basename $repo_url .git)" "$backup_location"

echo "Backup process completed."

How it works:
Cloning or Pulling a Repo: The script will either clone the repository if it doesn't exist locally, or pull the latest changes if it already exists.
Backup: Once the repository is cloned or updated, it compresses the repository into a .tar.gz archive and saves it in a backup folder.
Automation: You can schedule this script with a cron job to periodically back up your repositories.
Explanation of Functions:
backup_repo(): This function checks if the repository is already cloned. If it exists, it pulls the latest changes; if not, it clones the repository to the specified directory.
create_backup(): This function creates a .tar.gz compressed file of the repository's directory and saves it in the backup location with a timestamp.
Main Program: It asks the user for the GitHub repository URL, then proceeds to backup the repository, and creates a backup in the specified location.
Example of script output:
Enter the GitHub repository URL to backup:
https://github.com/example/repo.git
Repository does not exist. Cloning it...
Backup created at /home/user/backups/repo-20250215101000.tar.gz
Backup process completed.

Why is this useful in DevOps?
Automated Backups: Automating the backup of code repositories ensures that you always have a copy of the latest code, reducing the risk of data loss.
Version Control: The script uses git pull to always fetch the latest version of the code.
Backup for Deployment: Before deploying code, you can run this script to ensure you have a backup in case something goes wrong.
Schedule with Cron: You can schedule this script to run daily or weekly, keeping your repositories backed up automatically.
How to use it:
Save this script to a .sh file.
Give it execution permissions:
 chmod +x github_backup.sh


Run it:
 ./github_backup.sh


If you don't have access to services or remote resources, this can still be a helpful tool to manage and back up your GitHub repositories as part of your workflow. You can expand the script further to handle multiple repositories or more advanced backup strategies.





---

SEC:07_SAT

📘 Git Module 1: Why Version Control?

1️⃣ Real-World Analogy
Imagine working on a group project in school:
Everyone edits the same Word file.


People overwrite each other’s work.


Someone deletes a section by mistake.


You spend hours figuring out “who changed what and when?”.


👉 Without a proper system, chaos follows.
Version Control is like Google Docs for code ✨ — everyone can collaborate, track changes, and roll back mistakes.

2️⃣ Why Version Control is Important in Collaborative Development
Tracks changes: Who changed what, when, and why.


Collaboration: Multiple developers can work on the same project without conflicts.


Backup & recovery: Accidentally deleted code? Revert to an earlier version.


Branching & experimentation: Test new features without breaking the main product.


Industry standard: Every software team uses version control today.



3️⃣ Types of Version Control Systems
🖥️ 1. Local Version Control (e.g., RCS)
Changes tracked only on one computer.


Stores revisions in special files.


Problem: Only one person can really use it, no collaboration.


Analogy: A personal diary 📝 → only you see it.


🌐 2. Centralized Version Control (e.g., CVS, SVN, Perforce)
One central server stores all versions.


Developers check out code, work, then commit back to central server.


Advantage: Easy to manage.


Disadvantage: Single point of failure (if server is down, no one can work).


Analogy: A library 📚 → everyone borrows from one place.


🔀 3. Distributed Version Control (e.g., Git, Mercurial)
Every developer has a full copy of the repository on their computer.


Work offline, commit changes locally, and later sync with remote.


Advantage: Faster, no single point of failure, better branching.


Analogy: Everyone gets a full photocopy of the library 📑 → even if the main library burns down, people still have all the books.



4️⃣ Why Git is the Industry Standard
Distributed model → safe, fast, reliable.


Branching & merging → easy experimentation and teamwork.


Open-source & free → supported everywhere.


Massive ecosystem → GitHub, GitLab, Bitbucket integrate seamlessly with CI/CD pipelines.


Speed → commits, diffs, and merges are faster than older systems.


👉 That’s why almost every DevOps workflow starts with Git.

6️⃣ Mini Activities (with Answers ✅)
Q: Which type of version control stores everything on one machine only?
 ✅ Local version control (e.g., RCS).


Q: What happens if the central server in SVN goes down?
 ✅ Nobody can commit or fetch code → work is blocked.


Q: Why is Git safer than SVN?
 ✅ Because every developer has a full copy of the repository.


Activity: Run git --version on your machine. What do you see?
 ✅ Should display something like git version 2.34.1.


Activity: Run git config --list. What info do you see?
 ✅ Shows your user name, email, and other Git settings.



7️⃣ DevOps Angle 🎯
Git is the backbone of CI/CD → pipelines start by pulling code from a Git repository.


Teams use Git branching strategies (GitFlow, trunk-based) to manage releases.


Every DevOps tool (Jenkins, GitHub Actions, GitLab CI, etc.) integrates tightly with Git.




Perfect — this is the core Git concepts module where students begin to “see” Git’s power 🔥.
 I’ll make it:
Concept-driven (easy analogies)


Demo-ready (so you can show while they follow)


Visual explanations (ASCII diagrams since we can’t use slides here, but you can later convert them into slides/whiteboard drawings)


Activities with answers (so you can guide students confidently)



📘 Git Module 2: Introduction to Git Concepts

1️⃣ Git’s Role in Projects
Git is a time machine for code ⏳.


Every change is saved as a snapshot → you can rewind, fast-forward, or branch off.


In collaborative projects:


Tracks what changed, who changed it, and why.


Lets teams experiment safely without breaking main code.


Brings everyone’s work together with merges.



2️⃣ Key Concepts
🔹 Commits – Snapshots of Changes
A commit = saving your work at a moment in time.


Think of it like a save point in a video game 🎮.


Each commit has:


Unique ID (SHA hash).


Author, date, commit message.


Snapshot of changes since last commit.


Demo later: git commit -m "Added login feature"

🔹 Branches – Parallel Workstreams
A branch = a separate timeline of development.


Default branch = main (older repos = master).


Developers create branches to:


Add new features.


Fix bugs.


Experiment without affecting the main project.


Analogy: Multiple chefs cooking different dishes in separate kitchens 🍳 → they don’t mess with each other.

🔹 Merging – Bringing Work Together
Merging = combining branches back into one.


If no conflict → smooth merge.


If same file/line changed by 2 people → conflict (must resolve manually).


Analogy: Merging two different recipe versions into one cookbook 📖.

3️⃣ Visual Diagrams
Commits (Linear History)
Think of commits as checkpoints in a game 🎮.

[Commit 1] → [Commit 2] → [Commit 3]

You can always go back to an older save point.

Branching
Branches are like alternate storylines.

main:   A → B → C
                \
feature:         D → E

On main branch → commits A, B, C
On feature-1 branch → commits D, E (done separately)
👉 Work happens independently → no disturbance to the main storyline.

Merging
Merging is like combining storylines into one.
main:     C1 → C2 → C3 → M
                     \     /
feature-1:            D1 → D2

Commit M = merge commit → combines work from both branches.


After merge → main contains C1, C2, C3, D1, D2.


👉 It’s like two chefs cooking separately 🍳🍲 and then combining dishes into one buffet.

5️⃣ Mini Activities (with Answers ✅)
Q: What does a Git commit represent?
 ✅ A snapshot of project changes with a unique ID.


Q: Why do we use branches in Git?
 ✅ To isolate work (features, bug fixes, experiments) without affecting the main code.


Q: What happens if two developers change the same line and try to merge?
 ✅ A merge conflict occurs → must be resolved manually.



6️⃣ DevOps Angle 🎯
Feature branches let teams develop independently → later merged via Pull Requests (GitHub/GitLab).


Commits are audit logs → critical for debugging production issues.


Branching strategies (GitFlow, trunk-based) are standard in CI/CD pipelines.


Merge conflicts happen in real projects → learning to resolve them is a DevOps must-have skill.



📘 Git Module 3: Repositories, Commits, Branches & Merging

1️⃣ Repository Initialization vs Cloning
Initialize (git init) → Start a brand-new Git repo from scratch.
 Example: You create a new project folder.


Clone (git clone) → Copy an existing remote repo (like from GitHub).
 Example: Your team already has a repo, you want the same copy on your machine.


Demo:
# Initialize new repo
mkdir git-demo && cd git-demo
git init

# Clone an existing repo
git clone https://github.com/octocat/Hello-World.git
cd Hello-World


2️⃣ Checking Repository Status
git status

Shows:


Untracked files


Staged files (ready to commit)


Current branch


Think of it as “health check” for your repo.



3️⃣ Adding & Committing Changes
Step 1: Create/Edit a File
echo "Hello Git" > hello.txt

Step 2: Stage Changes
git add hello.txt

Prepares file for commit.


Analogy: Putting items in a shopping cart 🛒 before checkout.


Step 3: Commit Changes
git commit -m "Added hello.txt with greeting"

Commits = checkout at the cashier 🧾.


Always use meaningful commit messages (so teammates understand).



4️⃣ Branching Basics
Create a Branch
git branch feature-1

Switch to Branch
Older way:

 git checkout feature-1


Newer (recommended):

 git switch feature-1


👉 Now you’re working in parallel universe (feature-1).

5️⃣ Merging Branches
Step 1: Make changes in branch
echo "This is feature-1" >> hello.txt
git add hello.txt
git commit -m "Updated hello.txt with feature-1"

Step 2: Switch back to main
git switch main

Step 3: Merge
git merge feature-1

Git creates a merge commit (if needed).


All changes from feature-1 now exist in main.



6️⃣ Visualizing Commits & Branches
git log --oneline --graph --all

Example output:
*   9fceb02 (HEAD -> main) Merge branch 'feature-1'
|\  
| * e8b1e6d (feature-1) Updated hello.txt with feature-1
* | 1a410ef Added hello.txt with greeting

👉 Students see the ASCII tree (just like the diagrams earlier).

7️⃣ Mini Activities (with Answers ✅)
Q: How do you start a new Git repository in an empty folder?
 ✅ git init


Q: What’s the difference between git init and git clone?
 ✅ git init → start from scratch; git clone → copy existing repo.


Activity: Create a new branch called bugfix and switch to it.

 git branch bugfix
git switch bugfix


Activity: Add a new file readme.md and commit it.

 echo "# Demo Repo" > readme.md
git add readme.md
git commit -m "Added readme file"


Q: After merging, how do you confirm history visually?
 ✅ git log --oneline --graph --all



8️⃣ DevOps Angle 🎯
Repos (git clone) = source of truth in pipelines.


Branching = parallel teams (feature dev, bug fixes, hotfixes).


Merges = feature integration before deployment.


Git status/add/commit = daily developer workflow before CI/CD picks up code.



📘 Git Module 4: Git Workflow & Collaboration

1️⃣ The Typical Git Workflow
Think of Git workflow like writing a book with multiple authors:
Make changes ✍️


Edit files in your working directory.


Stage changes 🛒


Use git add to select which changes you want in the next commit.


Like putting specific chapters in the editor’s inbox.


Commit changes 🧾


git commit -m "Message" → snapshot of your changes.


A permanent entry in history.


Push changes 🚀


Send your commits to the remote repository (GitHub/GitLab).


Now teammates see your work.



2️⃣ Collaboration Workflows
🔹 Feature Branch Workflow
Developers don’t work directly on main.


Each new feature = new branch.


After testing, merge back to main.


main:     A → B → C
               \
feature:        D → E → merge


🔹 Pull Request (PR) Workflow
Common on GitHub/GitLab.


Developer pushes branch → opens a PR.


Team reviews → approves → merges.


Encourages code review + quality checks.


👉 In DevOps pipelines, merges often trigger automated tests & deployments.

3️⃣ Best Practices
✅ Write clear, meaningful commit messages:
❌ Bad: git commit -m "update"


✅ Good: git commit -m "Fix login bug: incorrect password validation"


✅ Commit small, logical chunks (not 500 lines at once).
✅ Always pull latest changes before merging.
✅ Resolve conflicts carefully → don’t just delete lines blindly.

4️⃣ Hands-On Demo
Step 1: Setup Repo
mkdir workflow-demo && cd workflow-demo
git init
echo "Line 1" > file.txt
git add file.txt
git commit -m "Initial commit with file.txt"

Step 2: Create Branch
git switch -c feature-branch
echo "Feature branch line" >> file.txt
git add file.txt
git commit -m "Added line from feature branch"

Step 3: Switch Back to Main
git switch main
echo "Main branch line" >> file.txt
git add file.txt
git commit -m "Added line from main branch"

Step 4: Merge Branch → Conflict Appears 🚨
git merge feature-branch

👉 Git will show a merge conflict in file.txt:
Line 1
<<<<<<< HEAD
Main branch line
=======
Feature branch line
>>>>>>> feature-branch


5️⃣ Resolving Merge Conflicts
Open file.txt.


Manually decide what the file should look like (keep both or choose one). Example resolution:


Line 1
Main branch line
Feature branch line

Stage the resolved file:

 git add file.txt
git commit -m "Resolved merge conflict between main and feature-branch"


✅ Conflict resolved, branches merged successfully.

6️⃣ Mini Activities (with Answers ✅)
Q: What’s the difference between staging and committing?
 ✅ Staging = selecting changes; Committing = saving a snapshot of staged changes.


Q: Why do teams prefer feature branches instead of committing to main directly?
 ✅ To avoid breaking production code and allow isolated feature development.


Activity: Create a branch called hotfix, add a change, and merge it into main.

 git switch -c hotfix
echo "Hotfix applied" >> file.txt
git add file.txt
git commit -m "Applied hotfix"
git switch main
git merge hotfix


Q: In a merge conflict, what do the <<<<<<< and >>>>>>> markers mean?
 ✅ They show the conflicting code between current branch (HEAD) and the branch being merged.


Q: What’s the advantage of a Pull Request workflow over directly merging branches?
 ✅ Code review, team discussion, automated CI/CD checks before merging.



7️⃣ DevOps Angle 🎯
Every CI/CD pipeline starts with git push → remote repo.


PRs act as gates for quality control (tests, linting, approvals).


Merge conflicts are real-world daily challenges → DevOps engineers must know how to fix them.






SEC:8_SUN

📘 Git Module 5: Branching & Merging Strategies

1️⃣ Creating & Switching Branches
Create a Branch
git branch feature-1

👉 This just creates the branch but doesn’t switch.
Switch to a Branch
git switch feature-1

(or older way)
git checkout feature-1

Shortcut: Create & Switch in one step
git switch -c feature-2   –or–    git checkout -b feature-2


2️⃣ Merging Strategies
When you merge, Git decides how to bring changes from one branch into another.

🔹 Fast-Forward Merge
A fast-forward merge happens when the branch you’re merging into (usually main) has not moved ahead since you created your feature branch.
In that case, Git doesn’t need to create a merge commit — it just moves the pointer forward.

Let’s visualize:

 — when I said diverged, I meant that the two branches (e.g., main and your feature) have different commits that don’t exist in each other.

Case 1 – No Divergence (Fast-Forward possible)
A --- B   (main)
       \
        C --- D   (feature)

Here:
main stopped at B.


feature moved forward with C and D.


👉 No commits were added to main after branching → history is in a straight line.
 So Git just moves main forward to D = fast-forward merge.

Case 2 – Diverged (Fast-Forward not possible)
A --- B --- C   (main)
       \
        D --- E   (feature)

Here:
main got commit C.


feature got commits D and E.


👉 Now both branches have unique commits. The histories diverged (they split apart).
To bring them back together, Git must:
Create a merge commit (normal merge), or


Rebase feature onto main.



🚦 Rule of Thumb:
No divergence → Git can do a fast-forward (just move the branch pointer).


Divergence → Requires a merge commit (or rebase) because you need to combine different histories.


Demo:
# Setup main branch
mkdir merge-demo && cd merge-demo
git init
echo "Line 1" > file.txt
git add file.txt
git commit -m "Initial commit"

# Create and switch to feature branch
git switch -c feature
echo "Feature work" >> file.txt
git add file.txt
git commit -m "Added feature work"

# Switch back and merge
git switch main
git merge feature

👉 This will be a fast-forward merge.
 Check with:
git log --oneline --graph --all


🔹 Three-Way Merge
Happens when both branches diverged (each has new commits).


Git creates a new merge commit.


Keeps history of parallel work.


Demo:
# From previous repo
git switch main
echo "Main branch change" >> file.txt
git add file.txt
git commit -m "Main branch update"

git switch feature
echo "Another feature change" >> file.txt
git add file.txt
git commit -m "Feature branch update"

# Now merge feature into main
git switch main
git merge feature

👉 Git will perform a three-way merge and create a merge commit.
Check with:
git log --oneline --graph --all


3️⃣ Hands-On Example Summary
Step
Command
Explanation
Create branch
git branch feature-1
Makes a new branch
Switch branch
git switch feature-1
Move to new branch
Shortcut
git switch -c feature-2
Create & switch at once
Merge (FF)
git merge feature
Moves pointer forward
Merge (3-way)
Diverged history → git merge feature
Creates a merge commit


4️⃣ Mini Activities (with Answers ✅)
Q: What’s the difference between git branch feature and git switch -c feature?
 ✅ git branch only creates the branch; git switch -c creates AND switches to it.


Activity: Create a branch test-branch, add a file test.txt, commit it, and merge back into main.

 git switch -c test-branch
echo "Testing branch" > test.txt
git add test.txt
git commit -m "Added test file"
git switch main
git merge test-branch


Q: How can you tell if a merge was fast-forward or three-way?
 ✅ git log --oneline --graph --all → fast-forward = straight line; three-way = merge commit node.


Activity: Make a commit in both main and feature branches, then merge. What type of merge occurs?
 ✅ A three-way merge with a merge commit.


Q: Why do some teams avoid fast-forward merges in real projects?
 ✅ Because FF merges hide the fact that a branch existed → teams often use --no-ff to keep branch history.



5️⃣ DevOps Angle 🎯
Feature branches allow teams to work independently.


Fast-forward merges = clean history (good for small fixes).


Three-way merges = show parallel work history (good for collaboration visibility).


CI/CD pipelines often trigger on merges, so understanding merge type matters for tracking.



📘 Git Module 6: Merge Conflicts & Resolution

1️⃣ What Causes Merge Conflicts?
Merge conflicts happen when two branches modify the same part of the same file differently, and Git doesn’t know which version to keep.
Examples:
Two developers edit the same line of code.


One developer deletes a file while another edits it.


Overlapping changes in a function, config, or README.


👉 Git is smart about merging, but it can’t guess intent when changes contradict each other.

2️⃣ Simulating a Conflict (Hands-On Demo)
Step 1: Setup repo
mkdir conflict-demo && cd conflict-demo
git init
echo "Line 1" > notes.txt
git add notes.txt
git commit -m "Initial commit"

Step 2: Create feature branch
git switch -c feature
echo "Feature branch edit" >> notes.txt
git add notes.txt
git commit -m "Edited notes.txt in feature branch"

Step 3: Switch back to main
git switch main
echo "Main branch edit" >> notes.txt
git add notes.txt
git commit -m "Edited notes.txt in main branch"

👉 Now main and feature have both modified the same file.
Step 4: Merge → Conflict appears
git merge feature

Git outputs:
CONFLICT (content): Merge conflict in notes.txt
Automatic merge failed; fix conflicts and then commit the result.


3️⃣ Resolving Conflicts
Conflict markers in notes.txt
The file will look like this:
Line 1
<<<<<<< HEAD
Main branch edit
=======
Feature branch edit
>>>>>>> feature

<<<<<<< HEAD → changes from current branch (main)


======= → divider


>>>>>>> feature → changes from the branch being merged



Manual Resolution (Command Line)
Open notes.txt in an editor.


Decide how to merge the lines. Example resolution:


Line 1
Main branch edit
Feature branch edit

Stage the resolved file:


git add notes.txt

Commit the resolution:


git commit -m "Resolved merge conflict between main and feature"

✅ Conflict resolved!

GUI Resolution (Optional for Students)
If students want, they can use:
VS Code: shows both versions with options ("Accept Current", "Accept Incoming", "Accept Both").


GitKraken / SourceTree: click-to-resolve conflicts.


This is often more visual and beginner-friendly.

4️⃣ Hands-On Activity (With Answers ✅)
Activity:
Create a repo and file demo.txt.


Add a line in main branch.


Create a branch experiment, edit the same line differently, and commit.


Edit the same line again in main and commit.


Merge experiment into main.


Resolve the conflict and commit.


Answer Walkthrough:
# Step 1
mkdir conflict-activity && cd conflict-activity
git init
echo "Original line" > demo.txt
git add demo.txt
git commit -m "Initial commit"

# Step 2
git switch -c experiment
echo "Experiment branch edit" > demo.txt
git commit -am "Edited in experiment branch"

# Step 3
git switch main
echo "Main branch edit" > demo.txt
git commit -am "Edited in main branch"

# Step 4
git merge experiment   # causes conflict

# Step 5: Resolve conflict in demo.txt
# Final content:
# Original line
# Main branch edit
# Experiment branch edit

git add demo.txt
git commit -m "Resolved conflict in demo.txt"


5️⃣ DevOps Angle 🎯
Merge conflicts are inevitable in collaborative development.


DevOps engineers often help teams resolve conflicts during CI/CD merges.


Knowing how to manually resolve conflicts ensures pipelines don’t break.



📘 Git Module 7: Remote Repositories & Collaboration

1️⃣ Why Remote Repositories Matter
Local Git = your personal copy of history.


Remote Git = shared source of truth for a team.


Collaboration happens when everyone pushes/pulls changes from the remote.


👉 Examples: GitHub, GitLab, Bitbucket.

2️⃣ Cloning a Remote Repository
git clone https://github.com/octocat/Hello-World.git

Creates a local copy of the remote repo.


By default, the remote is named origin.


Navigate into it:

 cd Hello-World



3️⃣ Pushing Changes to Remote
Make sure you’re on a branch (main, feature, etc.).


Push changes:

 git push origin main


origin → remote name


main → branch name


👉 If it’s your first push:
git push -u origin main

-u sets the upstream tracking branch, so next time you can just do git push.

4️⃣ Pulling Changes
Get changes from the remote and merge them into your branch:

 git pull origin main


👉 Equivalent to:
git fetch origin main
git merge origin/main


5️⃣ Fetching vs Pulling
Fetch: Downloads changes from remote → doesn’t merge automatically.

 git fetch origin
 Then inspect changes:

 git log origin/main


Pull: Fetch + Merge in one step.


👉 Fetch is safer when you want to review before merging.

6️⃣ Rebasing (Alternative to Merge)
Rebase = reapply your commits on top of updated branch history.
 Keeps history linear & clean, but can be tricky.
Demo:
# Update local branch with remote main
git fetch origin
git rebase origin/main

👉 This moves your local commits to the “top” of the latest main branch commits.


Git Command Comparison: Merge vs Fetch vs Pull vs Rebase
Command
Purpose (with Simple Summary)
Typical Use Case
git merge
Combine changes from one branch into another.
👉 “Mix together, keep history.”
Team collaboration where branch history should be preserved.
git fetch
Download changes from remote without merging.
👉 “Peek at what’s new, don’t touch your work yet.”
Checking remote updates before deciding how to integrate.
git pull
Fetch + Merge in one step (update your branch).
👉 “Fetch + Merge right away.”
Quickly update your local branch with remote changes.
git rebase
Reapply your commits on top of another branch.
👉 “Replay my work on top, keep it clean.”
Keeping a feature branch up to date with main before merging.


7️⃣ Hands-On Demo Workflow
Clone repo:

 git clone https://github.com/octocat/Hello-World.git
cd Hello-World


Create branch & commit:

 git switch -c feature
echo "My feature" > feature.txt
git add feature.txt
git commit -m "Added feature file"


Push branch:

 git push -u origin feature


Simulate someone else updating main (or use GitHub UI).


Pull latest main branch:

 git switch main
git pull origin main


Rebase feature on top of main:

 git switch feature
git rebase main



8️⃣ Mini Activities (with Answers ✅)
Q: What’s the difference between git clone and git init?
 ✅ git init starts a repo from scratch; git clone copies an existing remote repo.


Activity: Create a new branch experiment, add a file, and push it to remote.

 git switch -c experiment
echo "Testing remote branch" > exp.txt
git add exp.txt
git commit -m "Experiment file"
git push -u origin experiment


Q: What’s the difference between git fetch and git pull?
 ✅ Fetch = only downloads changes, Pull = fetch + merge.


Activity: Fetch changes from remote main without merging.

 git fetch origin main
git log origin/main


Q: Why do some teams prefer rebase over merge?
 ✅ Rebase creates a clean, linear history; merge preserves branching history.



9️⃣ DevOps Angle 🎯
Remote repos (GitHub/GitLab) are integrated with CI/CD pipelines.


Push triggers pipelines (build, test, deploy).


Fetch & rebase help keep branches up to date with production code.


Teams decide merge vs rebase based on project policy.



📘 Git Module 8: Git Hosting Platforms (GitHub, GitLab, Bitbucket)

1️⃣ Comparing Popular Platforms
Platform
Unique Features
Pricing
Community Support
GitHub
- Largest open-source community 🌍 - GitHub Actions (CI/CD) - Marketplace for integrations - Codespaces (cloud dev env)
Free for public & private repos Paid plans for advanced CI/CD, teams, enterprise
Extremely large — millions of repos, most active open-source hub
GitLab
- Built-in CI/CD pipelines - Issue tracking & Kanban boards - Self-hosted option (great for enterprises)
Free community edition Paid tiers for enterprise features
Strong DevOps community; more popular in enterprises than open source
Bitbucket
- Tight integration with Atlassian tools (Jira, Trello) - Supports Git & Mercurial (older) - Good for project management-heavy teams
Free for small teams (5 users) Paid plans for larger orgs
Smaller community compared to GitHub/GitLab

👉 Summary:
GitHub = Best for open-source, learning, and visibility.


GitLab = Great for enterprises with built-in CI/CD.


Bitbucket = Best if company already uses Jira/Trello.



2️⃣ Demo: Creating a Repository on GitHub
Go to github.com → Sign in.


Click New Repository.


Enter repo name → Choose Public or Private.


(Optional) Add README, license, .gitignore.


Click Create Repository.


👉 GitHub shows instructions to:
Initialize locally with git init and git remote add origin …


OR push existing local repo.



3️⃣ Forking a Repository
Fork = Make your own copy of someone else’s repo (in your account).


Used in open-source contributions.


Steps:
Visit a repo (e.g., https://github.com/octocat/Hello-World).


Click Fork (top-right).


Now you have your own copy → https://github.com/your-username/Hello-World.

5️⃣ Creating a Pull Request (PR)
👉 A Pull Request is how you propose changes to someone else’s project.
🔹 GitHub/GitLab Pull Request (PR)
A Pull Request means:


 “I made changes in my branch (maybe in my fork), and I’m requesting that you pull those changes into your branch (usually main).”



It’s not the same as the git pull command.


It’s a collaboration/review workflow on platforms like GitHub.


With a PR:


You can review code, discuss changes, and merge only when approved.


Often used when students/contributors fork → modify → send PR → you merge into main.



🔹 git pull (local Git command)
git pull = fetch changes from the remote repo + merge into your current branch.


It’s how you sync your local repo with the remote.

Workflow:
Fork + Clone the repo.


Create a new branch:

 git switch -c my-feature


Make changes, commit, and push:

 git push -u origin my-feature


Go to GitHub → Your repo → It suggests “Compare & Pull Request”.


Write a clear description and submit PR.


Repo owner reviews → Merges into main project.


Compare & Pull Request Demo:
Whenever u clone someone’s public repo > make code changes in private branch > push them, it will show “compare & PR button” in their GitHub acc.
GitHub shows Compare & PR whenever a non-default branch has differences from the default branch (main)


Can you contribute to my public repo after u clone it ?
🔹 If your repo is public:
Anyone can see and clone it:

 git clone https://github.com/you/repo.git
But they cannot push changes directly to your repo unless you explicitly give them write access.


By default:
Cloning = ✅ allowed for everyone.


Pushing = ❌ not allowed (they’ll get permission denied).



🔹 Options for students to contribute
Add them as collaborators (write access)


Go to your repo → Settings → Collaborators → Add their GitHub usernames.


Then they can git push directly.


Use fork + pull request (recommended for teaching)


Each student forks your repo (makes their own copy).


They clone their fork, make changes, then open a pull request to your main repo.


This keeps your repo clean and you can review their changes before merging.



🔹 Example workflow
Student clones:

 git clone https://github.com/you/repo.git


They create a branch, commit changes, then:


If they have write access → git push origin branch-name


If they don’t → they push to their fork, then open a pull request.


👉 So short answer:
Clone = Yes (since it’s public).


Push = No, unless you give them explicit write permissions.



6️⃣ Hands-On Activity (With Answers ✅)
Q: What’s the difference between cloning and forking?
 ✅ Clone = copy repo locally; Fork = copy repo into your GitHub account.


Activity: Fork octocat/Hello-World, clone it, create a file student.txt, commit & push, then open a PR.

 git clone https://github.com/your-username/Hello-World.git
cd Hello-World
git switch -c add-student
echo "Hello from student" > student.txt
git add student.txt
git commit -m "Added student.txt"
git push -u origin add-student
 → Go to GitHub → Open Pull Request.


Q: Why are PRs important in collaboration?
 ✅ They allow code review, discussion, testing before merging.


Activity: Create a private repo on GitHub, clone it, and push a simple file.

 echo "Private test" > private.txt
git add private.txt
git commit -m "Added private.txt"
git push -u origin main


Q: Which platform (GitHub/GitLab/Bitbucket) is best for open-source projects?
 ✅ GitHub (largest open-source community).



7️⃣ DevOps Angle 🎯
Remotes (GitHub/GitLab/Bitbucket) act as the central source of truth.


Pull Requests trigger CI/CD pipelines in most companies.


GitHub Actions, GitLab CI, Bitbucket Pipelines = all automate build/test/deploy.


Fork + PR is the industry-standard workflow for open source.



📘 Git Module 9: Git Hooks, Submodules & Subtrees

1️⃣ Git Hooks
🔹 What are Git Hooks?
Git hooks are custom scripts that Git runs when certain events happen in a repo (like commit, merge, push).


They help enforce rules, run tests, or automate actions.


Hooks live in .git/hooks/ folder.


🔹 Common Hooks
pre-commit → runs before a commit is finalized. Useful for:


Code linting (check formatting, run tests).


Preventing bad commits (like empty commit messages).


post-merge → runs after a merge. Useful for:


Updating dependencies.


Running build/test scripts automatically.



🔹 Demo: Pre-Commit Hook
Go to repo hooks folder:

 cd .git/hooks
ls
 You’ll see sample hook files (like pre-commit.sample).


Create a pre-commit script:

 nano pre-commit
 Add this simple script:

 #!/bin/bash
echo "Running pre-commit hook..."
if grep -q "TODO" *.txt; then
  echo " Commit blocked! Remove TODOs first."
  exit 1
fi


Make it executable:

 chmod +x pre-commit


Try committing with TODO inside a .txt file → Commit fails.
 Remove TODO → Commit succeeds.



🔹 Demo: Post-Merge Hook
Create .git/hooks/post-merge:

 nano .git/hooks/post-merge
 Example:

 #!/bin/bash
echo "✅ Merge completed! Running tests..."
# Simulate a test
echo "All good 🎉"


Make it executable:

 chmod +x .git/hooks/post-merge


After merging → Git runs this script automatically.



2️⃣ Git Submodules
🔹 What are Submodules?
A submodule lets you include one Git repo inside another.


Example: A project that depends on another library tracked in Git.


🔹 Adding a Submodule
# Start a new repo
mkdir superproject && cd superproject
git init

# Add a submodule
git submodule add https://github.com/octocat/Hello-World.git libs/hello
git commit -m "Added submodule"

Creates a libs/hello folder → linked to external repo.


✅ Submodules Analogy (Microsoft Office 365 Example)
Imagine Microsoft 365 as a superproject repo:
Main repo: ms-office-suite


Submodules:


word


excel


outlook


powerpoint


Each product (Word, Excel, Outlook) is its own independent repository, but all of them rely on common libraries (like authentication, UI components, storage).
With submodules, you can:


Keep Word, Excel, Outlook tracked individually.


Share common dependencies across them.


Still link them together under the main suite repo.


👉 This way, changes in Word don’t directly break Excel, but everything is tied together under the suite.
 👉 That’s exactly why DevOps teams often use submodules: to manage isolated but related products/services in a single umbrella project.

So yes ✅ you can confidently explain:
“Submodules help us manage isolated projects under one repo umbrella — like Microsoft keeping Word, Excel, Outlook as separate codebases but still bundled together in Office 365.”
✅ Important:
You don’t make direct code changes in the parent repo — it’s just a tracker.
 Do submodules automatically sync changes?
Short answer: ❌ No, submodules do not automatically sync.
Updating submodules in parent repo:
```
# Go inside the submodule and pull latest changes
cd word
git pull origin main

# Go back to parent repo
cd ..
git add word
git commit -m "Updated word submodule to latest commit"
git push origin main

```
This extra step is why submodules can be complicated — you need to remember to update submodule references in the parent repo whenever submodules change.

Commands Example
# Parent repo
git init office-suite
cd office-suite

# Add submodules
git submodule add https://github.com/company/word.git
git submodule add https://github.com/company/excel.git
git submodule add https://github.com/company/outlook.git
git submodule add https://github.com/company/powerpoint.git

# Commit submodule references
git add .
git commit -m "Added all Office submodules"

Now the parent repo tracks the submodule commits, but all development happens in the individual submodules.


Summary
Submodules = tracking tool for multiple repos under one roof.


No active development in the parent repo (optional, but usually avoided).


Keeps visibility of all code changes/PRs in one location.


DEMO of Using Git Submodule:
Here’s how you can add a submodule to your repository:
Navigate to your main repository:

 cd /path/to/main/repo

Add a submodule (e.g., a library from GitHub):

 git submodule add https://github.com/username/repository.git path/to/submodule

After adding the submodule, you’ll need to commit the change to your repository:

 git commit -m "Added submodule for library"

To clone a repository with submodules, use:

 git clone --recurse-submodules https://github.com/your/repository.git

3️⃣ Git Subtrees
🔹 What are Subtrees?
Subtree = another way to include one repo inside another.


Unlike submodules, subtree copies the code into your repo → Subtrees are an alternative where the code from each repo is copied into the parent repo, instead of being a separate-linked repo.

How is subtrees different from submodules ?
Other repos are copied into the main repo as subfolders.


You can make changes directly in the parent repo, commit, and push.


Updates from the original external repo can be pulled using git subtree pull.


Easier workflow for multi-project management in a single repo.


Example (Microsoft Suite analogy):


office-suite repo contains folders word/, excel/, outlook/ (all code inside main repo).


You can edit word/ directly, commit in office-suite, push to central repo.

🔹 Adding a Subtree
git remote add hello https://github.com/octocat/Hello-World.git
git subtree add --prefix=libs/hello hello main --squash

🔹 Updating a Subtree
git subtree pull --prefix=libs/hello hello main --squash

👉 Easier to manage than submodules, but less flexible if you need exact repo separation.

4️⃣ Hands-On Activity (With Answers ✅)
Activity: Create a pre-commit hook to block commits with empty commit messages.

 nano .git/hooks/pre-commit
 #!/bin/bash
if [ -z "$(git log -1 --pretty=%B)" ]; then
  echo "❌ Empty commit message not allowed."
  exit 1
fi
 chmod +x .git/hooks/pre-commit


Activity: Add a submodule.

 git submodule add https://github.com/octocat/Hello-World.git vendor/hello
git commit -m "Added Hello World as submodule"


Q: Difference between submodules and subtrees?
 ✅ Submodule = reference to another repo (separate clone).
 ✅ Subtree = copies repo content inside your repo (no extra clone needed).


Activity: Update submodules after cloning.

 git submodule update --init --recursive


Q: When should DevOps engineers prefer hooks?
 ✅ To enforce code quality (lint checks, tests) before code enters the repo.



5️⃣ DevOps Angle 🎯
Hooks: Automate quality checks → enforce coding standards.


Submodules: Useful when projects must stay separate (e.g., shared microservices).


Subtrees: Useful when you want all code bundled together (e.g., vendor libraries).



📘 Git Module 10: Contributing to Open Source

1️⃣ Why Contribute to Open Source
Skill Enhancement:


Work with real projects, large codebases, and professional development workflows.


Learn best practices like coding standards, pull request etiquette, and CI/CD pipelines.


Networking:


Collaborate with developers worldwide.


Gain visibility and connect with industry professionals.


Portfolio Building:


Every merged PR is a public proof of your skills.


Helps in job applications, internships, or freelance opportunities.



2️⃣ Finding Suitable Projects
Platforms: GitHub, GitLab, Bitbucket.


Tips for beginners:


Look for labels like “good first issue”, “beginner-friendly”, or “help wanted”.


Pick a language or framework you know.


Start small — documentation fixes, bug fixes, minor features.


Example:


GitHub search:

 https://github.com/search?q=good+first+issue&type=issues



3️⃣ Hands-On Activity: Fork + PR
Step 1: Fork a repository
Visit a GitHub repo (e.g., https://github.com/octocat/Hello-World).


Click Fork (top-right).


Step 2: Clone the fork locally
git clone https://github.com/your-username/Hello-World.git
cd Hello-World

Step 3: Create a new branch
git switch -c fix-typo

Step 4: Make a small change
echo "Added a line for demo" >> README.md
git add README.md
git commit -m "Fixed typo / added demo line"

Step 5: Push changes
git push -u origin fix-typo

Step 6: Open a Pull Request (PR)
Go to your fork on GitHub → Click Compare & Pull Request → Add description → Submit.


The original repo maintainer reviews and merges if approved.




5️⃣ DevOps Angle 🎯
Open source contributions teach collaborative workflows like branching, PR reviews, and CI/CD pipelines.


Helps students understand how large-scale projects manage code quality and deployment.


PR contributions are visible proof of competence in resumes and interviews.




---

Advanced Bash

1. Regular Expressions in Bash
Regular expressions (regex) are used to search for patterns in strings. In Bash, regex allows you to validate or extract specific information, like email addresses or IP addresses, from input.
1.1 Matching Email Addresses
Email validation often requires checking whether the input matches the standard email format (e.g., username@domain.com). A regex pattern is a great tool for this.
Regex:
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

Explanation:
^[a-zA-Z0-9._%+-]+: Matches the beginning of the string (^), and then looks for one or more (+) characters that can be uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), dots (.), underscores (_), percentage signs (%), plus signs (+), or hyphens (-).
@[a-zA-Z0-9.-]+: The @ symbol is mandatory. After the @, the domain part of the email can contain letters, digits, dots, and hyphens.
\.[a-zA-Z]{2,}$: Ensures the domain ends with a period (.), followed by at least two letters (e.g., .com, .org), ensuring a valid domain extension.
1.2 Matching IP Addresses
An IP address is a sequence of four numbers, each ranging from 0 to 255, separated by dots. A regular expression can validate whether an input string follows this format.
Regex:
^([0-9]{1,3}\.){3}[0-9]{1,3}$

Explanation:
^([0-9]{1,3}\.){3}: Matches the first three segments of the IP address. Each segment consists of 1 to 3 digits ([0-9]{1,3}), followed by a literal dot (\.). {3} means this pattern is repeated 3 times, handling the first three parts of the IP address.
[0-9]{1,3}$: The final part of the IP address is simply 1 to 3 digits, ensuring it ends with a valid numeric segment.
1.3 Practical Activities
Activity 1: Email Validation Script
Create a script that validates an email input using the regex pattern mentioned.
Create a file named validate_email.sh:

 #!/bin/bash
# Prompt the user for an email address
read -p "Enter email: " email

# Regular expression for validating email
regex="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Check if the input email matches the regex pattern
if [[ $email =~ $regex ]]; then
    echo "Valid email!"
else
    echo "Invalid email!"
fi


Save and run:

 chmod +x validate_email.sh  # Make the script executable
./validate_email.sh         # Run the script
 Example Outputs:


Input: alice@example.com → Output: Valid email!
Input: alice@.com → Output: Invalid email!

3. Bash Variables and Parameters
In Bash scripting, variables and parameters are essential for storing and working with data.
Variables in Bash are used to store values that can be used later in the script.
Parameters in Bash are special types of variables that can be used to pass information to scripts or functions. 
Use-cases:
Global variables are accessible throughout the script, while local variables are only accessible within the function where they are defined.
command-line arguments & parameter substitution are useful when you need to execute the same script multiple times with different inputs.
Example:
# Define a global variable
name="John"

my_function() {
    # Define a local variable inside the function
    local age=25
    echo "Age inside function: $age"
}

echo "Name outside function: $name"
my_function

Explanation:
The global variable name is accessible everywhere.
The local variable age is only accessible inside my_function.

3.2 Command-Line Arguments
Command-line arguments are passed to a script when it's executed. These arguments are stored in special variables like $1, $2, etc., and $# represents the number of arguments passed.
Example:
#!/bin/bash
# Print the first and second command-line arguments
echo "First argument: $1"
echo "Second argument: $2"

Usage:
./my_script.sh hello world

Example Output:
First argument: hello
Second argument: world


3.3 Parameter Substitution
Bash allows you to modify variable values using parameter substitution. This is useful for setting default values or modifying the content of variables.
Examples:
${var:-default}: If var is unset or null, use default.
${var#pattern}: Removes the shortest match of pattern from the beginning of $var.
${var%pattern}: Removes the shortest match of pattern from the end of $var.
Example:
# Default value if no argument is passed
name=${1:-"Guest"}  
echo "Hello, $name!"

Usage:
./greet.sh Alice  # Output: Hello, Alice!
./greet.sh        # Output: Hello, Guest!


3.4 Practical Activities
Activity 3: Command-Line Argument Processing
Create a script greet.sh:

 #!/bin/bash
# Default to "Guest" if no argument is passed
name=${1:-"Guest"}
echo "Hello, $name!"


Save and run:

 chmod +x greet.sh
./greet.sh Alice  # Output: Hello, Alice!
./greet.sh        # Output: Hello, Guest!

Script: command-line arguments & parameter substitution, local & global variables.
#!/bin/bash

# Define a global variable
Middle_Name="Anees"

# Function using local variables and command-line arguments
my_function() {
    # Define a local variable inside the function
    age=$1  # Command-line argument passed to the function
    echo "My Age: $age"
}

# Use parameter substitution to assign a default value to the age variable if not passed
age_input=${1:-25}  # If no command-line argument is provided, default age to 25

# Print global variable
echo "My Name is: $Middle_Name"

# Call the function with the command-line argument
my_function "$age_input"

# Example of parameter substitution for the name
echo "Full Name: ${Middle_Name:-Unknown}"

Explanation of Changes:
Global Variable (Middle_Name):


Middle_Name="Anees" remains the same and is a global variable. It is printed to show how global variables can be accessed outside functions.
Command-Line Arguments:


$1 is used to capture the first command-line argument passed to the script. In this example, it is used to set the age inside the function (age=$1).
If no command-line argument is passed, a default value of 25 is assigned to age_input using parameter substitution:
 age_input=${1:-25}
 This means if $1 is not provided (empty), age_input will default to 25.
Local Variable (age):


Inside the my_function, the age is assigned from the command-line argument ($1), making it a local variable.
Parameter Substitution:


In the line age_input=${1:-25}, if $1 (the first command-line argument) is empty or not provided, it assigns the default value of 25 to age_input.
Another example of parameter substitution is Full Name: ${Middle_Name:-Unknown}, which will print the value of Middle_Name, but if Middle_Name were unset or empty, it would print Unknown.
How to Run the Script:
Save the script as variables_with_args.sh.
Give it execution permissions:
 chmod +x variables_with_args.sh


Run the script with or without command-line arguments:
With a command-line argument (e.g., passing an age of 30):
 ./variables_with_args.sh 30


Without a command-line argument (it will default to 25):
 ./variables_with_args.sh


Example Outputs:
With Command-Line Argument (./variables_with_args.sh 30):

 My Name is: Anees
My Age: 30
Full Name: Anees


Without Command-Line Argument (./variables_with_args.sh):

 My Name is: Anees
My Age: 25
Full Name: Anees

RECAP of LOOPS< CONDITIONALS<FUNCTIONS
2. Arrays and Associative Arrays in Bash
Analogy::
A real-world analogy for arrays can be likened to a row of mailboxes.
Example: Mailboxes
Imagine you live in an apartment building with a long row of mailboxes, where each mailbox represents a "slot" in an array. Here's how the analogy works:
Array as Mailbox Row: The row of mailboxes is like an array in programming. It holds multiple individual mailboxes (data elements) in a specific order.
Indexing (Accessing Items): Each mailbox has a number or label (like 0, 1, 2, 3, etc.) that helps you locate a specific mailbox. In an array, each item also has an index number that allows you to access it directly (e.g., array[0] to access the first item).
Same Type of Content: In this analogy, all the mailboxes could hold letters, and similarly, in an array, all the elements usually hold the same type of data (like integers, strings, etc.).
Fixed Size: The row of mailboxes is a fixed length. Once it's built, you can't change the number of mailboxes easily. Similarly, an array has a fixed size when it is created.
Accessing Mail (Data): To get the mail (data) from a specific mailbox (index), you need to know which mailbox you're looking for. If you want to check the contents of the mailbox labeled "3", you open that specific one. Similarly, you access array elements by specifying their index.
Key Points:
Arrays have a fixed size (like a fixed number of mailboxes in a row).
Each element in an array can be accessed individually using an index (like opening a specific mailbox).
Arrays store multiple items of the same type (like storing only letters in all mailboxes).

Bash arrays allow you to store multiple values in a single variable. They can be indexed (numeric) or associative (string keys).
2.1 Indexed Arrays
An indexed array stores multiple elements by numeric index, starting from 0.




Example:
# Define an indexed array
fruits=("apple" "banana" "cherry")

# Access elements of the array
echo ${fruits[0]}  # Output: apple
echo ${fruits[1]}  # Output: banana
echo ${fruits[2]}  # Output: cherry

Explanation:
fruits=("apple" "banana" "cherry"): An array named fruits is created with three elements.
${fruits[0]}: The first element (apple) is accessed using index 0.
Similarly, ${fruits[1]} retrieves banana, and ${fruits[2]} retrieves cherry.

2.2 Associative Arrays
An associative array stores values using keys, which can be strings instead of numbers.
Associative arrays are particularly useful in cases where the values need to be dynamic or vary based on specific conditions. This flexibility allows you to map each key (e.g., a directory or service) to a value that can change or be more complex, such as backup destinations, configurations, or options.
Example:
# Declare an associative array
declare -A person

# Assign values to keys
person["name"]="Alice"
person["age"]=30

# Access values using keys
echo ${person["name"]}  # Output: Alice
echo ${person["age"]}   # Output: 30

Explanation:
declare -A person: Declares an associative array named person.
person["name"]="Alice" assigns the value "Alice" to the key "name".
To access the value associated with a key, you use ${person["name"]}.

2.3 Practical Activities
Activity 2: Storing Configuration Values with Associative Arrays
You can use associative arrays to store key-value pairs, like configuration settings for a program.
Create a script config.sh:

 #!/bin/bash
# Declare an associative array for configuration
declare -A config

# Assign values to configuration keys
config["hostname"]="localhost"
config["port"]="8080"
config["username"]="admin"

# Display the configuration values
echo "Hostname: ${config["hostname"]}"
echo "Port: ${config["port"]}"
echo "Username: ${config["username"]}"


Save and run:

 chmod +x config.sh  # Make the script executable
./config.sh         # Run the script
 Example Output:

 Hostname: localhost
Port: 8080
Username: admin


Polishing ur Bash Scripts
Refactoring & modular scripting with functions:
Modular scripting and script refactoring are two concepts that are often used in Bash scripting (and other programming languages) to improve the structure and readability of scripts, but they focus on different goals and approaches. 
Here's a detailed breakdown of each term and how they differ: 
6. Script Refactoring
Script refactoring improves the readability and maintainability of your code by making it more modular and efficient.

To make your Bash scripts more robust and fail-safe, you can use:
set -e
set -u
set -o pipefail

🔧 Where to use it?
You should place these lines at the very top of your Bash script, right after the shebang (#!/bin/bash), like this:
#!/bin/bash
set -euo pipefail

This is a shorthand for:
set -e     # Exit immediately if a command exits with a non-zero status
set -u     # Treat unset variables as an error and exit immediately
set -o pipefail  # Return the exit code of the first failed command in a pipeline


💡 Why Use These?
Option
Description
set -e
Makes the script exit if any command fails. Helps avoid continuing in a broken state.
set -u
Causes the script to exit when trying to use an undefined variable. Good for catching typos or logic errors.
set -o pipefail
Ensures that a failure in any part of a pipeline causes the script to fail, not just the last command.


🧪 Example Without vs With
Without:
#!/bin/bash
output=$(grep "foo" file.txt | awk '{ print $2 }')
echo "Done"

Even if grep fails (e.g., file.txt doesn't exist), the script continues.
With:
#!/bin/bash
set -euo pipefail
output=$(grep "foo" file.txt | awk '{ print $2 }')
echo "Done"

Now, if file.txt doesn't exist or grep fails, the script exits immediately.

7. Modular Scripting with Functions
Modular scripting involves breaking down a script into smaller, reusable functions. This makes the script easier to maintain, read, and debug. Functions allow for the separation of concerns, where each function performs a specific task. By organizing code into functions, you also avoid 

ALL_IN_ONE PROJECT: Bash: Functions, arrays, loops & conditionals


SUN::
Introduction to Python
Why Python is a Popular Choice in DevOps
Python’s simplicity and versatility have made it a favorite choice in the DevOps world. It allows teams to efficiently automate tasks, manage infrastructure, and integrate services, making complex workflows more manageable. 
Python is a popular programming language in DevOps because it's easy to learn and can automate many tasks. It's widely used in making complex workflows more manageable, manage servers, automate processes, and handle cloud services, which are important in DevOps.
Here’s why Python stands out:
Automation: Python excels at automating repetitive tasks, such as file manipulation, service monitoring, and server provisioning. For instance, automating the process of creating backups or rolling out updates can be done with a few lines of Python code.


Example: A script that automatically pulls the latest code from GitHub and deploys it on a server. You can automate this process by writing a Python script that interacts with Git and deploys the code after each update.
Infrastructure Management: Python allows DevOps teams to manage their infrastructure as code, which improves efficiency and reduces human errors. Popular tools like Ansible, Terraform, and CloudFormation are all Python-based or integrate seamlessly with Python.


Example: Automating the process of configuring virtual machines in AWS or provisioning new servers across various cloud providers using Python scripts and cloud SDKs.
CI/CD Pipelines: Python simplifies the automation of Continuous Integration and Continuous Deployment (CI/CD). Python scripts can be integrated into build systems like Jenkins or GitLab to trigger testing, building, and deployment pipelines automatically.


Example: A Python script that interacts with Jenkins to trigger a build and deployment once new code is pushed to a repository, reducing the manual steps and potential errors in the process.
Integration with Cloud Platforms and APIs: Python is well-suited for interacting with APIs and cloud services. The Boto3 library for AWS allows developers to create and manage resources in the cloud, making it a key tool for DevOps tasks in cloud environments.


Example: A Python script to launch EC2 instances, configure S3 buckets, and manage AWS IAM roles automatically, all using Python’s easy-to-use API interactions.

Python-based DevOps Tools
Ansible: Ansible is an IT automation tool written in Python. It allows you to automate configuration management, application deployment, and task orchestration.


Example: Using Ansible to automate the installation of software packages or configurations across multiple servers. Python underpins the core of Ansible, enabling scripting and module creation.
AWS Boto3: Python’s Boto3 library makes it easy to interact with Amazon Web Services (AWS) APIs, enabling DevOps teams to automate resource management in AWS.


Example: Using Python to automate the creation of S3 buckets or managing EC2 instances, checking their status, and updating configurations like instance sizes, types, and security settings.
Terraform: While Terraform itself is language-agnostic, Python is often used to automate processes surrounding Terraform, such as running deployment scripts, triggering Terraform commands, and managing configurations.


Example: Automating the process of provisioning infrastructure using Python scripts that trigger Terraform commands based on predefined parameters or events.
Other Python-based DevOps Tools: Python is integrated into other tools like SaltStack for configuration management and Fabric for deployment automation. These tools allow Python scripts to handle tasks such as multi-server orchestration and automated environment setups.


Example: Using Python to automate server setup across different environments with SaltStack or Fabric by writing Python scripts that call these tools’ APIs to apply configurations.

Scenarios Where Python Simplifies Repetitive or Complex Tasks in DevOps
Python is highly effective for simplifying complex tasks like infrastructure provisioning, service monitoring, and error handling. Here are some examples of how Python streamlines DevOps workflows:
Automating Deployment: Python scripts can be used to automate application deployment, reducing manual errors and speeding up deployment times. This is especially helpful in a CI/CD pipeline to ensure quick and error-free updates.


Example: A Python script that pulls the latest code from a Git repository and updates a running application on a server. It could also run tests before deploying the new version.
Infrastructure Automation: Python enables automation of infrastructure provisioning, which saves time and ensures consistency in the setup. For example, Python can interact with cloud providers to automatically launch, configure, and manage virtual machines, storage, and networking.


Example: Using Boto3 to create an EC2 instance on AWS and automatically configure security groups and IAM roles, ensuring a consistent and secure environment setup.
Monitoring and Alerts: Python is commonly used to create monitoring scripts that check server health, disk space, or application uptime. It can also be used to send alerts or notifications when an issue arises.


Example: A Python script that pings servers every 5 minutes and sends an email notification if a server is down or reaches a critical threshold for resources like CPU usage.

Introduction to Python: Syntax, Data Types, Variables, Operators
Python Syntax and Simplicity
Python's syntax is clean and easy to understand, making it an ideal language for DevOps tasks. The absence of semicolons and braces (using indentation instead) enhances readability and reduces code complexity, allowing DevOps engineers to write more efficient scripts with fewer mistakes.

Python Data Types & Collections:
In Python, data types are the different kinds of values that can be stored in a variable, while collections are ways to store multiple values together. Here's a simple breakdown:
Basic Data Types in Python
int (Integer): Whole numbers, positive or negative, without a decimal point.


Example: age = 30
float (Floating-point number): Numbers with a decimal point.


Example: price = 19.99
str (String): A sequence of characters, used for text.


Example: name = "Alice"
bool (Boolean): A type that can be either True or False.


Example: is_active = True

Collections in Python
Collections allow you to store multiple values in a single variable. These are more complex data types that group together several values.
list: An ordered collection of items that can be changed (mutable). Lists can hold different types of data.


Example:
 fruits = ["apple", "banana", "cherry"]


tuple: An ordered collection of items, but unlike a list, tuples are immutable (unchangeable after creation).


Example:
 colors = ("red", "green", "blue")


set: An unordered collection of unique items. It doesn’t allow duplicate values.


Example:
 numbers = {1, 2, 3, 4}


dict (Dictionary): A collection of key-value pairs, where each key is unique.


Example:
 person = {"name": "John", "age": 25}



Summary
Data Types: Single values like numbers, text, and True/False.
Collections: Group multiple values together using lists, tuples, sets, and dictionaries.
These data types and collections are essential for working with different kinds of information in Python.


Variables and Assignment Rules
In Python, variables are assigned without the need for explicit type declarations. Python automatically determines the type based on the assigned value.
age = 30         # int
price = 19.99    # float
name = "John"    # str
is_active = True # bool


Operators in Python


1. Arithmetic Operators
Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, division, etc. These are essential in DevOps when you’re automating tasks that involve calculations, such as resource allocation, load balancing, or disk space management.
Common Arithmetic Operators:
+ (Addition): Adds two values.
- (Subtraction): Subtracts one value from another.
* (Multiplication): Multiplies two values.
/ (Division): Divides one value by another.
// (Floor Division): Divides and returns the largest integer smaller than the result.
% (Modulo): Returns the remainder of the division.
** (Exponentiation): Raises a number to the power of another number.
Examples:
# Addition
a = 10
b = 5
sum_result = a + b  # Result: 15
print("Sum:", sum_result)

# Subtraction
diff_result = a - b  # Result: 5
print("Difference:", diff_result)

# Multiplication
product_result = a * b  # Result: 50
print("Product:", product_result)

# Division
division_result = a / b  # Result: 2.0
print("Division:", division_result)

# Floor Division
floor_result = a // b  # Result: 2 (returns the integer part)
print("Floor Division:", floor_result)

# Modulo (Remainder)
mod_result = a % b  # Result: 0 (remainder of 10 divided by 5)
print("Modulo:", mod_result)

# Exponentiation (Power)
exp_result = a ** b  # Result: 100000 (10 raised to the power of 5)
print("Exponentiation:", exp_result)


2. Comparison Operators
Comparison operators are used to compare two values. These are particularly useful in DevOps automation to check whether certain conditions are met (e.g., if a server is online, if a resource usage is within limits, etc.).
Common Comparison Operators:
== (Equal to): Checks if two values are equal.
!= (Not equal to): Checks if two values are not equal.
> (Greater than): Checks if the left value is greater than the right.
< (Less than): Checks if the left value is less than the right.
>= (Greater than or equal to): Checks if the left value is greater than or equal to the right.
<= (Less than or equal to): Checks if the left value is less than or equal to the right.
Examples:
# Equal to
x = 10
y = 20
print(x == y)  # Result: False, because 10 is not equal to 20

# Not equal to
print(x != y)  # Result: True, because 10 is not equal to 20

# Greater than
print(x > y)  # Result: False, because 10 is not greater than 20

# Less than
print(x < y)  # Result: True, because 10 is less than 20

# Greater than or equal to
print(x >= y)  # Result: False, because 10 is not greater than or equal to 20

# Less than or equal to
print(x <= y)  # Result: True, because 10 is less than or equal to 20

These comparison operators are useful for tasks like checking if a server’s CPU usage exceeds a certain limit, or if a backup was successfully completed.

3. Logical Operators
Logical operators are used to combine conditional statements. They help to build complex conditions that control the flow of your code. For example, in a DevOps pipeline, you might want to check if two conditions are true before deploying a new update.
Common Logical Operators:
and: Returns True if both conditions are true.
or: Returns True if at least one condition is true.
not: Reverses the logical state of the condition.
Examples:
# And operator: Both conditions must be true
a = 5
b = 10
c = 15
print(a < b and b < c)  # Result: True, because both conditions (a < b and b < c) are true

# Or operator: At least one condition must be true
print(a < b or b > c)  # Result: True, because the first condition (a < b) is true, even though the second is false

# Not operator: Reverses the condition
print(not(a < b))  # Result: False, because a < b is true, and not reverses it

These operators are especially useful for more complex conditions like "If server is up and the backup has been completed."

4. Assignment Operators
Assignment operators are used to assign values to variables. They are commonly used in DevOps automation to update configuration settings, track resource usage, or assign values during script execution.
Common Assignment Operators:
=: Assigns a value to a variable.
+=: Adds and assigns the result to the variable (equivalent to x = x + y).
-=: Subtracts and assigns the result to the variable (equivalent to x = x - y).
*=: Multiplies and assigns the result to the variable (equivalent to x = x * y).
/=: Divides and assigns the result to the variable (equivalent to x = x / y).
//=: Floor divides and assigns the result to the variable (equivalent to x = x // y).
%=: Assigns the remainder of the division to the variable (equivalent to x = x % y).
**=: Raises the variable to the power of the right-hand value and assigns it.
Examples:
# Basic Assignment
x = 10
print(x)  # Result: 10

# Adding and assigning
x += 5  # x = x + 5
print(x)  # Result: 15

# Subtracting and assigning
x -= 3  # x = x - 3
print(x)  # Result: 12

# Multiplying and assigning
x *= 2  # x = x * 2
print(x)  # Result: 24

# Dividing and assigning
x /= 6  # x = x / 6
print(x)  # Result: 4.0

# Floor dividing and assigning
x //= 2  # x = x // 2
print(x)  # Result: 2

# Modulo (remainder) and assigning
x %= 2  # x = x % 2
print(x)  # Result: 0

# Exponentiation and assigning
x **= 3  # x = x ** 3
print(x)  # Result: 0, because 0 ** 3 = 0

Summary:
Arithmetic Operators: Useful for handling numerical tasks like calculating the cost of resources or monitoring metrics.
Comparison Operators: Used to check conditions such as whether a server is up or whether a system is within acceptable performance limits.
Logical Operators: Often used in conditional statements, like checking if multiple conditions are met before proceeding with tasks (e.g., a deployment).
Assignment Operators: Frequently used to update values in configuration files, scripts, or manage resource allocations.


Hands-on Activity 1: Arithmetic and String Manipulation Script
Objective: Practice basic arithmetic operations and string manipulation.
Create a Python file named calc_and_str.py:
# Arithmetic Operations
num1 = 5
num2 = 3
sum_result = num1 + num2
product_result = num1 * num2

# String Manipulation
greeting = "Hello, " + "World!"

print("Sum:", sum_result)
print("Product:", product_result)
print(greeting)

Steps:
Create and save the file as calc_and_str.py.
Run the script with the command python3 calc_and_str.py and check the output.
The output will display the sum, product, and a greeting message.

Hands-on Activity 2: Advanced Arithmetic & String Operations
Objective: Perform arithmetic on a list and manipulate strings.
Create a Python file calc_advanced.py:
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)

sentence = "hello world"
capitalized = sentence.upper()

print(f"Average: {average}")
print(f"Capitalized Sentence: {capitalized}")

Steps:
Create and save the file as calc_advanced.py.
Run the script with python3 calc_advanced.py.
This script will compute the average of the numbers and capitalize the string.

Control Structures: if-else and Loops
Conditional Statements: if, if-else, and if-elif-else
Conditional statements allow you to control the flow of a program based on conditions. These statements check whether a condition is true or false and execute different blocks of code based on that evaluation.
1. if Statement
The if statement checks if a condition is true. If it is, it runs the block of code inside it.
Syntax:
 if condition:
    # Code to execute if condition is true


Example:
Let’s write a simple script to check if a user is old enough to drive.
age = int(input("Enter your age: "))  # Get the user’s age

if age >= 18:
    print("You are old enough to drive.")

In this case, the program only prints the message if the age entered is 18 or greater.
2. if-else Statement
The if-else statement allows you to specify one block of code to run when the condition is true and another block to run when the condition is false.
Syntax:
 if condition:
    # Code to execute if condition is true
else:
    # Code to execute if condition is false


Example:
Here’s how you might use an if-else statement to check if the user can vote.
age = int(input("Enter your age: "))  # Get the user’s age

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

If the user is under 18, the message "You cannot vote." will be printed.
3. if-elif-else Statement
The if-elif-else statement is used when you have multiple conditions to check. The elif (short for "else if") allows you to check more than one condition.
Syntax:
 if condition1:
    # Code to execute if condition1 is true
elif condition2:
    # Code to execute if condition2 is true
else:
    # Code to execute if none of the conditions are true


Example:
Let’s use if-elif-else to categorize the user’s age into different groups.
age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

In this case:
If the age is less than 13, it prints "You are a child."
If the age is between 13 and 17, it prints "You are a teenager."
If the age is 18 or older, it prints "You are an adult."

Loops: for loop and while loop
Loops are used to repeatedly execute a block of code until a condition is met. Python has two main types of loops: for loops and while loops.
1. for Loop
The for loop is used to iterate over a collection (like a list, tuple, or string) or a range of numbers.
Syntax:
 for variable in collection:
    # Code to execute for each item in the collection


Example:
Let’s iterate over a list of names and print a greeting for each one.
names = ["Alice", "Bob", "Charlie", "David"]

for name in names:
    print(f"Hello, {name}!")

Output:
Hello, Alice!
Hello, Bob!
Hello, Charlie!
Hello, David!

In this example, the loop iterates over each name in the list and prints a greeting message.
2. while Loop
The while loop repeatedly executes a block of code as long as a given condition is true.
Syntax:
 while condition:
    # Code to execute as long as the condition is true


Example:
Let’s write a script that repeatedly asks for user input until the user types "quit".
user_input = ""
while user_input != "quit":
    user_input = input("Type 'quit' to stop: ")
    print(f"You typed: {user_input}")

The loop will keep running until the user types "quit", and it will print what the user types each time.

Break, Continue, and Pass Statements
These are used to alter the flow of a loop.
break: Exits the loop completely.
continue: Skips the current iteration and moves to the next iteration.
pass: A placeholder for code that does nothing (useful in situations where code is syntactically required but you don’t want to implement it yet).
Examples:
python
Copy
# Using break
for i in range(5):
    if i == 3:
        break
    print(i)

Output:
Copy
0
1
2

python
Copy
# Using continue
for i in range(5):
    if i == 3:
        continue
    print(i)

Output:
Copy
0
1
2
4

python
Copy
# Using pass (does nothing)
for i in range(5):
    if i == 3:
        pass  # This does nothing
    print(i)

Output:
Copy
0
1
2
3
4


Hands-On Activity: Write a Script to Iterate Over a List of Server Names and Print Their Status
Now, let’s combine conditional statements and loops to write a script that simulates checking the status of multiple servers.
Objective: Iterate over a list of server names, check their status, and print whether each one is online or offline based on their simulated status.
Define the server list: We’ll create a list of server names.
Define a status dictionary: Each server’s status will be stored in a dictionary with either "online" or "offline" as the value.
Use a loop and if-else to check the status of each server: For each server, the script will print whether it’s online or offline.
Code:
# List of servers
servers = ["server1", "server2", "server3", "server4"]

# Simulated server statuses
server_status = {
    "server1": "online",
    "server2": "offline",
    "server3": "online",
    "server4": "offline"
}

# Loop through the server list
for server in servers:
    status = server_status.get(server, "unknown")  # Get the status of the server
    if status == "online":
        print(f"{server} is online.")
    elif status == "offline":
        print(f"{server} is offline.")
    else:
        print(f"{server} status is unknown.")

Steps:
Create and save the script: Save the code in a Python file, e.g., server_status_check.py.
Run the script: Open a terminal or command prompt and run the script:
 python3 server_status_check.py


Expected Output:
server1 is online.
server2 is offline.
server3 is online.
server4 is offline.


Summary
Conditional Statements (if, if-else, if-elif-else) are used to control the flow of a program based on certain conditions.
if: Runs the code block if the condition is true.
if-else: Runs one block of code if the condition is true and another if false.
if-elif-else: Checks multiple conditions and runs the corresponding code block for the first true condition.
Loops allow us to repeat a block of code multiple times:
for loop: Iterates over a collection or range.
while loop: Repeats a block of code while a condition is true.


Functions and Modules
Purpose of Functions in Python
Functions are essential building blocks in Python that help make code modular, reusable, and more organized. Functions enable you to break down complex tasks into smaller, manageable parts, and they allow you to perform specific actions with parameters (inputs) and return values (outputs). Using functions is particularly useful in DevOps automation, where tasks need to be repeated multiple times, such as checking server status, system health, or automating repetitive system administration tasks.
Key Benefits of Functions:
Reusability: Once defined, functions can be reused across the codebase.
Modularity: Functions help in breaking down a program into smaller pieces, making it easier to understand and maintain.
Readability: By organizing tasks into functions, the code becomes more readable and easier to follow.
Abstraction: Functions hide the implementation details and allow you to focus on the logic.

Defining and Calling Functions
In Python, a function is defined using the def keyword. The syntax for defining a function looks like this:
def function_name(parameters):
    # Function body
    return result

def is the keyword to define a function.
function_name is the name of the function (should be descriptive).
parameters are values that can be passed to the function (optional).
return sends a result or value back to the calling code.
Example of Function Definition and Calling
# Function definition
def greet_user(name):
    print(f"Hello, {name}!")

# Function calling
greet_user("Alice")  # Output: Hello, Alice!

In this example:
greet_user() is a function that takes name as an argument.
The function then prints a greeting message.
When we call greet_user("Alice"), it outputs: Hello, Alice!

Passing Arguments and Returning Values
Functions can accept multiple arguments and return values, allowing you to customize their behavior and reuse them in different contexts.
Example of Passing Multiple Arguments and Returning a Value
# Function to calculate disk space usage
def calculate_disk_space(total_space, used_space):
    free_space = total_space - used_space
    return free_space

# Calling the function with arguments
total = 500  # GB
used = 300   # GB

free = calculate_disk_space(total, used)
print(f"Free disk space: {free} GB")  # Output: Free disk space: 200 GB

total_space and used_space are arguments passed into the function.
The function calculates and returns the free disk space (free_space).
The returned value is stored in the free variable, which we then print.

Modules in Python
Modules are Python files that consist of reusable functions, classes, and variables. Python comes with a wide variety of built-in modules that provide functionality for common tasks, such as interacting with the operating system, managing files, or even networking.
By using modules, you can reuse code without having to write it yourself, and you can extend your scripts' capabilities easily.

Built-in Modules: os and sys
1. os Module:
The os module provides a way to interact with the operating system. It allows you to perform system-level operations like file management, working with environment variables, and executing commands.
Some common functions in the os module:
os.name: Returns the name of the operating system dependent module imported.
os.getcwd(): Returns the current working directory.
os.listdir(): Returns a list of files and directories in the specified path.
os.system(command): Executes a system command (like a shell command).
Example using the os module:
import os

# Get the current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# List files in the current directory
files = os.listdir()
print(f"Files in the current directory: {files}")

2. sys Module:
The sys module provides access to some variables used or maintained by the interpreter. It is especially useful for interacting with the command line, handling arguments, and managing the Python runtime environment.
Common functions in the sys module:
sys.argv: A list of command-line arguments passed to the script.
sys.exit(): Exits the program.
sys.version: Returns the Python version being used.
Example using the sys module:
import sys

# Get the Python version
print(f"Python version: {sys.version}")

# Exit the script
sys.exit("Exiting the program.")


Using Modules in Python
You can import a module using the import keyword and then use its functions and classes in your script. There are several ways to import a module:
Import the whole module:

 import os
print(os.getcwd())


Import specific functions from a module:

 from os import getcwd
print(getcwd())


Alias the module for easier reference:

 import os as operating_system
print(operating_system.getcwd())



Python script that checks how much disk space is available on your system. 
We'll use the os module because it has a function called statvfs() which can help us get information about the disk.
Step 2: What is the os Module?
The os module gives us functions to interact with the operating system, such as:
Checking file properties
Navigating directories
And for our case, checking disk space.
Step 3: Create the Script
Now, let’s write the Python script. We will:
Define a function that checks the disk space.
Use the os module to get disk space information.
Print the available space.
Step 4: The Code
import os  # Importing the os module to interact with the operating system

# Function to check disk space
def check_disk_space(path):
    # os.statvfs returns information about the file system for the given path
    statvfs = os.statvfs(path)
    # Calculate the free space by multiplying block size by available blocks
    free_space = statvfs.f_frsize * statvfs.f_bavail
    return free_space

# Let's check the disk space for the root directory "/"
path = "/"
free_space = check_disk_space(path)

# Print the available space in MB
print(f"Free space in {path}: {free_space / (1024 * 1024)} MB")

Step 5: Explanation of the Code
Import the os module: We start by importing the os module, which gives us access to system-related tasks.

 import os


Create a function to check disk space:

 def check_disk_space(path):
    statvfs = os.statvfs(path)  # os.statvfs gives file system info for the path
    free_space = statvfs.f_frsize * statvfs.f_bavail  # Calculate free space
    return free_space


os.statvfs(path): This returns a bunch of information about the filesystem (including how much space is free).
statvfs.f_frsize: This is the size of a block in the filesystem.
statvfs.f_bavail: This is the number of free blocks available.
We multiply them to get the total free space.
Call the function and print the result:

 path = "/"  # We want to check the disk space of the root directory
free_space = check_disk_space(path)  # Call our function
print(f"Free space in {path}: {free_space / (1024 * 1024)} MB")  # Convert bytes to MB and print


Here we are calling the function for the / directory (root directory).
We then convert the result from bytes to MB (1024 * 1024 converts bytes to megabytes) and print it.
Step 6: Run the Script
Save the file as check_disk_space.py and run it from the command line like this:
python3 check_disk_space.py

This will print out the available disk space in the root directory (or any directory you choose by changing the path variable).

Hands-On Activity Breakdown
Function: The check_disk_space function takes a directory path as an argument and returns how much free space is available.
Module: We use the os module to interact with the system (in this case, checking the file system).
Output: The script calculates and prints how much free space is left in the given directory (in MB).
Why This is Useful for DevOps Engineers:
DevOps engineers often need to automate system maintenance tasks. For example, checking the disk space regularly helps ensure servers don't run out of space, which could cause failures in deployments or application performance.

Hands-on Activity 5: Disk Space Check Script
Objective: Create a script that checks the available disk space.
Create a Python file disk_check.py:
import os

def check_disk_space(path):
    statvfs = os.statvfs(path)
    free_space = statvfs.f_frsize * statvfs.f_bavail
    return free_space

path = "/"
space = check_disk_space(path)
print(f"Free space in {path}: {space / (1024 * 1024)} MB")

Steps:
Save the file as disk_check.py.
Run the script with python3 disk_check.py.
It will print the free space available on the root directory.

Hands-on Activity 6: File Size Check
Objective: Check the size of a specific file.
Create a Python file file_size_check.py:
import os

def check_file_size(file_path):
    file_size = os.path.getsize(file_path)
    return file_size

file_path = "/path/to/your/file.txt"
size = check_file_size(file_path)
print(f"Size of the file: {size / 1024} KB")

Steps:
Save the file as file_size_check.py.
Run the script with python3 file_size_check.py.
It will output the size of the specified file.


# List of servers
servers = ["server1", "server2", "server3", "server4"]


# Simulated server statuses
server_status = {
   "server1": "online",
   "server2": "offline",
   "server3": "terminated",
   "server4": "crashed"
}


# Loop through the server list
for server in servers:
   status = server_status.get(server, "unknown")  # Get the status of the server
   if status == "terminated":
       print(f"{server} is terminated.")
   elif status == "crashed":
       print(f"{server} is crashed.")
   elif status == "offline":
       print(f"{server} is offline")
   else:
       print(f"{server} status is unknown.")



---

Bash Script: Functions, arrays, loops & conditionals (All-in-one)
Script Overview: Check and Install Tools (Git, Bash, Python3)
This script checks if certain tools (Git, Bash, and Python3) are installed on your system. If any of these tools are not installed, the script installs them. It also provides support for both macOS (via Homebrew) and Linux (via apt).
Sequence of execution:
Loop Through the Tools:


The first thing that happens is the for loop starts running:
 for tool in "${tools[@]}"; do
 This loop will iterate over each tool in the tools array ("git", "bash", and "python3").

Check If Tool is Installed:


For each tool in the array, the script checks if the tool is already installed using the command:
 if command -v $tool &> /dev/null; then


command -v $tool checks if the command for the tool exists in the system's path. If the tool is found, it proceeds to the "already installed" message and skips to the next tool.
If the tool is not installed, it calls the install_tool function:
 install_tool $tool


Install the Tool (inside the install_tool Function):


If a tool is missing, the function install_tool is invoked to handle the installation:
 install_tool() {
    # Function logic to install the tool
}
 Inside the install_tool function:
The function first prints that the tool is not installed.
It then checks the operating system (macOS or Linux) and runs the appropriate command to install the tool.
After attempting the installation, it verifies if the tool was installed successfully with command -v $tool.
If the installation was successful, a success message is printed. If not, it prints an error message.
Completion Message:


Once the loop has checked all the tools (and installed the ones that were missing), the script prints:
 echo "Installation check complete."
 This marks the end of the script.
To Summarize:
So, the loop first checks whether each tool is installed, and only when a tool is missing, does the logic inside the function run to install it.

Script:
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

Explanation of the Script:
Shebang Line (#!/bin/bash):


This line ensures the script runs using Bash as the shell interpreter.
Array Definition (tools=("git" "bash" "python3")):


An array tools is created, containing the names of the tools that need to be checked (Git, Bash, Python3).
Function Definition (install_tool):


install_tool is a function that installs a given tool.
It first checks whether the operating system is macOS or Linux.
For macOS (Darwin), it uses Homebrew (brew install).
For Linux, it uses apt (sudo apt install).
If the tool is successfully installed, it verifies the installation using command -v. If it fails, an error message is shown.
Looping through the Tools (for tool in "${tools[@]}"):


The script loops through the tools array.
For each tool, it checks whether it is installed using command -v $tool.
If the tool is not found, it calls the install_tool function to install the tool.
Final Completion Message:


Once all tools have been checked (and installed if needed), the script prints Installation check complete..
Key Commands in the Script:
command -v $tool: Checks if the tool is installed on the system. If the command exists, the tool is installed.
brew install $tool: Installs the tool using Homebrew (for macOS).
sudo apt install -y $tool: Installs the tool using APT (for Linux).
Usage Example:
When you run the script, it will:
Check if Git, Bash, and Python3 are installed.
If any tool is missing, it will install it according to the OS.
It will display messages indicating whether each tool was already installed or successfully installed.
At the end, the script will print "Installation check complete.".
Example Output:
git is already installed.
bash is already installed.
python3 is not installed. Installing python3...
Reading package lists... Done
Building dependency tree       
...
python3 has been installed successfully.
Installation check complete.

This script should be easy to follow and execute for installing and checking the tools, and it also provides feedback along the way.

