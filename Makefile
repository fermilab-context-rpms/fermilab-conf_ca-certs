_default:
	@echo "make"
sources:
	@echo "make sources"
	tar cvf - fermilab-conf_ca-certs | gzip --best > fermilab-conf_ca-certs.tar.gz
srpm: sources
	rpmbuild -bs --define '_sourcedir .' --define '_srcrpmdir .' fermilab-conf_ca-certs.spec
