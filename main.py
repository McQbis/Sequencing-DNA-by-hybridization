f = open("input.txt", "r")
words = list(set(f.read().split()))

result = words[0]
# # words.remove(result)

word_length = len(words[0])

# # while len(words) > 0:
# #     tmp_bool = 0
# #     # for k in range(word_length - 1, 1, -1):
# # # k = 9
for i in range(len(words)):
    tmp_bool = 0
    for k in range(word_length - 1, 1, -1):
        for word in words:
            if result[-k:] == word[:k]:
                result += word[k:]
                # words.remove(word)
                tmp_bool = 1
                break
        if tmp_bool:
            break

print(len(result))

# graph = dict()
# is_in_sequence = dict()

# for i in range(len(words)):
#     graph[words[i]] = []
#     is_in_sequence[words[i]] = 0
#     for k in range(word_length - 1, 1, -1):
#         for j in range(len(words)):
#             if i != j and words[i][-k:] == words[j][:k]:
#                 graph[words[i]].append(words[j])

# result = graph.keys()[0]
# for v in graph:
#     for adj in v:
#         if is_in_sequence[adj] == 0:
#             result += 
#             is_in_sequence[adj] = 1

# print(graph)