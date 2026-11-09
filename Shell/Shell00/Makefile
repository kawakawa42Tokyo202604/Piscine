SCRIPT ?= ex04/midLS
SCRIPTS = ex05/git_commit.sh ex06/git_ignore.sh ex04/midLS ex08/clean

all: check

check:
	@set -e; for script in $(SCRIPTS); do sh -n "$$script"; done

run:
	sh "$(SCRIPT)"

.PHONY: all check run
