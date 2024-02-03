data = open('./assets/data.txt', mode='r')
# print(data.read())
# print(data.read()) # Latihan dasar menangani file di python


# string = data.read()
# string = string.replace('adalah', 'merupakan')
# print(string)


# # Better practice
# try:
#    f = open('./assets/data.txt', mode='w', encoding='utf-8')
# finally:
#    f.close()

# Best practice
with open('./assets/data.txt', mode='w', encoding='utf-8') as f:
    pass



# Append
data = open('./assets/data.txt', mode='a')
data.write("Yuk belajar bahasa pemrograman Python!\n")
data.write("Agar jago harus sering berlatih!\n")
data.write("Agar jago harus sering berlatih!\n")
data.write("Agar jago harus sering berlatih!\n")
data.write("Agar jago harus sering berlatih! 2\n")
data.close()

# Write
data = open('./assets/data.txt', mode='w')
data.write("\nYuk belajar bahasa pemrograman Python!")
data.write("\nAgar jago harus sering berlatih!")
data.close()
