# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v7cL0TBF8N9Z3_xrmd1YrCcwYTp_TMfO

    https://stackoverflow.com/questions/67333582/how-to-enter-large-matrix-into-relational-databasedb-mysql
"""

import numpy as np
import pandas as pd
import random
class Music:
  def __init__(self, playlist, Q, R):
    self.R = R
    self.Q = Q
    self.playlist = playlist

  def rewardMatrix(self, user_Input):
    df = ['BollywoodSad', 'BollywoodSad', 'BollywoodSad', 'BollywoodDance', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodDance', 'Bollywood', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodSad', 'BollywoodDance', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodSad', 'BollywoodDance', 'BollywoodDance', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodSad', 'BollywoodSad', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodRomantic', 'Bollywood', 'BollywoodDance', 'BollywoodDance', 'BollywoodDance', 'BollywoodRomantic', 'Bollywood', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodSad', 'BollywoodSad', 'BollywoodDance', 'Bollywood', 'Bollywood', 'BollywoodDance', 'Bollywood', 'BollywoodSad', 'BollywoodSad', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodRomantic', 'Bollywood', 'Bollywood', 'Bollywood', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodSad', 'Bollywood', 'BollywoodDance', 'Bollywood', 'BollywoodDance', 'BollywoodSad', 'Bollywood', 'BollywoodDance', 'Bollywood', 'BollywoodDance', 'Bollywood', 'Bollywood', 'BollywoodDance', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodSad', 'Bollywood', 'BollywoodSad', 'BollywoodSad', 'Bollywood', 'Bollywood', 'BollywoodSad', 'BollywoodDance', 'BollywoodDance', 'BollywoodDance', 'BollywoodDance', 'Bollywood', 'Bollywood', 'BollywoodDance', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodDance', 'Bollywood', 'BollywoodSad', 'BollywoodSad', 'BollywoodSad', 'Bollywood', 'Bollywood', 'Bollywood', 'BollywoodRomantic', 'BollywoodRomantic', 'Bollywood', 'BollywoodSad', 'BollywoodRomantic', 'Bollywood', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodSad', 'BollywoodDance', 'Bollywood', 'BollywoodDance', 'BollywoodRomantic', 'Bollywood', 'Bollywood', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodDance', 'Bollywood', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodDance', 'Bollywood', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodSad', 'Bollywood', 'BollywoodRomantic', 'Bollywood', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodDance', 'BollywoodRomantic', 'Bollywood', 'BollywoodDance', 'BollywoodDance', 'BollywoodSad', 'BollywoodDance', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodRomantic', 'Bollywood', 'Bollywood', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodDance', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodDance', 'Bollywood', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodDance', 'Bollywood', 'BollywoodRomantic', 'BollywoodSad', 'Bollywood', 'BollywoodDance', 'BollywoodDance', 'Bollywood', 'Bollywood', 'Bollywood', 'BollywoodDance', 'Bollywood', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodDance', 'Bollywood', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodSad', 'Bollywood', 'Bollywood', 'BollywoodRomantic', 'BollywoodRomantic', 'Bollywood', 'BollywoodRomantic', 'BollywoodSad', 'Bollywood', 'Bollywood', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodSad', 'BollywoodDance', 'Bollywood', 'BollywoodDance', 'BollywoodDance', 'BollywoodSad', 'BollywoodDance', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodSad', 'BollywoodRomantic', 'Bollywood', 'Bollywood', 'BollywoodRomantic', 'Bollywood', 'BollywoodRomantic', 'BollywoodDance', 'Bollywood', 'BollywoodSad', 'BollywoodDance', 'BollywoodDance', 'BollywoodSad', 'BollywoodSad', 'BollywoodDance', 'BollywoodSad', 'BollywoodDance', 'Bollywood', 'BollywoodDance', 'BollywoodSad', 'BollywoodSad', 'BollywoodSad', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodDance', 'BollywoodDance', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodRomantic', 'Bollywood', 'BollywoodRomantic', 'Bollywood', 'BollywoodDance', 'Bollywood', 'BollywoodSad', 'BollywoodDance', 'BollywoodSad', 'Bollywood', 'BollywoodSad', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodSad', 'BollywoodDance', 'BollywoodRomantic', 'Bollywood', 'Bollywood', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodDance', 'Bollywood', 'Bollywood', 'BollywoodSad', 'Bollywood', 'Bollywood', 'BollywoodDance', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodDance', 'Bollywood', 'Bollywood', 'BollywoodSad', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodDance', 'BollywoodDance', 'BollywoodDance', 'BollywoodSad', 'BollywoodSad', 'BollywoodSad', 'BollywoodSad', 'Bollywood', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodRomantic', 'Bollywood', 'BollywoodRomantic', 'Bollywood', 'BollywoodRomantic', 'Bollywood', 'Bollywood', 'BollywoodDance', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodSad', 'Bollywood', 'Bollywood', 'BollywoodRomantic', 'Bollywood', 'BollywoodSad', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodDance', 'BollywoodRomantic', 'Bollywood', 'BollywoodDance', 'BollywoodRomantic', 'Bollywood', 'BollywoodSad', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodDance', 'Bollywood', 'Bollywood', 'BollywoodRomantic', 'BollywoodRomantic', 'Bollywood', 'BollywoodRomantic', 'BollywoodRomantic', 'Bollywood', 'BollywoodSad', 'BollywoodDance', 'BollywoodDance', 'BollywoodDance', 'BollywoodSad', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodRomantic', 'Bollywood', 'BollywoodSad', 'Bollywood', 'BollywoodRomantic', 'Bollywood', 'BollywoodSad', 'BollywoodDance', 'Bollywood', 'BollywoodSad', 'Bollywood', 'Bollywood', 'Bollywood', 'Bollywood', 'BollywoodDance', 'Bollywood', 'Bollywood', 'Bollywood', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodSad', 'Bollywood', 'Bollywood', 'BollywoodDance', 'Bollywood', 'BollywoodDance', 'BollywoodDance', 'BollywoodSad', 'Bollywood', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodRomantic', 'Bollywood', 'Bollywood', 'BollywoodDance', 'BollywoodDance', 'BollywoodDance', 'Bollywood', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodSad', 'BollywoodDance', 'BollywoodDance', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodDance', 'BollywoodSad', 'BollywoodSad', 'Bollywood', 'BollywoodSad', 'Bollywood', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodDance', 'BollywoodDance', 'BollywoodSad', 'BollywoodSad', 'BollywoodDance', 'Bollywood', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodRomantic', 'Bollywood', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodRomantic', 'Bollywood', 'BollywoodSad', 'BollywoodSad', 'BollywoodDance', 'BollywoodSad', 'BollywoodDance', 'BollywoodSad', 'BollywoodSad', 'BollywoodDance', 'Bollywood', 'BollywoodDance', 'Bollywood', 'BollywoodRomantic', 'BollywoodSad', 'Bollywood', 'BollywoodRomantic', 'Bollywood', 'Bollywood', 'BollywoodDance', 'BollywoodRomantic', 'Bollywood', 'BollywoodSad', 'BollywoodDance', 'Bollywood', 'BollywoodRomantic', 'Bollywood', 'BollywoodRomantic', 'BollywoodRomantic', 'BollywoodRomantic', 'Bollywood', 'Bollywood', 'Bollywood', 'Bollywood', 'BollywoodRomantic', 'Bollywood', 'BollywoodSad', 'BollywoodSad', 'BollywoodSad', 'BollywoodSad', 'BollywoodDance', 'Bollywood', 'Bollywood', 'BollywoodRomantic', 'BollywoodDance', 'BollywoodDance', 'BollywoodDance', 'BollywoodRomantic', 'BollywoodSad', 'BollywoodSad', 'BollywoodDance', 'Bollywood', 'BollywoodDance', 'Bollywood', 'Bollywood', 'BollywoodSad', 'BollywoodSad', 'Bollywood', 'BollywoodSad', 'BollywoodSad', 'Bollywood', 'Bollywood']
    for i in range(0, 10):
        n = self.playlist[i]
        x = df[n]
        for j in range(0, 500):
            self.R[j][n] = -1.0
            y = df[j]
            if n == j:
                self.R[n][j] = -1.0
            elif x == y:
                if self.R[n][j] != -1.0:
                    self.R[n][j] = self.R[n][j] + (0.35 * float(user_Input[i][1])) + (0.35 * (float((user_Input[i][2]) * 1.0) / 3600)) + (0.3)
                else:
                    self.R[n][j] = -1.0
            else:
                if self.R[n][j] != -1.0:
                    self.R[n][j] = self.R[n][j] + (0.35 * float(user_Input[i][1])) + (0.35 * ((float(user_Input[i][2]) * 1.0) / 3600))
                else:
                    self.R[n][j] = -1.0

  def get_poss_next_states(self, s, ns):
    poss_next_states = []
    for j in range(ns):
      if self.R[s, j] != -1: poss_next_states.append(j)
    return poss_next_states

  def get_rnd_next_state(self, s, ns):
    poss_next_states = self.get_poss_next_states(s, ns)
    next_state = np.random.choice(poss_next_states)
    return next_state

  def train(self, ns):
    stop = ns
    gamma = 0.5
    lrn_rate = 0.5
    for i in range(0, len(self.playlist)):
      curr_s = self.playlist[i]
      stop = 500
      while(stop > 0):
        next_s = self.get_rnd_next_state(curr_s, ns)
        poss_next_next_states = self.get_poss_next_states(next_s, ns)
        max_Q = -9999.99
        for j in range(len(poss_next_next_states)):
          nn_s = poss_next_next_states[j]
          q = self.Q[next_s, nn_s]
          if q >= max_Q:
            max_Q = q

        self.Q[curr_s][next_s] = ((1 - lrn_rate) * self.Q[curr_s][next_s]) + (lrn_rate * (self.R[curr_s][next_s] + (gamma * max_Q)))
        stop = stop - 1

  def NewRecommendation(self, user_Input):  # user matrix(songid,songlike,songlen,genre)10x4matrix.
    self.rewardMatrix(user_Input)
    self.train(500)
    Recommended_playlist = []
    for i in range(len(self.playlist)):
      curr = self.playlist[i]
      next1 = []
      for i in range(0, len(self.Q[curr])): 
        next1.append([self.Q[curr][i], i])
      next1.sort(reverse=True)  # sort in descending order to get the 10 songs with highest value.
      for k in range(3):
          Recommended_playlist.append(next1[k])
    
    Recommended_playlist.sort(reverse=True)
    del Recommended_playlist[7:30] 
    while(len(Recommended_playlist) < 10):
        x = random.randint(0, 499)
        print("this is x",x)


        for i in range(0,len(Recommended_playlist)):
            if x == Recommended_playlist[i][1]:
                flag = 1
                break
            else:
                flag = 0
        
        if flag == 0:
            Recommended_playlist.append([0.0, x])

    # recommended playlist is 7*2 matrix. 7 songs and Qmatrix value and song id.
          
    # this returns id for song which we suppose to play on html.
    self.playlist = Recommended_playlist
