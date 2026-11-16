PROJECTS = BSQ Rush/Rush00 Rush/Rush01 Rush/Rush02

.PHONY: test
test:
	@set -eu; for project in $(PROJECTS); do \
		$(MAKE) --no-print-directory -C "$$project" test; \
	done
