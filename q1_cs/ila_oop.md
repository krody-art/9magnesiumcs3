# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation is a fundamental concept of OOP wherein it combines data with methods into a single object. Its internal variables are private and can be controlled using controlled public methods. The user doesn't need to understand how the system works. For instance, you decide to withdraw cash from the bank. You cannot just get the money directly through the dispenser; You get your cash through managed transactions. 

Encapsulation bundles an item's data and actions into a single 'Product' class. It keeps properties like price and stockQuantity private while exposing public methods like updateStock. This prevents from the prices and quantities to be altered by individuals who have unrestricted access.

### 2. Abstraction
This OOP concept hides unnecessary internal details from the user, and lets the user focus on what an object does rather than how it does it. Let's say a phone; you can interact with it---(e.g., power button, Touch Screen, Wi-Fi, etc.)---but you don't need to comprehend how the phone really functions.

Abstraction hides complex inventory calculations from the store operator. The system provides a simple interface, like a checkout method, to process sales.

### 3. Inheritance
A core idea of OOP is that a new class takes the attributes of an existing class. This lets programmers reuse code and add new features. For example, a car is a vehicle, and so is a van; They both share a similar characteristic but are distinct to one another.

Inheritance allows items to inherit traits from the general class and can be divided into distinct categories. For instance, A parent class has a name, price, and quantity; A child class, like a perishable item, can have these traits but an addition to an expiry date.


### 4. Polymorphism
This concept simply means an object is treated as having numerous configurations, hence the name "Polymorphism" ("Many forms"). It enables a single interface to control access to different underlying data types. For example, all characters can attack in a game, but how they attack is different. All characters have health, but how much is different.

Polymorphism allows product types to perform their own version of a shared action. Items are sold differently, such as by bundles, discounts due to near expiration, or mostly by the piece. Let's say the price of a bag of chips and bananas are calculated through the same process, but the price of the bag of chips is fixed and by piece (exempt from inflation), while the bananas are measured in grams to find the price. (Many bananas have different weights and can't be sold by piece equally)

## Reflection
Object-Oriented Programming is a significant concept in programming because it is a way of writing computer code by grouping data and actions together as objects rather than writing lengthy, systematic code.

For the sari-sari store problem, the appropriate OOP rule to use is all 4 main rules---Encapsulation, Abstraction, Inheritance, and Polymorphism
