from sklearn import datasets
from sklearn.feature_extraction import DictVectorizer
from sklearn.datasets import load_iris
from model import db,TrainingResult
from sklearn import svm
import numpy
import pprint

measurements =[]
target_ar = []
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
      test[beacon]=9999
  return test





def find_best_room(test_data):
  print '-----Data to be feeded input------\n'
  vec = DictVectorizer()
  data = vec.fit_transform(measurements).toarray()

  pprint.pprint(data)
  print 'data feature '+str(vec.get_feature_names())

  print '-----Data to be feeded output------\n'

  target = numpy.array(target_ar)
  pprint.pprint(target)

  print "-----Test Data to be predicted normalized------\n"
  test_vec = DictVectorizer()
  test_data[0] = normalize_test(test_data[0],vec.get_feature_names())

  print "-----Test data after normalized------\n"
  test = test_vec.fit_transform(test_data).toarray()
  pprint.pprint(test_data)
  pprint.pprint(test)

  clf = svm.SVC(gamma=0.001, C=100.)
  clf.fit(data, target)
  print '-------Result----------'
  clf = svm.SVC(gamma=0.001, C=100.)
  clf.fit(data, target)
  prediction = clf.predict(test)
  print str(prediction)
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





