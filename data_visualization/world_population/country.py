from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    for code,country in COUNTRIES.items():
        if country == country_name:
            return code
    return None


