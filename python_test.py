#print to screen
print("Python is fun!")

#example of using a variables
message = "Python is fun!"
print(message)

#capitalizes name
name = "suzy strickler"
print(name.title())

first_name = "suzy"
last_name = "strickler"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"My name is, {full_name.title()}!")

#Manipulating Lists
states = ['New York', 'Pennsylvania', 'Hawaii']
print(states)

print(states[0])

#change an element
states[0] = 'Texas'
print(states)

#insert an element
states.insert(0, 'Montana')
print(states)

#Loops
states = ['New York', 'Pennsylvania', 'Hawaii']
for state in states:
    print(state)
print("All states in list printed")

#dictionaires
plants = {'color': 'blue', 'height' :  10}
print(plants['color'])

def weather():
    """Find out hte weather"""
    answer = input("How is the weather")
    print(answer)
weather()
