install:
	pip3 install fastapi "uvicorn[standard]"
run:
	uvicorn main:app --reload