"""
AI-Powered Virtual Try-On App
Streamlit Frontend Application
"""
import streamlit as st
from PIL import Image
import io
from backend import GeminiTryOnBackend


# Page configuration
st.set_page_config(
    page_title="FashionForge - AI Virtual Try-On",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    /* Main background and text */
    .stApp {
        background-color: #ffffff;
    }
    
    /* Center the main title */
    h1 {
        text-align: center;
        color: #1f1f1f !important;
        font-weight: 700;
        padding: 1rem 0;
    }
    
    /* Style headers - make them clearly visible */
    h2, h3 {
        color: #2c3e50 !important;
        font-weight: 600;
    }
    
    /* Paragraph text */
    p {
        color: #333333 !important;
    }
    
    /* Strong/bold text */
    strong, b {
        color: #1a1a1a !important;
        font-weight: 700;
    }
    
    /* Style buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        font-weight: 600;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    
    /* Center description */
    .main-description {
        text-align: center;
        color: #444444 !important;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* File uploader - keep default styling but adjust colors */
    .stFileUploader label {
        color: #333333 !important;
    }
    
    .stFileUploader section {
        background-color: #f8f9fa !important;
    }
    
    .stFileUploader [data-testid="stFileUploaderDropzone"] {
        background-color: #f8f9fa !important;
    }
    
    .stFileUploader [data-testid="stFileUploaderDropzoneInstructions"] p {
        color: #666666 !important;
    }
    
    /* Success message styling */
    .stSuccess {
        background-color: #d4edda !important;
    }
    
    .stSuccess p {
        color: #155724 !important;
    }
    
    /* Info message styling */
    .stInfo {
        background-color: #e8f4fd !important;
    }
    
    .stInfo p {
        color: #0c5460 !important;
    }
    
    /* Error message styling */
    .stError {
        background-color: #f8d7da !important;
    }
    
    .stError p {
        color: #721c24 !important;
    }
    
    /* Divider */
    hr {
        border-color: #e0e0e0 !important;
    }
    </style>
""", unsafe_allow_html=True)


def main():
    """Main application function"""
    
    # Title and description (centered)
    st.markdown("<h1>👗 FashionForge - AI Virtual Try-On</h1>", unsafe_allow_html=True)
    st.markdown(
        '<p class="main-description">Upload images and let AI create a stunning virtual try-on • Powered by Google Gemini AI</p>',
        unsafe_allow_html=True
    )
    
    # Initialize session state
    if 'generated_result' not in st.session_state:
        st.session_state.generated_result = None
    if 'person_img' not in st.session_state:
        st.session_state.person_img = None
    if 'garment_img' not in st.session_state:
        st.session_state.garment_img = None
    
    st.markdown("---")
    
    # Upload section with side-by-side uploaders and previews
    st.markdown("### 📤 Upload Images")
    
    # Create two columns for uploaders
    upload_col1, upload_col2 = st.columns(2)
    
    with upload_col1:
        st.markdown("**👤 Person Image**")
        person_file = st.file_uploader(
            "Choose person image",
            type=['png', 'jpg', 'jpeg'],
            key="person_uploader",
            help="Upload a clear image of a person",
            label_visibility="collapsed"
        )
        
        if person_file is not None:
            person_image = Image.open(person_file)
            st.session_state.person_img = person_image
            # Show small preview - fixed width of 250px
            st.image(person_image, caption="Person", width=250)
    
    with upload_col2:
        st.markdown("**👗 Garment Image**")
        garment_file = st.file_uploader(
            "Choose garment image",
            type=['png', 'jpg', 'jpeg'],
            key="garment_uploader",
            help="Upload an image of the clothing item",
            label_visibility="collapsed"
        )
        
        if garment_file is not None:
            garment_image = Image.open(garment_file)
            st.session_state.garment_img = garment_image
            # Show small preview - fixed width of 250px
            st.image(garment_image, caption="Garment", width=250)
    
    st.markdown("---")
    
    # Generate button (centered)
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        generate_button = st.button(
            "🎨 Generate Virtual Try-On",
            type="primary",
            use_container_width=True
        )
    
    st.markdown("---")
    
    # Results section
    if generate_button:
        # Validate inputs
        if st.session_state.person_img is None:
            st.error("❌ Please upload a person image first!")
            return
        
        if st.session_state.garment_img is None:
            st.error("❌ Please upload a garment image first!")
            return
        
        # Show loading spinner
        with st.spinner("🎨 Generating virtual try-on with AI... This may take a moment..."):
            try:
                # Initialize backend
                backend = GeminiTryOnBackend()
                
                # Generate try-on result (no prompt needed, uses default)
                result, error = backend.generate_tryon_image(
                    st.session_state.person_img,
                    st.session_state.garment_img
                )
                
                if error:
                    st.error(f"❌ Error: {error}")
                    st.info("💡 Make sure your GEMINI_API_KEY is set correctly in the .env file")
                else:
                    st.session_state.generated_result = result
                    
            except ValueError as ve:
                st.error(f"❌ Configuration Error: {ve}")
                st.info("""
                **Setup Instructions:**
                1. Copy `.env.example` to `.env`
                2. Get your API key from [Google AI Studio](https://aistudio.google.com/apikey)
                3. Add your API key to the `.env` file
                4. Restart the application
                """)
            except Exception as e:
                st.error(f"❌ Unexpected error: {e}")
    
    # Display result if available
    if st.session_state.generated_result:
        st.markdown("### ✨ Generated Result")
        st.success("✅ Virtual try-on generated successfully!")
        
        # Display the AI-generated image (centered, larger)
        result_col1, result_col2, result_col3 = st.columns([1, 3, 1])
        with result_col2:
            st.image(st.session_state.generated_result, caption="🎨 AI Generated Virtual Try-On", width="stretch")
    
    elif not generate_button:
        # Show placeholder/instructions only if button hasn't been clicked
        st.markdown("### � How to Use")
        
        instruction_col1, instruction_col2, instruction_col3 = st.columns(3)
        
        with instruction_col1:
            st.markdown("""
            **Step 1️⃣**
            
            Upload a clear photo of a person
            """)
        
        with instruction_col2:
            st.markdown("""
            **Step 2️⃣**
            
            Upload the garment/dress image
            """)
        
        with instruction_col3:
            st.markdown("""
            **Step 3️⃣**
            
            Click Generate and wait for AI magic!
            """)
    
 


if __name__ == "__main__":
    main()
