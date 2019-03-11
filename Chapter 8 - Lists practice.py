weights = [10, 15, 20, 30, 40, 50]
weights_2 = [60, 70, 80, 90, 100]
workouts = ['squats', 'pullups', 'pushups', 'curls']
message = "the 3 variables created are my workout references"

#just running a simple for loop with a list
count = 0
for x in weights:
    count = count + 1
    print(x)
print('This list contains',count,'numbers')

#this is how you look inside of a list...need to use square brackets.
#the 3rd character in the list is 90. It works similar to a string starting with 0 first
print(weights_2[3])

#this is how you change an element in a list using an index operator. Doesnt work with strings only integers
print(weights, 'I print the original list first')
weights[4] = 45
print(weights, 'I printed the changed number second')

#this is to check the length of a list
print(len(weights_2),'(this list has 5 characters)')
print(len(workouts),'(this list has 4 characters)')

#print(weights)
#print(weights_2)
#print('This is both weigth variables printed seperately')
print(weights + weights_2)
print('This is both weight variables concatenated')
print(len(weights_2),'This is the length of weights')
print(weights_2[0:3+1])

weights.append(10)
print(weights,'10 was added to the end of this list')

if 15 in weights:
    print('in list')
    print('in list')

if 23 in weights:
    print('not in list')

if 40 in weights:
    print('in list')

#print(dir(weights))

for workout in workouts:
    print('This is my favorite', workout)

for i in range(len(workouts)):
    workout = workouts[i]
    print('This is my favorite', workout)

print(len(workouts))
print(range(len(workouts)))

#this is how you split a list
work = message.split()
print(work)

#for this split method a delimiter wasnt specified here so the message will print with the colons
message_2 = 'this;is;my;favorite;message'
print(message_2)
msp = message_2.split()
print(msp)

#for this split method a delimiter was specified so the message will print with spaces
msp = message_2.split(';')
print(msp)

#double split method
words = message.split()
par = words[1]
rag = par.split('created')
print(rag[1])

#this is how your use a double split
email = 'From paragdesai2000@gmail.com Sunday December 12-16-2018'
w = email.split()
x = w[1]
z = x.split('@')
print(z[1])
