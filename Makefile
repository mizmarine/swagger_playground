

generate:
	swagger-codegen generate -l python -i swagger/api.yaml -o client

run:
	python server.py
