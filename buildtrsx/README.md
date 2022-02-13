
# TRSX generator

Input information about a NLU model and return the corresponding TRSX file ready 
to be used by the Mix.nlu tool.

# Motivation

In order to avoid manual manipulations using the UI of Mix.nlu and east the 
version control process of NLU models, it is preferable to work with .trsx 
files, which are a special type of XML files that conforms to Nuance Mix 
specifications.

# Features

This package allows to manage nodes separately, so the user can generate 
accepted files keeping separately the ontology, dictionaries and samples parts 
of the NLU project. 

# TRSX file structure 

## Project node

A project encapsulates a large part of what is in the NLU model. The project 
node is required for a TRSX file to be valid and for an import to proceed.

The project node contains 

- zero or one metadata node
- zero or one sources node 
- zero or one ontology node 
- zero or one dictionary node 

### Metadata node (zero-one)

Lets you manage extra details about your project, such as author or version.
The metadata node contains

- Entry node (zero-many)

The entry node contains the key-value pair that specifies the metadata. The 
entry node has the attribute key, which is a string. The entry's value can be 
any string.
        
### Sources node (zero-one)

The Sources node provides a list of sources used to label imported data to 
identify its origin. The sources node contains
    
- Source nodes (zero-many)
        
### Ontology node (zero-one)

The intents and entities defined in the ontology are used to annotate the 
training data, and thus form the interface between the NLU and the client 
application. The ontology node contains

- **Intents** (zero-one).
    - **intent nodes** (zero-many).
        - **links node** (zero-one).
        An intent is linked to a set of entities. The links node describes the 
        entities that can be used in sample annotations for this intent.
- **concepts** (one).
The concepts node is composed by the ontology entities and contains:
    - **concept** (zero-many).
    Each concept node defines a single entity and contains:
        - **relations** (zero-one).
        The relations node specifies the relation between entities. Relations 
        can be of type isA, hasA, or hasReferrers. The relations node contains:
            - **relation** (zero-many) 
                
### dictionary (zero-one)

A List entity can have an associated dictionary. The dictionary is the list of spoken forms that correspond to 
'mentions' that are part of the entity. The dictionaries node contains:
  - **dictionary** (zero-many) Contains a required attribute conceptref, which defines the entity the entries 
  apply to. Each dictionary node contains 
    - **entry** (zero-many)
            
### samples (zero-many)
    

# Code Examples

The build_project.py module contains the functions to manage the following nodes: 

- sources 
- metadata 

```python

from buildtrsx.build_project import trsx_sources_node

source1 = {"type": "CUSTOM"}
source2 = {
    "uri": "http://localhost:80/my_local_dtv_domain",
    "version": "1.0",
    "type": "PREBUILT",
}
source3 = {
    "uri": "http://localhost:80/ncs_ref_rejection_model",
    "version": "1.0",
    "type": "REJECTION",
}
source4 = {
    "displayName": "nuance_custom_data",
    "version": "1.0",
    "type": "CUSTOM",
    "useForOOV": "true",
}

sources = {
    "IOT_Domain": source1,  # key (source' name) value (optional attributes)
    "DTV_Domain": source2,
    "NCSRef_Rejection": source3,
    "My_data": None,
    "nuance_custom_data": source4,
}

project_attributes = {
    "xmlns:nuance": "https://developer.nuance.com/mix/nlu/trsx",
    "xml:lang": "eng-USA",  # 'fra-CAN'
    "nuance:enginePackVersion": "hosted",
}

# call the sources node
sources_node = trsx_sources_node._original(sources=sources)

# call the wrapped sources node
wrapped_sources_node = trsx_sources_node(sources=sources, attributes=project_attributes)

```  

```python

from buildtrsx.build_project import trsx_metadata_node

# call the metadata node
metadata_node = trsx_metadata_node._original(
    author="Danae Martinez",
    version="1.0.0",
    description="my NLU model",
    date="january 2022")
    
wrapped_metadata_node = trsx_metadata_node(
    author="Danae Martinez",
    version="1.0.0",
    description="my NLU model",
    date="january 2022",
    attributes=project_attributes)    
    
```


```  
entity1_make_inv = {'conceptref':'FROM_ACCOUNT', 'sourceref': 'some_source'}
entity2_make_inv = {'conceptref':'TO_ACCOUNT', 'sourceref': 'some_source'}
entity3_make_inv = {'conceptref': 'ACCOUNT_TYPE', 'sourceref': 'some_source'}
entity4_make_inv = {'conceptref': 'AMOUNT', 'sourceref': 'some_source'}
entity1_open_acc = {'conceptref':"ACCOUNT_TYPE"}

intent_entities = {"MAKE_INVESTMENT": [entity1_make_inv, 
                                       entity2_make_inv, 
                                       entity3_make_inv, 
                                       entity4_make_inv],
                   "OPEN_ACCOUNT" : [entity1_open_acc],
                   "OUT_OF_DOMAIN" : [],
                   "GOODBYE" : []}

intents_node = trsx_intents_node(intents = intent_entities)
``` 

``` 
entities = {"TO_ACCOUNT":{'type':"isA", 'conceptref':"ACCOUNT_TYPE"},
            "FROM_ACCOUNT":{'t
            ype':"isA", 'conceptref':"ACCOUNT_TYPE", "sourceref": "some source"},
            "AMOUNT":{'type':"isA", 'conceptref':"nuance_AMOUNT"},
            "BANK_ACCOUNT":{'type':"hasA", 'conceptref':["ACCOUNT_BALANCE", "ACCOUNT_NUMBER", "ACCOUNT_TYPE"]}}
            
concepts_node = trsx_concepts_node(entities = entities)            
```  

``` 
intents_node = trsx_intents_node(intents = intent_entities)
concepts_node = trsx_concepts_node(entities = entities)

ontology_node = trsx_ontology_node(intents_node = intents_node,
                                   concepts_node = concepts_node)
```  

```  
account_type = {'CELI':['CELI','Compte d’épargne libre d’impôt', 'Compte libre d’impôt'],
                'REER':['REER','Régime enregistré d’épargne retraite', 'Compte d’épargne-retraite']}

entities_literals_dict = {"ACCOUNT_TYPE":account_type}
trsx_dictionaries(entities = entities_literals_dict)
```  


