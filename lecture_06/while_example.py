# while loop - used for UNKNOWN number of repetitions
#
# <1. initialise>
# while <2. condition> is True:
#     <3. statement 1>
#     < statement 2>
#     ...
#     < statement n>
#     <4. update the condition to eventually False>
#

# Leg.go says cannot play Leg.go if you are > 99
# valid age 0 to 99

print("--- Welcome to Leg.go Bricks ---")
age = int(input("How old are you (0 to 99)? "))   # <1. init>

while age < 0 or age > 99:    # <2. condition>
    print("We know you love Leg.go")   # <3. statement 1>
    print("But please enter a valid age from 0 to 99")
    print("-------------------------")
    age = int(input("How old are you (0 to 99)? "))   # <4. update condition>


print("You are now welcome to play with the bricks.")


