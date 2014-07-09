
from model import db,TrainingResult
from sklearn import datasets, preprocessing,svm
from sklearn.feature_extraction import DictVectorizer
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
  load_data()
  if (len(measurements)>0 and len(target_ar)>1):
      calculate_model()
      #kp.define_kernel_param(measurements,target_ar,scaler)
      plot.plot_data(measurements,target_ar,scaler)



def calculate_model():
  print '-----Data to be feeded input------\n'

  data = inputDict.fit_transform(measurements).toarray()
  pprint.pprint(data)
  scaler.fit(data)
  data = scaler.transform(data)
  print "scaled data---------"

  pprint.pprint(data)
  print 'data feature '+str(inputDict.get_feature_names())

  print '-----Data to be feeded output------\n'

  target = numpy.array(target_ar)
  pprint.pprint(target)





  clf = svm.SVC(gamma=0.7, C=1.)
  clf.fit(data, target)
  print "saving model\n"

  global myclf
  myclf = pickle.dumps(clf)



def load_data():

  results = db.session.query(TrainingResult).all()
  for res in results:
    target_ar.append(res.outcome)
    rilevation = {}
    print "--------Training number "+ str(res.id) +"  outcome "+str(res.outcome )+"----------------"
    for data in res.data:
      print "adding "+str(data.id_beacon)+" at distance "+str(data.distance)
      rilevation[data.id_beacon] = data.distance
    measurements.append(rilevation)



if __name__ == "__main__":
    main()




