import pandas as pd


# We can access elements using index labels

# labels can be single or multiple

# Labels can be numerical or with their name

# Panda series is mutable

# We can drop element using drop method

# We can perform mathematical operations on the Series, given that operations are

# defined for it's elements


di = {"2":25, "key": 5, "door" : "iron", "42" : "string"}

series_dic = pd.Series(di)
print(di)
 

# Indexing

# We access the first element using number instead of the key '2'

#print(series_dic[0])  

#print(series_dic["2"])


# Mutable

series_dic["key"] = 15
#print(series_dic)


# More than one index

#print(series_dic[[0,1]]) # Indices mustt be in a list

#print(series_dic.iloc[ :2 ]) # will start from index 2

#print(series_dic.loc["2" : "door"])


# Drop elements from series. T take effect, store the remaining

# data in a variable or use the 'inplace' keyword

series_dic.drop(labels = "2", inplace = True)
print(series_dic)


# Performing mathematical operations


mathSeries_1 = pd.Series([1,5,6,8,3,4,6])

mathSeries_2 = pd.Series([3,2,8,7,9,10,2])

def jls_extract_def():
    # add the two elements together
    print(mathSeries_1.add(mathSeries_2)) # add the two elements together = jls_extract_def()

    return 


jls_extract_def()

