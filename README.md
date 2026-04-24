[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WDzgaYz0)
# AI Statistics Lab: Pairs of Random Variables

This lab is based on the topics:
- joint CDF
- probability over rectangular regions
- joint PDF
- marginal PDFs
- joint PMF
- marginal PMFs
- independence for discrete random variables

---

## Learning Goals

By the end of this lab, students should be able to:

1. Compute probabilities from a joint CDF over rectangular regions
2. Work with a continuous joint PDF and derive marginals
3. Work with a discrete joint PMF and derive marginals
4. Check whether two discrete random variables are independent

---

## Question 1: Continuous Pair on the Unit Square

Suppose (X, Y) is uniformly distributed on the unit square:

0 < x < 1, 0 < y < 1

Then the joint PDF is

f_XY(x, y) = 1,   0 < x < 1 and 0 < y < 1
              0,   otherwise

and the joint CDF is piecewise; in the interior of the unit square,

F_XY(x, y) = xy,  0 < x < 1 and 0 < y < 1. 

### Tasks

Implement the following functions:

1. `joint_cdf_unit_square(x, y)`
   - Return F_XY(x, y)

2. `rectangle_probability(x1, x2, y1, y2)`
   - Compute P(x1 < X <= x2, y1 < Y <= y2)
   - Use the joint CDF rectangle formula:
     F(x2, y2) - F(x1, y2) - F(x2, y1) + F(x1, y1) 

3. `marginal_fx_unit_square(x)`
   - Return the marginal PDF f_X(x)

4. `marginal_fy_unit_square(y)`
   - Return the marginal PDF f_Y(y)

---

## Question 2: Joint PMF, Marginals, and Independence

Use the discrete pair from the slides:

Flip two fair coins and define:
- X = number of heads in the first toss
- Y = total number of heads in both tosses

Possible outcomes:
- TT -> (0, 0)
- TH -> (0, 1)
- HT -> (1, 1)
- HH -> (1, 2)

So the joint PMF is:

             y=0   y=1   y=2
x=0          1/4   1/4    0
x=1           0    1/4   1/4


### Tasks

Implement the following functions:

1. `joint_pmf_heads(x, y)`
   - Return P_XY(x, y)

2. `marginal_px_heads(x)`
   - Return P_X(x)

3. `marginal_py_heads(y)`
   - Return P_Y(y)

4. `check_independence_heads()`
   - Return `True` if X and Y are independent, else `False`

---

## Instructions

Edit only:

`AI_stats_lab.py`

Do not modify the test file.


## Run Locally

```bash
pip install numpy pytest
pytest
