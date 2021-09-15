#!/usr/bin/env python
# coding: utf-8

# In[1]:


# First, initialize variables that will be used throughout
# Reminder: python indicies start at 0, so I am burning the first two indices so the index of 2 matches up with the value of 2
suit = ['burn','burn','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
values=[0,0,2,3,4,5,6,7,8,9,10,10,10,10,11]

from matplotlib import pyplot as plt
from random import randint


# In[2]:


#initialize list that stores the profit results of each trial
trial_profit=[]
#loop through 50,000 trials of playing 100 hands each
for trial in range(50000):
    # Initialize player's winnings
    player_cash=0
    #other statistics are not tracked per trial. if desired, another list like trial_profit can be initialized and the result be appended at the end.
    blackjack=0
    win=0
    loss=0
    standoff=0
    hands_played=0

    #simulation of player strategy replicating dealer strategy
    for hands in range(100):
        #player bets $1 to start the game
        player_cash-=1
        hands_played+=1

        #reset totals to 0 at the start of the hand
        player_total=0
        dealer_total=0

        #reset the number of aces that can be used as soft cards to 0
        player_soft=0
        dealer_soft=0

        #reset natural blackjack indicator
        player_naturals=False
        dealer_naturals=False

        #draw two random cards for each player and dealer
        player_1=randint(2, 14)
        player_2=randint(2, 14)
        dealer_up=randint(2, 14)
        dealer_down=randint(2, 14)

        #add a soft ace counter if any of the drawn cards are an ace
        if player_1==14:
            player_soft+=1
        if player_2==14:
            player_soft+=1
        if dealer_up==14:
            dealer_soft+=1
        if dealer_down==14:
            dealer_soft+=1

        #calculate the total value of each hand
        player_total=values[player_1]+values[player_2]
        dealer_total=values[dealer_up]+values[dealer_down]

        #if the dealer or player have 21 with just the first two cards, they have a natural blackjack
        if player_total==21:
            player_naturals=True
        if dealer_total==21:
            dealer_naturals=True

        #dealer strategy implementation: if total <=16, take a hit, otherwise, stand
        while(player_total)<=16:
            hit=randint(2, 14)

            #if the hit card is an ace, we must add one to the soft aces tally that can be flexed to 1
            if hit==14:
                player_soft+=1

            #add the hit value to the total
            player_total+=values[hit]

            #if there is a bust, we must check if there is an ace that can be flexed to a value of 1
            if player_total>21:
                if player_soft>0:
                    #subtract 10 to flex ace from 11 in value to 1
                    player_total-=10
                    #remove the ability to flex that ace
                    player_soft-=1
                else:
                    pass




        #dealer strategy implementation: if total <=16, take a hit, otherwise, stand
        while(dealer_total)<=16:
            hit=randint(2, 14)

            #if the hit card is an ace, we must add one to the soft aces tally that can be flexed to 1
            if hit==14:
                dealer_soft+=1

            #add the hit value to the total
            dealer_total+=values[hit]

            #if there is a bust, we must check if there is an ace that can be flexed to a value of 1
            if dealer_total>21:
                if dealer_soft>0:
                    #subtract 10 to flex ace from 11 in value to 1
                    dealer_total-=10
                    #remove the ability to flex that ace
                    dealer_soft-=1
                else:
                    pass




        #payouts
        #if the player has a natural blackjack and the dealer does not, payout 1.5 times the bet and return the bet.
        if player_naturals==True:
            if dealer_naturals==False:
                player_cash+=2.5
                blackjack+=1
                win+=1
            #if the dealer also has a natural blackjack, return the bet
            else:
                player_cash+=1
                standoff+=1

        #if we get to this point, the player does not have a natural blackjack
        #if the dealer has a natural blackjack, nothing is returned to the player. we only take action if the dealer does not have a natural blackjack
        elif dealer_naturals==False:
            #if the dealer busts and the player does not bust, the player wins
            if dealer_total>21:
                if player_total<=21:
                    player_cash+=2
                    win+=1
            #if we get to this point, the dealer didn't bust. we check to see if the player busted first. if they didn't, proceed
            #if the player's total is greater than the dealer's, the player wins
            elif player_total<=21:
                if player_total>dealer_total:
                    player_cash+=2
                    win+=1
                #if the player's total equals the dealer's total, it's a standoff and the bet is returned
                elif player_total==dealer_total:
                    player_cash+=1
                    standoff+=1
    trial_profit.append(player_cash)


# In[3]:


xbar=sum(trial_profit)/len(trial_profit)
s2 = sum([((x - xbar) ** 2) for x in trial_profit]) / len(trial_profit) 
s = s2 ** 0.5
n=50000
z=(1.960)
CI_high=xbar+z*s/(n**0.5)
CI_low=xbar-z*s/(n**0.5)
print('We are 95% confident that the player will gain between '+"${:,.2f}".format(CI_low)+' and '+"${:,.2f}".format(CI_high)+' from this strategy.')
plt.hist(trial_profit, 20)
plt.show()

