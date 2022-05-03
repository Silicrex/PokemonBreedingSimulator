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
   6h. [Egg group propagation: the how and why [Graphs]](#egg-group-propagation-the-how-and-why)  
   6i. [How big is the difference using optimal strategies, really?](#how-big-is-the-difference-using-optimal-strategies-really)  
7. [Final Thoughts](#final-thoughts)  
8. [Misc comments](#misc-comments)  
9. [Disclaimer](#disclaimer)  

## What is this?

* Various simulations for Pokemon **IV breeding**. **IVs** are hereditary values which have a role in determining the **stat values** of a Pokemon (they're like points added onto the species' base stats). Each Pokemon has **six IVs**— one for Health, Attack, Defense, Special Attack, Special Defense, and Speed. IVs range from **0–31** in value.
* The general **goal** of IV breeding is to get an **offspring with max-value IVs for all six stats**. This could be for **competitive, collector, completionist**, or etc purposes!
* Progress is made by **selectively breeding** to keep desirable values and remove undesirable values.
* Testing is all for the **BDSP (Brilliant Diamond & Shining Pearl)** games. Most concepts should apply to all the modern games (only difference I can think of is the egg group propagation, as there are different species available between different games, and some species have their egg groups changed ie Ralts).

## Usage

If you want to run the simulations yourself—

Files are meant to be edited and ran in an IDE. Settings are on the top of each script (for those which have settings). Results are printed to console.

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
* **Power Item** = There is a power item (a held item) corresponding to each of the six stats. When a parent is holding a power item, their **IV corresponding to the stat** of the power item is **guaranteed to be inherited by the offspring**. Trying to use a Power Item on both parents does NOT apply both effects, it will just randomly choose one to use, and the other will do nothing. If you combine this with the Destiny Knot (one parent holds the power item, the other holds a Destiny Knot), the guaranteed IV from the power item will take up one of the five inherited IVs from the Destiny Knot. *For example, say you had a male with a 31 Attack IV holding the attack power item, and a female holding a Destiny Knot. The offspring will have a 31 Attack IV, four other IVs inherited from the parents, and then one random IV.*
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
* **specific_position_31s.py** — Finds average tries to breed to an nIV Pokemon where the 31s are in a certain number of specific slots.
* **roll_new_31.py** — Finds chance to roll at least one 31 given a certain amount of rolled stats.
* **random_31s.py** — Calculate chance to randomly roll n 31s.
* **fixed_iv_roll.py** — Given three guaranteed 31s, what's the chance they're the exact three stats you wanted?
* **inherit_specific_stats.py** — What is the chance an offspring will inherit n number of specific stats from the pool?
* **optimal_male_ratio.py** — Breed to a certain number of IVs with different male ratios, and test for the optimal to reach the given goals. ie get a Male 6IV with 50% male chance, then 51%, 52%, etc for range given. Bit on the slower side, since it's running so many each time. Line of best fit generated currently always uses a 2nd-degree polynomial (depending on interval and situation, not always the best).

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

It's no contest, unique IVs are worth much more than overall IVs. It makes an extremely big difference to focus on adding new unique 31s into the IV pool instead of the overall IV number. Example (optimal Destiny Knot, 50-50 male ratio, no Power Items, first uses overall-focus, second uses unique-focus):

* **5IV** [31, 31, 31, 31, 31, 0] + **5IV** [31, 31, 31, 31, 31, 0] **(5 unique IVs):** ~190 average tries for 6IV
* **5IV** [31, 31, 31, 31, 31, 0] + **1IV** [0, 0, 0, 0, 0, 31] **(6 unique IVs):** ~108 average tries for 6IV

See below section on [How big is the difference using optimal strategies, really?](#how-big-is-the-difference-using-optimal-strategies-really) for a more in-depth comparison!

### When a Destiny Knot is optimal

* It is not always optimal to use a Destiny Knot. You don't want a low mutation rate when the current IV pool is lacking crucial components.  
* It slightly depends on your breeding approach (between Unique IVs focus vs Overall IVs focus).
> **Unique IVs Focus**

* If you are trying to optimally breed to 6IV with **Unique IVs focus**: DO NOT USE A DESTINY KNOT IF **neither parent is a 6IV and total_unique_31s == total_overall_31s / 2**. This represents the situation where the IV pool doesn't have all 6 unique IVs and all 31s are on overlaps *for example: [31, 31, 31, 0, 0, 0] and [31, 31, 31, 0, 0, 0]  is **missing unique IVs and all 31s are overlaps**.*  As portrayed in the section above, it is better to have a 1IV that gives you a new unique IV than a 5IV which only has overlaps with the other parent. Using a Destiny Knot is optimal in all other scenarios.

Scenarios where **no knot** wins (optimal Unique-focus breeding):
![From all_destiny_knot_scenarios.py](https://i.imgur.com/fyWsbKb.png)  
![From all_destiny_knot_scenarios.py](https://i.imgur.com/TWX3RD1.png)  
![From all_destiny_knot_scenarios.py](https://i.imgur.com/0JUeyg7.png)  
![From all_destiny_knot_scenarios.py](https://i.imgur.com/tefDJkA.png)  
![From all_destiny_knot_scenarios.py](https://i.imgur.com/48aWQLW.png)  
![From all_destiny_knot_scenarios.py](https://i.imgur.com/tKRhWXz.png)  

> **Overall IVs Focus**

* If you're breeding with an **Overall IVs focus**, there are only two scenarios to not use a Destiny Knot in: **0IV + 0IV** and **1IV + 1IV (1 overlap)**. 2IV + 2IV (2 overlaps) is close to even efficiency between knot or no knot, but it leans towards using the knot.

See below section on [How big is the difference using optimal strategies, really?](#how-big-is-the-difference-using-optimal-strategies-really) for a different comparison!


### When progenitor replacements are optimal

* When it increases the number of Unique 31s in the pool, or increases the number of Overall 31s without decreasing uniques.
* If you don't have any male 6IVs yet— instead of starting with two progenitors and branching exclusively from there, it's faster to do something like... 
  1. Get a Pokemon (that your target 6IV can breed with) for a 31 in each stat (like a Ditto for each IV slot)
  2. Use a Power Item to get three 1IVs (any stat, as long as they're different) with the desired species (skip if you already used the desired species for the step above)
  3. Use a Power Item + Destiny Knot to get two 2IVs (different genders), covering four unique IVs (one parent from the desired species, one parent from the other one for each)
  4. Continuing optimal breeding, use the two 2IVs to get a 4IV of those unique IVs.
  5. For the last two unique IVs you need, use the last of the desired species & other species from before to get a 2IV of the opposite gender as your 4IV.
  6. Use the 4IV and 2IV covering all six unique IVs to breed to 6IV with optimal replacements.

See below section on [How big is the difference using optimal strategies, really?](#how-big-is-the-difference-using-optimal-strategies-really) for a more in-depth comparison!


### Power items vs Everstone

* Power items are **always optimal for reaching 6IV** except for when you either have **two 0IVs**, already have **two 6IVs**, or are breeding for a **particular Nature**. If you're specifically trying to breed a Nature on (as opposed to nature candying in modern games), it will take the spot of power items and be decently slower.
* Say you had **[31, 31, 31, 31, 31, 31]** and **[0, 31, 31, 31, 31, 31]**. If you put a power item for the first IV slot on the first parent, this would be equal to breeding with two 6IVs. It's like a free IV!
* Power items do make a pretty big difference. With all optimal settings but no power items, it's around **315 breeds** on average to go from two 0IVs to a 6IV offspring (as one branch). With power items, that becomes around **232 breeds**.
* Starting from 6IV + 0IV goes from around **62 breeds** with no power items to **36 breeds** with power items.

### Offspring gender ratio
> **When does it matter?**

* Gender ratio mostly comes in concerning egg group propagation. This is because you need male 6IVs to propagate IVs to different species (the female parent determines the species, so you can't use their IVs across different species/egg groups).
* The progenitors you're starting with has a significant impact on what would be the most efficient gender ratio (for instance, if you have a 6IV Male + 0IV Female and are breeding for a 6IV of any gender, you'd want as low of a male ratio as possible, since the male progenitor is already the best possible and wouldn't need any progress, whereas how quickly you can improve the female progenitor would have a significant overall impact).
> **Breeding for 6IV from 0IV + 0IV**
* In terms of just 6IV breeding from scratch, where offspring gender doesn't matter, gender ratio should be as close to **50-50** as possible. See the below graph on the relationship between chance for a male offspring and average tries to get a 6IV offspring (optimal settings, no power items, one branch; **interval of 5%-95% male chance**).  
**Note: please mind the axis labels. These graphs do not start with y at 0.**  
  ![For just 6IVs, 50% is best](https://i.imgur.com/w9pybc6.png)
* If you're trying to breed a 6IV male (same simulation as above; **interval of 5%-95% male chance**):  
  ![5-95% male ratio interval](https://i.imgur.com/KcCQZwI.png)
* Here is a closer-up (**interval of 40%-90% male chance**):  
  ![40-90% male ratio interval](https://i.imgur.com/zLa3Sfw.png)
* 50% is definitely not the optimal point in this case! Starting from scratch, around a 65-72% chance for a male offspring is the most efficient.
> **Breeding for 6IV from 6IV + 0IV**

* Practically speaking, the most significant number concerning optimal gender ratios is for when you already have a 6IV male and want to propagate its IVs to other egg groups. Here is the graph for starting with a 6IV male and 0IV female (offspring must be a male 6IV; **45-90% male ratio interval**):  
  ![45-90% male ratio interval, start with 6IV male](https://i.imgur.com/nvbXLK1.png)
* Our optimal number is around 77% chance for a male offspring. Here is the same graph with a larger y-axis interval for reference  
  ![45-90% male ratio interval, start with 6IV male](https://i.imgur.com/3YTsKdf.png)
* In conclusion: when you're going for male 6IVs to propagate IVs, higher male ratios are noticeably more efficient than 50%. You really want to avoid anything below 50%. There is a sweet spot (around 70-85% male ratio), and efficiency quickly drops off when leaving that range in either direction. Starter Pokemon, which have 87.5% male ratios, are more efficient than normal 50-50 species. The following graph illustrates the drop-off towards a 100% male ratio (where you don't get female progenitor replacements anymore)  
  ![65-95% male ratio interval](https://i.imgur.com/RLs3aGg.png)

See below section on [How big is the difference using optimal strategies, really?](#how-big-is-the-difference-using-optimal-strategies-really) for continued comparison!

### Egg group propagation: the how and why

> **Do we have to start over from scratch each time we want to breed a new 6IV?**

No! Barring genderless/"undiscovered" Pokemon, which can't regularly breed (will not be repeating this clarification, but it applies whenever egg groups are mentioned), once you have a 6IV male, you can propagate (spread via breeding) those IVs to all other Pokemon species!

> **Egg group interconnectedness**

A lot of Pokemon belong to **two** egg groups. This is the key point of propagating IVs not just to other species in the same egg group, but all other egg groups as well. Below is a graph (generated using https://graphonline.ru/en/) illustrating all the connections using two-egg-group Pokemon in BDSP (it does vary between games based on what species are available).  
![Number = connection points](https://i.imgur.com/PzHGAC0.png)  
*Number corresponds to number of connections that egg group has*

For example, say you had three species: one in **Flying and Dragon**, one in **Dragon and Monster**, and one in **Monster and Field**. Each of these two-egg-group species contributes a link between each of their egg groups. Using mutual links, you can travel from one egg group to another even if there are no direct connections. In this case, you could use the **Dragon + Monster** as the intermediary between the **Flying** and **Field** egg groups. That would be a chain of **Flying -> Dragon -> Field**.

> **So, what's the strategy?**

The idea is to have a 6IV male for each egg group. That way, if you ever need to breed a 6IV, you can use the 6IV male you have in the corresponding egg group to easily work towards the 6IV you want. When you're at that point, breeding optimally (Destiny Knot, Power Items, selection strategy), it only takes about **4 breeds** to get to **5IV** (assuming normal gender ratio of 50-50). Including those 4 tries, it's around **36** breeds for a **6IV**!

> **The optimal way of propagating IVs to other egg groups (BDSP)**

This section is for if you want to reach all of the egg groups as efficiently as possible. I will go into detail about the starting point and how to progress from there, as well as what factors come into play.

The **factors**:

- **Amount of new egg group coverage per new species you obtain a 6IV male for**. The route should start with a duo-egg-group Pokemon (+2 coverage), and each new species you propagate to should add a new egg group coverage (+1). This means the route needs to be considerate of not requiring intermediary breeds of duo-egg-group species whose egg groups you already have coverage for.
- **Gender ratio**. Since we're specifically breeding for 6IV males so we can propagate the IVs to other species, this can make a notable difference.
- **Egg cycles**. Egg cycles determine how quickly eggs catch. The lower the number, the better.
- **Immediate-breedability of offspring**. Some species have offspring which need to be evolved before being breedable (for example, Lucario and Pikachu).

The **route (BDSP)**: Again, there are several routes you could take which are equally optimal. This is an example of a route which minimizes the cost of the above factors as much as possible. Credit to the https://pokemondb.net/egg-group/amorphous pages which I used for compiling the data.

```
MAGIKARP (UNLOCK DRAGON/WATER2)
MAGIKARP -> SWABLU (UNLOCK FLYING)
MAGIKARP -> CHARMANDER (UNLOCK MONSTER)
SWABLU -> TOGEPI (UNLOCK FAIRY)
TOGEPI -> MARILL (UNLOCK WATER 1)
TOGEPI -> PACHIRISU (UNLOCK FIELD)
TOGEPI -> SNORUNT (UNLOCK MINERAL)
MARILL -> SURSKIT (UNLOCK BUG)
MARILL -> LOTAD (UNLOCK GRASS)
MARILL -> CORPHISH (UNLOCK WATER3)
PACHIRISU -> SPINDA (UNLOCK HUMAN-LIKE)
SPINDA -> RALTS (UNLOCK AMORPHOUS)
```

![Example of an optimal route](https://i.imgur.com/Nz2AiYc.png)  
(connections connect species which share an egg group)

- You start with +2 egg group coverage. Each new species gives you +1 (there are no unnecessary intermediaries to fill in connections).
- Each egg group's Pokemon has the lowest hatch time for its egg group (aside from when it's 2nd-fastest and the 1st-fastest was used for a different egg group connection already; ie Togepi is the fastest hatch for both Fairy and Flying, but Togepi is used for Fairy, and Swablu (who is 2nd-fastest for Flying) is used for Flying).
- Gender ratio was converted into terms of overall hatch time to be compared. See chart below for more on that.
- For your starting point, you want to start off with whatever is the easiest, as the first 6IV is the most difficult. The amount of breeds you need to do and required egg cycles for hatching that species multiply together for overall cost, so you want to minimize what is being multiplied here.
- Five things to note:
  1. Of course, this comes down to RNG. You could get lucky or unlucky. What using an optimal route means is *on
     average* it's the fastest, so it's the best you can do. Same goes for all figures mentioned on this page. There
     can very much be high variance on an individual level.
  2. Pokemon with a high male ratio (Togepi and Charmander are 87.5% male) are harder to start off, but are faster in
     the long-term (on average avoids the pain of rolling female 6IVs half the time).
  3. Togepi needs to be evolved to breed, and it's a friendship evo (will evolve the next time it levels up if the
     Friendship stat is at least a certain value). Prepare any friendship berries (the ones which lower EVs but raise
     friendship; Pomeg Berry, Kelpsy Berry, Qualot Berry, Hondew Berry, Grepa Berry, and/or Tamato Berry). It only
     takes a Soothe Bell (held item to have the Togepi hold which multiplies friendship gained) and 8 (~~pending
     confirmation~~ confirmed for hatched -> Soothe Bell -> 8 friendship berries -> any level up) of these berries to have enough to evolve (then you can just win a battle and the XP share will be
     enough to cause Togepi to level up and evolve). You only need to do this when making a replacement, so at worst 6
     times (initial, 1IV, 2IV... 5IV). This does trade breeding expense for other expenses. Up to you which area you'd
     rather invest more time into (Though, the berries can be done 100% passively. You just need to plant them, water them one time, and them come back 36 hours later to 2-5x your supply. Game doesn't need to be on.).
  4. If you already have a certain 6IV you want which would replace a duo-egg-group slot's species but has higher
     hatch time, you may as well use that instead!
  5. For your starting point, it's easier to either mass-catch that Pokemon or Dittos (using PokeRadar) until you
     have a 31 in each stat slot (between different individual Pokemon). Since catching is so much faster than
     breeding, and you're only rolling for one 31 each, this is an easy way to kick it off. See above section on [When progenitor replacements are optimal](#when-progenitor-replacements-are-optimal) for more detail on this.

> **Make your own route (BDSP)**

Below is a table (for BDSP) of all the duo-egg-group Pokemon, sorted by efficiency.

- Header is the egg group you're unlocking.
- Format is like [Egg cycles (lower = better); other details] Pokemon_species (Egg group you need to reach this)
- Slash means the Pokemon separated make no difference
- *For ex:* `[(17.6) 20, 87.5% Male] Treecko/Charmander (Monster)` under the Dragon group. Factoring male ratio, the egg
  cycle value is 17.6 (20 regularly). Both species have an 87.5% male rate. Using Treecko vs Charmander makes no
  difference. Monster is the egg group you need to have already to link here. Dragon is the egg group you unlock.
- Gender ratio is handled like this: what is the percentage of tries more/less this gender ratio causes you to need?
  Apply that as a multiplier to the egg cycle value.  

| Male Ratio | Avg Breeds For 6IV Male | Multiplier  |
|:----------:|:-----------------------:|:-----------:|
|    25%     |          154.8          | 1.66990291  |
|    50%     |          92.7           |      1      |
|   87.5%    |          81.5           | 0.879180151 |

```
>>> Amorphous: 
    [20] Shellos (Water1), Ralts (Human-Like)
    [25] Castform (Fairy)
>>> Bug:
    [15] Surskit (Water1), Volbeat&Illumise (Human-Like)
    [20] Skorupi (Water3), Paras (Grass), Trapinch (Dragon)
>>> Dragon:
    [5] Magikarp (Water2)
    [(17.6) 20, 87.5% Male] Treecko/Charmander (Monster)
    [20] Feebas/Horsea (Water1), Swablu (Flying), Seviper/Ekans (Field), Trapinch (Bug)
    [40] Dratini (Water1), Gible (Monster)
>>> Fairy:
    [(8.8) 10, 87.5% Male, Friendship Evolution] Togetic (Flying)
    [10] Marill (Water1), Pachirisu (Field)
    [10, Friendship Evolution] Pikachu (Field)
    [15] Shroomish (Grass)
    [20] Snorunt (Mineral), Cherubi/Roselia/Hoppip (Grass), Mawile (Field)
    [25] Castform (Amorphous)
    [(25.04) 15, 25% Male] Skitty (Field)
    [(33.4) 20, 25% Male] Snubbull (Field)
>>> Field:
    [10] Pachirisu (Fairy)
    [10, Friendship Evolution] Pikachu (Fairy)
    [15] Bidoof (Water1), Spinda (Human-Like), Seedot (Grass)
    [(17.6) 20, 87.5% Male] Piplup (Water1), Chimchar (Human-Like)
    [20] Buizel/Spheal/Delibird/Wooper/Seel/Psyduck (Water1),
         Whismur/Mareep/Rhyhorn/Nidoran (Monster),
         Buneary (Human-Like), Farfetch'd (Flying), Mawile (Fairy), Seviper/Ekans (Dragon)
    [(21.98) 25, 87.5% Male, Daytime Friendship Evolution] Lucario (Human-Like)
    [(25.04) 15, 25% Male] Skitty (Fairy)
    [(33.4)  20, 25% Male] Snubbull (Fairy)
    [40] Wailmer (Water2)
>>> Flying:
    [(8.8) 10, 87.5% Male, Friendship Evolution] Togetic (Fairy)
    [20] Wingull (Water1), Farfetch'd (Field), Swablu (Dragon)
>>> Grass:
    [15] Lotad (Water1), Seedot (Field), Shroomish (Fairy)
    [(17.6) 20, 87.5% Male] Turtwig/Chikorita/Bulbasaur (Monster)
    [20] Snover (Monster), Cacnea (Human-Like), Cherubi/Roselia/Hoppip (Fairy), Paras (Bug)
    [25] Tropius (Monster)
>>> Human-Like:
    [15] Spinda (Field), Volbeat&Illumise (Bug)
    [(17.6) 20, 87.5% Male] Chimchar (Field)
    [20] Cacnea (Grass), Buneary (Field), Ralts (Amorphous)
    [(21.98) 25, 87.5% Male, Daytime Friendship Evolution] Lucario (Field)
>>> Mineral:
    [20] Snorunt (Fairy)
>>> Monster:
    [(17.6) 20, 87.5% Male] Mudkip/Totodile/Squirtle (Water1),
         Turtwig/Chikorita/Bulbasaur (Grass), Treecko/Charmander (Dragon)
    [20] Slowbro (Water1), Snover (Grass), Whismur/Mareep/Rhyhorn/Nidoran (Field)
    [25] Tropius (Grass)
    [40] Lapras (Water1), Gible (Dragon)
>>> Water 1:
    [10] Marill (Fairy)
    [15] Corphish (Water3), Lotad (Grass), Bidoof (Field), Surskit (Bug)
    [(17.6) 20, 87.5% Male] Mudkip/Totodile/Squirtle (Monster), Piplup (Field)
    [20] Remoraid (Water2), Slowbro (Monster), Wingull (Flying), 
         Buizel/Spheal/Delibird/Wooper/Seel/Psyduck (Field), Feebas/Horsea (Dragon),
         Shellos (Amorphous)
    [(26.4) 30, 87.5% Male] Kabuto/Omanyte (Water3)
    [(33.4) 20, 25% Male] Corsola (Water3)
    [(35.2) 40] Relicanth (Water2)
    [40] Lapras (Monster), Dratini (Dragon)
>>> Water 2:
    [5] Magikarp (Dragon)
    [20] Remoraid (Water1)
    [(35.2) 40] Relicanth (Water2)
    [40] Wailmer (Field)
>>> Water 3:
    [15] Corphish (Water1)
    [20] Skorupi (Bug)
    [(26.4) 30, 87.5% Male] Kabuto/Omanyte (Water1)
    [(33.4) 20, 25% Male] Corsola (Water1)
```

> **What about starting from scratch for each duo-egg-group?**

What about, instead of using IV propagation and needing 12 Pokemon to cover all the egg groups (+1 coverage per aside
from +2 start), we start over from scratch with duo-egg-group Pokemon each time and only use 7 (+2 coverage per aside
from +1 last). Propagating is by far faster on an individual level, but is saving on 5 Pokemon enough for starting from
scratch to actually be more efficient? Since the last step would be +1, you could propagate to save some there (13 egg
groups, 2 * 6 duos = 12 covered, one left). Let's calc it!

**What we need:**

* Average tries to get the 6IV male from scratch
* Average tries to get the 6IV from propagating
* Way to factor difference in average egg cycles (hatch time) requirement per Pokemon going to best 7 efficiencies
  instead of best 12.
* Way to factor wasted breeds from having to switch out the progenitors a lot more (in the time you could be getting
  more eggs, you're having to wait on specific building blocks on a smaller level and having to manage several branches
  at once).

> **Let's start with average tries for a 6IV male from scratch**   

Assume you have all 6 IVs between Dittos or anything
compatible with the starting Pokemon (so we can use Power Items to introduce them into our pool). It will take **3**
breeds to get three 1IVs (so we can start getting 2IVs).

For 2IVs, the first one's gender doesn't matter. That's **2.46** breeds on average to go from two 1IVs (no overlap) to a
2IV compromising the two unique IVs. The second 2IV's gender will matter, as it will need to breed with the first.
That's an average of **3.7** breeds. We'll use those to get a 4IV, and then will need another gender-specific 2IV
afterwards, so add another 3.7. `3 + 2.46 + 3.7*2 = 12.86` so far.

Next is the 4IV. Gender doesn't matter (we already considered the gender-specificity with the third 2IV from the last
section). That's an average of **9.7 breeds**.

Lastly is the 6IV, using the 4IV + 2IV. Must be male (even if we don't propagate to get our initial egg group coverage,
propagating to other species is still the ultimate purpose). That's an average of **102.3**
breeds. `102.3 + 9.7 + 12.86 = 124.86`. **124.86 average breeds to optimally breed to 6IV from scratch (50-50 male
ratio).**

> **Next, 6IV male from propagating, and an initial estimate**  

This is an easy figure to get from the simulation files.
Around **68** breeds on average. What have we got so far just based on # of Pokemon? With propagation, that's 1 from
scratch and 11 propagations: `124.86 + 68*11 = 872.86`. For the other approach, it's 6 from scratch and 1
propagation: `124.86*6 + 68 = 817.16`.😅

> **Factoring average egg cycles**

So far, we've covered the first two points in determining which is more efficient. We've also seen that, at a
little-more-than-cursory glance, it seems the  'starting from scratch' approach is more efficient for the *initial egg
group outreach* (with all we've considered so far, although from-scratch won, you are only getting seven 6IVs from ~817
breeds instead of twelve 6IVs from ~873 breeds). Let's see how we can factor the other two components in.

How do we factor the difference in **average amount of egg cycles per Pokemon**? I thought from-scratch would win in
this regard, since you work with the best 7 instead of best 12, but this is not the case. The majority of
super-low-egg-cycle duo-egg-group Pokemon have Fairy as one of their egg groups, and since we need to +2 each step (
aside from the last), we need absolutely no repeats.

From the propagation section, we know **171.4** is the lowest amount of base egg cycles to complete the route. The best
I could come up with for from-scratch was **106.4**:

```
Magikarp [5] (Water2/Dragon)
Togepi [8.8 (10)] (Fairy/Flying)
Ralts [20] (Amorphous/Human-like)
Skorupi [20] (Bug/Water3)
Snorunt [20] (Mineral)
Seedot [15] (Field/Grass)
Squirtle [17.6 (20)] (Water1/Monster)
```

What we have now:

* ~**124.86 breeds** for a male 6IV from scratch.
* ~**68 breeds** for a male 6IV from propagation.
* **171.4 base egg cycles** total for propagation (scaled to factor gender ratio).
* **106.4 base egg cycles** total for from-scratch (scaled to factor gender ratio).

We're ready to tackle the third point. We can multiply average tries per male 6IV by total base egg cycles for that
breed type (from-scratch vs propagation breed) to see how many total egg cycles on average we'll need to complete a full
route.

First, the propagation-centric route: `124.86 * 5 + 68 * 166.4 = 11939.5`. About **11940** total egg cycles. The **5**
comes from Magikarp's base egg cycles (we start from scratch with Magikarp), then the **166.4** from base egg cycles for
the propagation breeds (171.4 - the 5 from Magikarp).
Next, the from-scratch-centric route: `124.86 * 86.4 + 68 * 20 = 12147.904`. About **12148** total egg cycles. **86.4**
is the sum of base egg cycles to be done from-scratch, then the **20** is Snorunt's (propagation).

At this point, it's safe to say the propagation approach is more efficient based on egg cycles. The fourth point is a bit harder to
factor in, but it only works in favor of the propagation-centric route anyways (something like 5 breeds wasted for each
of the initial 1IVs, and then another few each for the 2IVs?).

> **Conclusion**  

It's close, but because of the lack of diversity in low-egg-cycle duo-egg-type Pokemon available in
BDSP, you can't cut down the base egg cycles enough for the from-scratch approach to overcome the extra breeds per 6IV.
The propagation approach is seemingly more efficient.

_(Later edit)_

One note I need to make— rate of egg production has an effect on this, especially if you don't have the Oval Charm (an item that significantly increases the chance for an egg to be produced on each roll). Every certain number of steps (according to Bulbapedia (https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_breeding) it's 256, but this doesn't seem consistent with my Poketch step counter, so I'm unsure), the game does an RNG roll to see if an egg should be produced or not. According to Bulbapedia:
* If the Pokemon breeding are incompatible, the chance is **0%**
* If the Pokemon are different species and were caught by the same trainer, it's **20%** (**40% with Oval Charm**)
* If either the species is the same or original trainer is different, it's **50%** (**80% with Oval Charm**)
* If both the species is the same and the original trainer is different, it's **70%** (**88% with Oval Charm**)

Since you will always be using the same species with the from-scratch approach (aside from last one), you will be getting eggs significantly faster. Does this necessarily matter? No, because you can only carry a certain amount of eggs to hatch at a time (5 when you have a **Flame Body** / **Magma Armor** Pokemon in your party (it's an ability with a special out-of-battle effect that reduces hatch time by 50% and is very necessary), and most of the time you'll have more than that overall anyway. With this increased rate, you will probably end up with max excess for 15+ egg cycle Pokemon (if not for even lower egg cycle ones; and be careful with that in BDSP, since you can't release eggs, they must be hatched).

The **Oval Charm** is very effective at mitigating the difference. In my experience, it is enough that you will already have an excess amount of eggs the majority of the time (especially for the 15+ egg cycle Pokemon). Also consider that if you get a 6IV female first during the propagation approach, you can swap that in for the same-species benefit as well (worth keeping at least one 5IV male around for this reason, just in case).

Without the same-species bonus, it does take more active engagement as how efficiently you pick up the new eggs becomes important, since you can't generate a new egg without picking up the prior one from the breeder (you can still increase the step counter towards the next roll before picking it up, but it's a wasted roll if you don't pick it up before the roll happens).

Another way of totally negating this aspect is if you have a friend/second copy of BDSP and can get your 5IV Female for the breeding process from there (this also substantially increases the Shiny odds). You could trade the 6IV Male & 5IV Female you were using already once you get to that point (or really anywhere earlier in the process), breed on the other game until you get a new 5IV Female, and then trade them back. Being from a different trainer will give the same boost to the rate of egg production. If you have an Oval Charm, either this or the same-species boost is more than enough, there's no need to worry about both (aside from maybe Magikarp, _maaybeee_ the 10 egg cycle ones, but either way it's extremely diminishing returns the more bonuses you stack and probably not worth the hassle). 

Overall it's something to consider especially for later games where the pool of dual-egg-group Pokemon to use for your route is larger. My impression is that it's not enough to make a big enough difference for this game (especially since from-scratch has so many more switches necessary and that wasn't even factored in yet).

### How big is the difference using optimal strategies, really?

> **Destiny Knot vs No Destiny Knot**

* Ok, look, you need a Destiny Knot. Even if you have two 6IV parents already, your best odds without a Destiny Knot
  are **1/32768**.

> **Optimal Destiny Knot vs Always Destiny Knot**

Starting with a **0IV + 0IV**, no power items, 50/50 male ratio, one-branch (start with two progenitors and doing
replacements from there, not collecting the unique IVs first):

* Using Destiny Knot optimally, it's around **313 breeds** on average for a 6IV.
* Always using Destiny Knot, it's around **485 breeds** on average for a 6IV.

> **Unique-IVs Priority vs Overall-IVs Priority (Progenitor Replacements)**

**0IV + 0IV**, optimal Destiny Knot (based on replacement strategy), no power items, 50-50 male ratio, one-branch:

* Unique-IVs-priority = around **147 breeds** on average for a 5IV
* Overall-IVs-priority = around **249 breeds** on average for a 5IV

**3IV + 3IV** (0 overlaps), optimal Destiny Knot (based on replacement strategy), no power items, 50-50 male ratio,
one-branch:

* Unique-IVs-priority = around **133 breeds** on average for a 6IV
* Overall-IVs-priority = around **231 breeds** on average for a 6IV

**3IV + 3IV** (0 overlaps), optimal Destiny Knot (based on replacement strategy), no power items, 50-50 male ratio,
one-branch:

* Unique-IVs-priority = around **21 breeds** on average for a 5IV
* Overall-IVs-priority = around **43 breeds** on average for a 5IV

P.S. The more spread out unique IVs are the more difficult it is to make progress. Two 3IVs covering all unique IVs is the "worst" best-case scenario.


|  Parents  | Avg Breeds For Progress |
|:---------:|:-----------------------:|
| 6IV + 0IV |           2.1           |
| 5IV + 1IV |            5            |
| 4IV + 2IV |          12.2           |
| 3IV + 3IV |          19.7           |


|  Parents  | Avg Breeds For Progress w/ Power Items |
|:---------:|:--------------------------------------:|
| 6IV + 0IV |                   2                    |
| 5IV + 1IV |                  4.9                   |
| 4IV + 2IV |                  10.8                  |
| 3IV + 3IV |                  11.5                  |

> **Power Items vs No Power Items**

**0IV + 0IV** optimal Destiny Knot, 50-50 male ratio, one-branch:

* Around **113 breeds** on average for a 5IV with Power items
* Around **145 breeds** on average for a 5IV without Power items

**0IV + 0IV** optimal Destiny Knot, 50-50 male ratio, one-branch:

* Around **232 breeds** on average for a 6IV with Power Items
* Around **315 breeds** on average for a 6IV without Power Items

**3IV + 3IV** (0 overlaps) optimal Destiny Knot, 50-50 male ratio, one-branch:

* Around **72 breeds** on average for a 6IV with Power items
* Around **132 breeds** on average for a 6IV without Power items

> **50-50 Male Ratio vs Optimal Male Ratio**  
> 
_Note_: these are approximations based on simulations, not exact calculation, so expect some variance (even potentially for values that should have the exact yield; some are adjusted a little to reflect when values "should" be the same)

**0IV + 0IV** optimal Destiny Knot, no power items, one-branch (using male as reference, but it goes the same for either specific gender if you swap values):

**Gender-unspecific:**
* Around **510 breeds** on average for an any-gender 6IV with a 5% male ratio
* Around **383 breeds** on average for an any-gender 6IV with a 12.5% male ratio
* Around **338 breeds** on average for an any-gender 6IV with a 23% male ratio
* ☆ Around **313 breeds** on average for an any-gender 6IV with a 50% male ratio
* Around **338 breeds** on average for an any-gender 6IV with a 77% male ratio
* Around **383 breeds** on average for an any-gender 6IV with a 87.5% male ratio
* Around **510 breeds** on average for an any-gender 6IV with a 95% male ratio  

**Gender-specific:**
* Around **899 breeds** on average for a male 6IV with a 10% male ratio
* Around **501 breeds** on average for a male 6IV with a 25% male ratio
* Around **371 breeds** on average for a male 6IV with a 50% male ratio
* ☆ Around **349 breeds** on average for a male 6IV with a 72% male ratio
* Around **353 breeds** on average for a male 6IV with a 77% male ratio
* Around **392 breeds** on average for a male 6IV with an 87.5% male ratio
* Around **513 breeds** on average for a male 6IV with a 95% male ratio

**6IV Male + 0IV Female** optimal Destiny Knot, no power items, one-branch (using male as reference, but it goes the same for either specific gender if you swap values):  

**Gender-unspecific:**  
* ☆ Around **58 breeds** on average for an any-gender 6IV with a 0% male ratio
* Around **58 breeds** on average for an any-gender 6IV with a 5% male ratio
* Around **58.5 breeds** on average for an any-gender 6IV with a 12.5% male ratio
* Around **59 breeds** on average for an any-gender 6IV with a 23% male ratio
* Around **60.5 breeds** on average for an any-gender 6IV with a 50% male ratio
* Around **67 breeds** on average for an any-gender 6IV with a 77% male ratio
* Around **76 breeds** on average for an any-gender 6IV with an 87.5% male ratio
* Around **103 breeds** on average for an any-gender 6IV with a 95% male ratio  

**Gender-specific:**
* Around **343 breeds** on average for a male 6IV with a 10% male ratio
* Around **154 breeds** on average for a male 6IV with a 25% male ratio
* Around **93 breeds** on average for a male 6IV with a 50% male ratio
* ☆ Around **77 breeds** on average for a male 6IV with a 77% male ratio
* Around **81 breeds** on average for a male 6IV with a 87.5% male ratio
* Around **106 breeds** on average for a male 6IV with a 95% male ratio

> **Egg Group Propagation Strategies (BDSP)**  

Comparisons between amount of breeds and amount of egg cycles required were done directly (in proportion) with even weighting. My reasoning for this is that they're directly-connected values, and modifying either has roughly the same overall impact on cost/time. If you have a species with **5 egg cycles** and need to breed 10 offspring, you will need to go through 50 egg cycles overall. If you doubled the amount you needed, you have to go through 50 egg cycles. If you instead doubled the amount of egg cycles per hatch, you'd still land at 50 egg cycles— the cost of picking up an extra egg in the first scenario is comparatively negligible.

**Best duo-egg-group propagation vs worst single-egg-group species selections**  
_6IV Male; Egg cycles scaled for male ratio_
* **Best propagation route I found:** **11939.5** average egg cycles (optimized propagation; 171.4 base).
* **Worst single-egg-group route I found:** **43725.972** average egg cycles (one-at-a-time from-scratch; 350.2 base).

**For duo-egg-group propagation:**  
_Start with duo-egg-group for +2, then +1 each propagating to duos for the rest_
* The lowest total base egg cycles I've found is **171.4**.
* The worst I've found is **353.98**.

**For efficient from-scratch:**  
_Six duo-egg-group species from scratch, then one from propagation_
* The lowest total base egg cycles I've found is **106.4**.
* The worst I've found is **180**.

### Final Thoughts

For pretty much each step in the process, one efficient pick alone would make a significant, noticeable difference. Cumulatively, the difference is incredibly large. It should be noted, though, that there are definitely cases where specific constraints or goals impact what strategies would be most efficient (things like version-exclusive Pokemon being inaccessible, already wanting certain 6IVs which can also be used for IV propagation, wanting to invest different levels of effort into certain areas, etc).  

I've learned a lot in the making of this, and do feel I found answers to all the questions I had walking into the project! Yay!  

Thanks so much for checking this out! 

### Misc comments

* Getting to 5IV is very consistent, but 6IV gets more complicated, since the most IVs an offspring can inherit is
  five (using Destiny Knot). This means even with two 6IV parents, the best odds you can achieve are 1/32 for another
  6IV offspring.
* The hardest simulation to develop was **all_destiny_knot_scenarios**. There were a lot of times I was super stumped, but aside from trying to minimize the cost of egg group propagation routes, nothing took as long to figure out! I was stumped for a
  long time on what "every possible scenario" really was. It took a lot of trial and error until I finally caught onto
  the significance of Unique IVs / overlaps, and then figured out how to formulaically loop through each combination.
  "Two 3IV parents" is actually almost too vague to be meaningful. There could be anywhere from 0-3 overlaps, which
  corresponds to 3-6 unique 31s (between half of the desired IVs somewhere in the pool and all of them).

## Disclaimer

* Any errors? Please feel free to reach out!
* I did not necessarily code the mechanics in a way that perfectly matches the real in-game process (I don't know how
  it's all specifically implemented— but the abstraction here is identical as far as I'm aware).
* For the overall base egg cycles sections, the search was done semi-manually, so I am not 100% sure they are the best possible. Will work on how to solve it computationally when I get a better idea for how that would be done!
