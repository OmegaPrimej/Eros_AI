import spacy

Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

Define a function to process user input
def process_input(user_input):
    # Analyze the user input
    doc = nlp(user_input)
    
    # Initialize the intent variable
    intent = ""
    
    # Check for booking intent
    if "book" in user_input.lower() or "reservation" in user_input.lower():
        intent = "booking"
    # Check for cancellation intent
    elif "cancel" in user_input.lower():
        intent = "cancellation"
    # Check for information intent
    elif "what" in user_input.lower() or "where" in user_input.lower() or "when" in user_input.lower():
        intent = "information"
    
    # Return the identified intent
    return intent

Example usage:
user_input = input("Please enter your query: ")
intent = process_input(user_input)
print("Intent:", intent)
