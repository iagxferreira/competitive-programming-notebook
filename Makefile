# Build and run any problem in the tree.
#
#   make syntax DIR=leetcode/0015-3sum     # compile-check only
#   make run    DIR=beecrowd/1000-hello-world
#   make run    DIR=... IN=in.txt          # feed a test file
#   make run    DIR=... SAN=1              # with sanitizers
#   make practice DIR=...                  # build practice.cpp instead
#   make check                             # syntax-check everything
#
# Two problem shapes:
#   stdin/stdout (beecrowd, codeforces, hackerrank) - solution.cpp has a
#     main, so `make run` works directly.
#   class Solution (leetcode) - no main, so `make run` needs a harness.
#     Drop a main.cpp in the problem directory and it is linked in
#     automatically. Without one, use `make syntax`.
#
# SAN=1 needs a sanitizer runtime. GCC needs the libasan/libubsan
# packages (dnf install libasan libubsan); clang ships its own, so
# CXX=clang++ SAN=1 always works.

CXX      ?= g++
WARN     := -std=c++20 -O2 -Wall -Wextra -Wshadow
SANFLAGS := -fsanitize=address,undefined -fno-omit-frame-pointer -g
CXXFLAGS ?= $(WARN) $(if $(SAN),$(SANFLAGS))
SRC      ?= solution.cpp
BIN      := /tmp/cp-build

need-dir:
	@test -n "$(DIR)" || { echo "usage: make $(MAKECMDGOALS) DIR=<problem-dir>"; exit 1; }
	@test -f "$(DIR)/$(SRC)" || { echo "no $(SRC) in $(DIR)"; exit 1; }

syntax: need-dir
	$(CXX) $(WARN) -fsyntax-only $(DIR)/$(SRC)

build: need-dir
	@mkdir -p $(BIN)
	@extra=""; [ -f "$(DIR)/main.cpp" ] && extra="$(DIR)/main.cpp"; \
	 set -x; $(CXX) $(CXXFLAGS) $(DIR)/$(SRC) $$extra -o $(BIN)/a.out

run: build
	@if [ -n "$(IN)" ]; then $(BIN)/a.out < $(DIR)/$(IN); else $(BIN)/a.out; fi

practice:
	@$(MAKE) run DIR=$(DIR) SRC=practice.cpp IN=$(IN)

check:
	@find leetcode beecrowd hackerrank codeforces -name solution.cpp | sort | \
	  xargs -P $$(nproc) -I{} sh -c '$(CXX) -std=c++20 -fsyntax-only "{}" || echo "FAIL: {}"' \
	  > /tmp/cp-check.log 2>&1; \
	if grep -q FAIL /tmp/cp-check.log; then grep FAIL /tmp/cp-check.log; exit 1; \
	else echo "all solutions compile"; fi

.PHONY: need-dir syntax build run practice check
