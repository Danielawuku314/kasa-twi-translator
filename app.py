import os
import re
import zipfile
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup

# ---------------------------------------------------------
# 1. PAGE LAYOUT & CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Kasa Twi Translator & Phrasebook",
    page_icon="🗣️",
    layout="wide"
)

# ---------------------------------------------------------
# 2. BACKEND EXTRACTION ENGINE
# ---------------------------------------------------------
@st.cache_data
def load_and_parse_zip(zip_path="files (4).zip"):
    """
    Extracts binary dataset archive and builds phrasebook data structure.
    """
    phrases = []
    documentation = ""

    if not os.path.exists(zip_path):
        st.error(f"Archive file `{zip_path}` not found in root path.")
        return pd.DataFrame(), ""

    try:
        with zipfile.ZipFile(zip_path, 'r') as archive:
            for file_info in archive.infolist():
                # Process HTML Phrasebook Dataset
                if file_info.filename.endswith('.html'):
                    with archive.open(file_info) as f:
                        soup = BeautifulSoup(f.read(), 'html.parser')
                        
                        # Strategy A: Table Row Parsing
                        rows = soup.find_all('tr')
                        for row in rows:
                            cols = [col.get_text(strip=True) for col in row.find_all(['td', 'th'])]
                            if len(cols) >= 2 and cols[0].lower() not in ['english', 'en']:
                                phrases.append({
                                    "English": cols[0],
                                    "Twi": cols[1],
                                    "Category": cols[2] if len(cols) > 2 else "General"
                                })

                        # Strategy B: Structured List / Key-Value Parsing
                        if not phrases:
                            elements = soup.find_all(['li', 'p', 'div'])
                            for el in elements:
                                text = el.get_text(strip=True)
                                if ":" in text or "—" in text or "-" in text:
                                    parts = re.split(r'[:—\-]', text, maxsplit=1)
                                    if len(parts) == 2 and parts[0].strip():
                                        phrases.append({
                                            "English": parts[0].strip(),
                                            "Twi": parts[1].strip(),
                                            "Category": "General"
                                        })

                # Process Markdown System Documentation
                elif file_info.filename.endswith('.md'):
                    with archive.open(file_info) as f:
                        documentation += f.read().decode('utf-8', errors='ignore') + "\n\n"

    except Exception as err:
        st.error(f"Error reading zip archive: {err}")

    # Build DataFrame
    df = pd.DataFrame(phrases).drop_duplicates()

    # Fallback dataset if archive parsing yields empty structure
    if df.empty:
        df = pd.DataFrame([
            {"English": "Good morning", "Twi": "Maakye", "Category": "Greetings"},
            {"English": "Good afternoon", "Twi": "Maaha", "Category": "Greetings"},
            {"English": "Good evening", "Twi": "Maadwo", "Category": "Greetings"},
            {"English": "Thank you", "Twi": "Medaase", "Category": "Basics"},
            {"English": "Please", "Twi": "Mepaakyew", "Category": "Basics"},
            {"English": "Yes", "Twi": "Aane", "Category": "Basics"},
            {"English": "No", "Twi": "Daabi", "Category": "Basics"}
        ])

    return df, documentation

# Load backend data
df_phrases, docs_text = load_and_parse_zip()

# Maintain reactive state
if "dataset" not in st.session_state:
    st.session_state.dataset = df_phrases

# ---------------------------------------------------------
# 3. FRONTEND UI & INTERACTION
# ---------------------------------------------------------
st.title("🗣️ Kasa Twi Translator & Phrasebook")

tab_phrasebook, tab_translator, tab_docs = st.tabs(["📖 Phrasebook", "🔄 Translator Engine", "📄 Documentation"])

# --- TAB 1: PHRASEBOOK VIEW ---
with tab_phrasebook:
    st.subheader("Interactive Phrasebook")
    
    col_cat, col_search = st.columns([1, 2])
    categories = ["All"] + sorted(list(st.session_state.dataset["Category"].unique()))
    
    with col_cat:
        selected_category = st.selectbox("Category Filter", categories)
    with col_search:
        search_query = st.text_input("🔍 Search (English or Twi)...")

    # Reactive Filtering
    view_df = st.session_state.dataset.copy()
    if selected_category != "All":
        view_df = view_df[view_df["Category"] == selected_category]
    if search_query:
        view_df = view_df[
            view_df["English"].str.contains(search_query, case=False, na=False) |
            view_df["Twi"].str.contains(search_query, case=False, na=False)
        ]

    st.dataframe(
        view_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Category": st.column_config.TextColumn("Category", width="medium"),
            "English": st.column_config.TextColumn("English Phrase"),
            "Twi": st.column_config.TextColumn("Twi Phrase")
        }
    )
    st.caption(f"Displaying **{len(view_df)}** of **{len(st.session_state.dataset)}** loaded entries.")

# --- TAB 2: TRANSLATOR ENGINE ---
with tab_translator:
    st.subheader("Translation Engine")
    
    direction = st.radio("Direction", ["English ➔ Twi", "Twi ➔ English"], horizontal=True)
    input_text = st.text_input("Enter text to translate:")
    
    if input_text:
        query = input_text.strip().lower()
        dataset = st.session_state.dataset
        
        if direction == "English ➔ Twi":
            exact = dataset[dataset["English"].str.lower() == query]
            target_col = "Twi"
        else:
            exact = dataset[dataset["Twi"].str.lower() == query]
            target_col = "English"
            
        if not exact.empty:
            st.success(f"**Translation:** {exact.iloc[0][target_col]}")
        else:
            st.warning("Exact match not found. Showing partial matches:")
            partials = dataset[
                dataset["English"].str.lower().str.contains(query, na=False) |
                dataset["Twi"].str.lower().str.contains(query, na=False)
            ]
            if not partials.empty:
                st.dataframe(partials, use_container_width=True, hide_index=True)
            else:
                st.error("No relevant matches found in dataset.")

# --- TAB 3: DOCUMENTATION & MANAGEMENT ---
with tab_docs:
    st.subheader("System Documentation")
    if docs_text:
        st.markdown(docs_text)
    else:
        st.info("No system documentation provided in archive.")

    st.divider()
    st.subheader("Add Entry to Current Session")
    with st.form("add_phrase_form"):
        c1, c2, c3 = st.columns(3)
        with c1: new_cat = st.text_input("Category", "General")
        with c2: new_eng = st.text_input("English")
        with c3: new_twi = st.text_input("Twi")
        
        if st.form_submit_button("Sync Phrase"):
            if new_eng and new_twi:
                new_row = pd.DataFrame([{"Category": new_cat, "English": new_eng, "Twi": new_twi}])
                st.session_state.dataset = pd.concat([st.session_state.dataset, new_row], ignore_index=True)
                st.success("Entry synced to session dataset.")
                st.rerun()