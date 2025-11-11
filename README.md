# AI Recipe Assistant

AI Recipe Assistant is a smart recipe generator powered by Google Gemini and built with Streamlit.  
It creates personalized recipes based on your available ingredients, taste preferences, diet, allergies, and budget.

---

## 🚀 Features
- Generate three unique recipes using Google Gemini
- The first recipe uses only available ingredients
- The second and third recipes may include optional "to buy" ingredients
- Budget control per serving (RON)
- Expandable and visually clean recipe cards
- Simple, modern Streamlit interface

---

## Technologies Used
| Layer | Technology |
|--------|-------------|
| **Language** | Python |
| **Frontend/UI** | Streamlit |
| **AI Engine** | Google Gemini 2.5 Flash |


---


## Setup Instructions

#### 1. Clone the repository
```bash
git clone https://github.com/Teo107/AI-Recipe-Assistant.git
cd AI-Recipe-Assistant
```

#### 2. Create and activate a virtual environment
```bash
python -m venv venv
```

##### On Windows (Command Prompt)
```bash
venv\Scripts\activate
```

##### On Windows (PowerShell)
```bash
venv\Scripts\Activate.ps1
```

##### On macOS/Linux
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure your Google Gemini API key
Create a `.env` file in the project root and add:
```
GOOGLE_API_KEY=your_api_key_here
```

### 5. Run the app
```bash
streamlit run app.py
```

---


## Author
**Teo**  
Information Engineering student passionate about building functional and creative software projects.  
💬 [LinkedIn](https://www.linkedin.com/in/teodora-topliceanu-5036b8328/)

---

## License
This project is open source and available under the MIT License.
