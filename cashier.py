def main():
	# write code here
	total=0
	counter = "done"
	item =""
	myList = []
	while item!=counter:
		item = input('Item (enter "done" when finished): ')
		if item==counter:
			break
		price = input('Price: ')
		quantity = input('Quantity: ')
		a = {'name':item ,'price':price ,'quantity':quantity}
		myList.append(a)
	#print(myList)
	print("\n------------------- \n receipt \n------------------- \n ")
	for key in myList:
		multiply = float(key['price']) * float(key['quantity'])
		print(key['quantity'],key['name'],multiply,"KD")
		total += multiply
	print("------------------\n Total price: {}KD".format(total))

if __name__ == '__main__':
	main()
