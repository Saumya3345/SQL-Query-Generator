# AI SQL Query Generator

An AI-powered SQL Query Generator built using **Python**, **Streamlit**, and **Google Gemini API**. This application converts natural language prompts into SQL queries, generates sample outputs, and provides easy-to-understand explanations, making SQL learning and query generation faster and more efficient.

---

## Features

- Convert natural language into SQL queries
- AI-powered query generation using Google Gemini API
- Generate sample tabular output
- Simple explanation for each generated SQL query
- Clean and interactive Streamlit interface
- Loading indicators for improved user experience
- Fast and responsive UI

---

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- Prompt Engineering
- SQL

---

## Project Structure

```
AI-SQL-Query-Generator
│── app.py
│── requirements.txt
│── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Saumya3345/AI-SQL-Query-Generator.git
```

### Move into the project directory

```bash
cd AI-SQL-Query-Generator
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Replace the placeholder API key in `app.py`:

```python
GOOGLE_API_KEY = "YOUR_API_KEY"
```

with your own Google Gemini API key.

---

## Run the Application

```bash
streamlit run app.py
```

The application will launch in your default web browser.

---

## How It Works

1. Enter your database requirement in plain English.
2. Click **Generate SQL Query**.
3. The application sends the prompt to the Google Gemini API.
4. Gemini generates an optimized SQL query.
5. The application displays:
   - SQL Query
   - Expected Sample Output
   - Query Explanation

---

## Skills Demonstrated

- Python Programming
- SQL
- Streamlit
- REST API Integration
- Google Gemini API
- Prompt Engineering
- Generative AI
- User Interface Development
- Problem Solving

---

## Future Improvements

- Support multiple SQL dialects (MySQL, PostgreSQL, SQL Server, Oracle)
- SQL query optimization suggestions
- Query execution on sample databases
- Database schema upload
- SQL syntax highlighting
- Query history
- Export generated SQL queries

---

## Learning Outcomes

This project strengthened my understanding of Python programming, SQL query design, API integration, prompt engineering, and Generative AI. It also improved my ability to build AI-powered applications that solve real-world problems through natural language processing and intelligent automation.

---

## Author

**Saumya Singh**

B.Tech – Computer Science & Engineering

Galgotias College of Engineering & Technology

GitHub: https://github.com/Saumya3345

LinkedIn: https://linkedin.com/in/saumya-singh-863128305

Email: singhsaumya18.09@gmail.com
