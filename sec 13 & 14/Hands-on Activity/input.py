import time

# Ask for user confirmation to start deployment
confirm = input("Are you sure you want to deploy the application? (yes/no): ").lower()

if confirm != 'yes':
    print("Deployment canceled.")
    exit(0)

# Ask for the environment to deploy to
env = input("Which environment would you like to deploy to? (production/staging): ").lower()

# Simulate deployment based on the environment
if env == 'production':
    print("Deploying to production...")
    # Simulate deployment
    time.sleep(2)
    print("Production deployment completed!")
elif env == 'staging':
    print("Deploying to staging...")
    # Simulate deployment
    time.sleep(2)
    print("Staging deployment completed!")
else:
    print("Invalid environment. Deployment failed.")
