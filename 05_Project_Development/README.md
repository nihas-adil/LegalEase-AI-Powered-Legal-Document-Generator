# Phase 05 – Project Development

## LegalEaseAI – AI-Powered Legal Document Generator

---

## 1. Introduction

The Project Development phase focuses on converting the planned system design and requirements into a functional software application.

LegalEaseAI is developed as an AI-powered legal document generation system that allows users to provide basic legal document information and generate structured legal documents automatically.

The system combines a web-based frontend, FastAPI backend, AI-based document generation, and document processing components.

---

## 2. Development Objectives

The main objectives of the development phase are:

* To implement the planned system architecture.
* To develop the backend API.
* To develop the frontend user interface.
* To integrate AI-based document generation.
* To implement legal document templates and formatting.
* To connect frontend and backend components.
* To implement error handling and validation.
* To test the developed modules during implementation.
* To prepare the system for final testing and demonstration.

---

## 3. Development Environment

The project was developed using the following environment:

| Component            | Technology                 |
| -------------------- | -------------------------- |
| Operating System     | Windows                    |
| Programming Language | Python                     |
| Backend Framework    | FastAPI                    |
| Frontend             | HTML, CSS, JavaScript      |
| AI Integration       | Google Gemini API          |
| API Testing          | Swagger UI                 |
| Code Editor          | Visual Studio Code         |
| Version Control      | Git                        |
| Repository           | GitHub                     |
| Virtual Environment  | Python Virtual Environment |

---

## 4. Technology Stack

### 4.1 Backend

The backend is developed using Python and FastAPI.

FastAPI is responsible for:

* Creating REST API endpoints.
* Receiving user inputs.
* Validating request data.
* Processing document generation requests.
* Communicating with the AI service.
* Returning generated results to the frontend.

### 4.2 Frontend

The frontend provides the user interface for entering legal document information.

The frontend is responsible for:

* Collecting document type.
* Collecting party information.
* Collecting legal terms.
* Collecting effective date.
* Sending data to the backend.
* Displaying generated document content.
* Providing a simple and user-friendly experience.

### 4.3 Artificial Intelligence

Google Gemini API is used as the AI generation component.

The AI receives structured information from the backend and generates a legal-document-style draft based on the provided requirements.

AI generation is intended to assist with document drafting and does not replace professional legal advice.

---

## 5. Project Structure

The major project components are organized as follows:

```text
LegalEasyAI/
│
├── ai_core/
│
├── backend/
│
├── frontend/
│
├── services/
│
├── utils/
│
├── fonts/
│
├── Image/
│
├── 01_Brainstorming_and_Ideation/
│
├── 02_Requirement_Analysis/
│
├── 03_Project_Design/
│
├── 04_Project_Planning/
│
├── 05_Project_Development/
│
├── 06_Project_Testing/
│
├── 07_Project_Documentation/
│
├── 08_Project_Demonstration/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

Sensitive configuration information such as API keys is stored using environment variables and is not intended to be exposed publicly.

---

## 6. Backend Development

The backend was implemented using FastAPI.

The backend provides API endpoints for interacting with the LegalEaseAI system.

### Main API endpoints

| Method | Endpoint    | Purpose                           |
| ------ | ----------- | --------------------------------- |
| GET    | `/`         | Checks whether the API is running |
| GET    | `/health`   | Checks system health              |
| POST   | `/generate` | Generates a legal document        |

---

## 7. Root API Development

The root endpoint was implemented to provide a basic confirmation that the LegalEaseAI API is running.

Example response:

```json
{
  "message": "LegalEase API is running"
}
```

This endpoint can be used to verify that the backend server has started successfully.

---

## 8. Health Check Development

The `/health` endpoint is implemented to check the availability of the backend service.

It can be used during development and testing to verify that the API is responding correctly.

---

## 9. Document Generation API

The `/generate` endpoint is the main API endpoint of the system.

It accepts information required to generate a legal document.

### Request structure

```json
{
  "document_type": "Freelance Work Contract",
  "parties": "Jane Doe (Service Provider), TechNova Inc. (Client)",
  "terms": "Payment to be made within 30 days of invoice; The provider agrees to deliver work by the agreed deadline; Confidentiality must be maintained at all times; Either party may terminate with 15 days notice",
  "effective_date": "2026-09-24"
}
```

### Input fields

| Field            | Description                                    |
| ---------------- | ---------------------------------------------- |
| `document_type`  | Type of legal document to generate             |
| `parties`        | Names and roles of involved parties            |
| `terms`          | Main terms and conditions                      |
| `effective_date` | Date from which the document becomes effective |

---

## 10. AI Document Generation Workflow

The AI document generation process follows these steps:

```text
User Input
    ↓
