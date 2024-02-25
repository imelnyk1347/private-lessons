def read_file():
    with open('random_text.txt', 'r') as file:
        with open('get_digits_from_random_text.txt', 'a') as update_file:
            for line in file:
                for word in line:
                    if word.isalnum():
                        for num in word:
                            if num.isdigit():
                                update_file.write(num)
                    else:
                        continue
    return 'Program finished successfully'


print(read_file())
