import pickle

with open('models', 'rb') as f_in:
    logistic_regression, decision_tree_classifier, svc_classifier, dv = pickle.load(f_in)


