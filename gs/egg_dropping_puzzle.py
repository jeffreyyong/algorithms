'''
The following is a decription of the instance of this famous puzzle involving 2 eggs
and building with k = 36 floors.

Suppose that we wish to know which stories in a 36-story building are safe to drop eggs from
and which will cause the eggs to break on landing. We make a few assumptions:

    1) An egg that survives a fall can be used again
    2) A broken egg must be discarded
    3) The effect of a fall is the same for all eggs.
    4) If an egg breaks when dropped, then it would break if dropped from a higher floor
    5) It is not ruled out that first-floor windows break eggs, nor is it ruled out that the
        36th floor do not cause anegg to break

    If only one egg is available and we wish to be sure of obtaining the right result, the experiment
    can be carried out in only one way. Drop the egg from the first-floor window; if it survices, drop
    it from the second floor window. Continue upward until it breaks. In the worst case, this 
    method requires 36 drops. Suppose 2 eggs are available. What is the least number of egg drops that
    is guaranteed to work in all case?

    The problem is not actually to find the critical floor, but merely to decide floors from which eggs
    should be dropped so that total number of trials are minimized.

1) Optimal Substructure:

When we drop an egg from a floor x, there can be two cases (1) The egg breaks (2) The egg doesn't break.

    1) If the egg breaks after dropping from xth floor, then we only need to check floorws lower than x with
        remaining eggs; so the problem reduces to x-1 floors and n-1 eggs

    2) If the egg doesn’t break after dropping from the xth floor, then we only need to check for floors higher 
        than x; so the problem reduces to k-x floors and n eggs.

        Since we need to minimize the number of trials in worst case, we take the maximum of two cases. We
        consider the max of above two cases for every floor and choose the floor which yields minimum number of trials.



2) Overlapping Subproblems:
'''


'''
Obtained from interviewcake.com

A Building has 100 floors. one of the floors is the highest floor an egg can be dropped without breaking

If an egg is dropped from above the floor, it will break. If it is dropped from that floor or below, it will
be completely undamaged and you can drop the egg again.

Given two eggs, find the highest floor an egg can be dropped from without breaking. With as few drops as possible.

GOTCHAS:
    We can do better than a binary appraoch, which would hvae a worst case of 50 drops.
    We can even do better than 19 drops!
    We can always find the highest floor an egg can be dropped from with a worst case of 14 total drops

BREAKDOOWN:
    What if we only had one egg? How could we find the correct floor?

    Because we can't use the egg again if it breaks, we'd have to play it safe and drop the gg from everyfloor, starting at
    the bottom and working our way up. In the worst case, the egg won't break until the top floor, so we'd drop the 
    egg 100 times.

    What does having two eggs allow us to do differenty?

    Since we have two eggs, we can skip multiple floors at a time until the first egg breaks, keeping track of which floors we
    dropped it from. Once that egg breaks we can use the second egg to try every floor, starting on the last floor where
    the egg didn't break and ending on the floor below the one where it did break.

How should we choose how many floors to skip with the first egg?

    What about trying binary approach? We could drop the first egg halfway up the building at the 50th floor. If the egg doesn't
    bnreak, we can try the 75th floor net. We keep going like this, dividing the problem in half at each step. As soon as
    the first egg breaks, wec can start using our second egg on our (now-hopefully narrow) range of possible floors.

    If we do that, what's the worst case number of total drops?

    The worst case is the highest floor an egg won't break from is floor 48 or 59. We'd drop the first egg from the 50th floor, 
    and then we'd have to drop the second egg from every floor from 1 to 49, for a total of 50 drops. (Even if the highest floor
    an egg won't break from is floor 48, we still won't know if it will break from floor 49 until we try.)

Can we do better than this binary approach?

    50 is probably too many floors to skip for the first drop. In the worst case, if the first egg breaks after a small number of drops,
    the second egg will break after a large number of drops. And if we went the other wayu and skipped 1 floor every time, we'd ahve
    the opposite problem! What would the worsrt case floor be then?

    The worst case would be floor 98 o 99 - the first egg would drop a large number of times (at every floor from 2 - 100 skiping one floor
    each time) and the last egg would drop a small number of times (only on floor 99),j for a total of 51 drops.

    Can we balance this out? Is there some number between 50 and 1 - the number of floors we'll skip with each drop for the first egg -
    where the first and second eggs would drop close to the same number of times in the worst case?

    Yes, we could skip 10 floors each time. The worst case would again be floor 98 or 99, but we'd onlyk drop the first 10 egg 10
    times and the second egg 9 times, for a total of 19 drops!

SOLUTION:
    We'll use the first egg to get a range of possible floors that contain the higest floor an egg can be dropped form without breaking.
    To do this, we'll drop it from increasingly higher floors until it breaks, skippping some number of floors each time.


'''
