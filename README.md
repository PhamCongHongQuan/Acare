# A*Care Clinic

A web application for managing a small clinic. Patients book and manage appointments, doctors follow their schedules and patients, and admins manage users, rooms and services. The site also has a RAG chatbot that answers questions about the clinic from its own documents.

## Features

- **Patients:** register and log in, book appointments, edit or cancel pending appointments, view appointment history, edit their profile.
- **Doctors:** view their schedule and patients, mark appointments as done, see monthly statistics.
- **Admins:** dashboard with appointment statistics and recent activity; manage users, rooms, services and appointments.
- **Chatbot:** answers questions about the clinic using retrieval-augmented generation (RAG).

## Tech stack

| Part | Technologies |
|---|---|
| Backend | Java 21, Spring Boot 3.5, Spring Data JPA, MySQL, Lombok |
| Frontend | React 19, Vite, React Router, Tailwind CSS, Recharts |
| Chatbot | Python, FastAPI, LangChain, FAISS, FastEmbed (`all-MiniLM-L6-v2`), Gemini 2.5 Flash |

## How the chatbot works

1. `ingest.py` reads the clinic documents in `data/docs/` (TXT, PDF, DOCX), splits them into chunks, embeds them and stores them in a FAISS index.
2. For each question, `rag.py` retrieves the 4 most relevant chunks and sends them to Gemini together with prompt rules: answer only from the documents, never diagnose, and suggest booking an appointment when appropriate.
3. `app.py` exposes the chatbot as `POST /ask` on port 8005, which the React frontend calls.

## Project structure

```
source/
├── Backend/                         Spring Boot REST API (port 8080)
│   └── src/main/python/RAG/         RAG chatbot service (port 8005)
└── Frontend/                        React app (port 5173)
```

## Running locally

Requirements: JDK 21, Node.js 18+, MySQL 8, Python 3.11+.

1. **Database:** create the `acare_clinic` database by running [`source/file_query.sql`](source/file_query.sql) in MySQL Workbench, then set your MySQL password in `source/Backend/src/main/resources/application.properties`.
2. **Backend:**
   ```bash
   cd source/Backend
   ./mvnw spring-boot:run
   ```
3. **Frontend:**
   ```bash
   cd source/Frontend
   npm install
   npm run dev
   ```
4. **Chatbot (optional):**
   ```bash
   cd source/Backend/src/main/python/RAG
   python -m venv .venv && .venv/Scripts/activate   # macOS/Linux: source .venv/bin/activate
   pip install -r requirements.txt
   cp .env.example .env                              # then put your Gemini API key in .env
   python ingest.py                                  # rebuild the vector index if documents change
   uvicorn app:app --port 8005
   ```

Open http://localhost:5173. A step-by-step guide in Vietnamese is in [HUONG_DAN_CHAY.txt](HUONG_DAN_CHAY.txt).
