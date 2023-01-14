no_work = 0
hardWork =0
totalListLen = 0

for people in range(34):
  input_string= input()
  input_list = input_string.split(",")

  # remove any whitespace from the items in the list
  input_list = [item.strip() for item in input_list]
  totalListLen += len(input_list)
  name = input_list.pop(0) 

  for x in input_list:
    if x == '0':
      no_work += 1
    if x == '5':
     hardWork += 1


print('No duty per', totalListLen//no_work,'days')
print('Average Duties per person :', no_work//17)
print('Hard duty per', totalListLen//hardWork,'days')
print('Average hard duties per person :', hardWork//17)