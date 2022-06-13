yellow_list = []
green = [' ',' ',' ',' ',' ']
word_file = open("wordlib.txt")

class Yellow:
  def __init__(self, idx, char):
    self.idx = idx
    self.char = char

def wordle_return_string():
    wordle_return_string = input('What was the Wordle return string?: ')
    if wordle_return_string == 'ggggg':
        print('The wordle is correct!')
        exit()
    return wordle_return_string

def decode_wordle_string(start_word, wordle_string):
    black_list = []
    for i in range(len(wordle_string)):
        if wordle_string[i] == 'g':
            green[i] = start_word[i]
        elif wordle_string[i] == 'y':
            yellow_list.append(Yellow(i, start_word[i]))
        elif wordle_string[i] == 'x':
            black_list.append(start_word[i])
    return (black_list, yellow_list, green)

def setup_word_count():
    word_list = []
    for word in word_file.readlines():
        word_list.append(word.strip())
    return word_list
    
def cut_word_count(word_list, current_word_list, black_list, yellow_list, green, count):
    cut_word_list = cut_black_list(word_list, current_word_list, black_list, count, green)
    cut_word_list = cut_yellow_list(cut_word_list, yellow_list)
    cut_word_list = green_word(cut_word_list, green)
    return cut_word_list

def cut_black_list(word_list, current_word_list, black_list, count, green):
    if count > 0:
        word_list = current_word_list
        current_word_list = []
    for word in word_list:
        flag = False
        for letter in black_list:
            if letter in green:
                if word[green.index(letter)] is not letter:
                    flag = True
                    break
            else:
                if letter in word:
                    flag = True
                    break
        if flag == False:
            current_word_list.append(word)
    return current_word_list

def cut_yellow_list(current_word_list, yellow_list):
    word_list = current_word_list
    current_word_list = []
    for word in word_list:
        flag = False
        for yellow in yellow_list:
            try:
                if yellow.char not in word or word[yellow.idx] is yellow.char:
                    flag = True
            except IndexError:
                    flag = True
        if flag == False:
            current_word_list.append(word)
    return current_word_list

def green_word(current_word_list, green):
    word_list = current_word_list
    current_word_list = []
    for word in word_list:
        flag = False
        for letter in green:
            if letter == ' ':
                continue
            elif green[green.index(letter)] is not word[green.index(letter)]:
                    flag = True
            else:
                flag = False
        if flag == False:
            current_word_list.append(word)
    return current_word_list

def guess_picker(current_word_list):
    if current_word_list != 1:
        return current_word_list[len(current_word_list) // 2]
    else:
        return current_word_list[0]
    
def main():
    current_word_list = []
    start_word = 'CRANE'
    word_list = setup_word_count()
    count = -1
    while True:
        count = count + 1
        wordle_guess = wordle_return_string()
        black_list, yellow_list, green = decode_wordle_string(start_word, wordle_guess)
        cut_word_list = cut_word_count(word_list, current_word_list, black_list, yellow_list, green, count)
        current_word_list = cut_word_list
        start_word = guess_picker(cut_word_list)
        print('Guess the word ' + start_word)

if __name__ == "__main__":
    main()