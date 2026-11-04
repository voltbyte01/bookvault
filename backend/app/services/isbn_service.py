import requests


def lookup_isbn(isbn: str):
    url = f"https://openlibrary.org/isbn/{isbn}.json"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "isbn": isbn,
        "title": data.get("title"),
        "publish_date": data.get("publish_date"),
        "publishers": data.get("publishers", [])
    }