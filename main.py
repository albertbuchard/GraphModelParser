import numpy as np

from src.graph_model_parser import GraphModelParser

if __name__ == '__main__':
    # Set seed for reproducibility
    np.random.seed(42)

    model_description = ''' 
            b_{t} = b_{t-1} + 2*b_{t-2} + a_0
            c_{t} = c_{t-1} + normal(1, 2)
            '''
    initial_values = {'a_0': 0, 'b_0': 0, 'b_1': 1, 'c_0': 0}
    model = GraphModelParser(model_description, initial_values)
    print(model(t=20, whole_history=True))