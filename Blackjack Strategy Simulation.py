#!/usr/bin/env python
# coding: utf-8

# In[1]:


# First, initialize variables that will be used throughout
# Reminder: python indicies start at 0, so I am burning the first two indices so the index of 2 matches up with the value of 2
suit = ['burn','burn','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
values=[0,0,2,3,4,5,6,7,8,9,10,10,10,10,11]

from random import randint


# In[2]:


# Initialize player's winnings
player_cash=0
blackjack=0
win=0
loss=0
standoff=0
hands_played=0

#simulation of player strategy replicating dealer strategy
for hands in range(2000000):
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


# In[3]:


print('If a player uses the same strategy as the dealer and bets $1 on every hand: ')
print('Hands Played: '+str(hands_played))
print('Player Winnings: '+"${:,.2f}".format(player_cash))
print('Hands Won: ' + str(win))
print('Stand-off Hands: '+str(standoff))
print('Winning Blackjacks: '+str(blackjack))
print('Hands Lost: ' + str(hands_played-win-standoff))


# In[4]:


# Initialize player's winnings
player_cash=0
blackjack=0
win=0
loss=0
standoff=0
hands_played=0

# Simulation of basic player strategy
for hands in range(2000000):
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
    player_1=randint(2,14)
    player_2=randint(2,14)
    dealer_up=randint(2,14)
    dealer_down=randint(2,14)

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

        
        
        
        
    #set targets for player_total based on dealer's up card
    if player_soft>0:
        target=18
    elif dealer_up>=7:
        target=17
    elif dealer_up>=4:
        target=12
    else:
        target=13

        
        
        
    #create a hitting loop while the player's total is less than the target. If the total equals the target or is higher, the loop breaks
    while(player_total)<target:
        hit=randint(2,14)
        
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
            
        #we need to reset targets every time at the end of the loop to account for soft cards being added in hits or flexed if the player busts
        if player_soft>0:
            target=18
        elif dealer_up>=7:
            target=17
        elif dealer_up>=4:
            target=12
        else:
            target=13

            
            
            
            
            
    #dealer strategy implementation: if total <=16, take a hit, otherwise, stand
    while(dealer_total)<=16:
        hit=randint(2,14)
        
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


# In[5]:


print('If a player uses basic strategy and bets $1 on every hand: ')
print('Hands Played: '+str(hands_played))
print('Player Winnings: '+"${:,.2f}".format(player_cash))
print('Hands Won: ' + str(win))
print('Stand-off Hands: '+str(standoff))
print('Winning Blackjacks: '+str(blackjack))
print('Hands Lost: ' + str(hands_played-win-standoff))


# In[6]:


# Initialize player's winnings
player_cash=0
blackjack=0
win=0
loss=0
standoff=0
double_down_count=0
hands_played=0

# Simulation of basic player strategy + doubling down
for hands in range(2000000):
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
    
    #reset double down indicator
    double_down=False

    #draw two random cards for each player and dealer
    player_1=randint(2,14)
    player_2=randint(2,14)
    dealer_up=randint(2,14)
    dealer_down=randint(2,14)

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

    #set double down indicator based on strategy
    if player_total==11:
        double_down=True
    if player_total==10:
        if dealer_up <10:
            double_down=True
    if player_total==9:
        if dealer_up<=6:
            double_down=True
            
    #if the player doubles down, they must double their bet
    if double_down==True:
        double_down_count+=1
        player_cash-=1
        
        
    #set targets for player_total based on dealer's up card
    if player_soft>0:
        target=18
    elif dealer_up>=7:
        target=17
    elif dealer_up>=4:
        target=12
    else:
        target=13

        
        
        
    #create a hitting loop while the player's total is less than the target. If the total equals the target or is higher, the loop breaks
    #only enter the hitting loop if double_down is false. otherwise, enter the else statement to play the double down
    if double_down==False:
        while(player_total)<target:
            hit=randint(2,14)

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

            #we need to reset targets every time at the end of the loop to account for soft cards being added in hits or flexed if the player busts
            if player_soft>0:
                target=18
            elif dealer_up>=7:
                target=17
            elif dealer_up>=4:
                target=12
            else:
                target=13
    else:
        #if a player doubles down, they take one hit and must stay
        hit=randint(2,14)
        
        #add the hit value to the total
        player_total+=values[hit]
        
        #if the hit card is an ace, we must add one to the soft aces tally that can be flexed to 1
        if hit==14:
            player_soft+=1
        
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
        hit=randint(2,14)
        
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
    #note: this isn't possible if the player qualified to double down, so we do not include double down logic in this portion
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
    #for all winnings, an extra dollar is awarded to the player for a double down, plus their extra dollar bet back
    #for all standoffs, the player gets their extra dollar back if they doubled down
    elif dealer_naturals==False:
        #if the dealer busts and the player does not bust, the player wins
        if dealer_total>21:
            if player_total<=21:
                player_cash+=2
                if double_down==True:
                    player_cash+=2
                win+=1
        #if we get to this point, the dealer didn't bust. we check to see if the player busted first. if they didn't, proceed
        #if the player's total is greater than the dealer's, the player wins
        elif player_total<=21:
            if player_total>dealer_total:
                player_cash+=2
                if double_down==True:
                    player_cash+=2
                win+=1
            #if the player's total equals the dealer's total, it's a standoff and the bet is returned
            elif player_total==dealer_total:
                player_cash+=1
                if double_down==True:
                    player_cash+=1
                standoff+=1


# In[7]:


print('If a player uses basic strategy + double downs and bets $1 on every hand: ')
print('Hands Played: '+str(hands_played))
print('Player Winnings: '+"${:,.2f}".format(player_cash))
print('Hands Won: ' + str(win))
print('Stand-off Hands: '+str(standoff))
print('Winning Blackjacks: '+str(blackjack))
print('Hands Lost: ' + str(hands_played-win-standoff))
print('Number of double downs: '+str(double_down_count))


# In[8]:


# Initialize player's winnings
player_cash=0
blackjack=0
win=0
loss=0
standoff=0
splits=0
hands_played=0

# Simulation of basic player strategy + splits
for hands in range(2000000):
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
    
    #reset split indicator
    split_ind=False

    #draw two random cards for each player and dealer
    player_1=randint(2,14)
    player_2=randint(2,14)
    dealer_up=randint(2,14)
    dealer_down=randint(2,14)
    
    #split strategy implementation
    if player_1==player_2:
        if player_1==14 or player_1==8:
            split_ind=True
        elif player_1==2 or player_1==3 or player_1==7:
            if dealer_up<8:
                split_ind=True
        elif player_1==6:
            if dealer_up<=6:
                split_ind=True
                
                
    #this gets a little bit complicated if the player ends up splitting
    #let's wrap the entire code below in an if statement so that we clearly separate the split scenario vs the non-split scenario
    
    if split_ind==False:

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





        #set targets for player_total based on dealer's up card
        if player_soft>0:
            target=18
        elif dealer_up>=7:
            target=17
        elif dealer_up>=4:
            target=12
        else:
            target=13




        #create a hitting loop while the player's total is less than the target. If the total equals the target or is higher, the loop breaks
        while(player_total)<target:
            hit=randint(2,14)

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

            #we need to reset targets every time at the end of the loop to account for soft cards being added in hits or flexed if the player busts
            if player_soft>0:
                target=18
            elif dealer_up>=7:
                target=17
            elif dealer_up>=4:
                target=12
            else:
                target=13






        #dealer strategy implementation: if total <=16, take a hit, otherwise, stand
        while(dealer_total)<=16:
            hit=randint(2,14)

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
                    
    #splitting scenario - player plays two hands, one with each of their split cards. they must bet an additional $1
    else:
        splits+=1
        player_cash-=1
        hands_played+=1
        
        #start with the dealer's hand, for simplicity in calculating winnings. even though this doesn't happen in real life, it won't affect our strategy in this simulation
        
        #add a soft ace counter if any of the drawn cards are an ace
        if dealer_up==14:
            dealer_soft+=1
        if dealer_down==14:
            dealer_soft+=1
            
        #calculate the total value of each hand
        dealer_total=values[dealer_up]+values[dealer_down]
        
        #if the dealer or player have 21 with just the first two cards, they have a natural blackjack
        if dealer_total==21:
            dealer_naturals=True
            
        #dealer strategy implementation: if total <=16, take a hit, otherwise, stand
        while(dealer_total)<=16:
            hit=randint(2,14)

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
        

        #now, play two hands with the player's split cards and calculate the result
        for split_hand in range(2):
            #reset totals to 0 at the start of the hand
            player_total=0
    
            #reset the number of aces that can be used as soft cards to 0
            player_soft=0

            #reset natural blackjack indicator
            player_naturals=False
            
            #player1=player_1 - this stays the same as before for the split
            player_2=randint(2,14)
    
            #add a soft ace counter if any of the drawn cards are an ace
            if player_1==14:
                player_soft+=1
            if player_2==14:
                player_soft+=1
                
            #calculate the total value of each hand
            player_total=values[player_1]+values[player_2]
            
            #if the dealer or player have 21 with just the first two cards, they have a natural blackjack
            if player_total==21:
                player_naturals=True
            
            #set targets for player_total based on dealer's up card
            if player_soft>0:
                target=18
            elif dealer_up>=7:
                target=17
            elif dealer_up>=4:
                target=12
            else:
                target=13
                
            #create a hitting loop while the player's total is less than the target. If the total equals the target or is higher, the loop breaks
            while(player_total)<target:
                hit=randint(2,14)

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

                #we need to reset targets every time at the end of the loop to account for soft cards being added in hits or flexed if the player busts
                if player_soft>0:
                    target=18
                elif dealer_up>=7:
                    target=17
                elif dealer_up>=4:
                    target=12
                else:
                    target=13
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
            


# In[9]:


print('If a player uses basic strategy + splitting and bets $1 on every hand: ')
print('Hands Played: '+str(hands_played))
print('Player Winnings: '+"${:,.2f}".format(player_cash))
print('Hands Won: ' + str(win))
print('Stand-off Hands: '+str(standoff))
print('Winning Blackjacks: '+str(blackjack))
print('Hands Lost: ' + str(hands_played-win-standoff))
print('Number of splits: '+str(splits))


# In[10]:


# Initialize player's winnings
player_cash=0
blackjack=0
win=0
loss=0
standoff=0
double_down_count=0
splits=0
hands_played=0

# Simulation of basic player strategy + doubling down + splits
for hands in range(2000000):
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
    
    #reset double down indicator
    double_down=False
    
    #reset split indicator
    split_ind=False

    #draw two random cards for each player and dealer
    player_1=randint(2,14)
    player_2=randint(2,14)
    dealer_up=randint(2,14)
    dealer_down=randint(2,14)
    
    #split strategy implementation
    if player_1==player_2:
        if player_1==14 or player_1==8:
            split_ind=True
        elif player_1==2 or player_1==3 or player_1==7:
            if dealer_up<8:
                split_ind=True
        elif player_1==6:
            if dealer_up<=6:
                split_ind=True

                
    #this gets a little bit complicated if the player ends up splitting
    #let's wrap the entire code below in an if statement so that we clearly separate the split scenario vs the non-split scenario
    
    if split_ind==False:
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

        #set double down indicator based on strategy
        if player_total==11:
            double_down=True
        if player_total==10:
            if dealer_up <10:
                double_down=True
        if player_total==9:
            if dealer_up<=6:
                double_down=True

        #if the player doubles down, they must double their bet
        if double_down==True:
            double_down_count+=1
            player_cash-=1


        #set targets for player_total based on dealer's up card
        if player_soft>0:
            target=18
        elif dealer_up>=7:
            target=17
        elif dealer_up>=4:
            target=12
        else:
            target=13




        #create a hitting loop while the player's total is less than the target. If the total equals the target or is higher, the loop breaks
        #only enter the hitting loop if double_down is false. otherwise, enter the else statement to play the double down
        if double_down==False:
            while(player_total)<target:
                hit=randint(2,14)

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

                #we need to reset targets every time at the end of the loop to account for soft cards being added in hits or flexed if the player busts
                if player_soft>0:
                    target=18
                elif dealer_up>=7:
                    target=17
                elif dealer_up>=4:
                    target=12
                else:
                    target=13
        else:
            #if a player doubles down, they take one hit and must stay
            hit=randint(2,14)

            #add the hit value to the total
            player_total+=values[hit]

            #if the hit card is an ace, we must add one to the soft aces tally that can be flexed to 1
            if hit==14:
                player_soft+=1

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
            hit=randint(2,14)

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
        #note: this isn't possible if the player qualified to double down, so we do not include double down logic in this portion
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
        #for all winnings, an extra dollar is awarded to the player for a double down, plus their extra dollar bet back
        #for all standoffs, the player gets their extra dollar back if they doubled down
        elif dealer_naturals==False:
            #if the dealer busts and the player does not bust, the player wins
            if dealer_total>21:
                if player_total<=21:
                    player_cash+=2
                    if double_down==True:
                        player_cash+=2
                    win+=1
            #if we get to this point, the dealer didn't bust. we check to see if the player busted first. if they didn't, proceed
            #if the player's total is greater than the dealer's, the player wins
            elif player_total<=21:
                if player_total>dealer_total:
                    player_cash+=2
                    if double_down==True:
                        player_cash+=2
                    win+=1
                #if the player's total equals the dealer's total, it's a standoff and the bet is returned
                elif player_total==dealer_total:
                    player_cash+=1
                    if double_down==True:
                        player_cash+=1
                    standoff+=1
                    
                    
    #splitting scenario - player plays two hands, one with each of their split cards. they must bet an additional $1
    else:
        splits+=1
        player_cash-=1
        hands_played+=1
        
        #start with the dealer's hand, for simplicity in calculating winnings. even though this doesn't happen in real life, it won't affect our strategy in this simulation
        
        #add a soft ace counter if any of the drawn cards are an ace
        if dealer_up==14:
            dealer_soft+=1
        if dealer_down==14:
            dealer_soft+=1
            
        #calculate the total value of each hand
        dealer_total=values[dealer_up]+values[dealer_down]
        
        #if the dealer or player have 21 with just the first two cards, they have a natural blackjack
        if dealer_total==21:
            dealer_naturals=True
            
        #dealer strategy implementation: if total <=16, take a hit, otherwise, stand
        while(dealer_total)<=16:
            hit=randint(2,14)

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
        

        #now, play two hands with the player's split cards and calculate the result
        for split_hand in range(2):
            #reset totals to 0 at the start of the hand
            player_total=0
    
            #reset the number of aces that can be used as soft cards to 0
            player_soft=0

            #reset natural blackjack indicator
            player_naturals=False
            
            #reset double down indicator
            double_down=False
            
            #player1=player_1 - this stays the same as before for the split
            player_2=randint(2,14)
            
            #add a soft ace counter if any of the drawn cards are an ace
            if player_1==14:
                player_soft+=1
            if player_2==14:
                player_soft+=1
                
            #calculate the total value of each hand
            player_total=values[player_1]+values[player_2]
            
            #if the dealer or player have 21 with just the first two cards, they have a natural blackjack
            if player_total==21:
                player_naturals=True

            #set double down indicator based on strategy
            if player_total==11:
                double_down=True
            if player_total==10:
                if dealer_up <10:
                    double_down=True
            if player_total==9:
                if dealer_up<=6:
                    double_down=True
                    
            #if the player doubles down, they must double their bet
            if double_down==True:
                double_down_count+=1
                player_cash-=1
                
            #set targets for player_total based on dealer's up card
            if player_soft>0:
                target=18
            elif dealer_up>=7:
                target=17
            elif dealer_up>=4:
                target=12
            else:
                target=13
            
            #create a hitting loop while the player's total is less than the target. If the total equals the target or is higher, the loop breaks
            #only enter the hitting loop if double_down is false. otherwise, enter the else statement to play the double down
            if double_down==False:
                while(player_total)<target:
                    hit=randint(2,14)

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

                    #we need to reset targets every time at the end of the loop to account for soft cards being added in hits or flexed if the player busts
                    if player_soft>0:
                        target=18
                    elif dealer_up>=7:
                        target=17
                    elif dealer_up>=4:
                        target=12
                    else:
                        target=13
            
            else:
                #if a player doubles down, they take one hit and must stay
                hit=randint(2,14)

                #add the hit value to the total
                player_total+=values[hit]

                #if the hit card is an ace, we must add one to the soft aces tally that can be flexed to 1
                if hit==14:
                    player_soft+=1

                #if there is a bust, we must check if there is an ace that can be flexed to a value of 1
                if player_total>21:
                    if player_soft>0:
                        #subtract 10 to flex ace from 11 in value to 1
                        player_total-=10
                        #remove the ability to flex that ace
                        player_soft-=1
                    else:
                        pass
                    
            #payouts
            #if the player has a natural blackjack and the dealer does not, payout 1.5 times the bet and return the bet.
            #note: this isn't possible if the player qualified to double down, so we do not include double down logic in this portion
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
            #for all winnings, an extra dollar is awarded to the player for a double down, plus their extra dollar bet back
            #for all standoffs, the player gets their extra dollar back if they doubled down
            elif dealer_naturals==False:
                #if the dealer busts and the player does not bust, the player wins
                if dealer_total>21:
                    if player_total<=21:
                        player_cash+=2
                        if double_down==True:
                            player_cash+=2
                        win+=1
                #if we get to this point, the dealer didn't bust. we check to see if the player busted first. if they didn't, proceed
                #if the player's total is greater than the dealer's, the player wins
                elif player_total<=21:
                    if player_total>dealer_total:
                        player_cash+=2
                        if double_down==True:
                            player_cash+=2
                        win+=1
                    #if the player's total equals the dealer's total, it's a standoff and the bet is returned
                    elif player_total==dealer_total:
                        player_cash+=1
                        if double_down==True:
                            player_cash+=1
                        standoff+=1


# In[11]:


print('If a player uses basic strategy + double downs + splitting and bets $1 on every hand: ')
print('Hands Played: '+str(hands_played))
print('Player Winnings: '+"${:,.2f}".format(player_cash))
print('Hands Won: ' + str(win))
print('Stand-off Hands: '+str(standoff))
print('Winning Blackjacks: '+str(blackjack))
print('Hands Lost: ' + str(hands_played-win-standoff))
print('Number of double downs: '+str(double_down_count))
print('Number of splits: '+str(splits))


# In[ ]:




