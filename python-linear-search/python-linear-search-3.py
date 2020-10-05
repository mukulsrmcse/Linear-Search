def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return "Not found"
arr = ['t','u','t','o','r','i','a','l']
x = '5'

if str(linearsearch(arr,x)) == 'Not found':

    print("Element not found")
    
else:
    print("Element found at index "+str(linearsearch(arr,x)))

      
      
