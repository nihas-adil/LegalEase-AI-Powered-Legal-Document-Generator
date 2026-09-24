# =========================================================
# PROJECT PATH FIX
# =========================================================

import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# =========================================================
# IMPORTS
# =========================================================

from datetime import date

import requests
import streamlit as st

from services.document_formatter import (
    format_docx,
    format_html_preview,
    format_pdf,
    format_txt,
)

from utils.config import (
    BACKEND_URL,
    REQUEST_TIMEOUT_SECONDS,
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="LegalEase AI",
    page_icon="⚖️",
    layout="wide",
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #777;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 700;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    .legal-preview {
        background-color: white;
        color: black;
        padding: 24px;
        border-radius: 10px;
        border: 1px solid #ddd;
        font-family: "Times New Roman", serif;
        font-size: 16px;
        line-height: 1.7;
        min-height: 500px;
        white-space: pre-wrap;
        word-break: normal;
        overflow-wrap: normal;
        width: 100%;
        box-sizing: border-box;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">⚖️ LegalEase AI</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">AI-powered Legal Document Generator</div>',
    unsafe_allow_html=True,
)


# =========================================================
# SESSION STATE
# =========================================================

if "document" not in st.session_state:
    st.session_state.document = ""

if "generated" not in st.session_state:
    st.session_state.generated = False

if "edit_mode" not in st.session_state:
    st.session_state.edit_mode = False


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("Document Details")

    document_type = st.text_input(
        "Document Type",
        placeholder="Example: Freelance Work Contract",
        help=(
            "Type the legal document you want to generate. "
            "Examples: Agreement, Contract, NDA, Lease Agreement, "
            "Employment Offer Letter."
        ),
        key="document_type_input",
    )

    parties = st.text_area(
        "Parties Involved",
        placeholder=(
            "Example:\n"
            "Jane Doe (Service Provider), "
            "TechNova Inc. (Client)"
        ),
        height=120,
        help=(
            "Enter the names and roles of the individuals "
            "or entities involved in the document."
        ),
        key="parties_input",
    )

    terms = st.text_area(
        "Terms & Conditions",
        placeholder=(
            "Example:\n"
            "Payment to be made within 30 days of invoice; "
            "The provider agrees to deliver work by the agreed deadline; "
            "Confidentiality must be maintained at all times; "
            "Either party may terminate with 15 days notice"
        ),
        height=180,
        help=(
            "Separate each term using a semicolon (;)."
        ),
        key="terms_input",
    )

    st.caption(
        "💡 Use semicolons (;) to separate each term."
    )

    effective_date = st.date_input(
        "Effective Date",
        value=date.today(),
        help=(
            "Select the date when the agreement becomes "
            "legally valid."
        ),
        key="effective_date_input",
    )

    generate_button = st.button(
        "Generate Document",
        width="stretch",
        type="primary",
    )


# =========================================================
# GENERATE DOCUMENT
# =========================================================

if generate_button:

    clean_document_type = document_type.strip()
    clean_parties = parties.strip()
    clean_terms = terms.strip()
    clean_date = effective_date.isoformat()

    if not clean_document_type:
        st.error("Please enter the document type.")
        st.stop()

    if not clean_parties:
        st.error("Please enter the parties involved.")
        st.stop()

    if not clean_terms:
        st.error("Please enter the terms and conditions.")
        st.stop()

    payload = {
        "document_type": clean_document_type,
        "parties": clean_parties,
        "terms": clean_terms,
        "effective_date": clean_date,
    }

    try:

        with st.spinner("Generating legal document..."):

            response = requests.post(
                f"{BACKEND_URL}/generate",
                json=payload,
                timeout=REQUEST_TIMEOUT_SECONDS,
            )

        if response.status_code == 200:

            result = response.json()

            generated_content = result.get(
                "content",
                "",
            )

            if not generated_content:

                st.error(
                    "Backend returned an empty document."
                )

            else:

                st.session_state.document = generated_content
                st.session_state.generated = True
                st.session_state.edit_mode = False

                st.session_state.document_type = (
                    clean_document_type
                )

                st.session_state.parties = clean_parties

                st.session_state.terms = clean_terms

                st.session_state.effective_date = clean_date

                st.success(
                    "Document generated successfully!"
                )

        else:

            st.error(
                f"Backend error: {response.status_code}"
            )

            try:

                error_details = response.json()

                st.code(
                    str(error_details)
                )

            except Exception:

                st.code(
                    response.text
                )

    except requests.exceptions.ConnectionError:

        st.error(
            "Cannot connect to LegalEase backend."
        )

        st.info(
            "Make sure FastAPI is running on port 8000."
        )

    except requests.exceptions.Timeout:

        st.error(
            "Request timed out. Please try again."
        )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )


