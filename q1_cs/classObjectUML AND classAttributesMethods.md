# SG4 - Understanding Classes and Objects
## RPG (Video Game) Characters
## This example is observable in every game in the world of Role-Playing Games. From the whole franchise of Fallout to the horrific world of The Witcher 3.
## Properties
| Property | Data Type | Description |
|---|---|---|
| Health | Float | Every game character has this essential property in fighting games |
| Stamina/Energy | Float | This is similar to the attribute "Health". Characters cannot perform certain actions without stamina. |
| Role | String | Roles define a character's duties and responsibilities.|
| Strength | Integer | Measures the raw power of a character and the numerical value of their physical attack. |
| Magic Attack | Integer | Measures the capabilities of a character to perform witchcraft on individuals (elements) |
| Currency | Integer |Can be used to purchase items. |
| Online Status | Boolean | Determines if the player is online or not. |

## Methods
| Method | Description |
|---|---|
| Buy_Item() | Lets the player purchase an item for their character to be stronger and more resilient |
| Attack() | Allows the character to inflict damage on another individual |
| Heal() | Recovers health |
| Block() | Helps reduce damage from an attacker |
 
## Class Diagram
<img width="1920" height="1080" alt="Class Diagram" src="https://github.com/user-attachments/assets/246335bb-f5c5-4fb9-8c68-b82c5d1aedbf" />

## Design Explanation
### Why did you choose this class? It is one of the most common examples in the realm of OOP. It encompasses the 4 major pillars, which are Encapsulation, Abstraction, Inheritance, and Polymorphism
### Which property is the most important? Why? Health and Strength, since it is the most fundamental property of a video game character
### Which method is the most useful? Why? Attack() since it is the most essential action of an RPG game.

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
A support heals Hero 1 and does not heal Hero 2.


