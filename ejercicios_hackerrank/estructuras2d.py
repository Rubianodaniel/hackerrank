def hourglassSum(arr):

    #sacar los relojes de arena
    list_muestra = []
    for i in range(len(arr)):
        fila1 = []
        for j in range(len(arr[i])):
            
            muestra = arr[i][j:j+3]
            if len(muestra) == 3:
                fila1.append(muestra)
        list_muestra.append(fila1)
    
    
    for element in range(len(list_muestra)):
        for k in range(len(list_muestra[element])):
            print(list_muestra[element][0])
        
    # print(list_muestra)
    # arreglado = []
    # for element in list_muestra:
    #     a = element[1]
       

if __name__ == '__main__':
  

    arr = [[1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0], 
        [1, 1, 1, 0, 0, 0], 
        [0, 0, 2, 4, 4, 0], 
        [0, 0, 0, 2, 0, 0], 
        [0, 0, 1, 2, 4, 0]]
             
    result = hourglassSum(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()

    # list =[[1,2,3,6,7,8],[4,5,6]]
    # j= 0
    # i = 4
    # print(list[0][j:i])