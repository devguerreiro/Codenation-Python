from datetime import datetime
from resources import records


PERMANENTE_TARIFF = 0.36  # custo base de cada ligação

# custo por cada x segundos da duração da ligação no período diurno
DAY_TIME_TARIFF = 0.09

# período diurno
START_DAY_TIME_PERIOD = 6
END_DAY_TIME_PERIOD = 22

X_SECONDS = 60  # a cada x segundos a tarifa do período será cobrada


def classify_by_phone_number(records: list) -> list:
    """
    retorna uma lista contendo um dicionário com duas chaves 'source' e 'total' para cada número de origem
    ordenado pelo maior valor de 'total'
    """

    total_by_phone_number = []

    for record in records:
        start_record_timestamp = record.get("start")
        end_record_timestamp = record.get("end")

        minutes = __get_difference_in_minutes_between_two_timestamp(
            end_timestamp=end_record_timestamp, start_timestamp=start_record_timestamp
        )

        total = __calculate_per_minute_tariff_by_period(
            minutes=minutes, start_timestamp=start_record_timestamp,
        )

        total_by_phone_number = __group_by_source_and_sum_total(
            phone_number=record.get("source"),
            total=total,
            total_by_phone_number=total_by_phone_number,
        )

    return sorted(
        total_by_phone_number, key=lambda record: record.get("total"), reverse=True
    )


def __group_by_source_and_sum_total(
    *, phone_number: str, total: float, total_by_phone_number: list
) -> list:

    for element in total_by_phone_number:
        if element.get("source") is phone_number:
            # se já está registrado, soma com o valor total do registro
            element["total"] = round(element.get("total") + total, 2)

            return total_by_phone_number

    # se não está registrado cria um novo registro
    total_by_phone_number.append({"source": phone_number, "total": total})

    return total_by_phone_number


def __calculate_per_minute_tariff_by_period(
    *, minutes: int, start_timestamp: datetime.timestamp
) -> float:
    total_tariff = PERMANENTE_TARIFF

    for minute in range(minutes):
        # para cada minuto, é verificado em qual período se encontra
        # com base no horário inicial do minuto completo
        if __is_daytime(start_timestamp):
            total_tariff += DAY_TIME_TARIFF

        # soma x segundos a data inicial para verificar o período do próximo minuto
        start_timestamp += X_SECONDS

    return round(total_tariff, 2)


# verifica através da hora se o timestamp atual está no período diurno
def __is_daytime(start_timestamp: datetime.timestamp) -> bool:
    period = datetime.fromtimestamp(start_timestamp).hour

    return True if START_DAY_TIME_PERIOD <= period < END_DAY_TIME_PERIOD else False


def __get_difference_in_minutes_between_two_timestamp(
    *, end_timestamp: datetime.timestamp, start_timestamp: datetime.timestamp
) -> int:

    return (end_timestamp - start_timestamp) // X_SECONDS


print(classify_by_phone_number(records))
