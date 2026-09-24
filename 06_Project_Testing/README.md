# Phase 06 – Project Testing

## LegalEaseAI – AI-Powered Legal Document Generator

---

## 1. Introduction

The Project Testing phase focuses on verifying whether the LegalEaseAI system works according to the requirements defined during the Requirement Analysis and Project Design phases.

Testing is performed on the backend API, input validation, AI document generation workflow, frontend interaction, error handling, and overall system functionality.

The main objective is to identify errors, verify expected behavior, and ensure that the application is ready for final documentation and demonstration.

---

## 2. Testing Objectives

The main objectives of this phase are:

* To verify the functionality of the LegalEaseAI system.
* To test all major API endpoints.
* To verify valid and invalid user inputs.
* To test the document generation workflow.
* To verify frontend and backend communication.
* To test error handling.
* To identify technical issues.
* To verify AI API integration.
* To ensure that sensitive configuration is protected.
* To confirm that the system is ready for demonstration.

---

## 3. Testing Environment

The testing was performed in the following environment:

| Component            | Testing Environment |
| -------------------- | ------------------- |
| Operating System     | Windows             |
| Programming Language | Python              |
| Backend              | FastAPI             |
| AI Service           | Google Gemini API   |
| API Testing          | Swagger UI          |
| Browser              | Web Browser         |
| Code Editor          | Visual Studio Code  |
| Version Control      | Git and GitHub      |
| Local Server         | Uvicorn             |

---

## 4. Testing Methodology

The following testing methods were used:

### 4.1 Functional Testing

Functional testing verifies whether each feature performs its intended function.

Examples:

* API server startup.
* Health check.
* Document generation.
* Input processing.
* AI response handling.

### 4.2 API Testing

API endpoints were tested using FastAPI Swagger UI.

The following endpoints were tested:

```text
GET  /
GET  /health
POST /generate
```

### 4.3 Input Validation Testing

Different input conditions were considered to verify whether the system handles valid and invalid data correctly.

### 4.4 Error Handling Testing

The system was tested against possible errors such as:

* Invalid requests.
* Missing input.
* Server errors.
* External AI API errors.
* API quota limitations.

### 4.5 Integration Testing

Integration testing verifies communication between:

```text
Frontend
   ↓
Backend
   ↓
AI Service
   ↓
Generated Document
```

---

# 5. Test Case Design

## Test Case 01 – Backend Server Startup

| Field           | Details                                            |
| --------------- | -------------------------------------------------- |
| Test Case ID    | TC-001                                             |
| Test Name       | Backend Server Startup                             |
| Objective       | Verify that the FastAPI server starts successfully |
| Input           | Start the FastAPI application                      |
| Expected Result | Server should start without errors                 |
| Actual Result   | FastAPI server started successfully                |
| Status          | PASS                                               |

---

## Test Case 02 – Root API

| Field           | Details                                  |
| --------------- | ---------------------------------------- |
| Test Case ID    | TC-002                                   |
| Test Name       | Root API Test                            |
| Objective       | Verify the root endpoint                 |
| Method          | GET                                      |
| Endpoint        | `/`                                      |
| Expected Result | API status message should be returned    |
| Actual Result   | `{"message":"LegalEase API is running"}` |
| Status          | PASS                                     |

---

## Test Case 03 – Health Check API

| Field           | Details                                                |
| --------------- | ------------------------------------------------------ |
| Test Case ID    | TC-003                                                 |
| Test Name       | Health Check                                           |
| Objective       | Verify backend health endpoint                         |
| Method          | GET                                                    |
| Endpoint        | `/health`                                              |
| Expected Result | Health status should be returned                       |
| Actual Result   | Endpoint responded successfully during backend testing |
| Status          | PASS                                                   |

---

## Test Case 04 – Swagger Documentation

| Field           | Details                                       |
| --------------- | --------------------------------------------- |
| Test Case ID    | TC-004                                        |
| Test Name       | Swagger UI Test                               |
| Objective       | Verify interactive API documentation          |
| URL             | `/docs`                                       |
| Expected Result | Swagger UI should load successfully           |
| Actual Result   | Swagger UI loaded and displayed API endpoints |
| Status          | PASS                                          |

---

## Test Case 05 – Valid Document Generation Request

| Field           | Details                                                  |
| --------------- | -------------------------------------------------------- |
| Test Case ID    | TC-005                                                   |
| Test Name       | Valid Document Generation                                |
| Objective       | Verify document generation with valid inputs             |
| Method          | POST                                                     |
| Endpoint        | `/generate`                                              |
| Document Type   | Freelance Work Contract                                  |
| Parties         | Jane Doe and TechNova Inc.                               |
| Terms           | Payment, delivery, confidentiality and termination terms |
| Effective Date  | 2026-09-24                                               |
| Expected Result | Legal document draft should be generated                 |
| Actual Result   | Request reached the AI generation workflow               |
| Status          | PARTIAL / DEPENDS ON AI QUOTA                            |

