.PHONY: all
all: build

.PHONY: build
build:
	docker build --rm -t ziyan/openrave .

.PHONY: push
push: build
	docker push ziyan/openrave
