from Crypto.Hash import MD4

for num in range(251288019,1000000000):
	var = "0e" + str(num)
	h = MD4.new()
	h.update(var)
	per = h.hexdigest()
	print(per)
	if per.startswith("0e") and per[2:].isnumeric(): 
		print (var) 
