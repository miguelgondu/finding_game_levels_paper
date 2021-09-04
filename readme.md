# Zelda experiments

All the agents that are implemented in the GVGAI singlePlayer track are the following:

- **sampleRandomController** ("tracks.singlePlayer.simple.sampleRandom.Agent"): a controller that takes random actions.
- **doNothingController** ("tracks.singlePlayer.simple.doNothing.Agent"): a controller that does nothing.
- **sampleOneStepController** ("tracks.singlePlayer.simple.sampleonesteplookahead.Agent"): a controller that models the Q function by looking at the effect of taking every possible action, only one step into the future.
- **sampleFlatMCTSController** ("tracks.singlePlayer.simple.greedyTreeSearch.Agent"): It's selecting the best child, but I don't really know what's the difference with oneStepAhead. TODO: check this in more detail.
- **sampleMCTSController** ("tracks.singlePlayer.advanced.sampleMCTS.Agent"): a controller that runs Monte Carlo Tree Search.
- **sampleRSController** ("tracks.singlePlayer.advanced.sampleRS.Agent"): a controller that performs random search in the tree.
- **sampleRHEAController** ("tracks.singlePlayer.advanced.sampleRHEA.Agent"): a controller that does Rolling Horizon Evolution.
- **sampleOLETSController** ("tracks.singlePlayer.advanced.olets.Agent"): a controller that runs Open-loop Expectimax Tree Search. (Search about how that works.)