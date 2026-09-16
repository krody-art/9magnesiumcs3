# Class Relationships: Association and Multiplicity
## Previous Work q1_cs/classObjectUML.md

Part I - Classes and Objects(q1_cs/classObjectUML.md)
Part II - Class Attributes and Methods(q1_cs/classAttribues&Methods.md)

## Existing Class
Class: RPG Video Game Characters
Description: Properties and actions of particular characters.
## New Related Class
Class: Loot and Equipment
Description: Variation of loot obtained or bought for getting buffs or curses.
## Association
# Relationship: 

| CHARACTERS CONTAIN EQUIPMENT | Hero 1 ------- 0..*Loot
|---|---|

Explanation: Some equipment may change, increase, decrease, or remove certain attributes or make characters unable to perform specific actions.
## Multiplicity

Multiplicity: 
| Capacity to equip weapons / miscellaneous items | Storage (Backpack) | 
|---|---|
| 0..1 | 0..50 |
Explanation: Characters can equip 1 weapon or none at all, and can store a maximum of 50 items in their storage.

## UML Class Relationship Diagram
![Class Relationship Diagram](<img width="1920" height="1080" alt="Class Diagram" src="https://github.com/user-attachments/assets/ced71c2a-6675-4cf9-be90-488921b7600d" />)

## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
