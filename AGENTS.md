PlayLink --- AI Agent Instructions
1. Project overview
PlayLink is a curated directory for discovering browser games and
websites that provide browser games. It is inspired by the
resource-directory approach of FMHY.

PlayLink is a directory, not a gaming platform. It lists resources
and links visitors to the original providers. Do not build game hosting,
an embedded game player, or gameplay features.

The project should stay simple, beginner-friendly, lightweight, and easy
to maintain.
2. Product goals
- Help visitors discover individual browser games and websites that
  host browser games.
- Organize resources into useful categories and tags.
- Provide search and filters to make discovery easy.
- Keep resource descriptions short, useful, and curated.
- Make it easy for contributors to suggest changes through GitHub.
- Follow the supplied PlayLink design screenshots: dark theme, compact
  resource rows, clear category navigation, and a simple contribution
  panel.
3. Fixed technology decisions
- Backend: Python with Flask.
- Frontend: HTML, CSS, and vanilla JavaScript.
- Templates: Flask/Jinja templates.
- Catalog storage: JSON files committed to Git.
- Search: Flask-powered search using query parameters and normal
  page reloads.
- Contributions: GitHub Issues and Pull Requests.
- License: MIT.
- Database: Not needed for v1.
- Authentication: Not needed for v1.
- Admin dashboard: Not needed for v1.
- Game hosting or gameplay: Out of scope.
- Deployment: Prefer a Python-capable free-tier host where
  practical. Do not promise that any hosting tier is permanently free.
Do not introduce React, Vue, a frontend build system, a REST API
framework, a database, user accounts, or other major dependencies unless
the project owner explicitly approves the change.
4. Planned pages and routes
- GET / --- Home page with the PlayLink introduction, curated links,
  and contribution/GitHub panels.
- GET /directory --- Main directory with search, category filtering,
  and All / Games / Websites filters.
- GET /contribute --- Explains how to contribute through GitHub
  Issues or Pull Requests.
- GET /about --- Project purpose, curation guidelines, and
  external-link disclaimer.
- A friendly 404 page for unknown routes.
- GET /health may be added if useful for deployment health checks.
Use query parameters for directory search and filters, for example:
- /directory?type=games
- /directory?type=websites
- /directory?category=puzzle
- /directory?q=agar
- /directory?category=racing&type=games
Validate query parameters and preserve the selected search/filter values
when rendering results. Invalid filter values should fail safely rather
than crash the app.
5. Planned repository structure
Keep the project close to this structure. Small changes are fine when
justified; avoid unnecessary folders and abstractions.
playlink/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── agent.md
├── data/
│   ├── games.json
│   ├── websites.json
│   └── categories.json
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── directory.html
│   ├── contribute.html
│   ├── about.html
│   └── 404.html
├── static/
│   ├── css/
│   │   ├── style.css
│   │   └── responsive.css
│   ├── js/
│   │   └── main.js
│   └── images/
└── tests/
    └── test_app.py
6. Catalog and resource data
Use JSON for the v1 catalog. Keep the schema consistent across
individual games and game-provider websites where practical.

Suggested resource fields:
- id: stable, unique identifier.
- name: display name.
- url: canonical external URL.
- type: game or website.
- category: main category identifier.
- tags: list of short tags.
- description: concise, factual description.
- featured: boolean indicating whether the resource can appear on
  the home page.
- status: optional curation state, such as active or unverified.
Categories should be defined in data/categories.json rather than
duplicated in multiple templates. Each category can include an
identifier, display name, description, icon, and display order.

Data rules:
- Keep JSON valid and consistently formatted.
- Use stable IDs and avoid duplicate entries.
- Use canonical URLs where possible.
- Do not invent resources, descriptions, verification results, or
  URLs.
- Do not mark a link as verified unless it has actually been checked.
- Keep descriptions concise and neutral.
- Do not copy game files or third-party artwork into the project
  without permission or a suitable license.
- Treat games and game-provider websites as external resources;
  PlayLink does not host them.
7. UI and design requirements
Use the supplied PlayLink screenshots as the primary visual reference.
- Dark background with clear contrast and readable typography.
- Compact, bordered resource rows with name, domain/URL, description,
  tags, and an external-link action.
- Shared header and navigation across pages.
- Home page with a short introduction, curated links, and
  contribution/GitHub/community panels.
- Directory page with a category sidebar, search input, All / Games /
  Websites selector, and grouped resource lists.
