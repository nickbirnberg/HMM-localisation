# HMM-localisation
AI Project

## Usage
```
python hmm_localisation/main.py --width 10 --height 10
```
###Sample Output:
1. `Robot is in: (7, 8)`
2. `Sensor senses: (8, 7)`
3. `Robot thinks it's in: (8, 7) with probability:  0.0321369375269`
4. `Manhattan distance: 2`
5. `Robot has been correct: 0.0 of the time.`

####Explained:
1. The space on the grid, coordinate between (0 -> width-1, 0 -> height - 1), the robot is in
2. The coordinate the robot’s faulty sensor reports.
3. The robot’s guess and the computed probability of the robot’s guess being correct.
4. The manhattan distance between the robot’s guess and actual location.
6. The percent of states guessed correctly up to this step.

## [Assignment](http://cs.lth.se/eda132-applied-artificial-intelligence/programming-assignments/probabilistic-reasoning/)
You are supposed to implement an HMM to do filtering for localisation in an environment with no landmarks. Consider the previously mentioned vacuum cleaner robot in an empty room, represented by an n x m rectangular grid. The robot’s location is hidden; the only evidence available to you (the observer) is a noisy sensor that gives a direct, but vague, approximation to the robot’s location. The sensor gives approximations S = (x',y') for the (true) location L = (x, y), the surrounding 8 fields L_s  = {(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)} and the “second surrounding ring” with 16 fields L_s2 = {(x-2, y-2), (x-2, y-1), (x-2, y), (x-2, y+1), (x-2, y+2), (x-1, y-2), (x-1, y+2), (x, y-2), (x, y+2), (x+1, y-2), (x+1, y+2), (x+2, y-2), (x+2, y-1), (x+2, y), (x+2, y+1), (x+2, y+2)} according to the following:

The sensor reports
 - the true location L with probability 0.1
 - any of the 8 surrounding fields L_s with probability 0.05 each
 - any of the next 16 surrounding fields L_s2 with probability 0.025 each
 - "nothing" with probability 0.1
 
Obviously, the overall probability for the sensor of being "one step off" is 8*0.05 = 0.4, the probability of being "two steps off" is essentially the same, i.e., 16*0.025 = 0.4. You need to decide for yourself how you handle a (simulated) noisy sensor reading "outside" the field - it can be reported as "nothing", which means locations along the walls and one step further into the field can in fact have slightly higher probabilities of creating the sensor reading "nothing", depending on how you translate this into your models. 
 
The robot moves according to the following strategy:
 
Pick random start heading h_0. For any new step pick new heading h_t+1 based on the current heading h_t according to:
 
P( h_t+1 = h_t | not encountering a wall) = 0.7
P( h_t+1 != h_t | not encountering a wall) = 0.3
P( h_t+1 = h_t | encountering a wall) = 0.0
P( h_t+1 != h_t | encountering a wall) = 1.0
 
In case a new heading is to be found, the new one is again randomly chosen.
 
Implement this as an HMM and do filtering to track the robot. This requires obviously a two-part implementation, as you need to simulate the robot and its movement (from which you also can simulate the sensor readings) to have some ground truth to evaluate your tracking against, and the HMM-based tracking algorithm as such.
