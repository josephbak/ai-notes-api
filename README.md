# AI Notes API

A Flask-based REST API for managing notes with AI-powered summarization capabilities using Hugging Face transformers.

## Purpose

This project was developed as a learning exercise to understand REST API design, implementation, and integration with modern AI technologies. It demonstrates practical application of web development concepts including CRUD operations, database management, and machine learning model integration.

## Features

- **CRUD Operations**: Create, read, update, and delete notes
- **AI Summarization**: Generate summaries of notes using BART model
- **SQLite Database**: Lightweight database storage
- **REST API**: Clean JSON API endpoints

## Tech Stack

- **Backend**: Flask, SQLAlchemy
- **Database**: SQLite
- **AI Model**: Facebook BART (via Hugging Face Transformers)
- **Python**: 3.12+

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ai-notes-api
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

The API will be available at `http://localhost:5000`

## API Endpoints

### Notes CRUD

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/notes` | Create a new note |
| GET | `/notes` | Get all notes |
| GET | `/notes/<id>` | Get a specific note |
| PUT | `/notes/<id>` | Update a note |
| DELETE | `/notes/<id>` | Delete a note |

### AI Features

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/notes/<id>/summarize` | Generate AI summary of a note |

## Usage Examples

### Create a note
```bash
curl -X POST http://localhost:5000/notes \
  -H "Content-Type: application/json" \
  -d '{"content": "Your note content here"}'
```

### Get all notes
```bash
curl http://localhost:5000/notes
```

### Summarize a note
```bash
curl -X POST http://localhost:5000/notes/1/summarize
```

## Project Structure

```
ai-notes-api/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── instance/
│   └── notes.db       # SQLite database (created automatically)
└── venv/              # Virtual environment
```

## Dependencies

- Flask - Web framework
- Flask-SQLAlchemy - Database ORM
- Transformers - Hugging Face AI models
- PyTorch - ML framework
- NumPy - Numerical computing

## Notes

- The AI model (BART) will be downloaded automatically on first run (~1.2GB)
- Database is created automatically when the app starts
- Uses SQLite for simplicity - suitable for development and small deployments

## License

MIT License