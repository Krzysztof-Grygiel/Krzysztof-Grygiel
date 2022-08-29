from json import load

correct_answers = 0
with open('quiz.json', encoding='utf8') as questions_file:
    questions = load(questions_file)

    for question in questions:
        print(question['question'])
        for index, answer in enumerate(question['answers']):
            print(index, answer['text'])

        user_answer = int(input('Jak myślisz, która odpowiedź jest prawidłowa? '))
        try:
            is_correct_answer = question['answers'][user_answer]['correct']
            if is_correct_answer:
                correct_answers += 1
        except IndexError:
            pass
        print('--' * 10)

print('Poprawnych odpowiedzi', correct_answers)

