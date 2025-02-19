# ******************** Ultra Basic QnA Bot (Without GUI) ********************

# Importing required functions from re library
from re import IGNORECASE, search

# Defining Knowledge database
knowledge_base = {
    "application deadline": "The application deadline is December 1st for regular decision. "
                            "For CSE admission, the deadline is April 31, 2024. "
                            "However, applying early increases your chances of acceptance.",
    "application requirements": "You will need to submit your transcripts, test scores, essays, and letters of recommendation.",
    "admission requirements": "The requirements vary depending on your program of interest, but generally include transcripts, test scores, essays, and letters of recommendation. You can find more specific details on the college website.",
    "canteen": "The canteen offers a variety of options, including vegetarian and healthy choices. There are also several cafes and restaurants on campus if you're looking for something different.",
    "Professors": "The faculty at MIT are highly qualified and passionate about their subjects. They are generally approachable and supportive of their students.",
    "research opportunities for undergraduates": "Yes, several departments offer research opportunities for students. You can talk to your professors or department head to learn more about available options.",
    "labs": "The labs are modern and well-equipped with the latest technology. You'll have access to all the resources you need for your studies and research.",
    "Seminars and Events": "Yes, the college regularly hosts lectures, workshops, and seminars by renowned scholars and professionals. It's a great way to learn from experts and explore new ideas.",
}

# Dictionary to store collected user information
user_info = {}

def greetAndAskName():
    """Greets the user and asks for their name."""
    global user_info  # Ensure we're using a dictionary
    user_info = {}  # Initialize as a dictionary

    # Welcome statement
    print("Welcome to the College Admission Q&A Bot! I'm here to help answer your questions about the application process.")

    # Ask Name
    name = input("Before we start, could you please tell me your name? ").strip()
    
    # Store name in user_info dictionary
    user_info["name"] = name

    # Print Greeting
    print(f"Nice to meet you, {name}! Feel free to ask me any questions about college admission.")

# Function to handle questions
def handle_question(question):
    """Searches for keywords in the user's question and returns an appropriate response."""
    for keyword in knowledge_base:
        if search(keyword, question, IGNORECASE):  # Case-insensitive keyword search
            return knowledge_base[keyword]
    
    return "I'm not sure I understand that question. Could you rephrase it or try asking something different?"

# Core Functionality of Bot
def bot():
    """Main function to interact with the user."""
    greetAndAskName()

    while True:
        question = input("You: ").strip()

        # Exit conditions
        if question.lower() in ["goodbye", "bye", "quit", "exit"]:
            print(f"Thanks for using the College Admission Q&A Bot, {user_info['name']}! Have a great day.")
            break

        # Handle questions and provide responses
        answer = handle_question(question)
        print("Bot:", answer)

# Run the Bot
if __name__ == "__main__":
    bot()
