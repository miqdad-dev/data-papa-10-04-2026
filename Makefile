
.PHONY: test run fmt
test:
	python -m pytest -q || true
run:
	@echo "Define run command for this project"
fmt:
	@echo "Add formatter (prettier/black/clang-format) if desired"
