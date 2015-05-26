.PHONY: module test clean

module: ROOTFS

ROOTFS: ROOTFS/sails

ROOTFS/sails:
	mkdir -p ROOTFS/sails
	cd ROOTFS/sails && npm install sails
	cd ROOTFS/sails && ./node_modules/.bin/sails new example
test:
	python test.py
clean:
	rm -rf ROOTFS npm-debug.log
