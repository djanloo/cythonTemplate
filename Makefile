.PHONY: generate profile clear

generate:
	make clear
	@python -m dummy_pkg.setup

profile:
	make clear
	@python -m dummy_pkg.setup --profile

notrace:
	make clear
	@python -m dummy_pkg.setup --notrace

hardcore:
	make clear
	@python -m dummy_pkg.setup --hardcore

clear: 
	@rm -f dummy_pkg/*.c
	@rm -f dummy_pkg/*.so
	@rm -R -f dummy_pkg/build
	@rm -R -f dummy_pkg/__pycache__