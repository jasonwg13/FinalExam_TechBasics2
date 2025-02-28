import streamlit as st
import pandas as pd
import random
from rapidfuzz import fuzz
from fuzzywuzzy import process

st.set_page_config(page_title="Welcome to PuzzlePortal")


# function for changing colors
def set_theme(theme_name):
    themes = {
        "Blue": {
            "primary_color": "#80c9ff",  # light medium blue
            "background_color": "#bfe4ff",  # bright blue
            "text_color": "#0066b3",  # medium blue
            "header_color": "#00487d"  # dark blue
        },
        "Purple": {
            "primary_color": "#9267AA",  # medium purple
            "background_color": "#9267AA",  # Dark purple
            "text_color": "#D1CCFF",  # light medium purple
            "header_color": "#E2CCFF"  # bright purple
        },
        "Brown": {
            "primary_color": "#bf8860",  # medium brown
            "background_color": "#806959",  # Dark brown
            "text_color": "#cca88f",  # light medium brown
            "header_color": "#e6d8cf"  # bright brown
        },
        "Green": {
            "primary_color": "#00b069",  # medium green
            "background_color": "#007b49",  # Dark green
            "text_color": "#80ffcc",  # light medium green
            "header_color": "#bfffe5"  # bright green
        }
    }

    # If the theme is valid, apply custom css, here I had help from ChatGPT
    if theme_name in themes:
        theme = themes[theme_name]
        custom_css = f"""
        <style>
            :root {{
                --primary-color: {theme['primary_color']};
                --background-color: {theme['background_color']};
                --text-color: {theme['text_color']};
                --header-color: {theme['header_color']};
            }}

            /* Apply background color and text color with higher specificity */
            html, body, div.stApp {{
                background-color: var(--background-color) !important;
                color: var(--text-color) !important;
            }}

            h1, h2, h3, h4, h5, h6 {{
                color: var(--header-color) !important;
            }}

            /* Streamlit-specific class adjustments */
            .css-18e3th9 {{
                background-color: var(--background-color) !important;
                color: var(--text-color) !important;
            }}

            .stButton > button {{
                background-color: var(--primary-color) !important;
                color: var(--text-color) !important;
            }}

            .stTextInput > div > div input {{
                background-color: var(--background-color) !important;
                color: var(--text-color) !important;
            }}

            .css-1cpxqw2 {{
                background-color: var(--background-color) !important;
            }}
        </style>
        """
        st.markdown(custom_css, unsafe_allow_html=True)


# create a sidebar for selecting different pages and the different color themes defined above
st.sidebar.header("Menu")
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #596f80;
    }
