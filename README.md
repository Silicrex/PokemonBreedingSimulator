
# PokemonBreedingSimulator  
## What is this?  
* Various simulations for Pokemon **IV breeding**. **IVs** are hereditary values which have a role in determining the **stat values** of a Pokemon (they're like points added onto the species' base stats). Each Pokemon has **six IVs**— one for Health, Attack, Defense, Special Attack, Special Defense, and Speed. IVs range from **0–31** in value.  
* The general **goal** of IV breeding is to get an **offspring with max-value IVs for all six stats**. This could be for **competitive, collector, completionist**, or etc purposes!  
* Progress is made by **selectively breeding** to keep desirable values and remove undesirable values.  
* Getting to 5IV is very consistent, but 6IV gets more complicated, since the most IVs an offspring can inherit is five (using Destiny Knot). This means even with two 6IV parents, the best odds you can achieve are 1/32 for another 6IV offspring.  
* Testing is all for the **BDSP (Brilliant Diamond & Shining Pearl)** games.  
## What are the goals?  
* To generalize— this project was for fun and to get a better general understanding of the statistics/strategy involved in competitive breeding.
* There were three primary areas I wanted to investigate! **Egg group propagation**, **optimal destiny knot usage**, and **most efficient selection strategy**.
## What are the common terms/concepts of this project?  
* **IV = Individual Value**; additional base stat points. Can contextually be short for referring to a max-value (31) IV. *For instance: "the offspring has more IVs" would imply the same as "the offspring has more 31s."*
* **6IV**, **5IV**, etc **(\<n>IV)** = Number corresponds to how many 'perfect' (31) IVs a Pokemon has. 6IV means a perfect Pokemon (maximum possible stats).
* **Overall IVs** = The total number of 31s in the pool between both parents. *3IV + 2IV? Five "overall IVs."*
* **Unique IVs** = The total number of IVs at least one parent has a 31 for. 
* **IV Overlap** = When both parents have a 31 in a certain stat.
* When breeding two Pokemon, the offspring will **normally inherit three random IVs** from the parents (even 50-50 chance for which parent; could be all 3 from one, or 2 from one and 1 from the other, etc). The other three IVs have **randomized values** within the possible range of 0-31 (they're like mutated genes).
* **Roll** = Outcome of a randomized event. As a verb: to receive something from a randomized event. Probably comes from the idea of rolling the dice?
* **Held Item** = Pokemon can hold an item (no more than one). Certain held items will affect the breeding process.
* **Destiny Knot** = A held item that causes the offspring to **inherit five IVs from the parents**, as opposed to the normal three. Breeding with Destiny Knot = **less mutation**. This could be good or bad depending on what is in the active breeding pool. Which parent holds this makes no difference.
* **Power Item** = There is a power item (a held item) corresponding to each of the six stats. When a parent is holding a power item, their **IV corresponding to the stat** of the power item is **guaranteed to be inherited by the offspring**. If you combine this with the Destiny Knot (one parent holds the power item, the other holds a Destiny Knot), the guaranteed IV from the power item will take up one of the five inherited IVs from the Destiny Knot. *For example, say you had a male with a 31 Attack IV holding the attack power item, and a female holding a Destiny Knot. The offspring will have a 31 Attack IV, four other IVs inherited from the parents, and then one random IV.*
## What does each file do?  
Each **file** is its own **separate simulation**. Trials are run a number of times and then averaged. Some simulations support graphing. There are settings to control things like number of trials, offspring gender ratio, destiny knot usage, and target number of 31s.  
* **breed_to_iv.py** is for average attempts to optimally breed to a certain \<n>IV offspring (offspring with n 31 IVs)
* **breed_to_any_iv_progress.py** is for seeing how many tries it takes to get an offspring that has more max-value IVs than the parent of the corresponding gender. Will run tests for both with and without a Destiny Knot, then compare.
* **breed_to_any_optimal_progress.py** is for seeing how many tries it takes to get an offspring that has a better IV pool than the parent of the corresponding gender, using the 'optimized' selection process (prioritize unique 31s instead of overall 31s). Will run tests for both with and without a Destiny Knot, then compare.
* **find_optimal_destiny_knot_for_ivs.py** is essentially **breed_to_any_iv_progress.py** but tries for each possible scenario, and reports in which cases not using a Destiny Knot is actually more efficient.
* **find_optimal_destiny_knot_for_progress.py** is essentially **breed_to_any_optimal_progress.py** but tries for each possible scenario, and reports in which cases not using a Destiny Knot is actually more efficient.
## Conclusions (WIP)
* Unique 31s are more valuable than overall 31s.
* I started with the assumption breeding follows one linear path, and while this is the case when you've already gotten a 6IV to propagate the IVs from, it's not the case when building up to that point. When going for the first 6IV, it's more like several trees that connect (since it's best to get to a point where you have at least one 31 between both parents for each stat, and it's easier to accomplish that using power items to get easy 2IVs).
* The hardest situation to find answers for, by far, was the **find_optimal_destiny_knot** files. I was stumped for a long time on what "every possible scenario" really was. It took a lot of trial and error until I finally understood what all the factors were, and then figured out how to formulaically loop through them all. The trickiest dimension that evaded me was the concept of overlaps. "Two 3IV parents" is actually almost too vague to be meaningful. There could be anywhere from 0-3 overlaps, which corresponds to 3-6 unique 31s (between half of the desired IVs somewhere in the pool and all of them).
* In general, it's best to use a Destiny Knot except when you have two Pokemon with the same number of 31s where the IVs are in the same positions (maximum overlaps, minimum unique 31s; aside from two 6IVs, of course). Realistically speaking, when starting out: may as well use power items and different trees to achieve two 2IVs with maximum unique 31s (no overlaps). Use Destiny Knot + one power item and eventually get that to a 4IV, use a new breeding 'tree' to get a 2IV of the other two IV types you need, then use Destiny Knot + power item to make progress with the 4IV/2IV (all six unique IVs at this point). Once you already have a 6IV, there's no reason not to use a Destiny Knot.
## Disclaimer  
* Any errors? Please feel free to reach out!
* I did not necessarily code the mechanics in a way that perfectly matches the real in-game process (I don't know how it's all specifically implemented— but the abstraction here is identical as far as I'm aware).