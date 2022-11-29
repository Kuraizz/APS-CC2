while True:
    print()  # pular linha
    pure = [0.94, 0.88, 0.88]  # porcentagem de pureza do combustível
    dens = [0.811, 0.85, 0.865]  # densidade (kg/l)
    fate = [0.56, 3.2, 3.2]  # fator de emissão equivalente (kg de co2/l)
    arvo = 163.4  # (kg de CO2, neutralização media de uma árvore por ano)

    cont = input('Deseja continuar? [s]im ou [n]ão: ')
    if cont == 'n':
        break  # verificar se o usuário deseja deixar o laço de repetição

    dist = input('Digite a distância percorrida (km): ')
    cons = input('Digite a taxa de consumo do seu veículo (km/l): ')
    comb = input('Digite o combustível utilizado: Diesel [s10], Diesel [s500] ou [e]tanol: ')

    if not dist.isnumeric() or not cons.isnumeric():
        print('Voce precisa digitar um número')
        continue  # verificar se foram digitados 2 números,
        # e caso contrário pular pro próximo laço

    emis = ()
    dist = int(dist)
    cons = int(cons)

    print()
    if comb == 'e':
        emis = (dist / cons * pure[0] * dens[0] * fate[0])
        cred = emis/1000  # 1 crédito de carbono = 1 tonelada ou 1000kg
        print(f'Durante a viagem de {dist}km foram efetuadas a emissão de {emis:.2f}kgCO2-eq (carbono equivalente)')
        arvo = (emis/arvo)
        print(f'Seria necessário o plantio de {arvo:.2f} árvores para compensar o impacto ambiental')
        print(f'ou o equivalente a {cred:.2f} créditos de carbono')

    elif comb == 's10':
        emis = (dist / cons * pure[1] * dens[1] * fate[1])
        cred = emis/1000
        print(f'Durante a viagem de {dist}km foram efetuadas a emissão de {emis:.2f}kgCO2-eq (carbono equivalente')
        arvo = (emis / arvo)
        print(f'Seria necessário o plantio de {arvo:.2f} árvores para compensar o impacto ambiental')
        print(f'ou o equivalente a {cred:.2f} créditos de carbono')

    elif comb == 's500':
        emis = (dist / cons * pure[2] * dens[2] * fate[2])
        cred = emis/1000
        print(f'Durante a viagem de {dist}km foram efetuadas a emissão de {emis:.2f}kgCO2-eq (carbono equivalente')
        arvo = (emis / arvo)
        print(f'Seria necessário o plantio de {arvo:.2f} árvores para compensar o impacto ambiental')
        print(f'ou o equivalente a {cred:.2f} créditos de carbono')
    else:
        print('Combustível inválido')
