import streamlit as st
import random
import string

# Page configuration
st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(to right, #d9a7c7, #fffcdc);
        }

        .main-title {
            font-size: 48px;
            font-weight: 800;
            text-align: center;
            color: #4b0082;
            margin-bottom: 20px;
            text-shadow: 1px 1px 2px #ccc;
        }


        .password-box {
            background-color: #f0f8ff;
            padding: 10px 20px;
            border-radius: 12px;
            margin: 10px 0;
            font-family: monospace;
            font-size: 18px;
            color: #333;
            box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
        }

        .stButton>button {
            background-color: #4b0082;
            color: white;
            font-size: 18px;
            border-radius: 12px;
            padding: 10px 24px;
            margin-top: 15px;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
        }

        .stButton>button:hover {
            background-color: #3a0066;
            transform: scale(1.03);
        }

        .footer {
            text-align: center;
            margin-top: 40px;
            font-size: 14px;
            color: #444;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='main-title'>🔐 Password Generator</div>", unsafe_allow_html=True)

# Input Section
with st.container():
    st.markdown("<div class='main-box'>", unsafe_allow_html=True)

    num_passwords = st.slider("How many passwords do you want?", 1, 20, 5)
    password_length = st.slider("Length of each password:", 6, 30, 12)

    include_digits = st.checkbox("Include Digits (0-9)", value=True)
    include_symbols = st.checkbox("Include Symbols (!@#$%)", value=True)
    include_uppercase = st.checkbox("Include Uppercase Letters (A-Z)", value=True)

    # Generate button
    if st.button("🔁 Generate Passwords"):
        characters = string.ascii_lowercase
        if include_digits:
            characters += string.digits
        if include_symbols:
            characters += "!@#$%^&*()-_=+[]{}|;:,.<>?"
        if include_uppercase:
            characters += string.ascii_uppercase

        if not characters:
            st.warning("⚠️ Please select at least one character type!")
        else:
            st.success(f"✅ Generated {num_passwords} Password(s):")
            for _ in range(num_passwords):
                password = ''.join(random.choice(characters) for _ in range(password_length))
                st.code(password, language="")

    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Made with 💜 by Sabila Aleem</div>", unsafe_allow_html=True)
