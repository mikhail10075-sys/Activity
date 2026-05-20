def add(P,Q):
    return(P+Q)

def subtract(P,Q):
    return(P-Q)

def multiply(P,Q):
    return(P*Q)

def divide(P,Q):
    return(P/Q)

print("Choose between:")
print("Addition")
print("Subtraction")
print("Multiplication")
print("Divison")
choice = input()
num_1 = float(input("Please enter a number:"))
num_2 = float(input("Please enter a number:"))



if choice == "Addition":
  print(add(num_1,num_2))

elif choice == "Subtraction":
    print(subtract(num_1,num_2))

elif choice == "Multiplication":
    print(multiply(num_1,num_2))

elif choice == "Divison":
    print(divide(num_1,num_2))

else:
    print("Error")