# competitive-programming-notebook
#
# Run `make` on its own for the command list.
#
# Two problem shapes:
#   stdin/stdout (beecrowd, codeforces, hackerrank) - java/Main.java has a main,
#     so `make run` and `make test` work directly.
#   class Solution (leetcode) - no main, nothing to execute. Use
#     `make syntax`, or add a Main.java harness and `make run` finds it.

JAVAC ?= javac
JAVA  ?= java
OUT   := /tmp/cp-build

# Bigger stack for deep recursion, matching Template.java.
JAVAFLAGS ?= -Xss256m

N ?= 1000
L ?= java

.DEFAULT_GOAL := help

help:
	@echo ''
	@echo '  make new P=leetcode ID=0146 SLUG=lru-cache L=python'
	@echo '                              scaffold a problem/language (L defaults to java)'
	@echo ''
	@echo '  make syntax DIR=<dir>       compile one problem'
	@echo '  make run    DIR=<dir>       compile and run it'
	@echo '  make run    DIR=<dir> IN=in.txt'
	@echo '                              ...feeding it one input file'
	@echo '  make test   DIR=<dir>       run every in*.txt, diff vs out*.txt'
	@echo '  make stress DIR=<dir> [N=1000]'
	@echo '                              Brute.java vs your solution on random input'
	@echo ''
	@echo '  make scaffold-test          verify all language scaffolds'
	@echo ''
	@echo '  make check                  compile every problem in the repo'
	@echo ''

need-dir:
	@test -n "$(DIR)" || { echo "usage: make $(MAKECMDGOALS) DIR=<problem-dir>"; exit 1; }
	@test -d "$(DIR)" || { echo "no such directory: $(DIR)"; exit 1; }

new:
	@test -n "$(P)"    || { echo 'usage: make new P=<platform> ID=<id> SLUG=<slug>'; exit 1; }
	@test -n "$(SLUG)" || { echo 'usage: make new P=<platform> ID=<id> SLUG=<slug>'; exit 1; }
	@tools/new.sh "$(P)" "$(ID)" "$(SLUG)" "$(L)"

scaffold-test:
	@tools/test-new.sh

syntax: need-dir
	@mkdir -p $(OUT)
	$(JAVAC) -d $(OUT) $(DIR)/java/*.java

# Runs whichever class in the directory declares a main.
run: syntax
	@main=$$(grep -lE 'static void main' $(DIR)/java/*.java | head -1); \
	 if [ -z "$$main" ]; then \
	   echo "no main in $(DIR) - leetcode problems have none, use 'make syntax'"; exit 1; \
	 fi; \
	 cls=$$(basename $$main .java); \
	 if [ -n "$(IN)" ]; then \
	   $(JAVA) $(JAVAFLAGS) -cp $(OUT) $$cls < $(DIR)/$(IN); \
	 else \
	   $(JAVA) $(JAVAFLAGS) -cp $(OUT) $$cls; \
	 fi

test: need-dir
	@tools/run.sh "$(DIR)"

stress: need-dir
	@tools/stress.sh "$(DIR)" "$(N)"

check:
	@mkdir -p $(OUT)
	@fail=0; \
	 for d in $$(find leetcode beecrowd hackerrank codeforces -mindepth 2 -maxdepth 2 -type d | sort); do \
	   ls $$d/java/*.java >/dev/null 2>&1 || continue; \
	   $(JAVAC) -nowarn -d $(OUT)/$$(basename $$(dirname $$d)) $$d/java/*.java 2>/tmp/cp-javac.err || { \
	     echo "FAIL: $$d"; head -3 /tmp/cp-javac.err; fail=1; }; \
	 done; \
	 if [ $$fail -eq 0 ]; then echo "all problems compile"; else exit 1; fi

.PHONY: help need-dir new scaffold-test syntax run test stress check
