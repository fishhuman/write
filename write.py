data = [1, 3, 5, 7, 9]
with open('sequence.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品,價格\n')
    for d in data:
        f.write(str(d) + ',')