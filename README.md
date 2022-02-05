  
# PokemonBreedingSimulator 
## Table of Contents  
1. [What is this?](#what-is-this)  
2. [Usage](#usage)  
3. [What are the common terms/concepts of this project?](#what-are-the-common-terms-and-concepts-of-this-project)
4. [What are the goals?](#what-are-the-goals)
5. [What does each file do?](#what-does-each-file-do)
6. [Conclusions](#conclusions)  

    6a. [Chance to roll n 31s without inheritance](#chance-to-roll-n-31s-without-inheritance)  
    6b. [Chance to inherit specific stat](#chance-to-inherit-specific-stat)  
    6c. [Unique IVs vs Overall IVs](#unique-ivs-vs-overall-ivs)  
    6d. [When a Destiny Knot is optimal](#when-a-destiny-knot-is-optimal)  
    6e. [When progenitor replacements are optimal](#when-progenitor-replacements-are-optimal)  
    6f. [Power items vs Everstone](#power-items-vs-everstone)  
    6g. [Offspring gender ratio [Graphs]](#offspring-gender-ratio)  
    6h. [Egg group propagation: the how and why](#egg-group-propagation-the-how-and-why)
7. [Misc comments](#misc-comments)
8. [Disclaimer](#disclaimer)
## What is this? 
* Various simulations for Pokemon **IV breeding**. **IVs** are hereditary values which have a role in determining the **stat values** of a Pokemon (they're like points added onto the species' base stats). Each Pokemon has **six IVs**— one for Health, Attack, Defense, Special Attack, Special Defense, and Speed. IVs range from **0–31** in value.    
* The general **goal** of IV breeding is to get an **offspring with max-value IVs for all six stats**. This could be for **competitive, collector, completionist**, or etc purposes!    
* Progress is made by **selectively breeding** to keep desirable values and remove undesirable values.    
* Testing is all for the **BDSP (Brilliant Diamond & Shining Pearl)** games. Most concepts should apply to all the modern games (only difference I can think of is the egg group propagation).
## Usage  
If you want to run the simulations yourself— 

Files are meant to be edited and ran in an IDE. Settings are on the top of each script (which has settings). Results are printed to console. 

Example of a settings panel and snippet of output (regular settings for **breed_to_iv.py**, then output from that simulation in interactive mode):
![breed_to_iv.py settings panel](https://i.imgur.com/eO49TyT.png)
*To clarify, this settings configuration does not correspond to the following output*
![breed_to_iv.py snippet of ending output in interactive mode](https://i.imgur.com/Qy68IS3.png)
## What are the common terms and concepts of this project? 
* **IV = Individual Value**; hereditary additional base stat points. Contextually, "IV" can be short for referring to a max-value (31) IV. *For instance: "the offspring has more IVs" would imply the same as "the offspring has more 31s."*  
* **6IV**, **5IV**, etc.. **(\<n>IV)** = Number corresponds to how many 'perfect' (31) IVs a Pokemon has. 6IV means a perfect Pokemon (maximum possible stats).  
* **Overall IVs** = The total number of 31s in the pool between both parents. *3IV + 2IV? Five "overall IVs."*  
* **Unique IVs** = The total number of IVs at least one parent has a 31 for.   
* **IV Overlap** = When both parents have a 31 in a certain stat.  
* **IV Pool** = The "gene pool" of IVs from the parents.
* **IV List** = I have represented IVs as lists with six elements (corresponding to the stats). *For example: [31, 31, 31, 0, 0, 0] represents a 3IV (first three stats). Specific position IS significant.*  
* When breeding two Pokemon, the offspring will **normally inherit three random IVs** from the parents (even 50-50 chance for which parent on each inherited stat; all three stats could come from one parent, or any other mix). The other three IVs have **randomized values** within the possible range of 0-31 (they're like mutated genes).  
* **Roll** = Outcome of a randomized event. As a verb: to receive something from a randomized event. Probably comes from the idea of rolling dice?  
* **Held Item** = Pokemon can hold an item (no more than one). Certain held items will affect the breeding process.  
* **Destiny Knot** = A held item that causes the offspring to **inherit five IVs from the parents**, as opposed to the normal three. Breeding with **Destiny Knot = less mutation**. This could be good or bad depending on what is in the current "gene pool." Which parent holds this makes no difference, and having each parent hold one is no different than only having one.  
* **Power Item** = There is a power item (a held item) corresponding to each of the six stats. When a parent is holding a power item, their **IV corresponding to the stat** of the power item is **guaranteed to be inherited by the offspring**. If you combine this with the Destiny Knot (one parent holds the power item, the other holds a Destiny Knot), the guaranteed IV from the power item will take up one of the five inherited IVs from the Destiny Knot. *For example, say you had a male with a 31 Attack IV holding the attack power item, and a female holding a Destiny Knot. The offspring will have a 31 Attack IV, four other IVs inherited from the parents, and then one random IV.*  
* **Nature** = Pokemon have another potentially-hereditary value: Nature. There are 25 Natures. Each Nature corresponds to increasing one stat by 10% and decreasing another by 10%. The only exception is the HP stat, which is never affected by Nature. Natures which increase and reduce the same stat are called "Neutral Natures," since they don't do anything. Nature is only hereditary when a parent is holding a held item called an **Everstone**.  
* **Everstone** = Held item which guarantees that the parent holding it will pass down their Nature to the offspring. If both parents hold one, it's random between the two. 
* **Egg Group** = Pokemon can only breed with other Pokemon that are in the same egg group. They don't necessarily need to be the same species, but they need to have the same egg group. Egg groups are broad categories, such as "Dragon", "Flying", and "Field". Pokemon can be in 1-2 egg groups.
* **Egg Group Propagation** = Utilizing the fact that Pokemon can be in 2 egg groups, you can take a 6IV you have and use it to breed a 6IV for another egg group as long as there is a mutual connection. For example, if you have a Pokemon in the "Dragon" and "Flying" egg groups, and a Pokemon in the "Flying" and "Fairy" egg groups. Since they have a mutual egg group (Flying), they will be able to breed— and you'll now have a contact point for the Fairy egg group. This way, you don't have to start over from scratch when you want to breed Pokemon from a different egg group. This is where offspring gender ratio starts coming in— as the female parent determines the species of a Pokemon, meaning your 6IV needs to be a male in order to propagate IVs to other species.
## What are the goals? 
* To generalize— this project was for fun and to get a better general understanding of the statistics/strategy involved in competitive breeding.  
* In particular, there were three primary areas I wanted to investigate (though it extended to several other areas in the process). **Optimal Destiny Knot usage**, **most efficient selection strategy**, and **egg group propagation**  
* **Optimal Destiny Knot usage** to understand when inheriting more IVs from parents is beneficial and when it's actually disadvantageous. Under what circumstances should I use a Destiny Knot?  
* **Most efficient selection strategy** to understand how to prioritize which progenitors to use. Of course, we want to accomplish the goal as efficiently as possible— and aside from knowing what tools you need to use, the biggest thing which impacts this is how you choose when to replace progenitors (thus affecting the active IV pool).
* **Egg group propagation** to propagate the IVs of the first male 6IV offspring to all other egg groups (aside from genderless/undiscovered) to never need to start from scratch again (and also spend the least possible breeding effort in propagating the IVs— this was definitely the trickiest part of the project).
## What does each file do? 
Each **file** is its own **separate simulation**. Trials are run a number of times and then averaged. Some simulations support graphing. Simulations have a variety of their own settings from things like number of trials, what selection method to use, offspring gender ratio, destiny knot usage, target number of 31s, seed, etc.   

In some circumstances, a mathematical formula is used to calculate the real chance. When this is the case, there will be a distinction.

* **breed_to_iv.py** — Simulates the average amount of tries to optimally breed to a certain number of desired IVs under the given conditions (optimal concerning progenitor replacements and destiny knot usage). This is the main simulation of the project, and is complete with a broad variety of settings!
* **all_destiny_knot_scenarios.py** — Goes through every possible starting condition of breeding and tests for the average amount of tries to make progress from that position, both with and without using a Destiny Knot. (See when using a Destiny Knot is more efficient.)
* **all_destiny_knot_scenarios_visualizer.py** — Visualizes all of the possible starting conditions mentioned above.
* **unique_vs_overall_ivs.py** — Compares the efficiency of prioritizing the number of unique 31s in the pool versus overall 31s in the pool.
* **breed_to_progress.py** — Compares averages tries to make any optimal progress towards a 6IV from given starting conditions with and without a Destiny Knot.
* **roll_new_31.py** — Finds chance to roll at least one 31 given a certain amount of rolled stats.
* **random_31s.py** — Calculate chance to randomly roll n 31s.
*  **fixed_iv_roll.py** — Given three guaranteed 31s, what's the chance they're the exact three stats you wanted?
* **inherit_specific_stats.py** — What is the chance an offspring will inherit n number of specific stats from the pool?
* **optimal_male_ratio.py** — Breed to a certain number of IVs with different male ratios, and test for the optimal to reach the given goals. ie get a Male 6IV with 50% male chance, then 51%, 52%, etc for range given. Bit on the slower side, since it's running so many each time.
## Conclusions
### Chance to roll n 31s without inheritance
|  n  | Chance                      |
|:---:|:----------------------------|
|  1  | 1/32 (3.125%)               |
|  2  | 1/1024 (0.098%)             |
|  3  | 1/32768 (0.003%)            |
|  4  | 1/1048576 (0.0001%)         |
|  5  | 1/33554432 (0.000003%)      |
|  6  | 1/1073741824 (0.000000093%) |


Rounded percentages; formula is `(1/32)^n`
### Chance to inherit specific stat
| # of specific stats | w/ Destiny Knot |  Regular  |
|:-------------------:|:---------------:|:---------:|
|          1          |    5/6 (83%)    | 1/2 (50%) |
|          2          |    4/6 (66%)    | 1/5 (20%) |
|          3          |    3/6 (50%)    | 1/20 (5%) |
|          4          |    2/6 (33%)    |    N/A    |
|          5          |    1/6 (16%)    |    N/A    |  


P.S. Some Pokemon are fixed to have at least three 31s (legendaries, revived fossils). The chance for their fixed IVs to be the three particular ones you want is the same as 3 specific stats with no knot (1/20).
### Unique IVs vs Overall IVs
It's no contest, unique IVs are worth much more than overall IVs. It makes an extremely big difference to focus on adding new unique 31s into the IV pool instead of the overall IV number. Example:
* **5IV** [31, 31, 31, 31, 31, 0] + **5IV** [31, 31, 31, 31, 31, 0] **(5 unique IVs):** ~190 average tries for 6IV
* **5IV** [31, 31, 31, 31, 31, 0] + **1IV** [0, 0, 0, 0, 0, 31] **(6 unique IVs):** ~108 average tries for 6IV
### When a Destiny Knot is optimal
\- It is not always optimal to use a Destiny Knot. You don't want a low mutation rate when the current IV pool is lacking crucial components.
\- It slightly depends on your breeding approach (between Unique IVs focus vs Overall IVs focus).
* If you are trying to optimally breed to 6IV with Unique IVs focus: DO NOT USE A DESTINY KNOT IF **neither parent is a 6IV and total_unique_31s == total_overall_31s / 2**. This represents the situation where the IV pool doesn't have all 6 unique IVs and all 31s are on overlaps *for example: [31, 31, 31, 0, 0, 0] and [31, 31, 31, 0, 0, 0]  is **missing unique IVs and all 31s are overlaps**.*  As portrayed in the section above, it is literally better to have a 1IV that gives you a new unique IV than a 5IV which only has overlaps with the other parent. Using a Destiny Knot is optimal in all other scenarios.
* If you're breeding with an Overall IVs focus, there are only two scenarios to not use a Destiny Knot in: 0IV + 0IV and 1IV + 1IV (1 overlap). 2IV + 2IV (2 overlaps) is close to even efficiency between knot or no knot, but it leans towards using the knot (again, to clarify, only with an Overall IVs focus, which is less efficient for reaching 6IV).

Scenarios where **no knot** wins (optimal Unique-focus breeding):
![From all_destiny_knot_scenarios.py](https://i.imgur.com/fyWsbKb.png)
![From all_destiny_knot_scenarios.py](https://i.imgur.com/TWX3RD1.png)
![From all_destiny_knot_scenarios.py](https://i.imgur.com/0JUeyg7.png)
![From all_destiny_knot_scenarios.py](https://i.imgur.com/tefDJkA.png)
![From all_destiny_knot_scenarios.py](https://i.imgur.com/48aWQLW.png)
![From all_destiny_knot_scenarios.py](https://i.imgur.com/tKRhWXz.png)
### When progenitor replacements are optimal
* When it increases the number of Unique 31s in the pool, or increases the number of Overall 31s without decreasing uniques.
* If you don't have any male 6IVs yet— instead of starting with two progenitors and branching exclusively from there, it's faster to do something like: get a Pokemon (that your target 6IV can breed with) for a 31 in each stat (like a Ditto for each IV slot), use power items to get a 2IV, use power items to get another 2IV with different stats slots, use a Destiny Knot to make a 4IV out of those 2IVs, use power items to get a 2IV of the last IVs you need, then use a Destiny Knot with the 4IV + 2IV (all 6 unique IVs in the pool at this point) and work towards 6IV directly.
### Power items vs Everstone
* Power items are always optimal for reaching 6IV except for when you either have two 0IVs, already have two 6IVs, or are breeding for a particular Nature. If you're specifically trying to breed (as opposed to nature candying in modern games) a Nature on, it will take the spot of power items and be decently slower.
* Say you had [31, 31, 31, 31, 31, 31] and [0, 31, 31, 31, 31, 31]. If you put a power item for the first IV slot on the first parent, this would be equal to breeding with two 6IVs. It's like a free IV!
* Power items do make a pretty big difference. With all optimal settings but no power items, it's around **315 breeds** on average to go from two 0IVs to a 6IV offspring (as one branch). With power items, that becomes around **232 breeds**.
* Starting from 6IV + 0IV goes from around **62 breeds** with no power items to **36 breeds** with power items.
### Offspring gender ratio
* Gender ratio mostly comes in concerning egg group propagation. This is because you need male 6IVs to propagate IVs to different species (the female parent determine the species, so you can't use their IVs across different species/egg groups).
* In terms of just 6IV breeding, no IV propagation considered, gender ratio should be as close to 50-50 as possible. See the below graph on the relationship between chance for a male offspring and average tries to get a 6IV offspring (specific simulation was starting from two 0IVs, optimal settings but no power items).
**Note: please mind the axis labels. These graphs do not start with y at 0.**
![For just 6IVs, 50% is best](https://i.imgur.com/nM0EQc3.png)
* If you're trying to breed a 6IV male (same simulation as above but offspring must be male; careful, first impression of this is very misleading, the scale being thrown off so hard by low male chance almost makes the rest of the graph look flat; see further graphs; **interval is 5-95% chance for male**):
![5-95% male ratio interval](https://i.imgur.com/UuA1uUH.png)  
Here is a closer-up (**interval of 40-90% male ratio**):
![40-90% male ratio interval](https://i.imgur.com/8wzMCOh.png)  
50% is definitely not the optimal point. The spiking is from smaller scale (would smoothen out with higher sample size too). Starting from scratch, around a 72% chance for a male offspring is the most efficient. Practically speaking, the most significant number concerning optimal gender ratios is for when you already have a 6IV male and want to propagate it to other egg groups.
Here is the graph for starting with a 6IV male and 0IV female (offspring must be a male 6IV; **45-90% male ratio interval**):
![45-90% male ratio interval, start with 6IV male](https://i.imgur.com/SqCNw6T.png)  
Our optimal number is around 77% chance for a male offspring. Here is the same graph with a larger y-axis interval for reference  
![45-90% male ratio interval, start with 6IV male](https://i.imgur.com/oKTLelN.png)  
In conclusion: when you're going for male 6IVs to propagate IVs, higher male ratios are noticeably more efficient than 50%. You really want to avoid anything below 50%. There is a sweet spot (around 70-85% male ratio), and efficiency quickly drops off when leaving that range in either direction. Starter Pokemon, which have 87.5% male ratios, are more efficient than normal 50-50 species.
The following graph illustrates the drop-off in the other direction, towards a 100% male ratio (where you don't get female progenitor replaces anymore)
![65-95% male ratio interval](https://i.imgur.com/TZUIWTy.png)
### Egg group propagation: the how and why

### Misc comments
* Getting to 5IV is very consistent, but 6IV gets more complicated, since the most IVs an offspring can inherit is five (using Destiny Knot). This means even with two 6IV parents, the best odds you can achieve are 1/32 for another 6IV offspring.  
* The hardest simulation to find answers for, by far, was the **all_destiny_knot_scenarios** files. I was stumped for a long time on what "every possible scenario" really was. It took a lot of trial and error until I finally caught onto the significance of Unique IVs / overlaps, and then figured out how to formulaically loop through each combination. "Two 3IV parents" is actually almost too vague to be meaningful. There could be anywhere from 0-3 overlaps, which corresponds to 3-6 unique 31s (between half of the desired IVs somewhere in the pool and all of them).  
## Disclaimer 
* Any errors? Please feel free to reach out!  
* I did not necessarily code the mechanics in a way that perfectly matches the real in-game process (I don't know how it's all specifically implemented— but the abstraction here is identical as far as I'm aware).