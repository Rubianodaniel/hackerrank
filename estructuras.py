def arr_reverse(arr):
    format_list = []
  
    for index in range(len(arr)):
        list_in=[]
        for element in str(arr[index]):
            list_in.append((element))
        format_list.append(list_in)
    format_list = format_list[::-1]

    lis_final=[]
    for element in range(len(format_list)):
        numeros = None
        for numero in (format_list[element]):
            if numeros == None:
                numeros = str(numero)
            else:
                numeros = numeros + str(numero)
        lis_final.append(int(numeros))
        
    return format_list

if __name__== '__main__':

    arr = [6257,2342,1234]
    arr_reverse(arr)


