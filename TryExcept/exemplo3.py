Idade = input("digite sua idade: ") 

try:
    Idade = int(Idade)
    if Idade <=16 :
        print("você não vota")
    else:
       print("você já pode votar")
except:
      print("procure a Justiça eleitoral")      
     
