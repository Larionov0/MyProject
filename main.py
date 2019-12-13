from time import sleep
name = input("Name: ")
# Выводим имя
seconds = 20
for i in range(seconds):
    print(seconds - i)
    sleep(0.3 * (1/(i + 1)))
print("---< ", name, ">----")

print("End")
