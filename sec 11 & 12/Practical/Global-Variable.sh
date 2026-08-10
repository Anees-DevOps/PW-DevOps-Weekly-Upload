# Define a global variable
name="John"

my_function() {
    # Define a local variable inside the function
    local age=25
    echo "Age inside function: $age"
}

echo "Name outside function: $name"
my_function
