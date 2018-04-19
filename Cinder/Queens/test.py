#!/usr/bin/env python

from cinder import objects
objects.register_all()

from oslo_config import cfg
from oslo_config import types
from cinder.volume import configuration
from cinder import context

from cinder.volume.drivers.huawei.huawei_driver import HuaweiFCDriver

def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))

c=configuration.DefaultGroupConfiguration()
d = HuaweiFCDriver(configuration=c)

d.do_setup(None)

# Here you can write your tests
