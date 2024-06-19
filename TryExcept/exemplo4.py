def idade (entrada):
    if entrada <= 18:
     return "você não vota"  
    else:
     return "você já pode votar"
    
entrada = input("digite sua idade: ")

try:
   votar = int(entrada)
   pode = idade(votar)
   print(f"{pode}")
except:
  print(f"procure o Tribunal Eleitoral") 