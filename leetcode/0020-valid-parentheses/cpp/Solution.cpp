#include <stack>
#include <string>

class Solution {
public:
  bool isValid(std::string s) {
    std::stack<char> stack;

    for (char ch : s) {
      if (ch == '(' || ch == '[' || ch == '{') {
        stack.push(ch);
        continue;
      } else {

        if (stack.empty())
          return false;

        char top = stack.top();
        stack.pop();

        if (ch == ')' && top != '(')
          return false;
        if (ch == ']' && top != '[')
          return false;
        if (ch == '}' && top != '{')
          return false;
      }
    }

    return stack.empty();
  }
};
