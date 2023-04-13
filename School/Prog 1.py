# 1a, Proper comment heading.
# Temperature Conversion Program, Celsius to Fahrenheit
# 1b, add a printed introduction to the user before the program starts
print("This program converts a given Celsius to Fahrenheit a given amount of times")
# 1d, Make program Loop for given amount of times
LoopAmount = int(input("How many temperatures do you want converted? "))

def main():
    # Input the temperature in Celsius
    celsius = int(input("What is the Celsius temperature? "))
    # Calculate the value of fahrenheit
    fahrenheit = (9/5) * celsius + 32
    # Print the results
    print("The temperature is " + str(fahrenheit) + " degrees Fahrenheit.")

# 1c, Loop the function for multiple temperatures
for _ in range(LoopAmount):
    main()

print("Goodbye!")
