# Task-Two-Constraint-Satisfaction-Program
Constraint Satisfaction Program
# Constraint Satisfaction Program - Map Colouring

This project solves two map colouring problems using constraint satisfaction:

1. **Australia (5 regions)** - Colour using exactly 3 colours (Blue, Red, Green)
2. **Nairobi Sub-counties (17 regions)** - Colour using the minimum possible number of colours

## Problem Description

### Part (a) - Australia
Colour five Australian regions (WA, NT, QLD, SA, NSW) such that no two adjacent regions share the same colour.  
**Available colours:** Blue, Red, Green

**Adjacency constraints:**
- WA borders NT and SA
- NT borders WA, SA, and QLD
- QLD borders NT, SA, and NSW
- SA borders WA, NT, QLD, and NSW
- NSW borders QLD and SA

### Part (b) - Nairobi Sub-counties
Colour Nairobi's 17 sub-counties using the least possible number of colours, with no two adjacent sub-counties sharing a colour.

**Sub-counties:**
1. Westlands
2. Dagoretti North
3. Dagoretti South
4. Lang'ata
5. Kibra
6. Roysambu
7. Kasarani
8. Ruaraka
9. Embakasi East
10. Embakasi West
11. Embakasi Central
12. Embakasi South
13. Embakasi North
14. Makadara
15. Kamukunji
16. Starehe
17. Mathare

## Requirements

Install the `python-constraint` library:

```bash
pip install python-constraint
