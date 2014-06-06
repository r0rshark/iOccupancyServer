from sklearn import datasets, preprocessing
from sklearn.feature_extraction import DictVectorizer
from sklearn.datasets import load_iris
from model import db,TrainingResult
from sklearn import svm
import numpy
import pprint
import pickle
import plot

measurements =[]
target_ar = []
inputDict = DictVectorizer(sparse=True)
scaler = preprocessing.StandardScaler()
myclf = None

def normalize_test(test,features):
  print '-----deleting key in test which are not present in training data------'
  for beacon in test.keys():

    if beacon not in features:
      print beacon
      test.pop(beacon)
  print '-----making  key not present in test  but in training data equals 0------'
  for beacon in features:

    if test.get(beacon) is  None:
      print beacon
      test[beacon]=99
  return test

def calculate_model():
  print '-----Data to be feeded input------\n'

  data = inputDict.fit_transform(measurements).toarray()
  scaler.fit(data)
  data = scaler.transform(data)
  print "scaled data---------"

  pprint.pprint(data)
  print 'data feature '+str(inputDict.get_feature_names())

  print '-----Data to be feeded output------\n'

  target = numpy.array(target_ar)
  pprint.pprint(target)





  clf = svm.SVC(gamma=0.001, C=100.)
  clf.fit(data, target)
  print "saving model\n"

  global myclf
  myclf = pickle.dumps(clf)






def find_best_room(test_data):

  print "-----Test Data in input------\n"
  pprint.pprint(test_data)
  print "-----Test Data to be predicted normalized------\n"
  test_vec = DictVectorizer()
  test_data[0] = normalize_test(test_data[0],inputDict.get_feature_names())
  pprint.pprint(test_data[0])



  print "-----Test data  scaled and standardized------\n"
  test = test_vec.fit_transform(test_data).toarray()
  test = scaler.transform(test)

  pprint.pprint(test)

  clf = pickle.loads(myclf)
  prediction = clf.predict(test)
  print '##########################Result######################\n'
  print str(prediction)+"\n\n"
  return prediction






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


  calculate_model()
  plot.plot_data(measurements,target_ar)


  '''
  measurements =[{'e2c56db5-dffb-48d2-b060-d0f5a71096e0035' : 0.23,'e2c56db5-dffb-48d2-b060-d0f5a71096e000':4.23,'e2c56db5-dffb-48d2-b060-d0f5a71096e029':4.23},
                            {'e2c56db5-dffb-48d2-b060-d0f5a71096e0035' : 1.23,'e2c56db5-dffb-48d2-b060-d0f5a71096e000':4.53,'e2c56db5-dffb-48d2-b060-d0f5a71096e021':5.23},
                           {'e2c56db5-dffb-48d2-b060-d0f5a71096e0035' : 0.73,'e2c56db5-dffb-48d2-b060-d0f5a71096e000':4.33},
                           {'e2c56db5-dffb-48d2-b060-d0f5a71096e0036' : 0.93,'e2c56db5-dffb-48d2-b060-d0f5a71096e000':3.23},
                           {'e2c56db5-dffb-48d2-b060-d0f5a71096e0036' : 8.23,'e2c56db5-dffb-48d2-b060-d0f5a71096e000':1.93},

                           {'e2c56db5-dffb-48d2-b060-d0f5a71096e0035' : 5.23,'e2c56db5-dffb-48d2-b060-d0f5a71096e000':0.93},
                           {'e2c56db5-dffb-48d2-b060-d0f5a71096e0035' : 5.53,'e2c56db5-dffb-48d2-b060-d0f5a71096e000':0.53},
                           {'e2c56db5-dffb-48d2-b060-d0f5a71096e0035' : 4.13,'e2c56db5-dffb-48d2-b060-d0f5a71096e000':0.93},
                           {'e2c56db5-dffb-48d2-b060-d0f5a71096e0037' : 4.23,'e2c56db5-dffb-48d2-b060-d0f5a71096e000':1.93},
  ]
  '''





