from sklearn import datasets
from sklearn.feature_extraction import DictVectorizer
from sklearn.datasets import load_iris
from sklearn import svm
import numpy
import pprint




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
      test[beacon]=0
  return test

def load_data():
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
  return measurements



def find_best_room(test_data):
  print '-----Data to be feeded input------\n'
  vec = DictVectorizer()
  measurements = load_data()
  data = vec.fit_transform(measurements).toarray()
  pprint.pprint(measurements)
  pprint.pprint(data)
  print 'data feature '+str(vec.get_feature_names())

  print '-----Data to be feeded output------\n'
  target_ar = []
  for i in range(5):
    target_ar.append('Taverna')
  for i in range(4):
    target_ar.append('Bagno')
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
  print str(clf.predict(test))


mytest=[{'e2c56db5-dffb-48d2-b060-d0f5a71096e0039' : 9.23,'e2c56db5-dffb-48d2-b060-d0f5a71096e000':1.93}]
find_best_room(mytest)

