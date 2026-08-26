import os
import re
import json
import zipfile
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup

# ---------------------------------------------------------
# 1. PAGE CONFIG & DESIGN SCAFFOLDING
# ---------------------------------------------------------
st.set_page_config(
    page_title="Kasa Twi System & Phrasebook",
    page_icon="🗣️",
    layout="wide"
)

st.markdown("""
    <style>
        .stMetric { background-color: #f8f9fa; padding: 15px; border-radius: 10px; }
        .phrase-card { background: #f0f2f6; padding: 15px; border-radius: 8px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. BACKEND EXTRACTION & DATA ENGINE
# ---------------------------------------------------------
@st.cache_data
def extract_and_parse_zip(zip_path="files (4).zip"):
    """
    Backend service to dynamically extract ZIP archives and parse 
    dataset files into structured data.
    """
    phrases = []
    docs = ""
    
    if not os.path.exists(zip_path):
        return pd.DataFrame(), "Zip archive file not found."

    try:
        with zipfile.ZipFile(zip_path, 'r') as archive:
            for file_name in archive.namelist():
                # Extract HTML dataset
                if file_name.endswith('.html'):
                    with archive.open(file_name) as f:
                        soup = BeautifulSoup(f.read(), 'html.parser')
                        # Extraction Strategy: Look for tabular data or list elements
                        rows = soup.find_all('tr')
                        for row in rows:
                            cols = [ele.text.strip() for ele in row.find_all(['td', 'th'])]
                            if len(cols) >= 2:
                                phrases.append({"English": cols[0], "Twi": cols[1], "Category": "General"})
                        
                        # Fallback parsing strategy for structured phrase elements
                        if not phrases:
                            items = soup.find_all(['li', 'div', 'p'])
                            for item in items:
                                text = item.text.strip()
                                if ":" in text or "-" in text:
                                    parts = re.split(r'[:\-]', text, maxsplit=1)
                                    if len(parts) == 2:
                                        phrases.append({
                                            "English": parts[0].strip(),
                                            "Twi": parts[1].strip(),
                                            "Category": "General"
                                        })

                # Extract Markdown documentation context
                elif file_name.endswith('.md'):
                    with archive.open(file_name) as f:
                        docs += f.read().decode('utf-8', errors='ignore') + "\n\n"

        # Construct DataFrame Backend
        df = pd.DataFrame(phrases).drop_duplicates()
        if df.empty:
            # Starter fallback dataset if extraction targets non-standard layout
            df = pd.DataFrame([
                {"Category": "Greetings", "English": "Good morning", "Twi": "Maakye"},
                {"Category": "Greetings", "English": "Good afternoon", "Twi": "Maaha"},
                {"Category": "Greetings", "English": "Good evening", "Twi": "Maadwo"},
                {"Category": "Basics", "English": "Thank you", "Twi": "Medaase"},
                {"Category": "Basics", "English": "Please", "Twi": "Mepaakyew"},
                {"Category": "Basics", "English": "Yes", "Twi": "Aane"},
                {"Category": "Basics", "English": "No", "Twi": "Daabi"}
            ])
            
        return df, docs
    except Exception as e:
        st.error(f"Engine Extraction Error: {str(e)}")
        return pd.DataFrame(), ""

# Initialize dataset backend into session state memory
df_phrases, docs_content = extract_and_parse_zip()

if "dataset" not in st.session_state:
    st.session_state.dataset = df_phrases

# ---------------------------------------------------------
# 3. INTERACTIVE FRONTEND UI & CONTROLLERS
# ---------------------------------------------------------
st.title("🗣️ Kasa Twi Interactive System")
st.caption("Backend Auto-Synced Engine | Dynamic Translation & Phrasebook Hub")

tab1, tab2, tab3 = st.tabs(["📖 Phrasebook", "🔄 Translator", "📄 System Specs & Data"])

# --- TAB 1: PHRASEBOOK ---
with tab1:
    st.subheader("Dynamic Phrasebook")
    
    col_filter, col_search = st.columns([1, 2])
    
    categories = ["All"] + sorted(list(st.session_state.dataset["Category"].unique()))
    with col_filter:
        selected_cat = st.selectbox("Category Filter", categories)
    with col_search:
        search_query = st.text_input("🔍 Search phrases (English or Twi)...", "")

    # Reactive Backend Querying
    filtered_df = st.session_state.dataset.copy()
    if selected_cat != "All":
        filtered_df = filtered_df[filtered_df["Category"] == selected_cat]
    if search_query:
        filtered_df = filtered_df[
            filtered_df["English"].str.contains(search_query, case=False, na=False) |
            filtered_df["Twi"].str.contains(search_query, case=False, na=False)
        ]

    # Render Synced Table
    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Category": st.column_config.TextColumn("Category", width="medium"),
            "English": st.column_config.TextColumn("English Phrase"),
            "Twi": st.column_config.TextColumn("Twi Translation"),
        }
    )
    st.caption(f"Showing **{len(filtered_df)}** entries out of **{len(st.session_state.dataset)}** total loaded phrases.")

# --- TAB 2: TRANSLATOR ENGINE ---
with tab2:
    st.subheader("Instant Translation Lookup")
    
    direction = st.radio("Direction", ["English ➔ Twi", "Twi ➔ English"], horizontal=True)
    input_phrase = st.text_input("Enter text to translate:")
    
    if input_phrase:
        query = input_phrase.strip().lower()
        engine_data = st.session_state.dataset
        
        if direction == "English ➔ Twi":
            match = engine_data[engine_data["English"].str.lower() == query]
            target_col, result_col = "English", "Twi"
        else:
            match = engine_data[engine_data["Twi"].str.lower() == query]
            target_col, result_col = "Twi", "English"
            
        if not match.empty:
            result = match.iloc[0][result_col]
            st.success(f"**Translation:** {result}")
        else:
            # Perform Partial Matching fallback
            st.warning("Exact phrase match not found in local backend. Partial matches below:")
            partials = engine_data[
                engine_data["English"].str.lower().str.contains(query, na=False) |
                engine_data["Twi"].str.lower().str.contains(query, na=False)
            ]
            if not partials.empty:
                st.dataframe(partials, use_container_width=True, hide_index=True)
            else:
                st.error("No relevant matches found in dataset.")

# --- TAB 3: SYSTEM SPECIFICATIONS & LOGS ---
with tab3:
    st.subheader("System Documentation & Raw Backend State")
    if docs_content:
        with st.expander("View Documentation (`kasa-system-documentation.md`)", expanded=True):
            st.markdown(docs_content)
    
    st.subheader("Add Data Record (Syncs Instantly)")
    with st.form("new_phrase_form"):
        c1, c2, c3 = st.columns(3)
        with c1: new_cat = st.text_input("Category", "General")
        with c2: new_eng = st.text_input("English Phrase")
        with c3: new_twi = st.text_input("Twi Translation")
        
        if st.form_submit_button("Sync to System"):
            if new_eng and new_twi:
                new_row = pd.DataFrame([{"Category": new_cat, "English": new_eng, "Twi": new_twi}])
                st.session_state.dataset = pd.concat([st.session_state.dataset, new_row], ignore_index=True)
                st.success("Dataset successfully updated!")
                st.rerun()
            else:
                st.error("Fields cannot be empty.")