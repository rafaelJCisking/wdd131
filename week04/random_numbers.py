import random


words = ["big", "red", "funny", "baby", "yellow", "wait", "python", "Joseph"]

def main():
    numbers = [16.2, 75.1, 52.3]
    
    
    word_list = [] 
    
    print(f"numbers: {numbers}")
    
    
    append_random_numbers(numbers, 3)
    print(f"numbers: {numbers}")

    
    append_random_words(word_list)
    print(f"words: {word_list}")
    
    append_random_words(word_list, 4)
    print(f"words: {word_list}")

def append_random_words(w_list, quantity=1):
    """Append quantity randomly chosen words onto the words list."""
    for _ in range(quantity):
        w_list.append(random.choice(words))

def append_random_numbers(numlist, quantity=1):
    for _ in range(quantity):
        num = random.uniform(0, 100)
        num = round(num, 1)
        numlist.append(num)

if __name__ == "__main__":
    main()