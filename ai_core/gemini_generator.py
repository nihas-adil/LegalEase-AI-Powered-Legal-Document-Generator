import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiDocumentGenerator:

    def __init__(self):

        self.api_key = os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in .env file"
            )

        self.client = genai.Client(
            api_key=self.api_key
        )

        self.model = os.getenv(
            "GEMINI_MODEL",
            "gemini-3.6-flash"
        )

    def generate_document(
        self,
        document_type: str,
        parties: str,
        terms: str,
        effective_date: str,
    ) -> str:

        prompt = f"""
You are LegalEase AI, an AI-powered legal document
drafting assistant.

Generate a professional legal document based on the
information provided by the user.

DOCUMENT TYPE:
{document_type}

PARTIES:
{parties}

EFFECTIVE DATE:
{effective_date}

IMPORTANT DATE RULE:
Use the EXACT effective date provided above.

Do not change, reinterpret, guess, or replace the
year, month, or day.

The effective date in the generated document MUST
exactly match the user's selected date.

TERMS AND CONDITIONS:
{terms}

Instructions:

1. Create a professional legal document.

2. Use the requested document type as the main title.

3. Include the effective date exactly as provided.

4. Clearly identify all parties.

5. Preserve all important terms provided by the user.

6. Organize the document into numbered legal sections.

7. Add appropriate standard clauses where necessary.

8. Use formal and professional legal language.

9. Include termination, confidentiality, governing law,
and entire agreement clauses where appropriate.

10. Include a signature section at the end.

11. Do not invent specific names, addresses, amounts,
dates, or facts that were not provided by the user.

12. Do not change the effective date.

13. Do not create a different date from the information
provided by the user.

14. Return only the final document text.

This document is an AI-generated draft and should be
reviewed by a qualified legal professional before use.
"""

        response = None

        for attempt in range(3):

            try:

                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt,
                )

                break

            except Exception as e:

                error_text = str(e).upper()

                if (
                    "503" in error_text
                    or "UNAVAILABLE" in error_text
                    or "SERVICE UNAVAILABLE" in error_text
                ):

                    if attempt < 2:

                        wait_time = 3 * (attempt + 1)

                        time.sleep(wait_time)

                        continue

                raise

        if response is None:
            raise ValueError(
                "Gemini did not return a response."
            )

        if not response.text:
            raise ValueError(
                "Gemini returned an empty response."
            )

        return response.text.strip()