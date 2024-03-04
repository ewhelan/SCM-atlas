#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import os

from collections import OrderedDict

import atlas1d
from atlas1d.Model import Model
from atlas1d.Simulation import Simulation


dir_atlas = '__DIR_RUN__/MyAtlas/'
name_atlas = 'TEST'

cases = ['ARMCU', 'RICO', 'SANDU']
subcases = OrderedDict([
        ('RICO' , ['SHORT',]),
        ('ARMCU', ['REF',]),
        ('FIRE',  ['REF',]),
        ('SANDU', ['REF']),
        ])

model = Model(name='arp632.gabls_CMIP6',binVersion='arp632.gabls',levgrid='L91',tstep=300)

simulations = OrderedDict()
for case in cases:
    simulations[case] = OrderedDict()
    for subcase in subcases[case]:
        simulations[case][subcase] = [
                Simulation(name='CMIP6',model=model,case=case,subcase=subcase,line='r',
                    ncfile=os.path.join('__DIR_ATLAS__','test/{0}_{1}_arp632.galbs_CMIP6_L91_300s_klevel.nc'.format(case,subcase))),
                ]
