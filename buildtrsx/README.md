# TRSX generator
A little brief about what the project is about. It should be like a small summary format
 informing about the main purpose of the project.
# Motivation
This section is for letting the reader know why you created this project, the reason 
behind pursuing such a project, and why you have decided to do it.
# Features
This is where you write what all extra features have been done in your project.
 Basically this is where you try to make your project stand out from the rest.

# Code Examples
This is where you try to compress your project and make the reader understand
 what it does as simply as possible. This should help the reader understand if your code
  solves their issue.
  

The build_project.py module contains the functions to manage the following nodes: 

- **Project node** : A project encapsulates a large part of what is in the NLU model.
 The project node is required for a TRSX file to be valid and for an import to proceed.
 The project node contains 
    - **Metadata node** (zero-one):
    Lets you manage extra details about your project, such as author or version.
    The metadata node contains
        - **Entry node**(zero-many):
        The entry node contains the key-value pair that specifies the metadata.
        The entry node has the attribute key, which is a string. The entry's value can be any string.
    - sources node (zero-one), 
    - ontology node (zero-one), 
    - dictionary node (zero-one)
    - sample node (zero-many).
  
```
metadata_node = trsx_metadata_node(author = "Danae Martinez",
                                   version = "1.0.0",
                                   description = "my NLU model",
                                   date = "january 2022")
```  

# How to Use?
As I have mentioned before, you never know who is going to read your readme. 
So it is better to provide information on how to use your project. A step-by-step guide 
is best suited for this purpose. It is better to explain steps as detailed as possible
 because it might be a beginner who is reading it.
