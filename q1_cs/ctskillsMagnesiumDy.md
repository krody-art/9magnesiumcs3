# Computational Thinking Exercise
## Smart School Canteen Queue
## Name: Karl Rafael O. Dy
## Section: 9 - Magnesium
## Date: 8/21/26


---

# Step 1: Identify the Big Problem

### Main Problem
# The canteen is small and gets packed with students during rush hour. Most students never even get a chance to eat their lunch, and worse, they waste money because they have a fixed meal plan that they pay for every week.


---

## Step 2: Identify the Sub-Problems
1. The cashier has to manually calculate the total amount and give change.
2. There is no system for tracking which resources are running out.
3. It takes a long time for students to receive their orders.


---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| The cashier has to manually calculate the total amount and give change | Algorithmic Design | Design a program that adds the total prices, tax, and calculates the exact change.  |
| There is no system for tracking which resources are running out. | Algorithmic Design and Data Representation. | Create an inventory database that updates resource quantities and alerts staff when they fall below a threshold. |
| It takes a long time for students to receive their orders. | Decomposition | Break down the ordering process into distinct micro-steps (Order placement, payment, food preparation, and pickup) to locate the exact problem and assign staff to each step. |

---
## Step 4: Algorithmic Solution
### Selected Sub-Problem

Sub-Problem #1: The cashier has to manually calculate the total amount and give change | Algorithmic Design | Design a program that sums the total prices and tax, then calculates the exact change.

### Pseudocode
START

Obtain the tender amount

Obtain the quantity of items

Obtain the prices of items

  For every item in the list:
  Keep adding until there is no item to add.

Add tax

Subtract the total amount from the tender amount

END

E---
