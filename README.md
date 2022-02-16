
# TRSX generator

Receives information about a NLU model and return the corresponding TRSX file 
ready to be used by the Mix.nlu tool.

# Motivation

In order to avoid manual manipulations using the UI of Mix.nlu and east the 
version control process of NLU models, it is preferable to work with .trsx 
files, which are a special type of XML files that conforms to Nuance Mix 
specifications. 

Sometimes, it is more flexible work with separate files that manage the 
ontology, the dictionaries and the samples separately. This set of functions 
allow users to automatically generate those separated files or one big file 
with all components. The final output is a .trsx file that can be interpreted 
by the Mix.nlu tool. 

# Features

This package allows to manage nodes separately, so the user can generate 
accepted files keeping the ontology, dictionaries and samples in separated parts 
of the NLU project that are then merged by Mix once uploaded. 

This package is composed by three sub-packages
- build dictionaries 
- build ontology 
- build samples 

The module build_project contains the functions to generate the metadata and 
sources node as well as the wrapper project function. 

# TRSX file structure 

## Project node

A project encapsulates a large part of what is in the NLU model. The project 
node is required for a TRSX file to be valid and for an import to proceed.

The project node contains 

- zero or one metadata node
- zero or one sources node 
- zero or one ontology node 
- zero or one dictionaries node 
- zero or many samples node 

```xml
<project nuance:version="2.5">
    <metadata/>
    <sources/>
    <ontology/>
    <dictionaries/>
    <samples/>
</project>
```

### Metadata node (zero-one)

The metadata node lets you manage extra details about your project, such as 
author or version.The metadata node contains zero or manu entry nodes. 

- Entry node (zero-many)

The entry node contains the key-value pair that specifies the metadata. The 
entry node has the attribute key, which is a string. The entry's value can be 
any string.

```python
from buildtrsx.build_project import trsx_metadata_node

metadata_node = trsx_metadata_node(
    author="Danae Martinez",
    version="1.0.0",
    description="my NLU model",
    date="february 2022",
)
print(metadata_node)
```

```xml
	<metadata>
		<entry key="author">Danae Martinez</entry>
		<entry key="version">1.0.0</entry>
		<entry key="description">my NLU model</entry>
		<entry key="date">february 2022</entry>
	</metadata>
```

### Sources node (zero-one)

The Sources node provides a list of sources used to label imported data to 
identify its origin. The sources node contains zero or many source nodes
    
- Source nodes (zero-many)

Contains one required attribute, name.

```python
from buildtrsx.build_project import trsx_sources_node

sources_nlu = {"My_data": {"type": "CUSTOM"}, "Prod_data": {"type": "VERINT"}}

sources_node = trsx_sources_node(sources=sources_nlu)
print(sources_node)
```

```xml
	<sources>
		<source  name="My_data" type="CUSTOM" />
		<source  name="Prod_data" type="VERINT" />
	</sources>
```

### Ontology node (zero-one)

The intents and entities defined in the ontology are used to annotate the 
training data, and thus form the interface between the NLU and the client 
application. The ontology node contains

- **Intents** (zero-one).
The intents node contains zero or many intent node. 
    - **intent nodes** (zero-many).
    Each intent in the ontology has its own intent node.
        - **links node** (zero-one).
        An intent is linked to a set of entities. The links node describes the 
        entities that can be used in sample annotations for this intent.
        
        ```python
        from buildtrsx.build_ontology.build_ontology import trsx_intents_node

        intent = {
            "MAKE_WITHDRAWAL": [
                {"conceptref": "FROM_ACCOUNT"},
                {"conceptref": "TO_ACCOUNT"},
                {"conceptref": "AMOUNT"},
            ],
            "MAKE_INVESTMENT": [
                {"conceptref": "FROM_ACCOUNT"},
                {"conceptref": "TO_ACCOUNT"},
                {"conceptref": "AMOUNT"},
            ],
        }
        
        intents_node = trsx_intents_node(intents = intent)
        print(intents_node)
        ```
        
        ```xml
            <intents>
            	<intent name="MAKE_WITHDRAWAL">
            		<links>
            			<link conceptref="FROM_ACCOUNT" />
            			<link conceptref="TO_ACCOUNT" />
            			<link conceptref="AMOUNT" />
            		</links>
            	</intent>
            	<intent name="MAKE_INVESTMENT">
            		<links>
            			<link conceptref="FROM_ACCOUNT" />
            			<link conceptref="TO_ACCOUNT" />
            			<link conceptref="AMOUNT" />
            		</links>
            	</intent>
            </intents>
        ```

