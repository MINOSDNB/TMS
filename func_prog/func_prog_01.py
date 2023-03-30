# Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}”

result = (lambda name: f"hello, {name}")('Boris')
print(result)


result = lambda name: f"hello, {name}"
print(result("Boris"))
