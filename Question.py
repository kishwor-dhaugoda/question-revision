from itertools import islice
import json

questions = {}
categories = {}

def load_questions():
    global questions
    global categories

    # Load the JSON data from the file
    with open("questions.json", "r") as file:
        questions = json.load(file)     

    with open('categories_themes.json', 'r') as file:
        data = json.load(file)    
        categories = data["categories"]

def write_questions():
    global questions

    with open("questions.json", "w") as file:
        json.dump(questions, file, indent=4)

def get_questions():
    global questions
    return questions

def get_categories():
    global categories
    return categories

def delete_selected_row(ids_to_delete):
    for id in ids_to_delete:
        questions.pop(id, None)
    write_questions()

def delete_one_row(id):
    global questions
    questions.pop(id, None)
    write_questions()

def add_revised(id):
    questions[id]["revised"] += 1
    write_questions()
    return questions[id]["revised"]


def search_question(qid):
    global questions
    return questions[qid]
    
def add_question(qid, question, solution, category, difficulty, revised):
    global questions
    
    questions[qid] = {
            "question": question,
            "solution": solution,
            "category": category,
            "difficulty": difficulty,
            "revised": revised
    }
    write_questions()

def search_questions_by_categories(no_ques, categories, difficulties, rev):
    global questions
    
    # Filter questions based on the selected categories

    if rev == -1:
        selected_questions = dict(islice(
        (
            (qid, question)
            for qid, question in questions.items()
            if question.get("category", "") in categories and question.get("difficulty", "") in difficulties
        ),
        no_ques  
    ))
    else:
        selected_questions = dict(islice(
        (
            (qid, question)
            for qid, question in questions.items()
            if question.get("category", "") in categories and question.get("difficulty", "") in difficulties and question.get("revised") < rev
        ),
        no_ques 
    ))
    # islice() must be used on a generator or iterable before it becomes a dict.
    # dict() wraps the result to rebuild it as a dictionary.

    return selected_questions

def search_by_one_difficulty_count(difficulty):
    global questions
    global questions
    return sum(
        1
        for qid, question in questions.items()
        if question.get("difficulty", "") == difficulty
    )



def show_questions():
    global questions

    # print(questions["3"]["solution"])
    # print(questions["5"]["solution"])
    # print(questions["13"]["solution"])

    for qid in questions:
        print(questions[qid]['solution'])

# load_questions()
# print(len(questions))
# print(search_by_one_difficulty_count("Hard"))