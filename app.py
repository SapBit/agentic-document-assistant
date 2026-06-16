import streamlit as st
import os
from dotenv import load_dotenv

from agents.document_agent import check_and_improve_document
from agents.summary_agent import summarize_document, create_bullet_summary
from agents.info_agent import extract_information, collect_topic_information, generate_report
from utils.file_handler import extract_text_from_file, save_output

load_dotenv()

st.set_page_config(
    page_title="Agentic AI Document Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); }
    .stApp > header { background: transparent !important; }
    .block-container { padding-top: 1.5rem !important; }
    h1, h2, h3, p, li, .markdown-text-container, .stMarkdown { color: #e0e0e0 !important; }
    .stTabs [data-baseweb="tab-list"] { background: rgba(255,255,255,0.06); border-radius: 10px; gap: 0; padding: 0.2rem; }
    .stTabs [data-baseweb="tab"] { color: #aaa !important; border-radius: 8px; font-weight: 500; }
    .stTabs [aria-selected="true"] { background: rgba(255,255,255,0.12) !important; color: #fff !important; }
    .stButton button { border-radius: 8px; font-weight: 500; border: none !important; }
    .stButton button:hover { transform: translateY(-1px); box-shadow: 0 4px 14px rgba(0,0,0,0.3); }
    .stDownloadButton button { border-radius: 8px; font-weight: 500; }
    .stTextInput input { background: rgba(255,255,255,0.08) !important; color: #e0e0e0 !important; border: 1px solid rgba(255,255,255,0.15) !important; border-radius: 8px !important; }
    .stTextInput input:focus { border-color: #6c63ff !important; box-shadow: 0 0 0 2px rgba(108,99,255,0.2) !important; }
    .stTextInput label { color: #ccc !important; }
    .stTextArea textarea { background: rgba(255,255,255,0.06) !important; color: #e0e0e0 !important; border: 1px solid rgba(255,255,255,0.1) !important; border-radius: 8px !important; }
    .stInfo { background: rgba(108,99,255,0.15) !important; border: 1px solid rgba(108,99,255,0.3) !important; color: #c8c4ff !important; }
    .stSuccess { background: rgba(0,200,83,0.12) !important; border: 1px solid rgba(0,200,83,0.3) !important; color: #80e8a0 !important; }
    .stError { background: rgba(255,82,82,0.12) !important; border: 1px solid rgba(255,82,82,0.3) !important; color: #ff8a8a !important; }
    .stWarning { background: rgba(255,193,7,0.12) !important; border: 1px solid rgba(255,193,7,0.3) !important; color: #ffe066 !important; }
    .stSpinner > div { border-color: #6c63ff !important; }
    .stExpander { background: rgba(255,255,255,0.04) !important; border: 1px solid rgba(255,255,255,0.08) !important; border-radius: 10px !important; }
    .stExpander summary { color: #ccc !important; font-weight: 500; }
    .stSidebar { background: rgba(0,0,0,0.3) !important; border-right: 1px solid rgba(255,255,255,0.05) !important; }
    .stSidebar .stMarkdown { color: #ccc !important; }
    .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar .stHeader { color: #e0e0e0 !important; }
    .stFileUploader { background: rgba(255,255,255,0.04) !important; border: 1px dashed rgba(255,255,255,0.2) !important; border-radius: 10px !important; }
    .stFileUploader:hover { border-color: #6c63ff !important; }
    .stFileUploader button { background: #6c63ff !important; color: #fff !important; border-radius: 8px !important; }
    .stCaption { color: #999 !important; }
    .agent-card {
        background: rgba(255,255,255,0.06); padding: 1.2rem; border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.1); margin-bottom: 0.5rem;
        backdrop-filter: blur(4px);
    }
    .agent-card h3 { margin: 0 0 0.3rem 0; font-size: 1.1rem; color: #e0e0e0 !important; }
    .agent-card p { margin: 0; color: #aaa !important; font-size: 0.9rem; }
    .agent-card strong { color: #6c63ff !important; }
    .model-badge {
        background: rgba(108,99,255,0.2); color: #b8b4ff; padding: 0.15rem 0.5rem;
        border-radius: 12px; font-size: 0.8rem; display: inline-block;
    }
    hr { border-color: rgba(255,255,255,0.08) !important; }
    .stAlert { border-radius: 8px !important; }
    [data-testid="stDecoration"] { background: linear-gradient(90deg, #6c63ff, #e040fb) !important; }
</style>
""", unsafe_allow_html=True)

st.title("🤖 Agentic AI Document Assistant")
st.markdown("Upload a document and let AI agents review, summarize, and extract information for you.")

with st.sidebar:
    st.header("📁 Document")
    uploaded_file = st.file_uploader(
        "Upload your document (PDF, DOCX, or TXT)",
        type=['pdf', 'docx', 'txt'],
        help="Max 50MB"
    )
    
    if uploaded_file:
        st.caption(f"Selected: **{uploaded_file.name}**")
    
    st.divider()
    
    st.header("🧠 Model")
    openrouter_model = os.getenv('OPENROUTER_MODEL', 'openrouter/free')
    st.markdown(f'<span class="model-badge">{openrouter_model}</span>', unsafe_allow_html=True)

if uploaded_file is None:
    st.info("👈 Upload a document from the sidebar to get started!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="agent-card">
            <h3>📝 Document Agent</h3>
            <p>Reviews grammar, clarity, and tone. Suggests improvements.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="agent-card">
            <h3>📋 Summary Agent</h3>
            <p>Creates executive summaries, bullet points, and key takeaways.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="agent-card">
            <h3>🔍 Info Agent</h3>
            <p>Extracts entities, organizes facts, and generates structured reports.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align:center; margin-top: 0.5rem; color: #888; font-size: 0.9rem;">
        Supported formats: PDF &bull; DOCX &bull; TXT
    </div>
    """, unsafe_allow_html=True)
else:
    os.makedirs('uploads', exist_ok=True)
    file_path = os.path.join('uploads', uploaded_file.name)

    with open(file_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("📖 Extracting text from document..."):
        extracted_text = extract_text_from_file(file_path)
        if "Error" in extracted_text:
            st.error(extracted_text)
            st.stop()
        st.success(f"✅ Document loaded successfully! ({len(extracted_text)} characters)")

    with st.expander("📄 Document Preview"):
        st.text_area(
            "Document Content:",
            extracted_text[:1000] + ("..." if len(extracted_text) > 1000 else extracted_text),
            height=200,
            disabled=True,
            label_visibility="collapsed"
        )

    tab1, tab2, tab3, tab4 = st.tabs([
        "📝 Document Review",
        "📋 Summarization",
        "🔍 Information Extraction",
        "💾 Download Results"
    ])

    with tab1:
        st.markdown("Check grammar, improve clarity, and enhance the writing quality of your document.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔍 Check & Improve Document", key="doc_check", use_container_width=True):
                with st.spinner("🔄 Document Agent is analyzing..."):
                    result = check_and_improve_document(extracted_text)
                    if result['status'] == 'success':
                        st.success("✅ Analysis Complete!")
                        st.write(result['analysis'])
                        st.session_state.doc_analysis = result['analysis']
                    else:
                        st.error(f"❌ Error: {result['error_message']}")
        
        with col2:
            if st.button("💡 Get Quick Review Tips", key="quick_tips", use_container_width=True):
                with st.spinner("🔄 Analyzing..."):
                    result = check_and_improve_document(extracted_text[:500])
                    if result['status'] == 'success':
                        st.info(result['analysis'])

    with tab2:
        st.markdown("Generate summaries, bullet points, and key takeaways from your document.")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📄 Full Summary", key="full_summary", use_container_width=True):
                with st.spinner("🔄 Summarization Agent is working..."):
                    result = summarize_document(extracted_text)
                    if result['status'] == 'success':
                        st.success("✅ Summary Complete!")
                        st.write(result['summary'])
                        st.session_state.saved_full_summary = result['summary']
                    else:
                        st.error(f"❌ Error: {result['error_message']}")
        
        with col2:
            if st.button("🎯 Bullet Points", key="bullet_summary", use_container_width=True):
                with st.spinner("🔄 Creating bullet points..."):
                    result = create_bullet_summary(extracted_text)
                    if result['status'] == 'success':
                        st.success("✅ Bullet Summary Created!")
                        st.markdown(result['bullet_points'])
                        st.session_state.saved_bullet_summary = result['bullet_points']
                    else:
                        st.error(f"❌ Error: {result['error_message']}")
        
        with col3:
            if st.button("🚀 Quick Summary (50 words)", key="quick_summary", use_container_width=True):
                with st.spinner("🔄 Creating quick summary..."):
                    text = f"Summarize the following text in exactly 50 words or less:\n\n{extracted_text[:1000]}"
                    result = summarize_document(text)
                    if result['status'] == 'success':
                        st.info(result['summary'])

    with tab3:
        st.markdown("Extract entities, key facts, and generate structured reports from your document.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🎯 Extract Entities & Facts", key="extract_info", use_container_width=True):
                with st.spinner("🔄 Information Agent is analyzing..."):
                    result = extract_information(extracted_text)
                    if result['status'] == 'success':
                        st.success("✅ Information Extracted!")
                        st.write(result['extracted_info'])
                        st.session_state.extracted_info = result['extracted_info']
                    else:
                        st.error(f"❌ Error: {result['error_message']}")
        
        with col2:
            if st.button("📊 Generate Report", key="gen_report", use_container_width=True):
                with st.spinner("🔄 Generating comprehensive report..."):
                    result = generate_report(extracted_text, report_type='comprehensive')
                    if result['status'] == 'success':
                        st.success("✅ Report Generated!")
                        st.write(result['report'])
                        st.session_state.generated_report = result['report']
                    else:
                        st.error(f"❌ Error: {result['error_message']}")
        
        st.divider()
        
        topic = st.text_input(
            "🔎 Research Additional Topic",
            placeholder="Enter a topic to research (e.g., 'Artificial Intelligence', 'Machine Learning')"
        )
        
        if st.button("🚀 Research Topic", key="research", use_container_width=True):
            if topic:
                with st.spinner(f"🔄 Researching '{topic}'..."):
                    result = collect_topic_information(topic)
                    if result['status'] == 'success':
                        st.success(f"✅ Research Complete for '{topic}'!")
                        st.write(result['research'])
                        st.session_state.topic_research = result['research']
                    else:
                        st.error(f"❌ Error: {result['error_message']}")
            else:
                st.warning("⚠️ Please enter a topic to research")

    with tab4:
        st.markdown("Save all your processed results for later use.")
        
        items = [
            ("doc_analysis", "Document Analysis", "down_doc", "document_analysis.txt"),
            ("saved_full_summary", "Full Summary", "down_sum", "summary.txt"),
            ("extracted_info", "Extracted Info", "down_info", "extracted_info.txt"),
            ("generated_report", "Report", "down_rep", "report.txt"),
            ("topic_research", "Research Results", "down_res", "research.txt"),
        ]
        
        available = [(k, l, d, f) for k, l, d, f in items if hasattr(st.session_state, k) and getattr(st.session_state, k)]
        
        if available:
            cols = st.columns(min(len(available), 4))
            for i, (key, label, dkey, fname) in enumerate(available):
                with cols[i % 4]:
                    path = save_output(getattr(st.session_state, key), key)
                    with open(path, 'r', encoding='utf-8') as f:
                        st.download_button(
                            label=f"📥 {label}",
                            data=f.read(),
                            file_name=fname,
                            mime="text/plain",
                            key=dkey
                        )
            
            st.info("💡 All downloaded files are also saved in the `outputs/` folder.")
        else:
            st.info("Run a task above first — results will appear here for download.")
