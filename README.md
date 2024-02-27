# Bulk download Twilio Recordings

A Python script that bulk downloads Twilio recordings

## Prerequisites
- Python 3
- Git

## Installation

### Mac/Linux

1. `git clone https://github.com/danohn/bulk-download-twilio-recordings.git`
2. `cd bulk-download-twilio-recordings`
3. `python3 -m venv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`
6. `cp .env.example .env`
7. `nano .env` (replace placeholders with real values)

### Windows

1. `git clone https://github.com/danohn/bulk-download-twilio-recordings.git`
2. `cd bulk-download-twilio-recordings`
3. `python3 -m venv venv`
4. `venv\Scripts\activate`
5. `pip install -r requirements.txt`
6. `copy .env.example .env`
7. `notepad .env` (replace placeholders with real values)

## Usage

Once the virtual environment has been activated, start the app by running `python app.py` or `python async_app.py` to run the asynchronous version

## Asynchronous version

The asynchronous version of the app uses Python's asynchronous programming features (`asyncio`) and the [`aiohttp`](https://pypi.org/project/aiohttp/) library to download recordings efficiently, significantly reducing download times. Testing both versions shows an increase of almost 2300% in performance!

### Comparison (based on 227 recordings, total size 636.2 MB)

| Method | Execution Time |
| ------ | -------------- |
| Synchronous `(app.py)` | 632.6 seconds |
| Asynchronous `(async_app.py)` | 26.38 seconds |


