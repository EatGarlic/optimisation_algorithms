# optimal
#   mutation prob is 0.1
#   eletism is 0.04

from genetic import genetic_algorithm
import chromosome 
import time

def run_parameter_test(gen=50, pop=50, trials=10):
    # mutation_probs = [0.01, 0.04, 0.07, 0.1, 0.15, 0.2, 0.3]
    # eletism_probs = [0.01, 0.04, 0.07, 0.1, 0.15, 0.2, 0.3]
    mutation_probs = [0.09, 0.1, 0.11]
    eletism_probs = [0.03, 0.04, 0.05]

    time_results = {}
    cost_results = {}

    combinations = len(mutation_probs) * len(eletism_probs)
    total_trials = trials * combinations

    print(f"Running {combinations} combinations over {total_trials} total trials")

    trial_i = 0

    for m in mutation_probs:
        for e in eletism_probs:
            
            key = f'({m=}, {e=})'

            time_results[key] = 0
            cost_results[key] = 0

            for _ in range(trials):
                chromosome._cost_cache = {}
                start = time.time()
                chromo = genetic_algorithm(gen, pop, mutation_prob=m, eletism=e)
                end = time.time()

                time_results[key] += end - start
                cost_results[key] += chromo.getCost()

                print(f'trial {trial_i}/{total_trials} (est {((end - start) * (total_trials-trial_i)):.2f}s)', end='\r', flush=True)
                trial_i += 1

        

    print()

    print('Time results')
    for k, v in sorted(time_results.items(), key=lambda x: x[1]):
        print(k, v)

    print('Cost results')
    for k, v in sorted(cost_results.items(), key=lambda x: x[1]):
        print(k, v)



def run_tornament_test(gen=50, pop=50, trials=20):
    # mutation_probs = [0.01, 0.04, 0.07, 0.1, 0.15, 0.2, 0.3]    
    # eletism_probs = [0.01, 0.04, 0.07, 0.1, 0.15, 0.2, 0.3]

    torn_sizes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 30]

    time_results = {}
    cost_results = {}

    combinations = len(torn_sizes)
    total_trials = trials * combinations

    print(f"Running {combinations} combinations over {total_trials} total trials")

    trial_i = 0

    for t in torn_sizes:
        
        key = f'({t=})'

        time_results[key] = 0
        cost_results[key] = 0

        for _ in range(trials):
            chromosome._cost_cache = {}
            start = time.time()
            chromo = genetic_algorithm(gen, pop, tornament_size=t)
            end = time.time()

            time_results[key] += end - start
            cost_results[key] += chromo.getCost()

            print(f'trial {trial_i}/{total_trials} (est {((end - start) * (total_trials-trial_i)):.2f}s)', end='\r', flush=True)
            trial_i += 1

        

    print()

    print('Time results')
    for k, v in sorted(time_results.items(), key=lambda x: x[1]):
        print(k, v)

    print('Cost results')
    for k, v in sorted(cost_results.items(), key=lambda x: x[1]):
        print(k, v)




if __name__ == "__main__":
    run_tornament_test()



# Cost results
#     (m=0.1, e=0.04) 1.6
#     (m=0.15, e=0.2) 1.7999999999999998
#     (m=0.2, e=0.1) 1.9999999999999998
#     (m=0.2, e=0.2) 1.9999999999999998
#     (m=0.3, e=0.04) 1.9999999999999998
#     (m=0.3, e=0.1) 1.9999999999999998
#     (m=0.3, e=0.2) 2.0
#     (m=0.01, e=0.1) 2.1999999999999997
#     (m=0.2, e=0.3) 2.2
#     (m=0.3, e=0.3) 2.2000000000000006
#     (m=0.15, e=0.04) 2.4
#     (m=0.3, e=0.01) 2.4
#     (m=0.3, e=0.07) 2.4
#     (m=0.1, e=0.2) 2.4000000000000004
#     (m=0.2, e=0.07) 2.5999999999999996
#     (m=0.15, e=0.1) 2.6
#     (m=0.15, e=0.3) 2.6
#     (m=0.2, e=0.04) 2.6000000000000005
#     (m=0.3, e=0.15) 2.6000000000000005
#     (m=0.04, e=0.1) 2.8000000000000003
#     (m=0.2, e=0.01) 2.8000000000000003
#     (m=0.2, e=0.15) 2.8000000000000003
#     (m=0.15, e=0.07) 2.8000000000000007
#     (m=0.04, e=0.04) 3.0
#     (m=0.1, e=0.07) 3.0
#     (m=0.1, e=0.15) 3.0000000000000004
#     (m=0.1, e=0.1) 3.000000000000001
#     (m=0.07, e=0.1) 3.1999999999999997
#     (m=0.15, e=0.15) 3.2
#     (m=0.07, e=0.15) 3.2000000000000006
#     (m=0.01, e=0.01) 3.4000000000000004
#     (m=0.07, e=0.07) 3.4000000000000004
#     (m=0.07, e=0.3) 3.400000000000001
#     (m=0.07, e=0.04) 3.6
#     (m=0.07, e=0.2) 3.6000000000000005
#     (m=0.04, e=0.15) 3.8000000000000003
#     (m=0.15, e=0.01) 3.8000000000000003
#     (m=0.01, e=0.15) 3.8000000000000007
#     (m=0.04, e=0.2) 4.0
#     (m=0.04, e=0.3) 4.0
#     (m=0.01, e=0.2) 4.000000000000001
#     (m=0.1, e=0.01) 4.000000000000001
#     (m=0.01, e=0.07) 4.2
#     (m=0.01, e=0.3) 4.4
#     (m=0.07, e=0.01) 4.4
#     (m=0.04, e=0.07) 4.6
#     (m=0.01, e=0.04) 4.800000000000001
#     (m=0.1, e=0.3) 5.0
#     (m=0.04, e=0.01) 5.4