- **concepts** (one).
The concepts node is composed by the ontology entities and contains zero or many 
concept node.
    - **concept** (zero-many).
    Each concept node defines a single entity and contains zero or one relations 
    node.
        - **relations** (zero-one).
        The relations node specifies the relation between entities. Relations 
        can be of type **isA**, **hasA**, or **hasReferrers**. The relations 
        node contains zero or many relation.  
        
            - **relation** (zero-many) 
            The relation node has two required attributes: the type, that 
            indicates the type of relation, and the conceptref, that indicates 
            the name of entity to which the relation applies. See the second 
            example below. 
          
            ```python
            from buildtrsx.build_ontology.build_ontology import trsx_concepts_node
            
            entities = {
                "TO_ACCOUNT": {},
                "FROM_ACCOUNT": {},
                "AMOUNT": {},
                "ACCOUNT_TYPE": {},
            }
            
            concepts_node = trsx_concepts_node(entities=entities)
            print(concepts_node)
            ```
            ```xml
                <concepts>
                    <concept name="AMOUNT"/>
                    <concept name="TO_ACCOUNT"/>
                    <concept name="FROM_ACCOUNT"/>
                    <concept name="ACCOUNT_TYPE"/>
                </concepts>
            ```
            The inner dictionary contains the attributes of the relation node.
            If left empty, the relations node won't be generated. 
            
            ```python
            entities = {
                "TO_ACCOUNT": {'type':"isA", 'conceptref':"ACCOUNT_TYPE"},
                "FROM_ACCOUNT": {'type':"isA", 'conceptref':"ACCOUNT_TYPE"},
                "AMOUNT": {'type':"isA", 'conceptref':"nuance_AMOUNT"},
                "ACCOUNT_TYPE": {},
            }
            concepts_node = trsx_concepts_node(entities=entities)
            print(concepts_node)
            ```
            
            ```xml  
                <concepts>
                    <concept name="AMOUNT">
                        <relations>
                            <relation type="isA" conceptref="nuance_AMOUNT"/>
                        </relations>
                    </concept>
                    <concept name="TO_ACCOUNT">
                        <relations>
                            <relation type="isA" conceptref="ACCOUNT_TYPE"/>
                        </relations>
                    </concept>
                    <concept name="FROM_ACCOUNT">
                        <relations>
                            <relation type="isA" conceptref="ACCOUNT_TYPE"/>
                        </relations>
                    </concept>
                    <concept name="ACCOUNT_TYPE"/>
                </concepts>
            ```
            
### Dictionaries (zero-one)

A List entity can have an associated dictionary. The dictionary is the list of spoken forms that correspond to 
'mentions' that are part of the entity. The dictionaries node contains zero or many dictionary nodes.
  - **dictionary** (zero-many) Contains a required attribute conceptref, which defines the entity the entries 
  apply to. Each dictionary node contains zero or many entry nodes. 
    - **entry** (zero-many)
    ```python
    from buildtrsx.build_dictionaries.build_dict import trsx_dictionaries
    
    account_type = {
        "CELI": ["CELI", "Compte libre d’impôt"],
        "REER": ["REER", "Compte d’épargne-retraite"],
        "REEE": ["REEE", "R trois E"],
    }
    
    literals = {"ACCOUNT_TYPE": account_type}
    print(trsx_dictionaries(entities=literals))
    
  ```
  ```xml
  <dictionaries>
      <dictionary conceptref="ACCOUNT_TYPE">
          <entry literal="CELI" value="CELI"/>
          <entry literal="Compte d'épargne-retraite" value="REER"/>
          <entry literal="Compte libre d’impôt" value="CELI"/>
          <entry literal="R trois E" value="REEE"/>
          <entry literal="REEE" value="REEE"/>
          <entry literal="REER" value="REER"/>
      </dictionary>
  </dictionaries>
  ```
    