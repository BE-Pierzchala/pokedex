create_env:
	conda env create -f environment.yml
export_env:
	conda env export > environment.yml
run:
	python Code/main.py
gui:
	python Gui.py