import streamlit as st
import time
import base64

# Set up session state to manage flow
if "step" not in st.session_state:
    st.session_state.step = 1
if "pleading_level" not in st.session_state:
    st.session_state.pleading_level = 0  # Initial pleading level
if "image_captured" not in st.session_state:
    st.session_state.image_captured = False
if "image_data" not in st.session_state:
    st.session_state.image_data = None
if "countdown" not in st.session_state:
    st.session_state.countdown = 3  # Set countdown to 3 seconds
if "countdown_active" not in st.session_state:
    st.session_state.countdown_active = False  # Track if countdown is active

# List of pleading titles
pleading_titles = [
    "Will you graciously accept your heartwarming sentence?",
    "Oh dear, please do not resist your charming decree!",
    "I implore you, will you follow through with this joyful verdict?",
    "My love, I plead, just embrace your delightful fate!",
    "Oh, my heart aches—please say yes to your adorable sentence!"
]

# Function to create a download link for the image
def create_download_link(img_data):
    b64_img = base64.b64encode(img_data).decode()
    href = f'<a href="data:file/png;base64,{b64_img}" download="captured_image.png">Download Your Precious Memory</a>'
    st.markdown(href, unsafe_allow_html=True)

# Step 1: Display the conviction message
if st.session_state.step == 1:
    st.markdown('<p style="font-size: 32px; font-weight: bold; color: #F8D3B7;">You’ve been found guilty of hiding your radiant smile for far too long! Your charm and grace have driven me utterly wild!</p>', unsafe_allow_html=True)

    # Move to the next step after 3 seconds
    time.sleep(3)
    st.session_state.step = 2
    st.experimental_rerun()

# Step 2: Display the punishment message and first pleading title
if st.session_state.step == 2:
    st.markdown('<p style="font-size: 32px; font-weight: bold; color: #F8D3B7;">For this charming "crime", your delightful sentence is as follows... </p>', unsafe_allow_html=True)
    st.markdown(f"<h2 style='color: #FFB3BA;'>{pleading_titles[st.session_state.pleading_level]}</h2>", unsafe_allow_html=True)

    # Buttons for "Yes" and "No"
    col1, col2 = st.columns(2)

    # Handle "No" button click
    if col1.button("No"):
        if st.session_state.pleading_level < len(pleading_titles) - 1:
            st.session_state.pleading_level += 1  # Move to the next pleading title
            st.experimental_rerun()  # Reload the page to show the next title
        else:
            st.markdown('<p style="font-size: 32px; font-weight: bold; color: #F8D3B7;">Oh no! You’re breaking my heart! Please, dear, say yes!</p>', unsafe_allow_html=True)

    # Handle "Yes" button click
    if col2.button("Yes"):
        st.session_state.step = 3  # Move to the next step
        st.experimental_rerun()  # Reload the page to show the next message

# Step 3: Capture image after user agrees
if st.session_state.step == 3:
    st.markdown('<p style="font-size: 32px; font-weight: bold; color: #F8D3B7;">Thank you for your kind agreement! The sweet punishment for this "crime" is...</p>', unsafe_allow_html=True)
    time.sleep(2)  # Delay before showing the next message
    st.markdown('<p style="font-size: 32px; font-weight: bold; color: #F8D3B7;">"You must take approximately 100 adorable pictures with me today, and the first one is now 😝 "</p>', unsafe_allow_html=True)

    # Start countdown if not active
    if not st.session_state.countdown_active:
        st.session_state.countdown_active = True

    # Countdown timer
    if st.session_state.countdown > 0:
        st.markdown(f"<h2 style='color: #FFB3BA;'>Picture Capturing in {st.session_state.countdown} seconds!</h2>", unsafe_allow_html=True)
        time.sleep(1)  # Wait for a second
        st.session_state.countdown -= 1  # Decrease the countdown
        st.experimental_rerun()  # Rerun to update the countdown display
    else:
        # Time's up, take the picture
        img = st.camera_input("Capture your beautiful smile")
        if img:
            # Save the image and move to the next step
            st.session_state.image_data = img.getvalue()  # Save the image bytes
            st.session_state.image_captured = True
            st.session_state.step = 4  # Move to the next step
            st.session_state.countdown_active = False  # Reset countdown state
            st.session_state.countdown = 3  # Reset countdown for next use
            st.experimental_rerun()

# Step 4: Display the download link and final punishment message
if st.session_state.step == 4 and st.session_state.image_captured:
    # Provide download link for the captured image
    if st.session_state.image_data:
        create_download_link(st.session_state.image_data)

    # Final punishment text
    st.markdown('<p style="font-size: 32px; font-weight: bold; color: #F8D3B7;">Your delightful punishment period begins now... Should you fail to fulfill this task today, you shall face the charming consequences. For further guidance, please consult your ever-loving partner 🥺</p>', unsafe_allow_html=True)

    # Call the balloons effect
    st.balloons()
