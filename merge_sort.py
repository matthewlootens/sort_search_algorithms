def mergeSort(list):
    """list: a list of any n integers, duplicates allowed
    Returns a sorted list in non-decreasing order."""
    global inverse
    global standard
    #Handles the base case and empty lists.
    sortedlist = []
    if len(list) <= 1:
        return list
        
    else:
        ###
        #The recursive call.
        ###
        
        x = len(list)
        lista = mergeSort(list[0:(x//2)])
        listb = mergeSort(list[(x//2):x+1])
        
        ####
        #The merge sub-routine.
        ####
        
        i, j = 0, 0
        #while i < (len(lista)) or j < (len(listb)): 
        while True:
            if lista[i] <= listb[j]:
                sortedlist.append(lista[i])
                if i < (len(lista)-1):#prevents falling off list
                    i = i + 1
                else:#if lista is empty, append remainder of listb to sortedlist
                    sortedlist = sortedlist + listb[j:]
                    break
            else:
                sortedlist.append(listb[j])
		inverse = inverse + (len(lista) - i)
                if j < (len(listb)-1):
                    j = j + 1
                else:
                    sortedlist = sortedlist + lista[i:]
                    break
        if len(sortedlist) == len(standard):
	         print "Final Result: " + str(inverse)
        return sortedlist


inverse = 0
file = 'data.txt'
datafile = open(file)
datalist = []
for line in datafile:
    datalist.append(int(line))
standard = len(datalist)

num_list = [6, -3, 213, 4, 403, 1000, 2, 0, 50, -12, 34, 34, 45, 32, -12, 0]
print(mergeSort(num_list))