# Time results
#     (m=0.04, e=0.3) 4.413709878921509
#     (m=0.1, e=0.04) 4.442044019699097
#     (m=0.04, e=0.04) 4.473444938659668
#     (m=0.04, e=0.15) 4.495573997497559
#     (m=0.01, e=0.1) 4.504899024963379
#     (m=0.07, e=0.07) 4.539271831512451
#     (m=0.15, e=0.3) 4.557441711425781
#     (m=0.07, e=0.3) 4.564068078994751
#     (m=0.01, e=0.2) 4.589852809906006
#     (m=0.01, e=0.3) 4.590112924575806
#     (m=0.01, e=0.15) 4.593708753585815
#     (m=0.15, e=0.2) 4.599383592605591
#     (m=0.04, e=0.1) 4.611319541931152
#     (m=0.1, e=0.07) 4.622843503952026
#     (m=0.2, e=0.3) 4.63086724281311
#     (m=0.04, e=0.2) 4.63313102722168
#     (m=0.1, e=0.15) 4.642470598220825
#     (m=0.01, e=0.07) 4.644604444503784
#     (m=0.3, e=0.3) 4.64771032333374
#     (m=0.07, e=0.04) 4.652222394943237
#     (m=0.1, e=0.3) 4.655875205993652
#     (m=0.1, e=0.2) 4.656428337097168
#     (m=0.15, e=0.04) 4.656917333602905
#     (m=0.2, e=0.1) 4.683093547821045
#     (m=0.07, e=0.2) 4.684644460678101
#     (m=0.3, e=0.1) 4.716461181640625
#     (m=0.15, e=0.1) 4.725327730178833
#     (m=0.04, e=0.07) 4.730963945388794
#     (m=0.07, e=0.15) 4.73409366607666
#     (m=0.2, e=0.2) 4.735132217407227
#     (m=0.07, e=0.1) 4.735175848007202
#     (m=0.3, e=0.2) 4.735252380371094
#     (m=0.2, e=0.07) 4.743896245956421
#     (m=0.01, e=0.01) 4.749732255935669
#     (m=0.01, e=0.04) 4.758323907852173
#     (m=0.15, e=0.15) 4.759068489074707
#     (m=0.2, e=0.15) 4.76008152961731
#     (m=0.1, e=0.1) 4.7697930335998535
#     (m=0.07, e=0.01) 4.778625726699829
#     (m=0.04, e=0.01) 4.796576738357544
#     (m=0.15, e=0.07) 4.817795038223267
#     (m=0.3, e=0.07) 4.822688579559326
#     (m=0.1, e=0.01) 4.827716588973999
#     (m=0.3, e=0.15) 4.854803562164307
#     (m=0.3, e=0.04) 4.859299898147583
#     (m=0.2, e=0.04) 4.861930847167969
#     (m=0.15, e=0.01) 4.879607677459717
#     (m=0.2, e=0.01) 4.8967461585998535
#     (m=0.3, e=0.01) 4.946240186691284



# Cost results
#     (m=0.1, e=0.04) 1.2
#     (m=0.1, e=0.05) 1.6
#     (m=0.11, e=0.05) 1.9999999999999998
#     (m=0.09, e=0.03) 2.0
#     (m=0.09, e=0.04) 2.4
#     (m=0.09, e=0.05) 2.4
#     (m=0.1, e=0.03) 2.6
#     (m=0.11, e=0.04) 2.8000000000000007
#     (m=0.11, e=0.03) 3.0

# Time results
#     (m=0.1, e=0.04) 4.376724481582642
#     (m=0.1, e=0.05) 4.545417547225952
#     (m=0.09, e=0.03) 4.682878494262695
#     (m=0.1, e=0.03) 4.7020463943481445
#     (m=0.11, e=0.04) 4.713714838027954
#     (m=0.09, e=0.04) 4.731910467147827
#     (m=0.11, e=0.05) 4.758275032043457
#     (m=0.11, e=0.03) 4.783535480499268
#     (m=0.09, e=0.05) 4.930730104446411