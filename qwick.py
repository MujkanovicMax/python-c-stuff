import numpy as np

def qwsort(arr):
    if len(arr) == 0:
        return arr
    elif len(arr) == 1:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            temp = arr[1]*1
            arr[1] = arr[0]*1
            arr[0] = temp*1
            return arr
        else:
            return arr

    else:
        arr_tail = np.array([])
        arr_head = np.array([])
        arr_mid = np.array([])
        print(len(arr)-1)
        r = np.random.randint(0,(len(arr)-1))
        print("r=",r)
        for i in range(len(arr)):
            if i == r:
                arr_mid = np.append(arr_mid,arr[i])
                print(arr_mid)
            else:
                if arr[i] > arr[r]:
                    arr_tail= np.append(arr_tail,arr[i])
                    print(arr_tail)
                else:
                    arr_head=np.append(arr_head,arr[i])
                    print(arr_head)

        arr_tail = qwsort(arr_tail)
        arr_head = qwsort(arr_head)
        arr = np.append(arr_head, arr_mid)
        arr =np.append(arr,arr_tail)

        return arr

                
arr = np.random.rand(30)
print(arr)
print(qwsort(arr))


