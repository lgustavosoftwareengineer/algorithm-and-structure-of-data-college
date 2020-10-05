from utils.Agent import Agent
from PesquisaBinaria.binarySearchRecursive import binaryResearch as binarySearchRecursive
from PesquisaBinaria.binarySearchIterative import binaryResearch as binarySearchIterative
from PesquisaSequencial.sequencialSearch import sequencialSearch

ValorantCharacters = []

ValorantCharacters.append(Agent(1, "Raze"))
ValorantCharacters.append(Agent(2, "Breach"))
ValorantCharacters.append(Agent(3, "Phoenix"))
ValorantCharacters.append(Agent(4, "Viper"))
ValorantCharacters.append(Agent(5, "Sova"))
ValorantCharacters.append(Agent(6, "Omen"))
ValorantCharacters.append(Agent(7, "Sage"))
ValorantCharacters.append(Agent(8, "Brimstone"))
ValorantCharacters.append(Agent(9, "Cypher"))
ValorantCharacters.append(Agent(10, "Jett"))
ValorantCharacters.append(Agent(11, "Reyna"))
ValorantCharacters.append(Agent(12, "Killjoy"))

# =====================================================================
#                    ITERATIVE BINARY SEARCH
# =====================================================================
AgentIterativeBinarySearch = binarySearchIterative(ValorantCharacters, 2)
print('--------------------------')
print('Iterative binary search example: ')
print('--------------------------')

if AgentIterativeBinarySearch is not None:
    print('Response: ' + AgentIterativeBinarySearch.name)
else:
    print("The value isn't in ValorantCharacters or the list is invalid")

# =====================================================================
#                    RECURSIVE BINARY SEARCH
# =====================================================================
AgentRecursiveBinarySearch = binarySearchRecursive(ValorantCharacters, 2)
print('--------------------------')
print('Recursive binary search example: ')
print('--------------------------')

if AgentRecursiveBinarySearch is not None:
    print('Response: ' + AgentRecursiveBinarySearch.name)
else:
    print("The value isn't in ValorantCharacters or the list is invalid")


# =====================================================================
#                    SEQUENCIAL SEARCH
# =====================================================================
AgentSequencialSearch = sequencialSearch(ValorantCharacters, 3)
print('--------------------------')
print('Sequencial search example: ')
print('--------------------------')

if AgentSequencialSearch is not None:
    print('Response: ' + AgentSequencialSearch.name)
else:
    print('The value isnt in ValorantCharacters or the list is invalid')
