products = []
while True:
	name = input('please enter product name: ')
	if name == 'q':
		break
	price = input('please enter price: ')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], 'price is: ', p[1])

with open ('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品' + ',' + '价格' + '\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
