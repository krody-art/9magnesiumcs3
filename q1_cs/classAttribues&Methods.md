## OOP Activity Part II
| Attribute | Data Type | Visibility | Why Public/Private? |
|---|---|---|---|
| Health | Float | Public | For teammates to know what state the character is in. |
| Stamina/Energy | Float | Public | For teammates to know what state the character is in. |
| Role | String | Public | For strategy planning purposes. |
| Strength | Integer | Private | Only the player knows the physical capabilites of their character |
| Magic Attack | Integer | Private | Only the player knows the physical capabilites of their character |
| Online | True | Public | To know if the player is online or not.

<img width="1920" height="1080" alt="Class Diagram (2)" src="https://github.com/user-attachments/assets/b05f7d45-d99e-4e4c-bed5-44b625b7c6f6" />

### Step 6:

## Hero 1:
| Attribute | Value |
|---|---|
| Health | 100 |
| Stamina | 50 |
| Role | Noobie Wizard |
| Strength | 15 |
| Magic Attack | 35 |
| Currency | 150 |
| Online Status | True |

## Hero 2:
| Attribute | Value |
|---|---|
| Health | 50 |
| Stamina | 150 |
| Role | Intermediate Assassin |
| Strength | 60 |
| Magic Attack | 5 |
| Currency | 400 |
| Online Status | False |

## Methods
A support heals (adds 10 to their health) Hero 1, but does not heal Hero 2.

Hero 1:
| Attribute | New Value |
|---|---|
| Health | **110** |
| Stamina | 50 |
| Role | Noobie Wizard |
| Strength | 15 |
| Magic Attack | 35 |
| Currency | 150 |
| Online Status | True |

Hero 2:
| Attribute | Value |
|---|---|
| Health | 50 |
| Stamina | 150 |
| Role | Intermediate Assassin |
| Strength | 60 |
| Magic Attack | 5 |
| Currency | 400 |
| Online Status | False |

^ --- Retains

<img width="1587" height="2245" alt="Blue and White Futuristic Page Border Portrait A3 Poster" src="https://github.com/user-attachments/assets/f1451202-d08b-443d-8b9b-4eafd43d9620" />

## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)

## Design Revision
I added attributes and methods to my class and instantiated objects that have distinct values.

## Analysis
|  |  |
|---|---|
| Why did you make your chosen attribute private? | To protect data and control how other parts of a program use it, and to hide complex internal mechanisms and show only what the user needs to see. |
| Which method changes the state of your object? | Mutator Method |
| How did your two objects demonstrate that instances are independent? | Each object has its own values and is not affected when another object is altered. |
| What is the difference between your class diagram and your object diagram? | A class diagram represents the structure or the blueprint of a system, while the object diagram represents the functionality of the class---Instantiating objects. |