# =========================================================
# DOCUMENT SECTION
# =========================================================

if st.session_state.document:

    st.divider()

    st.markdown(
        '<div class="section-title">Document Preview</div>',
        unsafe_allow_html=True,
    )

    preview_html = format_html_preview(
        st.session_state.document
    )

    st.markdown(
        preview_html,
        unsafe_allow_html=True,
    )

    st.divider()

    # =====================================================
    # EDIT BUTTON
    # =====================================================

    if not st.session_state.edit_mode:

        edit_button = st.button(
            "Edit Document",
            width="stretch",
            type="secondary",
        )

        if edit_button:

            st.session_state.edit_mode = True
            st.rerun()

    # =====================================================
    # EDIT MODE
    # =====================================================

    if st.session_state.edit_mode:

        st.markdown(
            '<div class="section-title">Edit Document</div>',
            unsafe_allow_html=True,
        )

        edited_document = st.text_area(
            "Editable Document Text",
            value=st.session_state.document,
            height=600,
            label_visibility="collapsed",
            key="document_editor",
        )

        save_col, cancel_col = st.columns(2)

        with save_col:

            save_button = st.button(
                "Save Changes",
                width="stretch",
                type="primary",
            )

        with cancel_col:

            cancel_button = st.button(
                "Cancel",
                width="stretch",
            )

        if save_button:

            st.session_state.document = edited_document
            st.session_state.edit_mode = False

            st.success(
                "Changes saved successfully!"
            )

            st.rerun()

        if cancel_button:

            st.session_state.edit_mode = False
            st.rerun()

        st.divider()

    # =====================================================
    # DOWNLOAD SECTION
    # =====================================================

    st.markdown(
        '<div class="section-title">Download Document</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    clean_document = (
        st.session_state.document
        .replace("**", "")
        .replace("\\_", "_")
    )

    saved_document_type = st.session_state.get(
        "document_type",
        document_type,
    )

    saved_parties = st.session_state.get(
        "parties",
        parties,
    )

    saved_terms = st.session_state.get(
        "terms",
        terms,
    )

    saved_effective_date = st.session_state.get(
        "effective_date",
        effective_date.isoformat(),
    )

    # =====================================================
    # DOCX
    # =====================================================

    with col1:

        try:

            docx_data = format_docx(
                text=clean_document,
                doc_type=saved_document_type,
                parties=saved_parties,
                terms=saved_terms,
                effective_date=saved_effective_date,
            )

            st.download_button(
                label="Download DOCX",
                data=docx_data,
                file_name="LegalEase_Document.docx",
                mime=(
                    "application/vnd.openxmlformats-officedocument."
                    "wordprocessingml.document"
                ),
                width="stretch",
            )

        except Exception as e:

            st.error(
                f"DOCX error: {str(e)}"
            )

    # =====================================================
    # PDF
    # =====================================================

    with col2:

        try:

            pdf_data = format_pdf(
                text=clean_document,
                doc_type=saved_document_type,
                effective_date=saved_effective_date,
            )

            st.download_button(
                label="Download PDF",
                data=pdf_data,
                file_name="LegalEase_Document.pdf",
                mime="application/pdf",
                width="stretch",
            )

        except Exception as e:

            st.error(
                f"PDF error: {str(e)}"
            )

    # =====================================================
    # TXT
    # =====================================================

    with col3:

        try:

            txt_data = format_txt(
                clean_document
            )

            st.download_button(
                label="Download TXT",
                data=txt_data,
                file_name="LegalEase_Document.txt",
                mime="text/plain",
                width="stretch",
            )

        except Exception as e:

            st.error(
                f"TXT error: {str(e)}"
            )


# =========================================================
# EMPTY STATE
# =========================================================

else:

    st.info(
        "Enter the document details from the sidebar "
        "and click Generate Document."
    )