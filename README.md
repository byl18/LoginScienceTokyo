# Science Tokyo Portal Auto Login Script

> This is a Python automation script using Selenium for automatically logging into the Science Tokyo Portal, including automatic input of username/password and matrix authentication code.

## Features

This project allows fully automated login to the Science Tokyo Portal:

1. Automatically enter the portal login page
2. Automatically click "Agree" for authentication method
3. Automatically input username and password
4. Automatically recognize matrix authentication positions (e.g., [D,7])
5. Automatically fetch and input corresponding matrix code
6. Automatically click OK to submit
7. Keep the browser open after successful login for user operations

## Project Structure

```
LoginScienceTokyo/
├── login_tokyo_science.py       # Main Python script
├── Matrix.csv                   # Matrix code table (user-defined)
├── .env                         # Environment variable config (user-defined)
└── requirements.txt             # Python dependencies
```

## Quick Start

### 1. Install dependencies

Recommended: use `conda` or `venv` to create an isolated environment.

Then install all required packages:

```bash
pip install -r requirements.txt
```

### 2. Set your Science Tokyo username and password

Create a `.env` file in the root directory:

```
USERNAME=your_id_here
PASSWORD=your_password_here
```

> Warning: Keep `.env` file private and NEVER upload it to GitHub.

### 3. Set your own Matrix Code Table

Edit `Matrix.csv` according to your own matrix card.

Example:

|    | A | B | C | D | E | F | G | H | I | J |
|----|---|---|---|---|---|---|---|---|---|---|
|1   |X  |N  |N  |I  |E  |G  |X  |M  |M  |M  |
|2   |O  |L  |N  |Y  |K  |W  |I  |M  |V  |Z  |
...

## Usage

Run the script:

```bash
python login_tokyo_science.py
```

> The browser will automatically:
- Open the portal page
- Complete all login steps
- Stay on the final logged-in page
- Wait for you to press Enter to close the browser

## Notes

|Note|Description|
|----|-----------|
|Browser|Default: Chrome. Please ensure ChromeDriver is installed and version matches your Chrome browser|
|Matrix Update|Update `Matrix.csv` if your matrix card changes|
|Security|Do NOT upload `.env` with sensitive info to public repositories|

## Contact

If you have any questions or suggestions, feel free to open an issue or contact me.
