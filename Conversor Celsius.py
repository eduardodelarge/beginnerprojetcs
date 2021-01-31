temp_fahr = input("Qual a temperatura em Fahrenheit?: ")
temp_cels = (int(temp_fahr) - 32 * 5 // 9)

print(f"{temp_fahr}º Fahrenheit equivale à {temp_cels}º Celsius")