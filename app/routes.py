from flask import jsonify, request
from app import app
from app.summarizer import generate_summary, generate_example
from app.models_in_depth import topic_desc_generator, Question_bank
from app.models import ask_from_pdf
@app.route('/generate_all', methods=['POST'])
def generate_all():
    data = request.get_json()
    keywords = data.get('keywords', [])
    topic_description = data.get('topic_description', '')

    summary = generate_summary(keywords, topic_description)
    example = generate_example(keywords, topic_description)
    in_depth_explanation = topic_desc_generator(keywords, topic_description)
    practice_questions = Question_bank(in_depth_explanation)

    # print(summary.content)
    # print(example)
    # print(in_depth_explanation)
    # print(practice_questions)

    return jsonify({
        'summary': summary.content,
        'example': example,
        'in_depth_explanation': in_depth_explanation,
        'practice_questions': practice_questions
    })

@app.route('ask_pdf', methods=['POST'])
def ask_pdf():
    data = request.get_json()
    pdf_file = data.get('pdf_file', [])
    question = data.get('question', '')
    answer = ask_from_pdf(pdf_file, question)
    return jsonify({
        'answer': answer
    })

@app.route('/')
def index():
    return 'Root Page'