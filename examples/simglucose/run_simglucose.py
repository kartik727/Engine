from seldonian.seldonian_algorithm import SeldonianAlgorithm
from seldonian.utils.io_utils import load_pickle

if __name__ == '__main__':
    # load specfile
    specfile = './spec.pkl'
    spec = load_pickle(specfile)
    spec.optimization_hyperparams['num_iters']=30
    spec.optimization_hyperparams['alpha_theta']=0.01
    spec.optimization_hyperparams['alpha_lamb']=0.01
    # Run Seldonian algorithm 
    SA = SeldonianAlgorithm(spec)
    passed_safety,solution = SA.run(debug=True,write_cs_logfile=True)
    if passed_safety:
        print("Passed safety test!")
        print("The solution found is:")
        print(solution)
    else:
        print("Failed safety test")
        print("No Solution Found")
    # print(SA.evaluate_primary_objective(branch='candidate_selection',theta=solution))
    # print(SA.evaluate_primary_objective(branch='safety_test',theta=solution))