- Responsive layout for mobile and desktop.
- Visible keyboard focus indicators and usable form labels.
- Semantic HTML and accessible button/link names.
- Avoid excessive animation, heavy dependencies, oversized cards, and
  unnecessary decorative elements.
- Do not redesign the project into a game launcher or game-playing
  interface.
The shared layout belongs in templates/base.html. Keep CSS in
static/css/ and JavaScript in static/js/; do not scatter large
inline styles or scripts across templates.
8. Search and filtering
Search is handled by Flask and causes a normal page reload. Do not
replace this with client-only instant search unless explicitly
requested.

Search should match useful text fields such as resource name,
description, domain/URL, category, and tags. Matching should be
case-insensitive. Combine search, type, and category filters when
multiple are selected.

Keep the implementation straightforward and testable. Do not add a
search engine or database for this catalog.
9. GitHub contribution workflow
There is no in-site submission database in v1.
- The Contribution page should explain how to suggest a resource using
  a GitHub Issue or Pull Request.
- Provide clear guidance for new resources and broken-link reports.
- Contributors should add or edit catalog entries in the relevant JSON
  file.
- Review submissions for URL validity, duplicates, category fit,
  useful descriptions, and obvious safety concerns.
- Only merge approved changes.
- Do not add GitHub tokens, passwords, or other secrets to source
  control.
- Do not assume that creating an issue automatically changes the live
  catalog.
Issue templates may be added for resource suggestions and broken-link
reports. Keep the process simple.
10. Security and reliability
- Use Jinja's normal auto-escaping for dynamic content. Do not mark
  untrusted content as safe HTML.
- Validate resource URLs and only allow http and https schemes for
  catalog links.
- Never execute user-provided content.
- Do not build an endpoint that fetches arbitrary user-supplied URLs
  from the server. If link checking is added later, design it to
  mitigate SSRF and unsafe redirects.
- If any form accepts user input, validate lengths and formats and
  handle errors gracefully.
- Do not store secrets in Git. Use environment variables for
  deployment-specific configuration.
- Do not expose debug mode in production.
- Provide useful error pages and avoid leaking tracebacks to visitors.
- Treat external websites as third-party services with their own
  content, privacy practices, and availability.
11. Code quality and working style
- Prefer clear, beginner-friendly Python over clever abstractions.
- Keep dependencies minimal and record runtime dependencies in
  requirements.txt.
- Keep route handlers small and move repeated catalog-loading or
  filtering logic into simple helper functions when useful.
- Use meaningful names and short comments only where they clarify
  non-obvious behavior.
- Avoid premature architecture, unnecessary classes, and speculative
  features.
- Do not silently change the fixed product scope or technology
  choices.
- Before editing, inspect the existing repository and preserve working
  code and conventions.
- Make focused changes rather than rewriting unrelated files.
- Never claim a test or deployment succeeded unless it was actually
  run and succeeded.
- If something is ambiguous, choose the simplest option consistent
  with this document and explain the assumption.
12. Testing expectations
Add or update tests for meaningful behavior, including:
- Home, directory, contribution, and about routes.
- Unknown routes returning the custom 404 page.
- Catalog JSON loading and validation.
- Search matching and combined filters.
- Invalid query parameters being handled safely.
- Resource entries having required fields and valid URL schemes.
Run the relevant tests after changes when the environment allows it.
Report any tests that could not be run.
13. Definition of done for v1
PlayLink v1 is ready when:
1. The home page and directory broadly match the supplied screenshots.
2. Pages work on desktop and mobile.
3. The home page and directory are rendered from JSON catalog data.
4. Search and category/type filters work through Flask with page
   reloads.
5. External links lead to the original providers.
6. Contribution instructions point to GitHub Issues and Pull Requests.
7. The MIT license, README, and .gitignore are present.
8. Basic automated tests pass.
9. The application can be run locally and is prepared for deployment on
   a Python-capable host.
14. Out of scope for v1
Do not implement these unless the project owner explicitly asks:
- Hosting or embedding games.
- User accounts, login, or cloud-synced favorites.
- A database.
- An admin dashboard.
- In-site resource submission storage.
- Automated web scraping or bulk catalog imports.
- A complex API.
- Frontend frameworks or a build pipeline.
- Paid services that are not necessary for the initial release.
Primary rule: Build the smallest reliable version of PlayLink that
matches the approved design and makes curated external browser-game
resources easy to discover.