list=[1,4,5,2,7,8,9]
list.sort()

first=0
last=len(list)-1
mid=(first+last)//2
search=int(input("Enter the search element:"))
found=False
while (first<=last and not found):
    mid=(first+last)//2
    if list[mid]==search:
        print(f"ELement is in the list at {mid}")
        found=True
    elif list[mid] < search:
        first=mid+1
    else:
        last=mid-1
if found==False:
    print("Number not found")
   

