import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError ('List must contain nine numbers')
    
    conv_list = np.array(list).reshape(3, 3)

    mean_axis1 = conv_list.mean(axis= 0).tolist()
    mean_axis2 = conv_list.mean(axis= 1).tolist()
    mean_flattened = conv_list.mean().tolist()

    var_axis1 = conv_list.var(axis= 0).tolist()
    var_axis2 = conv_list.var(axis= 1).tolist()
    var_flattened = conv_list.var().tolist()

    std_axis1 = conv_list.std(axis= 0).tolist()
    std_axis2 = conv_list.std(axis= 1).tolist()
    std_flattened = conv_list.std().tolist()

    max_axis1 = conv_list.max(axis= 0).tolist()
    max_axis2 = conv_list.max(axis= 1).tolist()
    max_flattened = conv_list.max().tolist()

    min_axis1 = conv_list.min(axis= 0).tolist()
    min_axis2 = conv_list.min(axis= 1).tolist()
    min_flattened = conv_list.min().tolist()

    sum_axis1 = conv_list.sum(axis= 0).tolist()
    sum_axis2 = conv_list.sum(axis= 1).tolist()
    sum_flattened = conv_list.sum().tolist()

    return{
        'mean': [mean_axis1, mean_axis2, mean_flattened],
        'variance': [var_axis1, var_axis2, var_flattened],
        'standard deviation': [std_axis1, std_axis2, std_flattened],
        'max': [max_axis1, max_axis2, max_flattened],
        'min': [min_axis1, min_axis2, min_flattened],
        'sum': [sum_axis1, sum_axis2, sum_flattened]
    }