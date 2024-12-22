# Gestell Guide

This example guide repo goes through in both `node` and `python`:

- Creating Organization and Collections

- Uploading Documents to Collections

- Prompting a Collection

- Searching a Collection

- Gathering features from a Collection

- Gathering tables from a Collection

## Setup

Add a `.env` file for convenience or add `GESTELL_API_KEY` to your terminal session:

```bash
export GESTELL_API_KEY="..."
```

## Node SDK

```bash
# Setup the collection and upload documents to it
node src/node/setup.js

# Run an example prompt
node src/node/prompt.js "Who is in the cast of Reservoir Dogs?"

# Run an example search
node src/node/search.js "Who is in the cast of Good Fellas?"

# View the table output
node src/node/table.js

# View the feature label output
node src/node/features.js
```

## Python SDK

You can run `uv install` in this repo and be able to run via `python 3.X`:

```bash
uv venv
source .venv/bin/activate
# If needed `uv pip install gestell`

# Setup the collection
python src/python/setup.py

# Run an example prompt
python src/python/prompt.py "Who is in the cast of Reservoir Dogs?"

# Run an example search
python src/python/search.py "Who is in the cast of Good Fellas?"

# View the table output
python src/python/table.py

# View the feature label output
python src/python/features.py
```
