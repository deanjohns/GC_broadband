def rateCardA(length=1):
    data = {
        "Cabinet": 1000,
        "verge": 50 * length,
        "road": 100 * length,
        "Chamber": 200,
        "Pot": 100,
    }
    return data


def rateCardB(length=1, trenchlength=1):
    data = {
        "Cabinet": 1200,
        "verge": 40 * length,
        "road": 80 * length,
        "Chamber": 200,
        "Pot": 20 * trenchlength,
    }
    return data
