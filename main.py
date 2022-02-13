
from buildtrsx.build_ontology.build_ontology import trsx_intents_node

intents_investment = {"MAKE_AMENDMENT":[],
                      "MAKE_INVESTMENT":[],
                      "MAKE_WITHDRAWAL":[],
                      "OPEN_ACCOUNT":[],
                      "REQUEST_BALANCE":[],
                      "REQUEST_FOLLOW_UP":[]}

# intents without entitites associated
intents_node = trsx_intents_node(intents=intents_investment)
print(intents_node)