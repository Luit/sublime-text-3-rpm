# Sublime Text 3 RPM builder container thing

To build an RPM for ST3, put the tarball in SOURCES, `docker build .` and `docker run` the result. 
Then you can pull the built RPMs from the container. Or you could use volumes. Your choice.