Frontend
    ↓
FastAPI Backend
    ↓
Input Validation
    ↓
AI Processing
    ↓
Generated Legal Draft
    ↓
Backend Response
    ↓
Frontend Display
```

The system converts the user's basic information into a structured prompt and sends the required information to the AI service.

The generated response is then returned to the application for display and further processing.

---

## 11. Document Types

The application is designed to support different types of legal documents.

Examples include:

* Agreements
* Contracts
* Non-Disclosure Agreements
* Lease Agreements
* Employment Offer Letters
* Freelance Work Contracts
* Other structured legal document drafts

The document type is provided by the user and used during AI generation.

---

## 12. Input Validation

Input validation is implemented to reduce invalid requests.

The system checks important input fields such as:

* Document type
* Parties
* Terms
* Effective date

Invalid or incomplete requests can be handled through appropriate error responses.

This improves the reliability of the application.

---

## 13. Error Handling

Error handling is included during development to identify and manage application failures.

Potential errors include:

* Missing input fields.
* Invalid request data.
* Backend connection errors.
* AI API errors.
* API quota limitations.
* Unexpected server errors.

The backend returns appropriate HTTP responses when possible so that problems can be identified during development and testing.

---

## 14. Environment Configuration

Sensitive configuration values are managed using environment variables.

The project uses a `.env` file for local development configuration.

Example:

```text
GEMINI_API_KEY=your_api_key
```

The actual API key is not included in the public GitHub repository.

The `.gitignore` file is used to prevent sensitive configuration files from being committed accidentally.

---

## 15. Dependency Management

The project dependencies are maintained using:

```text
requirements.txt
```

The required Python packages can be installed using:

```powershell
python -m pip install -r requirements.txt
```

A Python virtual environment is used to keep project dependencies isolated.

Example:

```powershell
python -m venv .venv
```

To activate the virtual environment in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 16. Running the Backend

After installing the required dependencies, the FastAPI backend can be started using the appropriate Uvicorn command.

Example:

```powershell
uvicorn backend.main:app --reload
```

The development server runs locally and provides access to the API.

Example:

```text
http://127.0.0.1:8000
```

---

## 17. Swagger API Documentation

FastAPI automatically provides interactive API documentation.

The Swagger UI can be accessed at:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows developers to:

* View available endpoints.
* View request structures.
* Send API requests.
* Test API responses.
* Identify API errors.
* Verify backend functionality.

The `/generate` endpoint was tested using Swagger UI during development.

---

## 18. Frontend Development

The frontend was designed to provide a simple interface for interacting with LegalEaseAI.

The interface is intended to allow users to enter:

1. Document type.
2. Party information.
3. Legal terms.
4. Effective date.

The entered information is submitted to the backend API.

The generated result can then be displayed to the user.

---

## 19. Frontend to Backend Communication

The frontend communicates with the FastAPI backend using HTTP requests.

The general process is:

```text
Frontend Form
      ↓
Collect User Data
      ↓
Create JSON Request
      ↓
POST /generate
      ↓
FastAPI Backend
      ↓
AI Document Generation
      ↓
JSON Response
      ↓
