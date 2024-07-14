# def main():
#     x = int(input("What is X? "))
#     if is_even(x):
#         print("X is even.")
#     else:
#         print("X is odd.")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# main()

name = input("What is your name? ")

match name:
    case "Messi" | "Di Maria" | "De Paul":
        print("Argentina")
    case "Ronaldo" | "Silva" | "Fernandes":
        print("Portugal")
    case "RM" | "Poleng":
        print("Cambodia")
    case _:
        print("No name")