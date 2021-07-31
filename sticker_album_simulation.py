# -*- coding: utf-8 -*-

# Librerías
import numpy as np
import random

#Semilla reproducibilidad
random.seed(1234)

#%% Function
def create_album(total_stickers):
    'It returns a vector with spaces equal to the number of total stickers in the album.'
    album=np.zeros(total_stickers, dtype=int)
    return album


def buy_stickers(total_stickers):
    '''With the number of total stickers, it returns a random number that
    represents the sticker we got.'''
    sticker=random.randint(0,total_stickers-1)
    return sticker


def howmany_stickers(total_stickers, n_repetitions):
    '''It creates a new album and simulates the filling of it.
    The simulations is repeated n_repetitions times.
    It returns the number of stickers we have to buy to fill the album
    in each simulation.'''
    # Vector with empty spaces equal to the number of simulations.
    full_album = np.empty(n_repetitions) 
    for i in range(n_repetitions):
        album=create_album(total_stickers)
        stickers_quantity = 0 # Counter
        while min(album) == 0: # While album is not still full
            # Which sticker we get randomly:
            sticker=buy_stickers(total_stickers)
            if album[sticker]==0:
                album[sticker]=1 # Fill with 1 the spaces of stickers we have already get.
            stickers_quantity+=1 # Increment for loop
        full_album[i] = stickers_quantity # Total number of sticker we needed to fill the album
    # It returns a vector with the number of stickers we have to buy to fill the album
    return full_album 


#%% Run the simulation

# Data of album
total_stickers=400
# 5 stickers per package
sticker_package = 5
# US$0.6 a package
package_price = 0.6

# Selected number of simulations
n_repetitions=1000

# Obtain the vector with the number of stickers we have to buy to fill the album
n_stickers=howmany_stickers(total_stickers,n_repetitions)

# average total number of stickers to fill the album
average_n_stickers=np.mean(n_stickers)
print(f' You need to buy {average_n_stickers:.0f} stickers on average to fill the album.')

# Calculating the price to fill the album
packages = n_stickers/5
print(f' A number of {packages:.0f} packages are necessary to fill the album.')

price = packages*package_price
print(f' Filling the album will cost US${price:.0f}.')