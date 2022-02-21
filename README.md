
# TRSX generator

Receives information about a NLU model and return the corresponding TRSX file 
ready to be used by the Mix.nlu tool.

# Motivation

In order to avoid manual manipulations using the UI of Mix.nlu and east the 
version control process of NLU models, it is preferable to work with .trsx 
files, which are a special type of XML files that conforms to Nuance Mix 
specifications. 

Sometimes, it is more flexible to work with separate files that manage the 
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

The module build_project.py contains the functions to generate the metadata and 
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
author or version.The metadata node contains zero or many entry nodes. 

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
identify its origin. The sources node contains zero or many source nodes.
    
- Source nodes (zero-many)

Contains one required attribute, name. To label data, in the concept node you 
set its `sourceref` attribute to the name of the source.

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
The intents node contains zero or many intent nodes. 
    - **intent node** (zero-many).
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
    Each concept node defines a single entity and contains zero or one settings
    and relations node.
        - **settings** (zero-one).Documentation about this specific node is 
        quite incomplete in the Nuance documentation. 
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
  
### samples node (zero-many)  

Samples are sentences that are used to train your NLU model. Samples are labeled with intents and annotated with entities. The samples node contains zero or many sample node and each sample node contains zero or many annotation node

The data augmentation using semantic signatures can be done at the same time as the node construction and annotation process. The example below show how to generate a samples node from a dictionary representing one phase structure corresponding to a particular semantic signature. 

```python

from buildtrsx.build_samples.build_utterances import (
    generate_utterances,
    generate_utterances_dict,
)
from buildtrsx.build_samples.build_samples import trsx_samples_node

samples = {
    "action_verb": ["take", "transfer", "withdraw"],
    "origin_prep": ["from my"],
    "FROM_ACCOUNT": ["checking account", "savings account"],
    "destination_prep": ["to my", "over to my", "into my", "to put in my"],
    "TO_ACCOUNT": [
        "TFSA",
        "Tax-Free Savings Account",
        "CELI",
        "RRSP",
        "RSP",
        "RESP",
    ],
}

utterances = generate_utterances(samples, sample_size=5)

dict_utterances = generate_utterances_dict(
    samples=utterances,
    samples_attr={"intentref": "MAKE_INVESTMENT"}
)

samples_node = trsx_samples_node(samples=dict_utterances)
print(samples_node)
```

```xml
<samples>
	<sample intentref="MAKE_INVESTMENT">withdraw from my savings account to my RRSP</sample>
	<sample intentref="MAKE_INVESTMENT">transfer from my checking account to put in my Tax-Free Savings Account</sample>
	<sample intentref="MAKE_INVESTMENT">transfer from my savings account to put in my RESP</sample>
	<sample intentref="MAKE_INVESTMENT">take from my savings account to my Tax-Free Savings Account</sample>
	<sample intentref="MAKE_INVESTMENT">withdraw from my savings account into my RESP</sample>
</samples>
```

It is also possible to annotate samples as a pre-requisite of the samples node construction. 

```python
from buildtrsx.build_samples.build_samples import (
    trsx_annotated_literals,
    trsx_samples_node,
)
from buildtrsx.build_samples.build_utterances import (
    generate_utterances,
    generate_utterances_dict,
)

entities = {
    "TO_ACCOUNT": {"type": "isA", "conceptref": "ACCOUNT_TYPE"},
    "FROM_ACCOUNT": {"type": "isA", "conceptref": "ACCOUNT_TYPE"},
    "AMOUNT": {"type": "isA", "conceptref": "nuance_AMOUNT"},
    "ACCOUNT_TYPE": {},
}

samples_ann = trsx_annotated_literals(entities=entities, samples=samples)
samples.update(samples_ann)

annotated_utterances = generate_utterances(samples, sample_size=5)

dict_utterances = generate_utterances_dict(
    samples=annotated_utterances,
    samples_attr={"intentref": "MAKE_INVESTMENT"}
)

samples_node = trsx_samples_node(samples=dict_utterances)
print(samples_node)
```


```xml
<samples>
	<sample intentref="MAKE_INVESTMENT">withdraw from my 
	    <annotation conceptref="FROM_ACCOUNT">
	        <annotation conceptref="ACCOUNT_TYPE">checking account </annotation>
	    </annotation> to put in my 
        <annotation conceptref="TO_ACCOUNT">
            <annotation conceptref="ACCOUNT_TYPE">RRSP</annotation>
        </annotation>
    </sample>
	<sample intentref="MAKE_INVESTMENT">take from my 
        <annotation conceptref="FROM_ACCOUNT">
            <annotation conceptref="ACCOUNT_TYPE">checking account</annotation>
        </annotation> into my 
        <annotation conceptref="TO_ACCOUNT">
            <annotation conceptref="ACCOUNT_TYPE">Tax-Free Savings Account</annotation>
        </annotation>
    </sample>
	<sample intentref="MAKE_INVESTMENT">withdraw from my 
        <annotation conceptref="FROM_ACCOUNT">
            <annotation conceptref="ACCOUNT_TYPE">savings account</annotation>
        </annotation> into my 
        <annotation conceptref="TO_ACCOUNT">
            <annotation conceptref="ACCOUNT_TYPE">RESP</annotation>
        </annotation>
    </sample>
	<sample intentref="MAKE_INVESTMENT">transfer from my 
        <annotation conceptref="FROM_ACCOUNT">
            <annotation conceptref="ACCOUNT_TYPE">checking account</annotation>
        </annotation> into my 
        <annotation conceptref="TO_ACCOUNT">
            <annotation conceptref="ACCOUNT_TYPE">CELI</annotation>
        </annotation>
    </sample>
	<sample intentref="MAKE_INVESTMENT">take from my 
        <annotation conceptref="FROM_ACCOUNT">
            <annotation conceptref="ACCOUNT_TYPE">checking account</annotation>
        </annotation> into my 
        <annotation conceptref="TO_ACCOUNT">
            <annotation conceptref="ACCOUNT_TYPE">RRSP</annotation>
        </annotation>
    </sample>
</samples>
```
