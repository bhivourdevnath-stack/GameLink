import json
from pathlib import Path
from urllib.parse import urlparse

import app as app_module
from app import app, validate_catalog


DATA_DIR = Path(__file__).parent.parent / "data"


DATA_DIR = Path(__file__).parent.parent / "data"


def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"PlayLink" in response.data
    assert b"Agar.io" in response.data


def test_directory_page():
    client = app.test_client()
    response = client.get("/directory")

    assert response.status_code == 200
    assert b"Find your next browser game" in response.data


def test_contribute_page():
    client = app.test_client()
    response = client.get("/contribute")

    assert response.status_code == 200
    assert b"Help improve PlayLink" in response.data


def test_catalog_schema_and_values():
    validate_catalog()

    games = json.loads((DATA_DIR / "games.json").read_text(encoding="utf-8"))
    websites = json.loads((DATA_DIR / "websites.json").read_text(encoding="utf-8"))
    resources = games + websites

    ids = [resource["id"] for resource in resources]
    assert len(ids) == len(set(ids))
    for resource in resources:
        parsed = urlparse(resource["url"])
        assert parsed.scheme in {"http", "https"}
        assert parsed.netloc


def test_directory_filters_catalog_data():
    client = app.test_client()

    response = client.get("/directory?q=krunker&type=game")
    assert response.status_code == 200
    assert b"Krunker.io" in response.data
    assert b"Agar.io" not in response.data

    response = client.get("/directory?type=games")
    assert response.status_code == 200
    assert b"Krunker.io" in response.data
    assert b"Poki" not in response.data

    response = client.get("/directory?type=websites")
    assert response.status_code == 200
    assert b"Poki" in response.data
    assert b"Krunker.io" not in response.data

    response = client.get("/directory?q=racing&type=games")
    assert response.status_code == 200
    assert b"Slope Game" in response.data

    response = client.get("/directory?category=not-a-category&type=invalid")
    assert response.status_code == 200
    assert b"Agar.io" in response.data


def test_directory_no_results_message():
    response = app.test_client().get("/directory?q=definitely-not-a-resource")

    assert response.status_code == 200
    assert b"No matching links found" in response.data


def test_malformed_catalog_fails_safely(monkeypatch, tmp_path):
    (tmp_path / "games.json").write_text("not json", encoding="utf-8")
    (tmp_path / "websites.json").write_text("[]", encoding="utf-8")
    (tmp_path / "categories.json").write_text("[]", encoding="utf-8")
    monkeypatch.setattr(app_module, "DATA_DIR", tmp_path)
    client = app.test_client()

    assert client.get("/").status_code == 200
    assert client.get("/directory").status_code == 200


def test_catalog_categories_are_ordered():
    categories = json.loads((DATA_DIR / "categories.json").read_text(encoding="utf-8"))
    orders = [category["order"] for category in categories]

    assert len(orders) == len(set(orders))


def test_health_route():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_unknown_route_uses_custom_404():
    client = app.test_client()
    response = client.get("/does-not-exist")

    assert response.status_code == 404
    assert b"Page not found" in response.data
