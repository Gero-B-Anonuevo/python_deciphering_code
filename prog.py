word = input("Please insert a sentence: ")
change_a = word.replace('*', 'a')
change_e = change_a.replace('&', 'e')
change_i = change_e.replace('#', 'i')
change_o = change_i.replace('+', 'o')
change_u = change_o.replace('!', 'u')
print(f"Your new word: {change_u}")
