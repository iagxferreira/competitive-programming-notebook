# Build any solution.cpp in the tree.
#   make run DIR=leetcode/0015-three-sum
#   make run DIR=leetcode/0015-three-sum IN=in.txt
#   make practice DIR=leetcode/0015-three-sum   # build practice.cpp instead

CXX      ?= g++
CXXFLAGS ?= -std=c++20 -O2 -Wall -Wextra -Wshadow -fsanitize=address,undefined -g
SRC      ?= solution.cpp
BIN      := /tmp/cp-build

$(BIN):
	@mkdir -p $(BIN)

build: $(BIN)
	@test -n "$(DIR)" || { echo "usage: make build DIR=<problem-dir>"; exit 1; }
	$(CXX) $(CXXFLAGS) $(DIR)/$(SRC) -o $(BIN)/a.out

run: build
	@if [ -n "$(IN)" ]; then $(BIN)/a.out < $(DIR)/$(IN); else $(BIN)/a.out; fi

practice:
	@$(MAKE) run DIR=$(DIR) SRC=practice.cpp IN=$(IN)

# Compile every solution.cpp that is non-empty, to catch rot.
check: $(BIN)
	@fail=0; for f in $$(find leetcode beecrowd hackerrank codeforces -name solution.cpp -size +1c); do \
		$(CXX) -std=c++20 -O2 -fsyntax-only $$f 2>/dev/null || { echo "FAIL $$f"; fail=1; }; \
	done; exit $$fail

.PHONY: build run practice check
