# Code for Finding Game Levels

This repo contains all the code related to the paper *Finding Game Levels with the Right Difficulty in a Few Trials through Intelligent Trial-and-Error*. See the paper on arxiv [here](https://arxiv.org/abs/2005.07677), and on IEEE Explore [here](https://ieeexplore.ieee.org/abstract/document/9231548/).

# A guide through the code
This code relies on two small libraries I wrote, which implement MAP-Elites and ITAE.

# TL;DR

Intelligent Trial-and-Error is the name given to applying Bayesian Optimization to a corpus of "behaviors" (e.g. levels, robot gaits, environments for Reinforcement Learning) learned using the evolutionary algorithm MAP-Elites.

In this paper we try to apply ITAE for finding levels with a certain win rate for several planning agents. We start by computing several priors for these agents using MAP-Elites, and we then finding ideal levels for all pairs (e.g. using levels optimized for an MCTS agent, trying to find a level that's good for Rolling-Horizon evolution).
