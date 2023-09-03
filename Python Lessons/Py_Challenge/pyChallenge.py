
# Take a list of numbers and sort them according to sort option. Ascending or descending

def sortList(sortOption, args=[]) :
        
    if sortOption == "asc" :
         args.sort(reverse = False)
         return args
    elif sortOption == "dsc" :
         args.sort(reverse = True)
         return args
    elif sortOption == "none" :
        return args
    

sortOption = "none"
lists = sortList(sortOption, [1,54,58,52,14,87])

print(lists)