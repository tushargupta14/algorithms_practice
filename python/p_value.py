# hypothesis testing and calculating p-value
# https://www.interviewbit.com/problems/hypothesis-testing-in-salary-of-data-scientists/

import numpy as np
from scipy.stats import t

def solve(salary_lst, mu):
    
    new = np.mean(salary_lst)
    
    s = np.std(salary_lst)
    
    t_score = (new - mu) / (s / np.sqrt(len(salary_lst)))
    df = len(salary_lst) - 1
    # 2 tailed test
    p_value = t.sf(np.abs(t_score), df) * 2
    
    return True if p_value < 0.05 else False