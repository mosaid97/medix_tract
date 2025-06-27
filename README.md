# MediExtract 🩺

A lightweight, API-driven service to extract structured medical entities like patient names, medications, and diagnoses from unstructured clinical text using Natural Language Processing.

## Key Features

- **Entity Extraction:** Identifies key medical and demographic entities from raw text.
- **REST API:** Provides a clean, simple, and scalable `/extract` endpoint.
- **NLP Powered:** Leverages spaCy's pre-trained models for Named Entity Recognition (NER).
- **Containerized:** Fully containerized with Docker for easy deployment and reproducibility.

## Tech Stack

- **Backend:** Python 3.12
- **NLP:** spaCy
- **API:** FastAPI
- **Server:** Uvicorn
- **Containerization:** Docker

## Installation & Setup

Follow these steps to set up the project locally.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/mosaid97/medix-tract.git](https://github.com/mosaid97/medix-tract.git)
    cd medi-extract
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies from `requirements.txt`:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download the spaCy language model:**
    ```bash
    python -m spacy download en_core_web_sm
    ```

## Usage

1.  **Run the API server:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

2.  **Access the Interactive Docs:**
    Open your browser and navigate to `http://127.0.0.1:8000/docs`. You can interact with the API directly from this page.

3.  **Send a `curl` Request:**
    Alternatively, you can use a command-line tool like `curl`:
    ```bash
    curl -X 'POST' \
      '[http://127.0.0.1:8000/extract/](http://127.0.0.1:8000/extract/)' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "text": "Patient John Smith, age 56, was prescribed Lisinopril 10mg for his hypertension. He reports a persistent cough since starting the medication on 2025-06-15."
    }'
    ```

### Sample API Response

```json
{
  "input_text": "Patient John Smith, age 56, was prescribed Lisinopril 10mg for his hypertension. He reports a persi...",
  "extracted_entities": {
    "PERSON": [
      "John Smith"
    ],
    "DATE": [
      "age 56",
      "2025-06-15"
    ],
    "CARDINAL": [
      "10"
    ]
  }
}
```

## Future Improvements

- [ ] **Fine-tune a custom NER model** to accurately recognize specific `MEDICATION` and `DIAGNOSIS` entities.
- [ ] **Expand the API** to handle batch processing of multiple documents.
- [ ] **Add unit and integration tests** using `pytest` to ensure reliability.
