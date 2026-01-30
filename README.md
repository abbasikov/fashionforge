# 👗 FashionForge - AI Virtual Try-On App

An AI-powered virtual try-on application built with Python, Streamlit, and Google Gemini API. Upload images of a person and a garment, and let AI describe how they would look together!

## Features

- 📤 Upload person and garment images
- 💬 Custom text prompts for try-on descriptions
- 🤖 Powered by Google Gemini AI
- 🎨 Clean and intuitive Streamlit interface
- ⚡ Real-time AI-generated fashion analysis

## Project Structure

```
FashionForge2/
├── app.py                 # Streamlit frontend application
├── backend.py            # Gemini API backend logic
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variable template
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key (get it from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Installation & Setup

### Step 1: Clone or navigate to the project directory

```bash
cd /Users/user/projects/FashionForge2
```

### Step 2: Create a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set up your API key

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Get your Gemini API key:
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with your Google account
   - Click "Create API Key"
   - Copy the generated API key

3. Edit the `.env` file and add your API key:
```bash
GEMINI_API_KEY=your_actual_api_key_here
```

## Running the Application

### Start the Streamlit app:

```bash
streamlit run app.py
```

The app will automatically open in your default browser at `http://localhost:8501`

### Test the backend (optional):

```bash
python backend.py
```

This will verify that your API key is configured correctly.

## How to Use

1. **Upload Person Image**: Click the first file uploader and select a clear photo of a person
2. **Upload Garment Image**: Click the second file uploader and select an image of a dress/garment
3. **Enter Prompt**: Customize the text prompt to describe how you want the garment to appear
4. **Generate Try-On**: Click the "Generate Try-On" button
5. **View Results**: The AI will generate a detailed description of how the garment would look on the person

## Example Prompts

- "Describe how this dress would look on this person. Consider the fit, style, and overall appearance."
- "Analyze how this outfit would complement the person's body type and skin tone."
- "Provide a detailed fashion critique of this garment on this person, including fit, color harmony, and style suggestions."

## Dependencies

- **streamlit**: Web application framework
- **google-generativeai**: Google Gemini API client
- **python-dotenv**: Environment variable management
- **Pillow**: Image processing library

## Important Notes

⚠️ **Current Implementation**: This version uses Gemini's vision capabilities to provide AI-generated **descriptions** of how the garment would look on the person. It does NOT generate actual composite images.

For actual image generation (overlaying garment on person), you would need:
- Image generation models like Stable Diffusion with ControlNet
- Specialized virtual try-on models (e.g., VITON, HR-VITON)
- Additional image processing pipelines

The current implementation is excellent for:
- Fashion consultation and analysis
- Style recommendations
- Fit and compatibility assessments
- Educational purposes

## Troubleshooting

### "GEMINI_API_KEY not found" error
- Make sure you've created a `.env` file (not just `.env.example`)
- Verify your API key is correctly pasted in the `.env` file
- Restart the Streamlit application after updating `.env`

### Import errors
- Make sure you've activated your virtual environment
- Run `pip install -r requirements.txt` again

### API errors
- Check your API key is valid
- Verify you have internet connection
- Check [Google AI Studio](https://makersuite.google.com/) for API status

## Future Enhancements

- [ ] Actual image generation with virtual try-on models
- [ ] Support for multiple garment types
- [ ] Save/download results
- [ ] History of previous try-ons
- [ ] Style recommendations
- [ ] Multi-language support

## License

This project is for educational purposes.

## Credits

Built with:
- [Streamlit](https://streamlit.io/)
- [Google Gemini AI](https://deepmind.google/technologies/gemini/)
- Python & PIL

---

Made with ❤️ by FashionForge Team | 2026
