#EX 3 - LISTA 2 - Fernando Barreto
q=0
i1=0
p1=0
i2=0
for x in range(0, 30):
    i= int(input('Digite a idade:'))
    a= float(input('Digite a altura:'))
    p= float(input('Digite o peso:'))
#A
    if i>50:
        q+=1
#C
        if p<40:
            p1+=1
            
#B
    elif 10<=i<=20:
        i1+=a
        i2+=1
        if p<40:
            p1+=1
i3=i1/i2
r= (p1/30)*100
print('Pessoas com idade superior a 50 anos:', q)
print('Média das alturas das pessoas com idade entre 10 e 20 anos:', i3)
print('Porcentagem de pessoas com peso inferior a 40 quilos:',)
    
        
    
    
