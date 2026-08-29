# Build and run any problem in the tree.
#
#   make run    DIR=beecrowd/1000-hello-world
#   make run    DIR=... IN=in.txt          # feed a test file
#   make check                             # compile every problem
#   make syntax DIR=leetcode/0015-3sum     # compile one problem only
#
# Two problem shapes:
#   stdin/stdout (beecrowd, codeforces, hackerrank) - Main.java or
#     Solution.java has a main, so `make run` works directly.
#   class Solution (leetcode) - no main, nothing to run. Use `make syntax`,
#     or add a Main.java harness in the directory and `make run` picks it up.

JAVAC ?= javac
JAVA  ?= java
OUT   := /tmp/cp-build

# Bigger stack for deep recursion, matching the template.
JAVAFLAGS ?= -Xss256m

need-dir:
	@test -n "$(DIR)" || { echo "usage: make $(MAKECMDGOALS) DIR=<problem-dir>"; exit 1; }
	@test -d "$(DIR)" || { echo "no such directory: $(DIR)"; exit 1; }

syntax: need-dir
	@mkdir -p $(OUT)
	$(JAVAC) -d $(OUT) $(DIR)/*.java

# Runs whichever class in the directory declares a main.
run: syntax
	@main=$$(grep -lE 'static void main' $(DIR)/*.java | head -1); \
	 if [ -z "$$main" ]; then \
	   echo "no main in $(DIR) - leetcode problems have none, use 'make syntax'"; exit 1; \
	 fi; \
	 cls=$$(basename $$main .java); \
	 if [ -n "$(IN)" ]; then \
	   $(JAVA) $(JAVAFLAGS) -cp $(OUT) $$cls < $(DIR)/$(IN); \
	 else \
	   $(JAVA) $(JAVAFLAGS) -cp $(OUT) $$cls; \
	 fi

check:
	@mkdir -p $(OUT)
	@fail=0; \
	 for d in $$(find leetcode beecrowd hackerrank codeforces -mindepth 1 -maxdepth 1 -type d | sort); do \
	   ls $$d/*.java >/dev/null 2>&1 || continue; \
	   $(JAVAC) -nowarn -d $(OUT)/$$(basename $$d) $$d/*.java 2>/tmp/cp-javac.err || { \
	     echo "FAIL: $$d"; head -3 /tmp/cp-javac.err; fail=1; }; \
	 done; \
	 if [ $$fail -eq 0 ]; then echo "all problems compile"; else exit 1; fi

.PHONY: need-dir syntax run check
