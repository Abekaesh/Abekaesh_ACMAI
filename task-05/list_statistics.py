# ALL THE BEST!!!

def valid_list(list):
    flag = 0
    for i in list:
        if not isinstance(i,int):
            flag = 1
            break
    if flag or list == []:
        return "Invalid input"
    return "Valid"
  
def unique_nums(list):
    count = 0
    visited = []
    for i in list:
        if i not in visited:
            visited.append(i)
            count += 1
    print(count)
  
def smallest_num(list):
  print(min(list))
  
def largest_num(list):
  print(max(list))
  
def avg_list(list):
  print(int(sum(list)/len(list)))

# Do not change any code from here onwards.
n = int(input())
nums = []

for i in range(n):
    inp = input()
    
    if inp.replace('-', '').isnumeric():
        nums.append(int(inp))
        
    else:
        nums.append(inp)
        
valid = valid_list(nums)

if valid == 'Invalid input':
    print(valid)
    
else:
    unique_nums(nums)
    smallest_num(nums)
    largest_num(nums)
    avg_list(nums)
