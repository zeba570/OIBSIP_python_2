from db import get_history


def get_statistics():

    data = get_history()

    bmi_values = [item['bmi'] for item in data]

    if len(bmi_values) == 0:

        return {

            "average": 0,
            "highest": 0,
            "lowest": 0,
            "total": 0
        }

    return {

        "average":
            round(sum(bmi_values) / len(bmi_values), 2),

        "highest":
            max(bmi_values),

        "lowest":
            min(bmi_values),

        "total":
            len(bmi_values)
    }