Display Result
```

This architecture separates the user interface from the backend processing logic.

---

## 20. AI Prompt Processing

The AI generation component uses the provided document information to construct a structured legal document draft.

The prompt processing considers:

* Document type.
* Parties.
* Terms and conditions.
* Effective date.
* Required document structure.

The generated document is intended to be clear, structured, and suitable as a starting draft.

---

## 21. Document Formatting

The generated legal document is organized into appropriate sections depending on the requested document type.

Typical sections may include:

* Title
* Effective Date
* Parties
* Definitions
* Terms and Conditions
* Responsibilities
* Confidentiality
* Payment Terms
* Termination
* Signatures

The exact sections depend on the type and information provided by the user.

---

## 22. Security Implementation

Security considerations during development include:

* Protecting API keys.
* Using environment variables.
* Excluding `.env` from Git.
* Validating user input.
* Avoiding unnecessary exposure of sensitive information.
* Separating configuration from source code.

The project is intended for educational and prototype purposes.

---

## 23. Version Control

Git was used throughout the development process.

The GitHub repository is:

```text
https://github.com/nihas-adil/LegalEase-AI-Powered-Legal-Document-Generator.git
```

Development changes are committed with descriptive commit messages.

The project follows a phase-wise documentation approach so that the development progress can be tracked.

---

## 24. Development Milestones Completed

The following development milestones have been achieved:

### Milestone 1 – Project Setup

* Project repository created.
* Project folders organized.
* Python environment configured.
* Required dependencies prepared.

### Milestone 2 – Backend Setup

* FastAPI backend implemented.
* Backend server tested.
* Root endpoint implemented.
* Health endpoint implemented.

### Milestone 3 – API Development

* Document generation endpoint implemented.
* Request structure defined.
* Input fields configured.
* Swagger API documentation verified.

### Milestone 4 – AI Integration

* Google Gemini API integration implemented.
* AI prompt processing connected to document generation.
* Generated document workflow established.

### Milestone 5 – Testing Preparation

* API requests tested.
* Error handling reviewed.
* AI quota/error conditions identified.
* System prepared for dedicated testing phase.

---

## 25. Development Challenges

During development, several technical challenges were encountered.

### 25.1 Dependency Installation

Some Python packages were initially unavailable in the development environment.

The required dependencies were installed using pip.

### 25.2 API Configuration

The AI API required correct environment configuration and API key management.

Environment variables were used to avoid exposing credentials.

### 25.3 AI API Quota

During testing, the Gemini API returned a `RESOURCE_EXHAUSTED` / HTTP 429 error when the free-tier request quota was exceeded.

This demonstrated the importance of handling external API limitations during application development.

The application should therefore handle AI service errors gracefully.

### 25.4 Cloud Deployment

Cloud deployment may require additional cloud billing configuration depending on the selected deployment service.

For the current academic prototype, local development and API testing are used as the primary development environment.

---

## 26. Current Development Status

The major development components of LegalEaseAI have been implemented.

Current status:

| Component             | Status                        |
| --------------------- | ----------------------------- |
| Project Structure     | Completed                     |
| Backend Setup         | Completed                     |
| FastAPI API           | Completed                     |
| Root Endpoint         | Completed                     |
| Health Endpoint       | Completed                     |
| Generate Endpoint     | Completed                     |
| Swagger Documentation | Completed                     |
| AI Integration        | Implemented                   |
| Input Validation      | Implemented                   |
| Error Handling        | Implemented                   |
| Frontend Integration  | In Development / Verification |
| Full System Testing   | Next Phase                    |

---

## 27. Development Outcome

The development phase successfully transformed the planned design into an implemented software prototype.

The LegalEaseAI system now contains the core components required for:

* Receiving legal document requirements.
* Processing user inputs.
* Communicating with the AI service.
* Generating structured legal document drafts.
* Providing API-based interaction.
* Testing the application through Swagger UI.

---

## 28. Legal and Educational Disclaimer

LegalEaseAI is an educational software project developed as part of the Naan Mudhalvan academic project.

The generated documents are AI-assisted drafts and should not be considered professional legal advice.

Users should consult a qualified legal professional before relying on any generated document for an actual legal matter.

---

## 29. Phase Completion

**Phase 05 – Project Development: Completed**

The core development work has been implemented and the application is ready to proceed to the dedicated testing phase.

### Next Phase

**Phase 06 – Project Testing**

The next phase will focus on:

* Functional testing.
* API testing.
* Input validation testing.
* Error handling testing.
* AI integration testing.
* User interface testing.
* Test cases.
* Test results.
* Bug identification and resolution.
* Final system verification.
