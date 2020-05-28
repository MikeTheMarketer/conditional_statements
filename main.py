current_temp = int(input("Please enter current temperature in Farnheit: "))
print("\n")

convert_to_celsius = (5/9) * (current_temp - 32)
print(convert_to_celsius)
print("\n")

fibonacci_count = 59
fibonacci_sequence = [1,]
fib_count = 1
fib_counter = 0
x=1
while x <= fibonacci_count:
    fibonacci_sequence.append(x)
    x = x + fibonacci_sequence[-2]

print(fibonacci_sequence)
print("\n")

net_bonus = 0
number_of_years = int(input("How many years have you worked at the company? "))
current_salary = int(input("What is your current salary? "))

if number_of_years >= 5:
  net_bonus = current_salary * 0.05
  
print("Your net bonus this year is : $", net_bonus)
print("\n")

user_list = []
user_1_age = int(input("User 1 please enter your current age: "))
user_2_age = int(input("User 2 please enter your current age: "))
user_3_age = int(input("User 3 please enter your current age: "))
user_list.append(user_1_age)
user_list.append(user_2_age)
user_list.append(user_3_age)
user_list.sort()
print(user_list)
print("\n")

classes_held = int(input("Please enter your number of classes held: "))
classes_attended = int(input("Please enter number of classes attended: "))

if classes_attended > (classes_held * 0.75):
  num_class = (classes_attended/classes_held) * 100
  print("You attended {}% of classes".format(num_class))
  print("Congrats! You can attend the exam!")
else:
  print("Sorry, you did not attend enough classes to take the exam!")
print("\n")

vowels = ['a', 'e', 'i', 'o', 'u']
vowelish = ['y']

user_input_letter = input("Please enter a letter: ")
if user_input_letter in vowels:
  print("Your letter is a vowel!")
elif user_input_letter in vowelish:
  print("Y is sometimes a vowel and sometimes a consonant!")
  
  

