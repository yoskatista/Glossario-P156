rios = {
        'Mississipi':'Estados Unidos',
        'Amazonas':'Brazil',
        'Nilo':'Egito'       
       }


for rio in rios.keys():
        
        if rio in rios:
                print("O rio " + rio.title() + ' banha o ' + rios[rio].title())


Nome = {'Mikael':'Python','Teu pai':'Java'}

for name in Nome.keys():

        print('\n' + 'O ' + name + ' gosta de ' + Nome[name].title())
