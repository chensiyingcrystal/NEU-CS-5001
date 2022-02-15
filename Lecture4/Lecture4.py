"""Iteration using while loops"""
def main():
    my_number = random.randint(1, 100)
    guess = 1
    while guess!= my_number:
        guess += 1;
    print("I guess!")

def main():
    answer = input("Please give an ansewer between 0 and 1")
    while answer > 1 or answer < 0:
        print("Only number between 0 and 1 will work here")
        answer = input("Please give me an answer between 0 and 1")
        