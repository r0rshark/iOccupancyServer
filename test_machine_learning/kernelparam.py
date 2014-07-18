import numpy as np
import pylab as pl

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.cross_validation import StratifiedKFold
from sklearn.grid_search import GridSearchCV
from sklearn import preprocessing
from sklearn.feature_extraction import DictVectorizer

def define_kernel_param(X,Y):






  # It is usually a good idea to scale the data for SVM training.
  # We are cheating a bit in this example in scaling all of the data,
  # instead of fitting the transformation on the trainingset and
  # just applying it on the test set.

  # For an initial search, a logarithmic grid with basis
  # 10 is often helpful. Using a basis of 2, a finer
  # tuning can be achieved but at a much higher cost.

  C_range = 10. ** np.arange(-2, 9)
  gamma_range = 10. ** np.arange(-5, 4)

  param_grid = dict(gamma=gamma_range, C=C_range)

  grid = GridSearchCV(SVC(), param_grid=param_grid, cv=StratifiedKFold(y=Y, n_folds=5))

  grid.fit(X, Y)

  print("The best classifier is: ", grid.best_estimator_)

  # plot the scores of the grid
  # grid_scores_ contains parameter settings and scores
  score_dict = grid.grid_scores_

  # We extract just the scores
  scores = [x[1] for x in score_dict]
  scores = np.array(scores).reshape(len(C_range), len(gamma_range))

  # Make a nice figure
  pl.figure(figsize=(8, 6))
  pl.subplots_adjust(left=0.15, right=0.95, bottom=0.15, top=0.95)
  pl.imshow(scores, interpolation='nearest', cmap=pl.cm.spectral)
  pl.xlabel('gamma')
  pl.ylabel('C')
  pl.colorbar()
  pl.xticks(np.arange(len(gamma_range)), gamma_range, rotation=45)
  pl.yticks(np.arange(len(C_range)), C_range)
  pl.show()
