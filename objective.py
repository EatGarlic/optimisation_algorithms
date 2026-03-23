import random
from context import *


# weights
_a = 0.20
_b = 0.20
_d = 0.20
_t = 0.20
_y = 0.20


__cost_cache = {}
def calculate_cost(scenario: list[int], cache=True) -> float:
    if str(scenario) in __cost_cache and cache:
        return __cost_cache[str(scenario)]

    staff_dict = {s.id: s for s in STAFF_LIST}

    staff_projects = {s.id: [] for s in STAFF_LIST}

    for proj_idx, staff_id in enumerate(scenario):
        staff_projects[staff_id].append(PROJECTS_LIST[proj_idx])

    overwork_penalty = 0.0
    skill_penalty = 0.0
    difficulty_penalty = 0.0
    deadline_penalty = 0.0

    # unique assignment
    assignment_violation = len(scenario) - len(set(scenario))

    for staff_id, projects in staff_projects.items():
        staff = staff_dict[staff_id]

        # capacity constraint (overworked hours)
        overwork_penalty += max(0, sum(p.estimated_time for p in projects) - staff.available_hours)

        for project in projects:
            # specialized skill matching
            if project.required_skill not in staff.skills:
                skill_penalty += 1

            # skill level constraint (difficulty)
            difficulty_penalty += max(0, project.difficulty - staff.skill_level)

        # deadline consideration
        time_sum = 0

        for project in sorted(projects, key=lambda p: p.estimated_time):
            time_sum += project.estimated_time
            deadline_penalty += max(0, time_sum - project.deadline)

    out = _a * overwork_penalty + _b * skill_penalty + _d * difficulty_penalty + _t * deadline_penalty + _y * assignment_violation
    
    if cache:
        __cost_cache[str(scenario)] = out
    
    return out


def print_scenario(scenario: list[int], cost:False) -> None:
    for p, s in enumerate(scenario):
        print(f"P{p + 1} -> S{s}")
    
    if cost:
        print(f'  Cost: {calculate_cost(scenario)}')


def randomScenario():
    return [random.randint(1, len(STAFF_LIST)) for _ in range(len(PROJECTS_LIST))]


# class Assignment:


#     def __init__(self, assignment=None):
#         self.__vector = assignment
#         if assignment == None:
#             self.__vector = randomScenario()

    
#     def getVector(self, copy=False):
#         if copy:
#             return self.__vector[:]

#         return self.__vector
    
#     def cost(self):
#         return calculate_cost(self.__vector)

        



if __name__ == "__main__":
    scenarios = {
        'good': [[1, 2, 3, 2, 5, 4, 1, 4, 3, 5], None],
        'okay': [[1, 2, 1, 5, 3, 2, 4, 4, 1, 4], None],
        'bad': [[3, 3, 1, 3, 1, 3, 1, 1, 3, 1], None]
    }

    print_scenario(scenarios['good'][0])
    print()

    for s in scenarios:
        score = round(calculate_cost(scenarios[s][0]), 2)

        print(f'{s}: {score}')

        if score != scenarios[s][1] and scenarios[s][1] != None:
            print(f"ERROR {score} != {scenarios[s][1]}")