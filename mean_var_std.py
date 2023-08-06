import numpy as np

def calculate(list):
    if len(list) == 9:
        list = np.array(list).reshape(3,3)
        calculator = {
        'mean': [np.mean(list,axis=0).tolist(), np.mean(list,axis=1).tolist(), np.mean(list)], 
        'variance': [np.var(list,axis=0).tolist(), np.var(list,axis=1).tolist(), np.var(list)],
        'standard deviation': [np.std(list,axis=0).tolist(), np.std(list,axis=1).tolist(), np.std(list)],
        'max': [np.max(list,axis=0).tolist(), np.max(list,axis=1).tolist(), np.max(list)],
        'min': [np.min(list,axis=0).tolist(), np.min(list,axis=1).tolist(), np.min(list)],
        'sum': [np.sum(list,axis=0).tolist(), np.sum(list,axis=1).tolist(), np.sum(list)]
        }
        print(calculator)
    else:
        raise ValueError('List must contain 9 numbers.')
    return calculator

calculate([0,1,2,3,4,5,6,7,8,9])
