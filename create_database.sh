#!/usr/bin/env python
import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/.."))
from iBeaconOccupancy.model.tests import *
from iBeaconOccupancy.model.beacons import *
from iBeaconOccupancy.model.training import *

db.create_all()
