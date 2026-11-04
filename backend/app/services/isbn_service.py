import requests


def lookup_isbn(isbn: str):

    response = requests.get(
        f"https://openlibrary.org/isbn/{isbn}.json"
    )

    if response.status_code != 200:
        return None

    data = response.json()

    cover_url = (
        f"https://covers.openlibrary.org/b/isbn/"
        f"{isbn}-L.jpg"
    )

    return {
        "isbn": isbn,
        "title": data.get("title"),
        "authors": "",
        "publisher":
            data.get("publishers", ["Unknown"])[0],
        "publish_date":
            data.get("publish_date"),
        "cover_url":
            cover_url
    }