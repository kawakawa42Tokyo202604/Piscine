SCRIPT ?= ex02/find_sh.sh
SCRIPTS = ex01/print_groups.sh ex02/find_sh.sh ex03/count_files.sh ex04/MAC.sh ex06/skip.sh

all: check

check:
	@set -e; for script in $(SCRIPTS); do sh -n "$$script"; done

run:
	sh "$(SCRIPT)"

.PHONY: all check run
