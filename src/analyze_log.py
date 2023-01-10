from statistics import mode


def read_file(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        orders = []
        with open(path_to_file, 'r') as file:
            for line in file:
                order = line.replace('\n', '').split(',')
                orders.append(order)
        return orders
    except FileNotFoundError:
        raise ValueError(f"Arquivo inexistente: '{path_to_file}'")


def most_requested_by_maria(orders):
    mariaDishes = []
    for order in orders:
        if order[0] == 'maria':
            mariaDishes.append(order[1])

    return mode(mariaDishes)


def arnaldo_hamburguer(orders):
    count = 0
    for order in orders:
        if order[0] == 'arnaldo' and order[1] == 'hamburguer':
            count += 1

    return count


def joao_never_request(orders):
    joaoDishes = []
    notResquests = set()
    for order in orders:
        if order[0] == 'joao':
            joaoDishes.append(order[1])

    for dish in orders:
        if dish[1] not in joaoDishes:
            notResquests.add(dish[1])

    return notResquests


def joao_didnt_go(orders):
    joaoDays = []
    didntGo = set()
    for order in orders:
        if order[0] == 'joao':
            joaoDays.append(order[2])

    for dish in orders:
        if dish[2] not in joaoDays:
            didntGo.add(dish[2])

    return didntGo


def write_infos(orders):
    maria = most_requested_by_maria(orders)
    arnaldo = arnaldo_hamburguer(orders)
    joao = joao_never_request(orders)
    joaoDays = joao_didnt_go(orders)

    result = (
        f'{maria}\n'
        f'{arnaldo}\n'
        f'{joao}\n'
        f'{joaoDays}\n'
    )
    write_file = open('data/mkt_campaign.txt', 'w')
    write_file.write(result)
    write_file.close()


def analyze_log(path_to_file):
    orders = read_file(path_to_file)
    write_infos(orders)
