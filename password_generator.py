import random


def generate_password():
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    symbols = ['!', '#', '$', '&', '/', '(', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    characters = uppercase + lowercase + symbols + numbers

    password = []

    for i in range(15):
        random_character = random.choice(characters)
        password.append(random_character)

    password = ''.join(password)
    return password

def run():
    password = generate_password()
    print('Your new password is: ' + password)


if __name__ == "__main__":
    run()