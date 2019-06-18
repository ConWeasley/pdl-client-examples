#! /usr/bin/env python


import os
import sys
import datetime

# add ProductClient directory to path
sys.path.append(os.path.join('lib', 'ProductClient'))

# import Product, which parses ExternalNotificationListener arguments
from ExampleListener import Product



if __name__ == '__main__':
	# write data to a log file
	logfile = os.path.join('data', os.path.basename(sys.argv[0]) + '.log')
	f = open(logfile, 'a+')
	# current time
	print('# %s' % datetime.datetime.now().isoformat(), file=f)
	# command line arguments
	print('# arguments = ' + ' '.join(sys.argv), file=f)
	# parse command line arguments
	product = Product.getProduct()
	# output parsed product
	product.display(f)
	# check if moment tensor is Mww
	props = product.properties
	if 'derived-magnitude-type' in props and props['derived-magnitude-type'] == 'Mww':
		print('wphase', file=f)
		# now read quakeml
		quakeml = product.getContentPath('quakeml.xml')
		with open(quakeml) as q:
			data = q.read()
			print('quakeml content', file=f)
			print(data, file=f)
	else:
		print('not wphase', file=f)
	print('\n', file=f)
