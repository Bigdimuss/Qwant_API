# QWant Api Client

This is a Python library for interacting with the QWant API. It provides methods for performing various types of searches, including web search, knowledge search, news search, image search, video search, and shopping search.

## Usage

Here is an example of how to use this library:

```python
from qwant_api_client import Qwant_Api

# Create an instance of the Qwant_Api class
q = Qwant_Api()

# Perform a search
search = q.get_search('Your Search Words')
print(search)
```

## API Reference

### Qwant_Api Class

#### `__init__(self, headers: dict = headers, session_type: str = SessionType.normal)`

- `headers`: A dictionary containing the headers to be sent with the requests (default: `headers`).
- `session_type`: The type of session to use (`SessionType.normal` or `SessionType.junior`, default: `SessionType.normal`).

#### `get_search(self, q: str, freshness: str = 'all', locale: str = 'fr_FR', offset: int = 0, safesearch: int = 1) -> dict`

Performs a web search.

- `q`: The search query.
- `freshness`: The freshness of the search results (default: 'all').
- `locale`: The locale of the search results (default: 'fr_FR').
- `offset`: The offset of the search results (default: 0).
- `safesearch`: The safesearch level (default: 1).

Returns a dictionary containing the search results.

#### `get_knowledge(self, q: str, locale: str = 'fr_FR', tgp: int = 50) -> dict`

Performs a knowledge search.

- `q`: The search query.
- `locale`: The locale of the search results (default: 'fr_FR').
- `tgp`: The tgp parameter (default: 50).

Returns a dictionary containing the search results.

#### `get_news(self, q: str, freshness: str = 'all', source: str = 'all', order: str = 'relevance', locale: str = 'fr_FR', offset: int = 0, safesearch: int = 1) -> dict`

Performs a news search.

- `q`: The search query.
- `freshness`: The freshness of the search results (default: 'all').
- `source`: The source of the news (default: 'all').
- `order`: The order of the search results (default: 'relevance').
- `locale`: The locale of the search results (default: 'fr_FR').
- `offset`: The offset of the search results (default: 0).
- `safesearch`: The safesearch level (default: 1).

Returns a dictionary containing the search results.

#### `get_images(self, q: str, freshness: str = 'all', size: str = 'all', imagetype: str = 'all', license: str = 'all', color: str = 'all', locale: str = 'fr_FR', offset: int = 0, safesearch: int = 1) -> dict`

Performs an image search.

- `q`: The search query.
- `freshness`: The freshness of the search results (default: 'all').
- `size`: The size of the images (default: 'all').
- `imagetype`: The type of the images (default: 'all').
- `license`: The license of the images (default: 'all').
- `color`: The color of the images (default: 'all').
- `locale`: The locale of the search results (default: 'fr_FR').
- `offset`: The offset of the search results (default: 0).
- `safesearch`: The safesearch level (default: 1).

Returns a dictionary containing the search results.

#### `get_shopping(self, q: str, locale: str = 'fr_FR', safesearch: int = 1, tgp: int = 80) -> dict`

Performs a shopping search.

- `q`: The search query.
- `locale`: The locale of the search results (default: 'fr_FR').
- `safesearch`: The safesearch level (default: 1).
- `tgp`: The tgp parameter (default: 80).

Returns a dictionary containing the search results.

#### `get_videos(self, q: str, source: str = 'all', order: str = 'relevance', locale: str = 'fr_FR', offset: int = 0, safesearch: int = 1) -> dict`

Performs a video search.

- `q`: The search query.
- `source`: The source of the videos (default: 'all').
- `order`: The order of the search results (default: 'relevance').
- `locale`: The locale of the search results (default: 'fr_FR').
- `offset`: The offset of the search results (default: 0).
- `safesearch`: The safesearch level (default: 1).

Returns a dictionary containing the search results.

﻿
