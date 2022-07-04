ammounts=[400, 800, 1700, 4500, 10000]
cost  =  [499, 999, 1999, 4999, 9999]
# costs in cents
# the costs and ammounts are the same for usd and eur

print('Enter "D" as a value to continue')

inputs = []
doneInputting = False
while not doneInputting:
    inBobux = input('Please enter a value\n')
    if not inBobux.isnumeric and not inBobux == "D":
        raise "Input is not a number!"
    elif inBobux == "D":
        doneInputting = True
    elif inBobux.isnumeric:
        inputs.append(int(inBobux))
    else:
        raise "what the heck did you do to get here"

# set the ammount array to the sum of the inputs
ammount=0
for i in range(len(inputs)):
    ammount+=inputs[i]

# reverse the ammounts array in tmp
tmp=[]
for i in range(len(ammounts)):
        tmp.insert(-len(tmp), ammounts[i])

# check what packages to buy
done=False
toBuy=[]
extra=False
while not done:
    for i in range(len(tmp)):
        if ammount >= tmp[i]:
            ammount-=tmp[i]
            toBuy.append(tmp[i])
        
    if ammount<tmp[0]:
        if not ammount<=0:
            extra=True
        done=True

# summarize to a readable way
print('\n--Robux to buy to get to the desired ammount--')
print('Total ammount: ', ammount)
print('Packages to buy: ')
for i in range(len(toBuy)):
    print('     ', toBuy[i], '      Price: ', cost[ammounts.index(toBuy[i])]/100)
if extra:
    print('     ', ammounts[0], '      Price: ', cost[0]/100)