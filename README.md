# Agentic System Design Pattern Explorer

An interactive web application for composing, executing, observing, evaluating, and exporting agentic workflows. This system is designed for advanced users to explore the full agentic design surface area.

## Getting Started

### Backend

1.  **Create a virtual environment:**
    ```bash
    python3 -m venv backend/venv
    ```

2.  **Install dependencies:**
    ```bash
    backend/venv/bin/pip install -r backend/requirements.txt
    ```

3.  **Run the server:**
    ```bash
    backend/venv/bin/uvicorn backend.main:app --host 0.0.0.0 --port 8000
    ```
