from datetime import date

meses_positivistas = [
    "Moisés", "Homero", "Aristóteles", "Arquimedes", "César", "São Paulo",
    "Carlos Magno", "Dante", "Gutenberg", "Shakespeare", "Descartes",
    "Frederico II", "Bichat"
]

def para_calendario_positivista(data_gregoriana):
    """Converte uma data do calendário gregoriano para o calendário positivista.

    Args:
        data_gregoriana (date): A data no calendário gregoriano.

    Returns:
        date: A data no calendário positivista.
    """

    ano_positivista = data_gregoriana.year - 1791
    mes_positivista = (data_gregoriana.month - 1) % 13
    dia_positivista = data_gregoriana.day

    return date(ano_positivista, mes_positivista, dia_positivista)

def para_calendario_gregoriano(data_positivista):
    """Converte uma data do calendário positivista para o calendário gregoriano.

    Args:
        data_positivista (date): A data no calendário positivista.

    Returns:
        date: A data no calendário gregoriano.
    """

    mes_gregoriano = data_positivista.month - 1
    ano_gregoriano = data_positivista.year + 1791
    dia_gregoriano = data_positivista.day

    return date(ano_gregoriano, mes_gregoriano + 1, dia_gregoriano)

if __name__ == "__main__":
    # Exibe um menu para o usuário escolher qual calendário deseja converter.
    print("Escolha qual calendário deseja converter:")
    print("1. Gregoriano para positivista")
    print("2. Positivista para gregoriano")

    # Lê a escolha do usuário.
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        # Solicitar ao usuário o dia, mês e ano do calendário gregoriano.
        dia = int(input("Digite o dia (calendário gregoriano): "))
        mes = int(input("Digite o mês (calendário gregoriano): "))
        ano = int(input("Digite o ano (calendário gregoriano): "))

        # Converte a data para o calendário positivista.
        data_gregoriana = date(ano, mes, dia)
        data_positivista = para_calendario_positivista(data_gregoriana)

        # Exibe a data no calendário positivista.
        mes_positivista_nome = meses_positivistas[data_positivista.month - 1]
        print("Data no calendário positivista:")
        print(f"Ano: {data_positivista.year}, Mês: {mes_positivista_nome}, Dia: {data_positivista.day}")

    elif escolha == 2:
        # Solicitar ao usuário o dia, mês e ano do calendário positivista.
        dia_positivista = int(input("Digite o dia (calendário positivista): "))
        mes_positivista = int(input("Digite o mês (calendário positivista): "))
        ano_positivista = int(input("Digite o ano (calendário positivista): "))

        # Converte a data para o calendário gregoriano.
        data_positivista = date(ano_positivista, mes_positivista, dia_positivista)
        data_gregoriana = para_calendario_gregoriano(data_positivista)

        # Exibe a data no calendário gregoriano.
        print("Data no calendário gregoriano:")
        print(f"Ano: {data_gregoriana.year}, Mês: {data_gregoriana.month}, Dia: {data_gregoriana.day}")

    else:
        print("Escolha inválida.")
