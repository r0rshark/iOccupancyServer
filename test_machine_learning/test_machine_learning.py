#!/usr/bin/env python
import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))


from  iBeaconOccupancy.model.training import *
from sklearn import datasets, preprocessing,svm
from sklearn.feature_extraction import DictVectorizer
import optparse
import pickle
import pprint
import plot
import kernelparam as kp
import numpy




measurements =[]
target_ar = []
inputDict = DictVectorizer(sparse=True)
scaler = preprocessing.StandardScaler()
myclf = None

def main():
  X = []
  Y =[]
  p = optparse.OptionParser(description='Show different info for parameter tuning',
                            prog='SVMTuning',
                            version='0.1',
                            usage='%prog [options] at least one parameter')
  p.add_option('-p', '--plot', action ='store_true', help='plot the data in a graphic')
  p.add_option('-c', '--confusion', action ='store_true', help='show confusion matrix')
  p.add_option('-t', '--tuning', action ='store_true', help='try to find the best parameter for the ')

  options, arguments = p.parse_args()
  p.print_help()

  load_data()

  if (len(measurements)>0 and len(target_ar)>1):
    calculate_model()
    data = inputDict.fit_transform(measurements).toarray()
    scaled_data = scaler.transform(data)
    X = scaled_data  # we only take the first two features. We could
                        # avoid this ugly slicing by using a two-dim dataset
    le = preprocessing.LabelEncoder()
    le.fit(target_ar)
    target = le.transform(target_ar)

    Y = numpy.array(target)
    #kp.define_kernel_param(measurements,target_ar,scaler)
    if options.plot:
      print "plot"
      plot.plot_data(X,Y)
    if options.confusion:
      print "confusion"
      plot.print_confusion_matrix(X,Y)
    if options.tuning:
      kp.define_kernel_param(X,Y)







def calculate_model():

  data = inputDict.fit_transform(measurements).toarray()
  scaler.fit(data)
  data = scaler.transform(data)

  target = numpy.array(target_ar)

  clf = svm.SVC(gamma=0.7, C=1.)
  clf.fit(data, target)


  global myclf
  myclf = pickle.dumps(clf)



def load_data():

  results = db.session.query(TrainingResult).all()
  for res in results:
    target_ar.append(res.outcome)
    rilevation = {}
    for data in res.data:
      rilevation[data.id_beacon] = data.distance
    measurements.append(rilevation)



if __name__ == "__main__":
    main()




