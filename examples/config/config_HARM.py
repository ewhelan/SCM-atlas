#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import os

from collections import OrderedDict

import atlas1d
from atlas1d.Model import Model
from atlas1d.Simulation import Simulation

dir_musc = '/home/ewhelan/EMS_test_new/ems_test'

dir_atlas = '/home/ewhelan/Atlas1DU/1.2.1'
name_atlas = 'HARM'


##atlas_ARMCU.py
#atlas_ASTEX.py
### atlas_AYOTTE.py
### atlas_AYOTTE_00SC.py
### atlas_AYOTTE_00WC.py
### atlas_AYOTTE_03SC.py
### atlas_AYOTTE_05SC.py
### atlas_AYOTTE_05WC.py
### atlas_AYOTTE_24F.py
###atlas_AYOTTE_24SC.py
#atlas_BOMEX.py
##atlas_FIRE.py
#atlas_GABLS1.py
#atlas_IHOP.py
#atlas_RICO.py
#atlas_SANDU.py
#atlas_SANDU_FAST.py
#atlas_SANDU_REF.py
#atlas_SANDU_SLOW.py



cases = ['ARMCU','RICO','SANDU']
subcases = OrderedDict([
        ('RICO' , ['SHORT',]),
        ('ARMCU', ['REF',]),
        ('SANDU', ['REF','SLOW','FAST']),
        ])

cases = ['ARMCU','RICO','FIRE']
subcases = OrderedDict([
        ('FIRE' , ['REF',]),
        ('RICO' , ['SHORT',]),
        ('ARMCU', ['REF',]),
        ('SANDU', ['REF']),
        ])

model = Model(name='Harmonie',binVersion='dev46h1',levgrid='L60',tstep=50)
# /home/ewhelan/EMS_test_new/ems_test/simulations/46t1/46h1_HARMAROME_DEV
simulations = OrderedDict()
for case in cases:
    simulations[case] = OrderedDict()
    for subcase in subcases[case]:
        simulations[case][subcase] = [
                Simulation(name='HARM',model=model,case=case,subcase=subcase,line='r',
                    ncfile=os.path.join(dir_musc,'simulations/46t1/46h1_HARMAROME_DEV',case,subcase,'Output/netcdf/Out_klevel.nc')),
                        ]
