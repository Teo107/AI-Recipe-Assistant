import streamlit as st
import json
import time
from controllers.recipe_controller import generate_recipes
# Page configuration
st.set_page_config(
    page_title="AI Recipe Assistant",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for the pink panel look
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@300;400;700&family=Dancing+Script:wght@400;500;600&display=swap');

/* Pink AI Kitchen Theme */
:root {
    --bg-dark: #0e1117;
    --panel-dark: #1e1e1e;
    --pink-light: #fbdbed;
    --pink-mid: #ffacc7;
    --text-light: #fbdbed;
    --text-dark: #0e1117;
}

/* Remove spacing above header */
.block-container {
    padding-top: 25px !important;
    margin-top: -10px !important;
}

/* Background */
.stApp {
    background-color: var(--bg-dark) !important;
}

/* Title */
.title-text {
    font-family: "Dancing Script", cursive;
    font-size: 3.3rem !important;
    color: var(--pink-light);
    text-align: center;
    margin-bottom: 0;
}
.subtitle-text {
    font-family: "Comic Neue", cursive;
    font-size: 1.2rem !important;
    color: var(--pink-light);
    text-align: center;
    margin-top: -8px;
    opacity: .85;
}

/* Labels & text */
h3, label, h4 {
    color: var(--pink-light) !important;
    font-family: "Comic Neue", cursive !important;
}

/* Inputs: textarea & text input = pink bubble */
.stTextInput > div > div,
.stTextArea > div > div {
    background-color: var(--pink-light) !important;
    border: 2px solid var(--pink-mid) !important;
    border-radius: 12px !important;
}
.stTextInput input,
.stTextArea textarea {
    color: var(--text-dark) !important;
}

/* Placeholder text */
.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: var(--text-dark) !important;
    opacity: .7;
}

/* Selectbox pink */
div[data-testid="stSelectbox"] > div {
    background-color: var(--pink-light) !important;
    border: 2px solid var(--pink-mid) !important;
    border-radius: 12px !important;
}

/* Dropdown menu */
div[data-baseweb="select"] ul {
    background-color: var(--pink-light) !important;
}
div[data-baseweb="select"] li {
    color: var(--text-dark) !important;
    background-color: var(--pink-light) !important;
}
div[data-baseweb="select"] li:hover {
    background-color: var(--pink-mid) !important;
    color: var(--text-dark) !important;
}
div[data-baseweb="select"] span {
    color: var(--text-dark) !important;
}

/* Radio buttons: keep minimal */
div[data-testid="stRadio"] label span, 
div[data-testid="stRadio"] p {
    color: var(--pink-light) !important;
    font-family: "Comic Neue", cursive !important;
}

/* Slider styling - made all labels pink */
div[data-testid="stTickBarMin"],
div[data-testid="stTickBarMax"],
div[data-testid="stThumbValue"] {
    color: var(--pink-mid) !important;
    font-family: "Comic Neue", cursive !important;
}

/* Slider track and thumb */
.stSlider > div > div > div {
    background: var(--pink-light) !important;
}
.stSlider > div > div > div > div {
    background: linear-gradient(45deg, var(--pink-light), var(--pink-mid)) !important;
}

/* Slider thumb (circle) */
.stSlider > div > div > div > div > div {
    background-color: var(--pink-mid) !important;
    border: 2px solid var(--pink-light) !important;
}

/* Button */
div.stButton > button {
    background: linear-gradient(45deg, var(--pink-light), var(--pink-mid)) !important;
    color: var(--bg-dark) !important;
    border: none !important;
    border-radius: 25px !important;
    padding: 13px 26px !important;
    font-family: "Comic Neue", cursive !important;
    font-weight: bold !important;
    font-size: 1.1rem !important;
    width: 100%;
    margin-top: 15px;
    transition: .2s ease;
}
div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 15px var(--pink-mid);
}

/* Response box & recipe cards */
.response-area {
    background-color: var(--panel-dark);
    border: 2px dashed var(--pink-light);
    border-radius: 18px;
    padding: 40px;
    text-align: center;
    color: var(--text-light);
    font-family: "Comic Neue", cursive;
}
.recipe-card {
    background-color: var(--panel-dark);
    border-left: 5px solid var(--pink-mid);
    border-radius: 14px;
    padding: 18px;
    margin: 12px 0;
    font-family: "Comic Neue", cursive;
    color: var(--text-light);
}
</style>

