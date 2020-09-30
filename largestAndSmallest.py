largest = None
smallest = None
while True:
    num =input("Enter a number: ")
    if num == "done" : break
    try:
        n=int(num)
    except:
        print("Invalid input")
    if(largest==None and smallest==None):
        largest=n
        smallest=n
    if(n>largest):
        largest=n
    if(n<smallest):
        smallest=n
print("Maximum is", largest)
print("Minimum is", smallest)
