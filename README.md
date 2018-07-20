Indexer Listener Example
==============================

Run a python ExternalIndexerListener configured to process indexer changes.  See https://usgs.github.io/pdl/ for more information.


Dependencies
------------

- java
- python 2.7
- python dateutil ( `pip install python-dateutil` )
- (optional) bash

Getting Started
---------------

- Run `./init.sh start`

  > If you do not have bash, or do not want to run PDL as a background process, you can run this command (from the project directory): `java -jar lib/ProductClient/ProductClient.jar --configFile=config.ini --receive`

- Watch the log files created in the `data` directory, in particular `data/IndexerListener.py.log` that is created once the first product is processed.

- You can also inspect the PDL log files to see the commands used to call the configured `IndexerListener.py` script.  You can edit `config.ini` to call any other executable instead.