""", unsafe_allow_html=True)

def main():

    # Header
    st.markdown('<h1 class="title-text">AI Recipe Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text">Your cute AI kitchen companion ✨</p>', unsafe_allow_html=True)

    if 'generated' not in st.session_state:
        st.session_state.generated = False

    # Layout
    left, right = st.columns([1, 1])

    with left:
        st.markdown("### Your Kitchen Details")

        flavor = st.radio("#### 👅 Choose your flavor vibe:",
                          ["🌶️ Spicy", "🍬 Sweet", "🧂 Salty", "🍲 Comfort", "🌿 Fresh"])

        diet = st.selectbox("#### 🥗 Select your diet:",
                            ["🍽️ No restrictions", "🌱 Vegetarian", "💚 Vegan"])

        allergies = st.text_input("#### ⚠️ Allergies (optional)", placeholder="Type here...")

        budget = st.slider("#### 💰 Max budget per serving (RON):", 5, 100, 40)

        generate = st.button("✨ Generate Magical Recipes!", use_container_width=True)

    with right:
        st.markdown("### 📝 Your Ingredients")
        ingredients = st.text_area("", height=200,
                                   placeholder="Type your ingredients here...")

        st.markdown("### 🍳 Response")
        recipe_area = st.container()

    # Logic
    # Logic
    if generate:
        if ingredients.strip():
            with st.spinner("Whipping up something delicious... "):
                recipes = generate_recipes(ingredients, flavor, diet, allergies, budget)

            try:
                recipes_data = recipes
                st.session_state.generated = True

                with recipe_area:
                    st.success("Recipes generated successfully! Enjoy your magic!")
                    # cards
                    for recipe in recipes_data:
                        to_buy_html = ""
                        if recipe.get("to_buy"):  # only show if key exists and not empty
                            to_buy_html = (
                                    "<h4 style='color: #ffacc7; margin-top:15px;'>🛒 To buy</h4>"
                                    "<ul>"
                                    + "".join(f"<li>{item}</li>" for item in recipe["to_buy"])
                                    + "</ul>"
                            )

                        html_block = f"""
                    <div class="recipe-card" style="
                        background-color:#1e1e1e;
                        border-radius:16px;
                        border-left:5px solid #ffacc7;
                        margin-bottom:15px;
                        padding:15px 20px;
                    ">
                    <details>
                    <summary style="
                        cursor:pointer;
                        font-family:'Comic Neue',cursive;
                        font-size:1.3rem;
                        color:#fbdbed;
                        display:flex;
                        justify-content:space-between;
                        align-items:center;
                    ">
                    <span>🍽️ {recipe['name']}</span>
                    <span style="font-size:0.9rem;opacity:0.9;">
                        {recipe.get('calories', '-')} • ⏱️ {recipe.get('prep_time', '-')} • 💰 {recipe.get('price', recipe.get('Price', '-'))}
                    </span>
                    </summary>
                    <div style="margin-top:15px;color:#fbdbed;">
                    <h4 style="color:#ffacc7;">🧂 Ingredients</h4>
                    <ul>{''.join(f"<li>{ing}</li>" for ing in recipe['ingredients'])}</ul>
                    {to_buy_html}
                    <h4 style="color:#ffacc7;">👩‍🍳 Steps</h4>
                    <ol>{''.join(f"<li>{step}</li>" for step in recipe['steps'])}</ol>
                    </div>
                    </details>
                    </div>
                    """.strip().replace("\n", "")

                        st.markdown(html_block, unsafe_allow_html=True)



            except Exception as e:
                st.error(e)
        else:
            st.markdown("""
            <div class="response-area">
                <div style="font-size: 3rem;">⚠️</div>
                <p style="font-size:1.2rem;">Enter your ingredients first, chef! 👩‍🍳✨</p>
            </div>
            """, unsafe_allow_html=True)

    # nothing generated
    if not st.session_state.generated:
        with recipe_area:
            st.markdown("""
            <div class="response-area">
                <div style="font-size: 4rem; margin-bottom: 20px;">🍳</div>
                <h3>Your recipes will appear here!</h3>
                <p style="opacity: 0.8;">Click the button to generate recipes.</p>
            </div>
            """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()