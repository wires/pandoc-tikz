#/bin/bash
TAG=testing-pandoc-tikz
PWD=$(pwd)
docker build -t $TAG .
docker run -i -v $PWD:/test -t $TAG /bin/bash -c "cd test && ./run.sh"
