import numpy as np
def calculate(list):
    if len(list)<9:
        raise ValueError("List must contain nine numbers.")
        
    npa = np.array(list)
    npa = npa.reshape(3,3)
    
    mean_val = np.mean(npa).tolist()
    mean_val1 = np.mean(npa, axis=0).tolist()
    mean_val2 = np.mean(npa, axis=1).tolist()
    mean_vals = [mean_val1, mean_val2, mean_val]

    var_val = np.var(npa)
    var_val1 = np.var(npa, axis=0).tolist()
    var_val2 = np.var(npa, axis=1).tolist()
    var_vals = [var_val1, var_val2, var_val]

    std_val = np.std(npa)
    std_val1 = np.std(npa, axis=0).tolist()
    std_val2 = np.std(npa, axis=1).tolist()
    std_vals = [std_val1, std_val2, std_val]

    max_val = np.max(npa)
    max_val1 = np.max(npa, axis=0).tolist()
    max_val2 = np.max(npa, axis=1).tolist()
    max_vals = [max_val1, max_val2, max_val]

    min_val = np.min(npa)
    min_val1 = np.min(npa, axis=0).tolist()
    min_val2 = np.min(npa, axis=1).tolist()
    min_vals = [min_val1, min_val2, min_val]

    sum_val = np.sum(npa)
    sum_val1 = np.sum(npa, axis=0).tolist()
    sum_val2 = np.sum(npa, axis=1).tolist()
    sum_vals = [sum_val1, sum_val2, sum_val]

    calculations = {'mean': mean_vals, 
        'variance': var_vals, 
        'standard deviation': std_vals,
        'max': max_vals,
        'min': min_vals,
        'sum': sum_vals
         }

    return calculations