</style>
""", unsafe_allow_html=True)

# list of the page options in the sidebar
options = ['Welcome To PuzzlePortal', 'Find Your Puzzle!', 'Reviews', 'Get Inspired!', 'My Puzzle Journey']
page_selection = st.sidebar.selectbox("Choose the page", options)

# list of the color themes in the sidebar
st.sidebar.header("Design")
theme_name = st.sidebar.selectbox("Which colour theme do you prefer",
                                  ["Blue", "Purple", "Brown", "Green"], index=0)
# apply the selected theme
set_theme(theme_name)


# definition for random pop-up messages
def random_message():
    # list of pop-up messages
    messages = [
        "Hey there! Just finished my puzzle—took me 15 minutes. What’s your time looking like?",
        "Pro tip: Start with the corners; it’s a game changer!",
        "How’s it going? I always find the edges first; works for me!",
        "Wow, I just unlocked a 6x6 grid. Have you tried it yet?",
        "Did you know the world’s largest jigsaw puzzle had over 500,000 pieces? Imagine that!",
        "Almost there? I can’t wait to see the finished puzzle!",
        "You’re doing amazing—keep it up! Don’t let that one tricky piece fool you.",
        "Fun fact: Puzzles were invented in the 1760s. You're part of a historic tradition!",
        "Think of it like life: one piece at a time, and it all fits together.",
        "Need a break? Sometimes a fresh perspective makes all the difference!",
        "I just unlocked a cat-themed puzzle—so adorable! What’s your favorite theme?",
        "Have you tried rotating pieces? Sometimes the solution’s simpler than you think.",
        "Challenge accepted! I’m trying to beat your time on the last puzzle.",
        "Puzzles are like meditation for the brain. Feeling zen yet?",
        "Wow, your puzzle looks great! Want to swap tips on tough spots?",
        "I love how satisfying it is when the final piece clicks. Almost there?",
        "You’re inspiring me! I might take on a harder level next.",
        "Stuck? Look at the colors and patterns—it always helps me!",
        "I just discovered there’s a world championship for puzzling. Should we enter?",
        "Way to go, puzzler extraordinaire! I’m cheering you on from here!",
    ]

    # randomly choose one of the messages and make it appear in the upper right corner with st.toast
    message = random.choice(messages)
    st.toast(message)


# definition for the page that will be displayed first when opening the website
# the information texts on the page are based on the following website: https://www.puzzle.de/puzzle-geschichte/
def welcome_page():
    st.title("Welcome to PuzzlePortal!🧩🧩🧩")
    st.subheader("This is the perfect page for Puzzle ENTHUSIASTS!🥳🎊🎉 Have fun clicking through the website, may your "
                 "day be as satisfying as fitting the final piece of a puzzle!")
    st.write(
        "For centuries, puzzles have fascinated people all over the world – they challenge our minds, help us relax, "
        "and bring us together. Dive into the world of puzzles!")

    # creating two columns for displaying the content
    c1, c2 = st.columns(2)

    # definition for the displaying the content in the first column
    def info_puzzling_one():
        tile = st.container()
        # images and texts that will be shown in the container
        tile.image("https://images.unsplash.com/photo-1621211255064-8915268b62f4?q=80&w=2340&auto=format&fit=crop"
                   "&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
        tile.write("The first puzzle was made in 1766 by John Spilsbury, a British mapmaker. He cut a map into small "
                   "pieces to help students learn geography in a fun way. Over time, puzzles changed from simple "
                   "wooden pieces to colorful pictures with thousands of parts. Today, people enjoy puzzles of all "
                   "kinds, from famous paintings to personal photos.")
        tile.image("https://images.unsplash.com/photo-1688930495342-eac24a42d65a?q=80&w=2348&auto=format&fit=crop"
                   "&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
        tile.write("Today, puzzles are still a great way to have fun and take a break from daily life. They bring "
                   "families and friends closer and give a sense of achievement when finished. No matter if it’s a "
                   "rainy day or a quiet evening at home, puzzles make every moment more enjoyable.")

    # definition for the displaying the content in the second column
    def info_puzzling_two():
        tile = st.container()
        # images and texts that will be shown in the container
        tile.write("For hundreds of years, puzzles have amazed people all over the world. They are more than just a "
                   "fun game – they make us think, help us relax, and bring people together. Looking for the right "
                   "piece and putting it in the right place feels exciting and satisfying. That’s why puzzles are a "
                   "favorite activity for kids and adults alike.")
        tile.image("https://www.historytoday.com/sites/default/files/2021-03/Jigsaws.jpg")
        tile.write("Puzzles are not just for children. Many adults love solving them because they are both "
                   "challenging and relaxing. Puzzling helps train the brain by improving focus, patience, "
                   "and problem-solving skills. Whether you are working on a small puzzle or a giant one with "
                   "thousands of pieces, it is always exciting to see the picture slowly come together.")
        tile.image("https://m.media-amazon.com/images/I/71egJKcfAiL.jpg")

    # displaying the information in the two columns
    with c1:
        info_puzzling_one()

    with c2:
        info_puzzling_two()

# definition for the preference page
def preference_page():
    random_message() # displaying the random messages with st.toast

    # list of puzzles, each with its name, image URL, and attributes (landscape, detailed, etc.)
    puzzles = [
        {
            "name": "Lavendelfeld zur goldenen Sonne 16724",
            "image_url": "https://m.media-amazon.com/images/I/61qBAseyBBL._AC_UF1000,1000_QL80_.jpg",
            "attributes": ["Landscape", "Detailed", "Nature", "Fewer pieces", "Realistic", "Colourful"]
        },
        {
            "name": "Guanajuato in Mexiko 17442",
            "image_url": "https://m.media-amazon.com/images/I/611tjCHSSoL._AC_UF1000,1000_QL80_.jpg",
            "attributes": ["Landscape", "Detailed", "City", "A lot of pieces", "Realistic", "Monochrome"]
        },
        {
            "name": "Magische Stimmung über dem Leuchtturm von Akranes, Island 12000732",
            "image_url": "https://m.media-amazon.com/images/I/61OpG-BKUwL._AC_UF894,1000_QL80_.jpg",
            "attributes": ["Landscape", "Detailed", "Coastal town", "A lot of pieces", "Realistic", "Earth tones"]
        },
        {
            "name": "Schlacht auf hoher See 13969",
            "image_url": "https://m.media-amazon.com/images/I/71EGLaamQcL.jpg",
            "attributes": ["Ocean", "Detailed", "Coastal town", "A lot of pieces", "Cartoon", "Earth tones"]
        },
        {
            "name": "Geheimnisvolle Unterwasserwelt 16661",
            "image_url": "https://i.pinimg.com/736x/cb/5a/03/cb5a038c26f04bd30b73bbd53be4becc.jpg",
            "attributes": ["Ocean", "Undetailed", "Nature", "A lot of pieces", "Cartoon", "Monochrome"]
        },
        {
            "name": "Almbock mit Baby 12000809",
            "image_url": "https://scale.coolshop-cdn.com/product-media.coolshop-cdn.com/23JB8Y/8326844d67cc442bbaf1bc8f6aaf5510.jpg/f/ravensburger-puzzle-foto-city-landscape-3000p-12000809.jpg",
            "attributes": ["Mountains", "Detailed", "Nature", "A lot of pieces", "Realistic", "Colourful"]
        },
        {
            "name": "Regenbogenberge, China 17324",
            "image_url": "https://m.media-amazon.com/images/I/71zg-x0qpmL._AC_UF894,1000_QL80_.jpg",
            "attributes": ["Mountains", "Detailed", "Nature", "Fewer pieces", "Realistic", "Colorful"]
        },
        {
            "name": "Zauberhafte Wüste 15069",
            "image_url": "https://m.media-amazon.com/images/I/81-4l9-nVaL.jpg",
            "attributes": ["Desert", "Detailed", "Nature", "Fewer pieces", "Realistic", "Earth tones"]
        },
        {
            "name": "In den Dünen 146130",
            "image_url": "https://m.media-amazon.com/images/I/91MMqfZH-AL.jpg",
            "attributes": ["Ocean", "Undetailed", "Coastal town", "Fewer pieces", "Realisitc", "Earth tones"]
        },
        {
            "name": "Wasserfall von Kirkjufell, Island 19539",
            "image_url": "https://m.media-amazon.com/images/I/61WOdfMmGrL.jpg",
            "attributes": ["Mountains", "Undetailed", "Coastal town", "Fewer pieces", "Realistic", "Earth tones"]
        },
        {
            "name": "Pokémon Classics 12000726",
            "image_url": "https://data.puzzle.de/.5/pokemon-classics-1500-teile--puzzle.91804-2.fs.jpg",
            "attributes": ["Landscape", "Undetailed", "City", "A lot of pieces", "Cartoon", "Colorful"]
        },
    ]

    # function for finding the best puzzle match based on the user preferences with fuzzywuzzy
    def find_best_puzzle(user_preferences, puzzles, threshold=70):
        best_match = None # initialize the best match to none
        highest_score = 0 # initialize the highest score to 0

        for puzzle in puzzles:
            # Compare each attribute of the puzzle to the user preferences using fuzz.ratio to get a similarity score
            scores = [fuzz.ratio(user_attr, puzzle_attr) for user_attr, puzzle_attr in
                      zip(user_preferences, puzzle["attributes"])]
            avg_score = sum(scores) / len(scores) # Calculate the average score

            # if the average score is higher than the current highest score and meets the threshold, update the match
            if avg_score > highest_score and avg_score >= threshold:
                highest_score = avg_score
                best_match = puzzle

        return best_match, highest_score # return the best match and its score

    # definition for gathering user preferences
    def preference():
        st.title("Find Your Perfect Puzzle!🌸🌟")
        st.write("Answer the following questions to find the best puzzle for you!")

        # questions for user preferences
        question1 = st.radio("Do you prefer Landscape or Ocean?", ["Landscape", "Ocean", "Mountains", "Desert"])
        question2 = st.radio("Do you prefer detailed or undetailed?", ["Detailed", "Undetailed"])
        question3 = st.radio("Do you prefer city or nature?", ["City", "Nature", "Coastal town"])
        question4 = st.radio("Do you prefer a lot of pieces or fewer pieces?", ["A lot of pieces", "Fewer pieces"])
        question5 = st.radio("Do you prefer a realistic image or a cartoon image?", ["Realistic", "Cartoon"])
        question6 = st.radio("Do you prefer colourful or monochrome?", ["Colourful", "Monochrome", "Earth tones"])

        # collect user preferences in a list
        user_preferences = [question1, question2, question3, question4, question5, question6]

        # find the best puzzle match when the button is clicked
        if st.button("Find My Puzzle!"):
            best_match, score = find_best_puzzle(user_preferences, puzzles)

            # if a match is found, display the puzzle with its image and score
            if best_match:
                st.write(f"We found a match for you!🧩 ({score:.2f}% match)")
                st.image(best_match["image_url"], caption=best_match["name"])
            # if no match is found, show a random puzzle suggestion
            else:
                st.write("No perfect match found, but here’s a random suggestion!")
                random_puzzle = random.choice(puzzles)
                st.image(random_puzzle["image_url"], caption=random_puzzle["name"])

    if __name__ == "__main__":
        preference()

# definition for the review page
def review_page():
    st.title("Review Page")
    st.write("You have an opinion on a puzzle? Here is the place to write your review!")
    random_message()

    # create a DataFrame to store reviews, with help from the TechBasics tutors
    df_reviews = pd.DataFrame(columns=["Item Number", "Name", "Stars", "Comment"])

    # load the data
    if "df_reviews" not in st.session_state:
        st.session_state.df_reviews = pd.DataFrame(columns=["Item Number", "Name", "Stars", "Comment"])

    # form for adding new reviews
    with st.form("review_form"):
        st.subheader("Add a new review!")
        item_number = st.text_input("Item Number", placeholder="e.g. 123456")
        name = st.text_input("Name", placeholder="Your Name")
        stars = st.slider("Stars", min_value=1, max_value=5, step=1)
        comment = st.text_area("Comment", placeholder="Write your comment here...")
        submit_button = st.form_submit_button("Save")

    # save the data when the form is submitted
    if submit_button:
        if item_number and name and comment: # makes sure all fields are filled
            new_review = {
                "Item Number": item_number,
                "Name": name,
                "Stars": stars,
                "Comment": comment
            }
            new_review = pd.DataFrame([new_review]) # convert the new review to a DataFrame
            st.session_state.df_reviews = pd.concat([st.session_state.df_reviews, new_review], ignore_index=True) # add review to session state
            st.success("Review saved successfully!")
        else:
            st.error("Please fill out everything.") # show an error if some fields are empty

    # displaying the saved reviews
    st.subheader("Saved Reviews")
    if not st.session_state.df_reviews.empty:
        st.dataframe(st.session_state["df_reviews"])
    else:
        st.write("No reviews yet.")

# definition for the inspiration page
def inspiration_page():
    st.title("Inspiration for new hobbies similar to puzzling!🧶🎨🖌️🖼️")
    st.write("If you love puzzles but are looking for something new, this page introduces you to exciting hobbies that "
             "offer similar creativity, challenge, and relaxation.")
    random_message()

    # create three columns with different hobbies
    c1, c2, c3 = st.columns(3)

    # function for displaying information about Origami
    def origami_info():
        tile = st.container(border=True)
        tile.title("Origami")
        tile.image("https://www.japanwelt.de/media/image/origami-figuren-tiere-falten.jpg")
        tile.write("Origami is the Japanese art of paper folding, transforming a simple sheet into intricate designs "
                   "like animals, flowers, and geometric shapes. It promotes creativity, patience, and fine motor "
                   "skills.")

    # function for displaying information about Knitting
    def knitting_info():
        tile = st.container(border=True)
        tile.title("Knitting")
        tile.image("https://nimble-needles.com/wp-content/uploads/2021/09/how-to-knit-for-beginners-720x720.jpg")
        tile.write("Knitting is a relaxing craft where yarn is looped together to create textiles, from scarves to "
                   "sweaters. It’s a meditative activity that enhances focus and creativity while producing beautiful "
                   "handmade items.")

    # function for displaying information about Sudoku
    def sudoku_info():
        tile = st.container(border=True)
        tile.title("Sudoku")
        tile.image("https://sudoku-puzzles.net/wp-content/puzzles/butterfly-sudoku/easy/1.png")
        tile.write("Sudoku is a number puzzle that challenges logical thinking by requiring players to fill a grid so "
                   "that each row, column, and section contain all digits exactly once. It’s a great mental workout that "
                   "improves problem-solving skills.")

    # function for displaying information about Crossword
    def crossword_info():
        tile = st.container(border=True)
        tile.title("Cross- word")
        tile.image("https://www.treevalleyacademy.com/wp-content/uploads/6th-Grade-Fall-Crossword-791x1024.png.webp")
        tile.write("Crossword puzzles test vocabulary and general knowledge by asking players to fit words into a grid "
                   "using given clues. They help expand language skills and keep the mind sharp.")

    # function for displaying information about Coding
    def coding_info():
        tile = st.container(border=True)
        tile.title("Coding")
        tile.image("https://i.insider.com/60144316a7c0c4001991dde6?width=800&format=jpeg&auto=webp")
        tile.write(
            "Coding involves writing and structuring computer programs, similar to solving a puzzle with logic and "
            "creativity. It enhances problem-solving skills and is used in everything from web development to "
            "artificial intelligence.")

    # function for displaying information about Wooden Puzzles
    def wooden_puzzles_info():
        tile = st.container(border=True)
        tile.title("Wooden Puzzles")
        tile.image(
            "https://magicholz.de/cdn/shop/files/LKB01-Classic-Gramophone-Robotime-ROKR-v10.png?v=1699300249&width=960")
        tile.write(
            "Wooden puzzles come in many forms, from interlocking pieces to handcrafted brain teasers. They offer "
            "a tactile and engaging challenge that improves spatial reasoning and patience.")

    # function for displaying information about Metal Puzzles
    def metal_puzzles_info():
        tile = st.container(border=True)
        tile.title("Metal Puzzles")
        tile.image(
            "https://www.kastner-oehler.de/metal+earth-3d+metallbausatz+-+star+wars+-+sith+tie+fighter-1-768_1024_75-7429781_1.webp")
        tile.write(
            "Metal puzzles involve disentangling linked rings, wires, or shapes, requiring a mix of dexterity and "
            "logical thinking. They are fun and satisfying brain teasers that test patience and problem-solving "
            "skills.")

    # function for displaying information about Lego
    def lego_info():
        tile = st.container(border=True)
        tile.title("Lego")
        tile.image("https://lego.storeturkey.com.tr/millennium-falcon-v29-star-wars-lego-24646-33-B.jpg")
        tile.write("Building with Lego allows for endless creativity, whether constructing detailed models or original "
                   "designs. It enhances spatial awareness, engineering skills, and imagination in both children and "
                   "adults.")

    # function for displaying information about Painting
    def painting_info():
        tile = st.container(border=True)
        tile.title("Painting")
        tile.image("https://images.seattletimes.com/wp-content/uploads/2019/07/ross1_0723.jpg?d=1020x680")
        tile.write(
            "Painting is a creative expression that allows artists to bring their imagination to life using colors "
            "and brushes. It can be a relaxing hobby that enhances focus, emotional expression, and artistic "
            "skills while producing unique and personal artworks.")

    # with the columns display the different hobbies
    with c1:
        origami_info()

    with c2:
        knitting_info()

    with c3:
        sudoku_info()

    with c1:
        crossword_info()

    with c2:
        coding_info()

    with c3:
        wooden_puzzles_info()

    with c1:
        metal_puzzles_info()

    with c2:
        lego_info()

    with c3:
        painting_info()


# definition for the journey page
def journey_page():
    st.title("My Puzzle Journey🌟🧩🧠💓")
    st.write("I started puzzling during the COVID lockdown and quickly fell in love with it. Since then, "
             "I’ve completed around 30 puzzles and 20 wooden puzzles, but I’ve lost count of how many LEGO sets "
             "I’ve built. It’s my favorite way to spend my free time—it helps me relax, clear my mind, and unwind. "
             "The best part is seeing the finished product and using it to decorate my room, turning my hobby into "
             "something both creative and rewarding.")
    st.subheader("Here are some impressions of me and my 🧩Puzzles🧩")
    random_message() # display random message with st.toast

    # create two columns to display different puzzle images
    c1, c2 = st.columns(2)

    # definition for the first columns and the images displayed in it
    def journey_images_one():
        tile = st.container()
        tile.image("images/IMG_2663.JPG")
        tile.image("images/23E5963A-E0CA-4FEC-82F9-CC2BB34937C3.JPG")
        tile.image("images/IMG_2661.JPG")
        tile.image("images/IMG_3093.JPG")
        tile.image("images/IMG_1187.jpg")
        tile.image("images/9B63ECCC-7F06-4E37-B174-61DCA2E733A9 2.jpg")
        tile.image("images/F089577B-648F-4F1D-A21C-6EFA02A326AA.jpg")
        tile.image("images/7D140F56-97D3-4FE3-83BA-1C144F05C1D8 2.JPG")

    # definition for the second columns and the images displayed in it
    def journey_images_two():
        tile = st.container()
        tile.image("images/IMG_4876.JPG")
        tile.image("images/IMG_2665.JPG")
        tile.image("images/IMG_2097.jpg")
        tile.image("images/IMG_2670.JPG")
        tile.image("images/IMG_4036.JPG")
        tile.image("images/IMG_2664.JPG")

    # display the images in the columns
    with c1:
        journey_images_one()

    with c2:
        journey_images_two()

# page selection: when the user selects a page, show the new content
if page_selection == "Welcome To PuzzlePortal":
    welcome_page()
elif page_selection == "Find Your Puzzle!":
    preference_page()
elif page_selection == "Reviews":
    review_page()
elif page_selection == "Get Inspired!":
    inspiration_page()
elif page_selection == "My Puzzle Journey":
    journey_page()
