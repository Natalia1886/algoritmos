def contar_formas_Escalera(n):
    dp=[]

    for i in range (n+1):
        dp.append(0)



# Caso base


    dp[0] = 1
    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 2

    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]+ dp[i-3]

    return dp[n]


nNum=int(input("Numero de escalones: "))
resultado = contar_formas_Escalera(nNum)
print("Total de formas:", resultado)
