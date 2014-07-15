
from pprint import pprint as pp
import numpy as np
import pylab as pl
from sklearn import cross_validation
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
from sklearn.feature_extraction import DictVectorizer
from sklearn import svm, datasets
from sklearn.metrics import *
def plot_data(X,Y):
  # import some data to play with

  pp(Y)

  h = .02  # step size in the mesh

  # we create an instance of SVM and fit out data. We do not scale our
  # data since we want to plot the support vectors
  C = 1.  # SVM regularization parameter
  #C = 100.  # SVM regularization parameter
  svc = svm.SVC(kernel='linear', C=C).fit(X, Y)
  rbf_svc = svm.SVC(gamma=0.7, C=C).fit(X,Y)

  poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, Y)
  lin_svc = svm.LinearSVC(C=C).fit(X, Y)

  # create a mesh to plot in
  x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
  y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
  xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                       np.arange(y_min, y_max, h))

  # title for the plots
  titles = ['SVC with linear kernel',
            'SVC with RBF kernel',
            'SVC with polynomial (degree 3) kernel',
            'LinearSVC (linear kernel)']


  for i, clf in enumerate((svc, rbf_svc, poly_svc, lin_svc)):
      # Plot the decision boundary. For that, we will assign a color to each
      # point in the mesh [x_min, m_max]x[y_min, y_max].
      pl.subplot(2, 2, i + 1)
      Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

      # Put the result into a color plot
      Z = Z.reshape(xx.shape)
      pl.contourf(xx, yy, Z, cmap=pl.cm.Paired)
      pl.axis('off')

      # Plot also the training points
      pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)

      pl.title(titles[i])

  pl.show()

def print_confusion_matrix(x_set,y_set):
  lenght = len(y_set)/15
  print "lenght "+str(lenght)

  x_train= x_set[0:lenght]
  print "x_train lenght "+str(len(x_train))
  pp(x_train)



  y_train = y_set[0:lenght]
  print "y_train lenght "+str(len(y_train))
  pp(y_train)

  print "------test------------ "

  x_test= x_set[lenght:]
  print "x_test lenght ="+str(len(x_test))
  pp(x_test)

  y_test = y_set[lenght:]
  print "y_test ="+str(y_test)+"lenght "+str(len(y_test))


  print "--------prediction------------"
  rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=1.0).fit(x_train, y_train)
  y_pred = rbf_svc.predict(x_test)
  print "y_pred "+str(y_pred)
  print "y_test"+str(y_test)

  scores = cross_validation.cross_val_score(
  rbf_svc, x_set, y_set, cv=25)

  print "score cross validation "+str(scores)

  cm = confusion_matrix(y_test, y_pred)
  print "\n\n\n"
  print "---------Overall information ---------\n"

  print "number of samples:             561"
  print "correct classified samples:    529"
  print "incorrect classified samples:  32"
  print "accuracy score:                " +str(accuracy_score(y_test, y_pred))
  print "min absolute error score:      "+str(mean_absolute_error(y_test, y_pred))

  print "min squared error              "+str(mean_squared_error(y_test, y_pred))

  print "\n\n"
  print "---------Classification report by class---------\n"

  print(classification_report(y_test, y_pred))

  print "\n\n"
  print "---------Confusion matrix---------\n"

  print(cm)

  # Show confusion matrix in a separate window

  pl.matshow(cm)
  pl.title('Confusion matrix')
  pl.colorbar()
  pl.ylabel('True label')
  pl.xlabel('Predicted label')
  pl.show()


