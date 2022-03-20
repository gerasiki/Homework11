import json

__data = []


def load_candidates_from_json(path):
    '''возвращает список кандидатов'''
    global __data
    with open(path, 'r', encoding='utf-8') as file:
        __data = json.load(file)
    return __data


def get_candidate(candidate_id):
    '''возвращает одного кандидата по его id'''
    for candidate in __data:
        if candidate['id'] == candidate_id:
            return {'name': candidate['name'],
                    'position': candidate['position'],
                    'picture': candidate['picture'],
                    'skills': candidate['skills']
                    }
    return {'not_found': 'Кандидат не найден'}


def get_candidates_by_name(candidate_name):
    '''возвращает кандидатов по имени'''
    return [candidate for candidate in __data if candidate_name.lower() in candidate['name'].lower()]
    # Мой цикл
    # candidate = []
    # for i in __data:
    #     if candidate_name.lower() in i['name'].lower():
    #         candidate.append(i)
    # return candidate


def get_candidates_by_skill(skill_name):
    '''возвращает кандидатов по навыку'''
    list_candidates_skills = []
    for candidate in __data:
        skills = candidate['skills'].lower().split(', ')
        if skill_name.lower() in skills:
            list_candidates_skills.append(candidate)
    return list_candidates_skills