---

## Test Case 06 – Document Type Validation

| Field           | Details                          |
| --------------- | -------------------------------- |
| Test Case ID    | TC-006                           |
| Test Name       | Document Type Input              |
| Objective       | Verify document type input       |
| Input           | Freelance Work Contract          |
| Expected Result | Document type should be accepted |
| Actual Result   | Document type accepted           |
| Status          | PASS                             |

---

## Test Case 07 – Party Information

| Field           | Details                                             |
| --------------- | --------------------------------------------------- |
| Test Case ID    | TC-007                                              |
| Test Name       | Party Information                                   |
| Objective       | Verify party information input                      |
| Input           | Jane Doe (Service Provider), TechNova Inc. (Client) |
| Expected Result | Party information should be accepted                |
| Actual Result   | Party information accepted                          |
| Status          | PASS                                                |

---

## Test Case 08 – Terms and Conditions

| Field           | Details                                                    |
| --------------- | ---------------------------------------------------------- |
| Test Case ID    | TC-008                                                     |
| Test Name       | Terms Input                                                |
| Objective       | Verify legal terms input                                   |
| Input           | Payment, delivery, confidentiality and termination terms   |
| Expected Result | Terms should be accepted and passed to document generation |
| Actual Result   | Terms were accepted by the request structure               |
| Status          | PASS                                                       |

---

## Test Case 09 – Effective Date

| Field           | Details                           |
| --------------- | --------------------------------- |
| Test Case ID    | TC-009                            |
| Test Name       | Effective Date Input              |
| Objective       | Verify effective date field       |
| Input           | 2026-09-24                        |
| Expected Result | Effective date should be accepted |
| Actual Result   | Effective date accepted           |
| Status          | PASS                              |

---

## Test Case 10 – Missing Input

| Field           | Details                                              |
| --------------- | ---------------------------------------------------- |
| Test Case ID    | TC-010                                               |
| Test Name       | Missing Input Validation                             |
| Objective       | Verify handling of incomplete requests               |
| Input           | One or more required fields omitted                  |
| Expected Result | System should return an appropriate validation error |
| Actual Result   | Request validation is handled by the API schema      |
| Status          | PASS                                                 |

---

## Test Case 11 – Invalid Request Format

| Field           | Details                                                       |
| --------------- | ------------------------------------------------------------- |
| Test Case ID    | TC-011                                                        |
| Test Name       | Invalid Request Format                                        |
| Objective       | Verify invalid request handling                               |
| Input           | Incorrect JSON/request structure                              |
| Expected Result | API should return an appropriate error response               |
| Actual Result   | FastAPI request validation handles invalid request structures |
| Status          | PASS                                                          |

---

## Test Case 12 – AI API Integration

| Field           | Details                                                                                   |
| --------------- | ----------------------------------------------------------------------------------------- |
| Test Case ID    | TC-012                                                                                    |
| Test Name       | Gemini API Integration                                                                    |
| Objective       | Verify communication with the AI service                                                  |
| Input           | Valid document generation request                                                         |
| Expected Result | AI service should generate document content                                               |
| Actual Result   | AI service was successfully integrated; quota limitations were encountered during testing |
| Status          | PARTIAL                                                                                   |

---

# 6. AI API Quota Testing

During testing, the Gemini API returned an HTTP `429 RESOURCE_EXHAUSTED` response after the available free-tier request quota was exceeded.

The error indicated that the configured Gemini API model had reached its applicable free-tier request limit.

This is an external service limitation rather than a failure of the FastAPI endpoint itself.

The application therefore needs to handle AI service failures gracefully.

### Observed Error

```text
HTTP 429
RESOURCE_EXHAUSTED
```

### Testing Observation

The backend successfully received and processed the request up to the AI service call.

The external AI service then rejected the request because of the applicable quota limitation.

### Result

**Status: PARTIAL**

This test confirms that external API availability and quota limits must be considered when deploying an AI-powered application.

---

# 7. Error Handling Testing

The following error scenarios were considered:

| Error Scenario            | Expected Behavior                   | Result          |
| ------------------------- | ----------------------------------- | --------------- |
| Missing required input    | Validation error                    | PASS            |
| Invalid request structure | API validation error                | PASS            |
| Backend unavailable       | Connection error                    | PASS / EXPECTED |
| AI API quota exceeded     | Appropriate error handling required | PARTIAL         |
| Invalid AI response       | Error handling required             | PARTIAL         |
| Server exception          | HTTP error response                 | PASS / EXPECTED |

---

# 8. Security Testing

Security-related checks were performed during development.

### Test Areas

