class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skillMap = {req_skills[i]: i for i in range(len(req_skills))}
        newPeople = []
        for i in people:
            skill = 0
            for j in i:
                skill += 2 ** skillMap[j]
            newPeople.append(skill)
        # print(len(newPeople), len(set(newPeople)))

        people = []
        included = set()
        for i in range(len(newPeople)):
            if newPeople[i] in included or not newPeople:
                continue
            isSubset = False
            for j in range(len(newPeople)):
                if j != i and (newPeople[i] | newPeople[j] == newPeople[j]) and newPeople[i] != newPeople[j]:
                    isSubset = True
                    break
            if isSubset:
                continue
            people.append((newPeople[i], i))
            included.add(newPeople[i])
        target = sum(2 ** skillMap[i] for i in req_skills)
        # print(target, people)

        finalTeam = []
        def dp(index: int, val: int, team: list[int]) -> None:
            if val == target:
                nonlocal finalTeam
                if not finalTeam or len(team) < len(finalTeam):
                    finalTeam = team.copy()
                return
            if index == len(people):
                return
            dp(index + 1, val, team)
            dp(index + 1, val | people[index][0], team + [people[index][1]])
            return

        dp(0, 0, [])
        return finalTeam