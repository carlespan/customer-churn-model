#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

def plot_decision_boundary(estimator, X, y):
    
    '''
    plot_decision_boundary(estimator,X,y)
    
    Params:
        estimator: Estimator with "fit" method
        X: X_train, training data
        y: y_train, target
    
    '''
    np.random.seed(10)
    
    X = X.reset_index().drop('index', axis=1)
    y = y.reset_index().drop('index', axis=1)
    
    estimator.fit(X, y.iloc[:,0])
    X_color = X.sample(300)
    y_color = y.loc[X_color.index]
    x_axis, y_axis = np.arange(-3.5, 5, .05), np.arange(-3, 5, .05)
    xx, yy = np.meshgrid(x_axis, y_axis)
    xx_ravel = xx.ravel()
    yy_ravel = yy.ravel()
    X_grid = pd.DataFrame([xx_ravel, yy_ravel]).T
    y_grid_predictions = estimator.predict(X_grid)
    y_grid_predictions = y_grid_predictions.reshape(xx.shape)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.contourf(xx, yy, y_grid_predictions, cmap=plt.cm.autumn_r, alpha=.3)
    ax.scatter(X_color.iloc[:, 0], X_color.iloc[:, 1], c=y_color.values.ravel(), alpha=1)
    fields = X.columns
    ax.set(
        xlabel=fields[0],
        ylabel=fields[1],
        title=str(estimator))

