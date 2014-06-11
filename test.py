from model import Beacons,db,Locations
import learning_machine
import json
import pprint as pp

def test():
    myjson=' {"type":"client","method":"delete","data":{"device":"devicemac","beacon":"beacon id"}}'
    myjson2=' {"device":"device mac","type":"server","method":"delete","data":[{"id_beacon":"e2c56db5-dffb-48d2-b060-d0f5a71096e0035","distance":9.527709992845516}]}'
    data = json.loads(myjson2)
    if (data['type'] == 'client'):
        logic_on_client(data)
    elif (data['type'] == 'server'):
        logic_on_server(data)
    else:
        print "type has not been recognised"


def logic_on_client(data):
    device = data['data']['device']
    beacon = data['data']['beacon']
    print "device "+device+" beacon "+beacon
    if data['method'] =='post':
        db.session.merge(Locations(device, beacon))
        db.session.commit()
        return
    elif data['method'] =='delete':
        loc =Locations.query.get(device)

        if loc is None:
            print "no location with this characteristic"
            return
        print str(loc)
        db.session.delete(loc)
        db.session.commit()



def logic_on_server(data):
    if data['method'] == 'post':
        print "data "+str(data['data'])
        pp.pprint(data['data'])
        test_data = []
        info ={}
        for information in data['data']:
            info[information['id_beacon']]=information['distance']
        test_data.append(info)
        print type(test_data)
        pp.pprint(test_data)

        prediction = learning_machine.find_best_room(test_data)
        print str(prediction)
        db.session.merge(Locations(data['device'],prediction))
        db.session.commit()

    elif data['method'] == 'delete':
        loc =Locations.query.get(data['device'])
        if loc is None:
            print "no location with this characteristic"
            return
        db.session.delete(loc)
        db.session.commit()

test()
