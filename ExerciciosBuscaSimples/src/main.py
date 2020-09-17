from utils.Agent import Agent
from PesquisaBinaria.binarySearchRecursive import researchAgentsRecursive
from PesquisaBinaria.binarySearchIterative import researchAgentsIterative

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

#Agent = researchAgentsRecursive(ValorantCharacters, 6)
Agent = researchAgentsIterative(ValorantCharacters, 2)

if Agent is not None:
    print(Agent.name)
else:
    print('The value isnt in ValorantCharacters or the list is invalid')
