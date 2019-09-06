import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'

counter=0


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    while True:
        try:
            return int(input('Guess the secret number? '))
        except:
            print("Please enter a number in integer format.")


def check_guess(guess, secret):
    global counter
    counter += 1
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct.upper()
    if guess < secret:
        return too_low.upper()
    if guess > secret:
        return too_high.upper()


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:

            print("you needed this many guesses", counter)
            break



if __name__ == '__main__':
    main()
