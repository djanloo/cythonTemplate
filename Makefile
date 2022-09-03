.PHONY: generate profile clear

generate:
	@python -m dummy_pkg.setup

profile:
	@python -m dummy_pkg.setup --profile

notrace:
	@python -m dummy_pkg.setup --notrace

hardcore:
	@python -m dummy_pkg.setup --hardcore

clear: 
	@rm -f dummy_pkg/*.c
	@rm -f dummy_pkg/*.so
	@rm -R -f dummy_pkg/build
	@rm -R -f dummy_pkg/__pycache__