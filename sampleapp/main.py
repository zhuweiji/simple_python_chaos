import requests

from chaos.network import add_latency


@add_latency(min_delay=1, max_delay=3)
def get(endpoint):
    response = requests.get(endpoint)
    return response


if __name__ == "__main__":
    get("https://google.com")
