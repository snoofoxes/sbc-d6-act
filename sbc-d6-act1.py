word = input("Enter a text: ")
text = []
for i in word.replace(" ",""):
	i.split()
	text.append(i)
sep = " "
rev = sep.join(text[::-1])
if rev == sep.join(text):
	print(f"Palindrome: {rev}")
else:
	print(f"Not Palindrome: {rev}")