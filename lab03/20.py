# bai20
def number_to_words(n):
    if n == 0:
        return "zero"
    ones = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    ]
    teens = [
        "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    tens = [
        "", "", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"
    ]

    words = []

    if n >= 100:
        words.append(ones[n // 100] + " hundred")
        n %= 100
    if n >= 20:
        words.append(tens[n // 10])
        n %= 10
    elif n >= 10:
        words.append(teens[n - 10])
        n = 0
    if n > 0:
        words.append(ones[n])

    return ' '.join(words).strip()


def convert_numbers_to_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
    updated_content = []
    for line in content:
        new_line = ''
        words = line.split()
        for word in words:
            if word.isdigit():
                number = int(word)
                new_line += number_to_words(number) + ' '
            else:
                new_line += word + ' '
        updated_content.append(new_line.strip())
    with open("output2.txt", 'w', encoding='utf-8') as file:
        for line in updated_content:
            file.write(line + '\n')