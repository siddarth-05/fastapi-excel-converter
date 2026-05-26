# Excel to JSON 

A lightweight web application that converts Excel files (`.xls`, `.xlsx`) to JSON via a clean browser interface. Built with FastAPI and Pandas.

## Features

- Upload Excel files through a minimal web UI
- Converts spreadsheet rows to a list of JSON records
- Returns structured JSON with filename, size, and parsed data
- Input validation for file type and size

## Project Structure

```
LTM/
├── app/
│   ├── main.py              
│   ├── routes/
│   │   └── route.py          
│   ├── services/
│   │   └── excelconvert.py   
│   ├── templates/
│   │   └── index.html        
│   └── static/
│       └── index.css          
├── uploads/                   
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd LTM

# Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
# Create an app/.env file and add your secret API key:
echo "API_KEY=your_secret_key" > app/.env

```

### Running the App

```bash
cd app
uvicorn main:app --reload
```

The app will be available at http://127.0.0.1:8000.

## API Reference

### `GET /`

Serves the upload form page.

### `POST /uploadfile/`

Upload an Excel file and receive its contents as JSON.

**Request:** 
- `multipart/form-data` with a `file` field (`.xls` or `.xlsx`).
- **Header:** `x-api-key` (string, required) containing your secret API key.


**Success Response (200):**

```json
{
  "success": true,
  "filename": "data.xlsx",
  "size": 10240,
  "type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
  "data": [
    {"Column1": "value1", "Column2": "value2"},
    {"Column1": "value3", "Column2": "value4"}
  ]
}
```

**Error Responses:**

| Status | Detail |
|--------|--------|
| 400 | Upload Excel (.xls or .xlsx) file only |
| 400 | File Read Error |

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — Web framework
- [Uvicorn](https://www.uvicorn.org/) — ASGI server
- [Pandas](https://pandas.pydata.org/) — Data processing
- [openpyxl](https://openpyxl.readthedocs.io/) — Excel file engine
- [Jinja2](https://jinja.palletsprojects.com/) — HTML templating

