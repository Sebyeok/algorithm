def solution(players, callings):
    answer = []
    dic = {}
    for i in range(len(players)):
        dic[players[i]] = i
    for calling in callings:
        x = dic[calling]
        players[x], players[x-1] = players[x-1], players[x]
        dic[players[x-1]], dic[players[x]] = x-1, x
    answer = players
    return answer