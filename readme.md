# Code for _Finding Game Levels_

This repo contains all the code related to the paper *Finding Game Levels with the Right Difficulty in a Few Trials through Intelligent Trial-and-Error*. See the paper on arxiv [here](https://arxiv.org/abs/2005.07677), and on IEEE Explore [here](https://ieeexplore.ieee.org/abstract/document/9231548/).


## TL;DR

Intelligent Trial-and-Error (ITAE) is the name given to applying Bayesian Optimization to a corpus of "behaviors" (e.g. levels, robot gaits or environments for Reinforcement Learning) learned using the evolutionary algorithm MAP-Elites.

In this paper we try to apply ITAE for finding levels with a certain win rate for several planning agents. We start by computing several priors for these agents using MAP-Elites, and we then finding ideal levels for all pairs (e.g. using levels optimized for an MCTS agent, trying to find a level that's good for Rolling-Horizon evolution).
## A guide through the code

This code relies on two small libraries I wrote, which implement MAP-Elites and ITAE ([pymelites](https://github.com/miguelgondu/pymelites) and [pyITaE](https://github.com/miguelgondu/pyITaE) respectively). So you can start by cloning them and installing them using `pip install -e .`.

After that, the core work done for the experiments is done by `zelda_map_elites_experiment.py` (which evolves a corpus of levels for a certain agent), and by `zelda_itae_experiment.py` (which takes one of these generations and updates it using B.O.) This pieces of code rely on a custom version of the [GVGAI game compiler](https://github.com/GAIGResearch/GVGAI).

The rest of the code was implemented either for visualizing and debugging ideas, or for plotting the final results that appear on the paper. 

## Replicating the results

There are two `.sh` files that should be enough for replicating the results of the paper.

1. Run `to_run.sh` for the MAP-Elites prior creation. Then create a new folder `./zelda_experiment/generations` and put the final generations of all agents.
2. After that, you should be able to run `to_run_itae.sh`.
