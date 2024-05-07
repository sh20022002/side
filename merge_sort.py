
def main():
    file = open(r"C:\\Users\\shmue\\projects\\JavaScript\\inversions\\test.txt", 'r')

    data = file.read()
    arr = [elt.strip() for elt in data.split('\n')]
    
    print(merge_sort(arr))
 
    file.close()
def merge_sort(arr):
    def sort(left, right):
   
        tarr = []
        i = 0
        j = 0
        while (i < len(left) and j < len(right)):
            if(int(right[j]) < int(left[i])):
                tarr.append(right[j])
                j += 1
                
            else:
                tarr.append(left[i])
                i += 1
        while(i < len(left)):
            tarr.append(left[i])
            i += 1
        while(j < len(right)):
            tarr.append(right[j])
            j += 1
        return tarr
    if len(arr) == 1:
        return arr
    else:
        # mid = round(len(arr) / 2)
        mid = 1
        left = merge_sort(arr[0:mid])
        right = merge_sort(arr[mid:])
        return sort(left, right)
    
    
if __name__ =='__main__':
    main()