# PlayLink

PlayLink is a curated directory for discovering browser games and websites that provide browser games. It is a lightweight Flask application and does not host or embed games.

## Requirements

- Python 3.10 or newer

## Local development

Create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies and run the app:

```powershell
python -m pip install -r requirements.txt
flask --app app run --debug
```

Then open `http://127.0.0.1:5000`.

## Catalog format

Add games to `data/games.json` and game portals or resource websites to `data/websites.json`. Every resource uses this schema:

```json
{
  "id": "stable-unique-id",
  "name": "Display name",
  "url": "https://example.com",
  "type": "game",
  "category": "puzzle",
  "tags": ["Puzzle", "Casual"],
  "description": "A short factual description.",
  "featured": false,
  "status": "active"
}
```

Use `game` or `website` for `type`, use a category ID defined in `data/categories.json`, and use either `active` or `unverified` for `status`. Resource IDs must be unique across both catalog files, and URLs must use HTTP or HTTPS.

## Project layout

- `app.py` — Flask application and routes
- `templates/` — Jinja templates
- `static/` — CSS, JavaScript, and images
- `data/` — JSON catalog data
- `tests/` — automated tests

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
