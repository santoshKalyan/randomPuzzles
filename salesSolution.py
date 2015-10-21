"""
From the two tab delimited files, product.tab , sales.tab
Get the top 5 categories by sales and top product by sales in category 'Candy'

"""

import operator
x = {1: 2, 3: 4, 4:3, 2:1, 0:0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))

def read_file_into_array(file_path):
    infile = open(file_path)
    arr = []
    for line in infile.readlines():
        fields = line.rstrip().split("\t")
        if(len(fields) > 1):
            arr.append(fields)
    return arr

products_arr = read_file_into_array("products.tab")
sales_arr    = read_file_into_array("sales.tab")

products_dict = dict((x[0],x[1:]) for x in products_arr)
sales_dict = dict((x[0],x[1:]) for x in sales_arr)
combined = { k : sales_dict[k] + products_dict[k] for k in products_dict if k in sales_dict }

categories = { combined[k][1] : 0.0 for k in combined}
for k in combined:
    category = combined[k][1]
    categories[category] += float(combined[k][0])
sorted_categories = sorted(categories.items(), key=operator.itemgetter(1))

##Solution to 1st question
count = 0
for i in range(len(sorted_categories) -1, -1, -1):
    if(count==5):
        break
    print sorted_categories[i][0] + "\t" + str(sorted_categories[i][1])
    count += 1
    
##Solution to 2nd question
all_candies = { k : float(combined[k][0]) for k in combined if combined[k][1] == 'Candy'}
sorted_candies = sorted(all_candies.items(), key=operator.itemgetter(1))
print "Top candy by sales is ",
print sorted_candies[len(sorted_candies) - 1][0]

