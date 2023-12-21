def invert(st):
    arr = ""
    for i in range(len(st)):
        arr += st.pop()
    return arr


stek = list(input("Введите строку: "))
print("Инвертированная строка ", invert(stek))
