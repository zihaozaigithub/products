import os


products = []
if os.path.isfile('products.csv'):
	print('file exist')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品，价格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name,price])
	print(products)
else:
	print('file not exist')

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
