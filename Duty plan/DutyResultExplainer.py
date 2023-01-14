input_string= input()

# split the string by comma and store the resulting list in a variable

for people in range(17):
input_list = input_string.split(",")

no_work = 0
hardWork =0

# remove any whitespace from the items in the list
input_list = [item.strip() for item in input_list]
name = input_list.pop(0) 

for x in input_list:
  if x == '0':
    no_work+=1
  if x == '5':
    hardWork +=1

print('average no workdays :', len(input_list)/no_work)
print('No work days: ', no_work)
print('average hard work days:', len(input_list)/hardWork)
print('hardWork : ', hardWork)

# print the final list
print(input_list)