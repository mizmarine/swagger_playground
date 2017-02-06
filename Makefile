

generate:
	swagger-codegen generate -l python -i swagger/api.yaml -o client -c config.json

run:
	python server.py