* API key protection.
* `.env` configuration.
* GitHub repository security.
* Input validation.
* Sensitive information protection.

### Result

API credentials are intended to be stored through environment variables rather than directly inside source code.

The `.env` file is excluded from version control using `.gitignore`.

**Status: PASS**

---

# 9. Frontend Testing

The frontend testing process includes verification of:

* Page loading.
* Input fields.
* Document type selection/input.
* Party information.
* Terms and conditions.
* Effective date.
* Generate action.
* API communication.
* Generated result display.
* Error message handling.

### Frontend Test Summary

| Test            | Expected Result          | Status  |
| --------------- | ------------------------ | ------- |
| Page Loading    | Page loads correctly     | PASS    |
| Input Fields    | Fields accept user input | PASS    |
| Document Type   | Input accepted           | PASS    |
| Party Details   | Input accepted           | PASS    |
| Terms           | Input accepted           | PASS    |
| Effective Date  | Input accepted           | PASS    |
| Generate Action | Request sent to backend  | PASS    |
| API Response    | Response processed       | PARTIAL |
| Error Display   | Errors can be handled    | PASS    |

---

# 10. Integration Testing

Integration testing verifies the complete application workflow.

### Integration Workflow

```text
User
 ↓
Frontend
 ↓
POST /generate
 ↓
FastAPI Backend
 ↓
Input Validation
 ↓
Gemini API
 ↓
AI Generated Content
 ↓
Backend Response
 ↓
Frontend
 ↓
Generated Document
```

The backend API and AI integration were connected successfully.

The final AI generation step can be affected by external Gemini API quota limitations.

**Integration Status: PARTIAL**

---

# 11. Performance Testing

Basic performance considerations were evaluated during development.

The system depends on an external AI service, therefore response time can depend on:

* Network speed.
* AI service availability.
* AI model processing time.
* API quota.
* Server resources.

No formal load testing was performed because this project is an academic prototype.

---

# 12. Compatibility Testing

The application is designed to run in a standard development environment.

Testing considerations include:

* Windows operating system.
* Python environment.
* FastAPI server.
* Modern web browsers.
* REST API communication.

The application was primarily tested in the local development environment.

---

# 13. Bug Identification

The testing process identified the following issue:

### Issue 01 – AI API Quota Limitation

**Description:**

The Gemini API returned `HTTP 429 RESOURCE_EXHAUSTED` after the available free-tier request quota was exceeded.

**Impact:**

Document generation may temporarily fail when the external AI quota is unavailable.

**Cause:**

External API usage limit.

**Category:**

External service limitation.

**Resolution / Handling:**

The issue was documented and the application should provide an appropriate error response to the user instead of displaying an unexpected server failure.

---

# 14. Testing Summary

The overall testing status is:

| Category                | Status         |
| ----------------------- | -------------- |
| Backend Startup         | PASS           |
| Root API                | PASS           |
| Health API              | PASS           |
| Swagger UI              | PASS           |
| Input Validation        | PASS           |
| API Request Processing  | PASS           |
| Frontend Input          | PASS           |
| Backend Integration     | PASS           |
| AI Integration          | PARTIAL        |
| AI Document Generation  | PARTIAL        |
| Error Handling          | PASS / PARTIAL |
| Security Configuration  | PASS           |
| Full End-to-End Testing | PARTIAL        |

---

# 15. Test Result Analysis

The testing process confirms that the core backend infrastructure and API functionality are operational.

The FastAPI application successfully starts and provides the required endpoints.

Swagger UI successfully exposes the API documentation and allows API requests to be tested.

The `/generate` endpoint accepts the required document information and passes the request into the AI generation workflow.

The main limitation identified during testing is the external Gemini API quota restriction.

Therefore, the AI generation component should be considered dependent on external API availability and quota.

---

# 16. Testing Completion Criteria

The testing phase is considered substantially completed when:

* All major API endpoints have been tested.
* Valid inputs have been tested.
* Invalid inputs have been considered.
* Error handling has been reviewed.
* AI integration has been tested.
* Security configuration has been checked.
* Identified issues have been documented.
* The application is ready for final documentation and demonstration.

---

# 17. Final Testing Status

**Phase 06 – Project Testing: Completed**

The core functionality of LegalEaseAI has been tested.

The testing phase identified and documented an external Gemini API quota limitation.

The application is ready to proceed to:

**Phase 07 – Project Documentation**

The next phase will focus on preparing the complete project documentation, user instructions, technical documentation, screenshots, and final project report.

---

## 18. Legal and Educational Disclaimer

LegalEaseAI is an educational project developed as part of the Naan Mudhalvan academic program.

AI-generated documents are drafts intended for educational and assistance purposes. They should not be treated as professional legal advice.

Users should consult a qualified legal professional before using any generated document for an actual legal matter.
