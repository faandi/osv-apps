from osv.modules import api

api.require('node')

default = api.run(cmdline="--cwd=/sails/ /libnode.so ./example/app.js")
