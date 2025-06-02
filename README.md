# API Testing Template (JSONPlaceholder)

This project provides a simple and professional Python-based API testing template using `pytest` and `httpx` with asynchronous support. It targets JSONPlaceholder, a free fake REST API for testing and prototyping.

---

## Tech Stack

- Python 3.11+
- Pytest
- Pytest-asyncio
- HTTPX (async HTTP client)

---

## Project Structure

.
├── cli.py                  # Command-line entry to run tests  
├── test_jsonplaceholder.py # All test cases  
├── .gitignore              # Git ignored files  
└── README.md               # Project overview

---

## Features

- Test GET/PUT endpoints for `/posts` and `/users`
- Structured test functions using `async` + `pytest`
- Easy CLI to run all tests

---

## Getting Started

1. Install dependencies:

   pip install -r requirements.txt

2. Run tests:

   pytest -v

Or run using the CLI:

   python cli.py

---

## Sample Test Commands (CMD)

   pytest test_jsonplaceholder.py -v

   pytest -q --tb=short  (for cleaner output)


---

## License

This project is licensed under the MIT License, allowing commercial and personal use with proper attribution.

---

## Contributing

Pull requests are welcome! If you find a bug or have an idea for improvement, feel free to open an issue.

---

## Author

**[Byron McDowell]** — QA Automation Enthusiast  
Connect on [LinkedIn](https://www.linkedin.com/in/byronmcdowell) · [GitHub](https://github.com/blmcdowe) 
  
---
