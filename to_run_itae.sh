# --------------------------------------------------------------------------------
# prior: baselineRandomPrior
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_baselineRandomPrior_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_baselineRandomPrior_to_olets --path_to_updates=./zelda_experiments/updates --prior_folder=baselineRandomPrior_prior --agent=tracks.singlePlayer.advanced.olets.Agent --parallel > log_prior_baselineRandomPrior_agent_olets.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_baselineRandomPrior_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_baselineRandomPrior_to_sampleMCTS --path_to_updates=./zelda_experiments/updates --prior_folder=baselineRandomPrior_prior --agent=tracks.singlePlayer.advanced.sampleMCTS.Agent --parallel > log_prior_baselineRandomPrior_agent_sampleMCTS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_baselineRandomPrior_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_baselineRandomPrior_to_sampleRHEA --path_to_updates=./zelda_experiments/updates --prior_folder=baselineRandomPrior_prior --agent=tracks.singlePlayer.advanced.sampleRHEA.Agent --parallel > log_prior_baselineRandomPrior_agent_sampleRHEA.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_baselineRandomPrior_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_baselineRandomPrior_to_sampleRS --path_to_updates=./zelda_experiments/updates --prior_folder=baselineRandomPrior_prior --agent=tracks.singlePlayer.advanced.sampleRS.Agent --parallel > log_prior_baselineRandomPrior_agent_sampleRS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_baselineRandomPrior_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_baselineRandomPrior_to_greedyTreeSearch --path_to_updates=./zelda_experiments/updates --prior_folder=baselineRandomPrior_prior --agent=tracks.singlePlayer.simple.greedyTreeSearch.Agent --parallel > log_prior_baselineRandomPrior_agent_greedyTreeSearch.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_baselineRandomPrior_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_baselineRandomPrior_to_sampleonesteplookahead --path_to_updates=./zelda_experiments/updates --prior_folder=baselineRandomPrior_prior --agent=tracks.singlePlayer.simple.sampleonesteplookahead.Agent --parallel > log_prior_baselineRandomPrior_agent_sampleonesteplookahead.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_baselineRandomPrior_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_baselineRandomPrior_to_sampleRandom --path_to_updates=./zelda_experiments/updates --prior_folder=baselineRandomPrior_prior --agent=tracks.singlePlayer.simple.sampleRandom.Agent --parallel > log_prior_baselineRandomPrior_agent_sampleRandom.txt
# --------------------------------------------------------------------------------
# prior: olets
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_olets_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_olets_to_olets --path_to_updates=./zelda_experiments/updates --prior_folder=olets_prior --agent=tracks.singlePlayer.advanced.olets.Agent --parallel > log_prior_olets_agent_olets.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_olets_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_olets_to_sampleMCTS --path_to_updates=./zelda_experiments/updates --prior_folder=olets_prior --agent=tracks.singlePlayer.advanced.sampleMCTS.Agent --parallel > log_prior_olets_agent_sampleMCTS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_olets_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_olets_to_sampleRHEA --path_to_updates=./zelda_experiments/updates --prior_folder=olets_prior --agent=tracks.singlePlayer.advanced.sampleRHEA.Agent --parallel > log_prior_olets_agent_sampleRHEA.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_olets_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_olets_to_sampleRS --path_to_updates=./zelda_experiments/updates --prior_folder=olets_prior --agent=tracks.singlePlayer.advanced.sampleRS.Agent --parallel > log_prior_olets_agent_sampleRS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_olets_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_olets_to_greedyTreeSearch --path_to_updates=./zelda_experiments/updates --prior_folder=olets_prior --agent=tracks.singlePlayer.simple.greedyTreeSearch.Agent --parallel > log_prior_olets_agent_greedyTreeSearch.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_olets_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_olets_to_sampleonesteplookahead --path_to_updates=./zelda_experiments/updates --prior_folder=olets_prior --agent=tracks.singlePlayer.simple.sampleonesteplookahead.Agent --parallel > log_prior_olets_agent_sampleonesteplookahead.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_olets_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_olets_to_sampleRandom --path_to_updates=./zelda_experiments/updates --prior_folder=olets_prior --agent=tracks.singlePlayer.simple.sampleRandom.Agent --parallel > log_prior_olets_agent_sampleRandom.txt
# --------------------------------------------------------------------------------
# prior: sampleMCTS
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleMCTS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleMCTS_to_olets --path_to_updates=./zelda_experiments/updates --prior_folder=sampleMCTS_prior --agent=tracks.singlePlayer.advanced.olets.Agent --parallel > log_prior_sampleMCTS_agent_olets.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleMCTS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleMCTS_to_sampleMCTS --path_to_updates=./zelda_experiments/updates --prior_folder=sampleMCTS_prior --agent=tracks.singlePlayer.advanced.sampleMCTS.Agent --parallel > log_prior_sampleMCTS_agent_sampleMCTS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleMCTS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleMCTS_to_sampleRHEA --path_to_updates=./zelda_experiments/updates --prior_folder=sampleMCTS_prior --agent=tracks.singlePlayer.advanced.sampleRHEA.Agent --parallel > log_prior_sampleMCTS_agent_sampleRHEA.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleMCTS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleMCTS_to_sampleRS --path_to_updates=./zelda_experiments/updates --prior_folder=sampleMCTS_prior --agent=tracks.singlePlayer.advanced.sampleRS.Agent --parallel > log_prior_sampleMCTS_agent_sampleRS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleMCTS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleMCTS_to_greedyTreeSearch --path_to_updates=./zelda_experiments/updates --prior_folder=sampleMCTS_prior --agent=tracks.singlePlayer.simple.greedyTreeSearch.Agent --parallel > log_prior_sampleMCTS_agent_greedyTreeSearch.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleMCTS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleMCTS_to_sampleonesteplookahead --path_to_updates=./zelda_experiments/updates --prior_folder=sampleMCTS_prior --agent=tracks.singlePlayer.simple.sampleonesteplookahead.Agent --parallel > log_prior_sampleMCTS_agent_sampleonesteplookahead.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleMCTS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleMCTS_to_sampleRandom --path_to_updates=./zelda_experiments/updates --prior_folder=sampleMCTS_prior --agent=tracks.singlePlayer.simple.sampleRandom.Agent --parallel > log_prior_sampleMCTS_agent_sampleRandom.txt
# --------------------------------------------------------------------------------
# prior: sampleRHEA
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRHEA_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRHEA_to_olets --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRHEA_prior --agent=tracks.singlePlayer.advanced.olets.Agent --parallel > log_prior_sampleRHEA_agent_olets.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRHEA_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRHEA_to_sampleMCTS --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRHEA_prior --agent=tracks.singlePlayer.advanced.sampleMCTS.Agent --parallel > log_prior_sampleRHEA_agent_sampleMCTS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRHEA_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRHEA_to_sampleRHEA --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRHEA_prior --agent=tracks.singlePlayer.advanced.sampleRHEA.Agent --parallel > log_prior_sampleRHEA_agent_sampleRHEA.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRHEA_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRHEA_to_sampleRS --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRHEA_prior --agent=tracks.singlePlayer.advanced.sampleRS.Agent --parallel > log_prior_sampleRHEA_agent_sampleRS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRHEA_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRHEA_to_greedyTreeSearch --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRHEA_prior --agent=tracks.singlePlayer.simple.greedyTreeSearch.Agent --parallel > log_prior_sampleRHEA_agent_greedyTreeSearch.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRHEA_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRHEA_to_sampleonesteplookahead --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRHEA_prior --agent=tracks.singlePlayer.simple.sampleonesteplookahead.Agent --parallel > log_prior_sampleRHEA_agent_sampleonesteplookahead.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRHEA_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRHEA_to_sampleRandom --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRHEA_prior --agent=tracks.singlePlayer.simple.sampleRandom.Agent --parallel > log_prior_sampleRHEA_agent_sampleRandom.txt
# --------------------------------------------------------------------------------
# prior: sampleRS
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRS_to_olets --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRS_prior --agent=tracks.singlePlayer.advanced.olets.Agent --parallel > log_prior_sampleRS_agent_olets.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRS_to_sampleMCTS --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRS_prior --agent=tracks.singlePlayer.advanced.sampleMCTS.Agent --parallel > log_prior_sampleRS_agent_sampleMCTS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRS_to_sampleRHEA --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRS_prior --agent=tracks.singlePlayer.advanced.sampleRHEA.Agent --parallel > log_prior_sampleRS_agent_sampleRHEA.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRS_to_sampleRS --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRS_prior --agent=tracks.singlePlayer.advanced.sampleRS.Agent --parallel > log_prior_sampleRS_agent_sampleRS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRS_to_greedyTreeSearch --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRS_prior --agent=tracks.singlePlayer.simple.greedyTreeSearch.Agent --parallel > log_prior_sampleRS_agent_greedyTreeSearch.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRS_to_sampleonesteplookahead --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRS_prior --agent=tracks.singlePlayer.simple.sampleonesteplookahead.Agent --parallel > log_prior_sampleRS_agent_sampleonesteplookahead.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRS_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRS_to_sampleRandom --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRS_prior --agent=tracks.singlePlayer.simple.sampleRandom.Agent --parallel > log_prior_sampleRS_agent_sampleRandom.txt
# --------------------------------------------------------------------------------
# prior: greedyTreeSearch
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_greedyTreeSearch_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_greedyTreeSearch_to_olets --path_to_updates=./zelda_experiments/updates --prior_folder=greedyTreeSearch_prior --agent=tracks.singlePlayer.advanced.olets.Agent --parallel > log_prior_greedyTreeSearch_agent_olets.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_greedyTreeSearch_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_greedyTreeSearch_to_sampleMCTS --path_to_updates=./zelda_experiments/updates --prior_folder=greedyTreeSearch_prior --agent=tracks.singlePlayer.advanced.sampleMCTS.Agent --parallel > log_prior_greedyTreeSearch_agent_sampleMCTS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_greedyTreeSearch_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_greedyTreeSearch_to_sampleRHEA --path_to_updates=./zelda_experiments/updates --prior_folder=greedyTreeSearch_prior --agent=tracks.singlePlayer.advanced.sampleRHEA.Agent --parallel > log_prior_greedyTreeSearch_agent_sampleRHEA.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_greedyTreeSearch_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_greedyTreeSearch_to_sampleRS --path_to_updates=./zelda_experiments/updates --prior_folder=greedyTreeSearch_prior --agent=tracks.singlePlayer.advanced.sampleRS.Agent --parallel > log_prior_greedyTreeSearch_agent_sampleRS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_greedyTreeSearch_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_greedyTreeSearch_to_greedyTreeSearch --path_to_updates=./zelda_experiments/updates --prior_folder=greedyTreeSearch_prior --agent=tracks.singlePlayer.simple.greedyTreeSearch.Agent --parallel > log_prior_greedyTreeSearch_agent_greedyTreeSearch.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_greedyTreeSearch_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_greedyTreeSearch_to_sampleonesteplookahead --path_to_updates=./zelda_experiments/updates --prior_folder=greedyTreeSearch_prior --agent=tracks.singlePlayer.simple.sampleonesteplookahead.Agent --parallel > log_prior_greedyTreeSearch_agent_sampleonesteplookahead.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_greedyTreeSearch_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_greedyTreeSearch_to_sampleRandom --path_to_updates=./zelda_experiments/updates --prior_folder=greedyTreeSearch_prior --agent=tracks.singlePlayer.simple.sampleRandom.Agent --parallel > log_prior_greedyTreeSearch_agent_sampleRandom.txt
# --------------------------------------------------------------------------------
# prior: sampleonesteplookahead
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleonesteplookahead_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleonesteplookahead_to_olets --path_to_updates=./zelda_experiments/updates --prior_folder=sampleonesteplookahead_prior --agent=tracks.singlePlayer.advanced.olets.Agent --parallel > log_prior_sampleonesteplookahead_agent_olets.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleonesteplookahead_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleonesteplookahead_to_sampleMCTS --path_to_updates=./zelda_experiments/updates --prior_folder=sampleonesteplookahead_prior --agent=tracks.singlePlayer.advanced.sampleMCTS.Agent --parallel > log_prior_sampleonesteplookahead_agent_sampleMCTS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleonesteplookahead_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleonesteplookahead_to_sampleRHEA --path_to_updates=./zelda_experiments/updates --prior_folder=sampleonesteplookahead_prior --agent=tracks.singlePlayer.advanced.sampleRHEA.Agent --parallel > log_prior_sampleonesteplookahead_agent_sampleRHEA.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleonesteplookahead_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleonesteplookahead_to_sampleRS --path_to_updates=./zelda_experiments/updates --prior_folder=sampleonesteplookahead_prior --agent=tracks.singlePlayer.advanced.sampleRS.Agent --parallel > log_prior_sampleonesteplookahead_agent_sampleRS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleonesteplookahead_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleonesteplookahead_to_greedyTreeSearch --path_to_updates=./zelda_experiments/updates --prior_folder=sampleonesteplookahead_prior --agent=tracks.singlePlayer.simple.greedyTreeSearch.Agent --parallel > log_prior_sampleonesteplookahead_agent_greedyTreeSearch.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleonesteplookahead_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleonesteplookahead_to_sampleonesteplookahead --path_to_updates=./zelda_experiments/updates --prior_folder=sampleonesteplookahead_prior --agent=tracks.singlePlayer.simple.sampleonesteplookahead.Agent --parallel > log_prior_sampleonesteplookahead_agent_sampleonesteplookahead.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleonesteplookahead_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleonesteplookahead_to_sampleRandom --path_to_updates=./zelda_experiments/updates --prior_folder=sampleonesteplookahead_prior --agent=tracks.singlePlayer.simple.sampleRandom.Agent --parallel > log_prior_sampleonesteplookahead_agent_sampleRandom.txt
# --------------------------------------------------------------------------------
# prior: sampleRandom
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRandom_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRandom_to_olets --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRandom_prior --agent=tracks.singlePlayer.advanced.olets.Agent --parallel > log_prior_sampleRandom_agent_olets.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRandom_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRandom_to_sampleMCTS --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRandom_prior --agent=tracks.singlePlayer.advanced.sampleMCTS.Agent --parallel > log_prior_sampleRandom_agent_sampleMCTS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRandom_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRandom_to_sampleRHEA --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRandom_prior --agent=tracks.singlePlayer.advanced.sampleRHEA.Agent --parallel > log_prior_sampleRandom_agent_sampleRHEA.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRandom_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRandom_to_sampleRS --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRandom_prior --agent=tracks.singlePlayer.advanced.sampleRS.Agent --parallel > log_prior_sampleRandom_agent_sampleRS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRandom_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRandom_to_greedyTreeSearch --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRandom_prior --agent=tracks.singlePlayer.simple.greedyTreeSearch.Agent --parallel > log_prior_sampleRandom_agent_greedyTreeSearch.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRandom_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRandom_to_sampleonesteplookahead --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRandom_prior --agent=tracks.singlePlayer.simple.sampleonesteplookahead.Agent --parallel > log_prior_sampleRandom_agent_sampleonesteplookahead.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_sampleRandom_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_sampleRandom_to_sampleRandom --path_to_updates=./zelda_experiments/updates --prior_folder=sampleRandom_prior --agent=tracks.singlePlayer.simple.sampleRandom.Agent --parallel > log_prior_sampleRandom_agent_sampleRandom.txt
# --------------------------------------------------------------------------------
# prior: doNothing
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_doNothing_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_doNothing_to_olets --path_to_updates=./zelda_experiments/updates --prior_folder=doNothing_prior --agent=tracks.singlePlayer.advanced.olets.Agent --parallel > log_prior_doNothing_agent_olets.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_doNothing_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_doNothing_to_sampleMCTS --path_to_updates=./zelda_experiments/updates --prior_folder=doNothing_prior --agent=tracks.singlePlayer.advanced.sampleMCTS.Agent --parallel > log_prior_doNothing_agent_sampleMCTS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_doNothing_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_doNothing_to_sampleRHEA --path_to_updates=./zelda_experiments/updates --prior_folder=doNothing_prior --agent=tracks.singlePlayer.advanced.sampleRHEA.Agent --parallel > log_prior_doNothing_agent_sampleRHEA.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_doNothing_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_doNothing_to_sampleRS --path_to_updates=./zelda_experiments/updates --prior_folder=doNothing_prior --agent=tracks.singlePlayer.advanced.sampleRS.Agent --parallel > log_prior_doNothing_agent_sampleRS.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_doNothing_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_doNothing_to_greedyTreeSearch --path_to_updates=./zelda_experiments/updates --prior_folder=doNothing_prior --agent=tracks.singlePlayer.simple.greedyTreeSearch.Agent --parallel > log_prior_doNothing_agent_greedyTreeSearch.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_doNothing_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_doNothing_to_sampleonesteplookahead --path_to_updates=./zelda_experiments/updates --prior_folder=doNothing_prior --agent=tracks.singlePlayer.simple.sampleonesteplookahead.Agent --parallel > log_prior_doNothing_agent_sampleonesteplookahead.txt
python zelda_itae_experiment.py ./zelda_experiments/generations/generation_doNothing_2020_03_12_20h_10_gens_50_iter_100_init_40_roll_23_seed_00009.json --iterations=10 --rollouts=40 --processors=10 --performance_bound=0.75 --seed=53 --updates=20 --comment=2020_03_24_02h_42m_59s_all_pairs_incl_baseline_prior_doNothing_to_sampleRandom --path_to_updates=./zelda_experiments/updates --prior_folder=doNothing_prior --agent=tracks.singlePlayer.simple.sampleRandom.Agent --parallel > log_prior_doNothing_agent_sampleRandom.txt
