// 103. Binary Tree Zigzag Level Order Traversal
// BFS / level order (deque, alternate direction per level)
// TODO: solve

// Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

#include <deque>
#include <vector>
class Solution {
public:
  std::vector<std::vector<int>> zigzagLevelOrder(TreeNode *root) {
    std::vector<std::vector<int>> answer;
    if (!root)
      return answer;

    std::deque<TreeNode *> dq;
    dq.push_back(root);

    bool reverse = false;

    while (!dq.empty()) {
      int size = dq.size();
      std::vector<int> level;

      for (int i = 0; i < size; i++) {
        if (!reverse) {
          TreeNode *node = dq.front();
          dq.pop_front();
          level.push_back(node->val);
          if (node->left)
            dq.push_back(node->left);

          if (node->right)
            dq.push_back(node->right);
        } else {

          TreeNode *node = dq.back();
          dq.pop_back();
          level.push_back(node->val);
          if (node->right)
            dq.push_front(node->right);

          if (node->left)
            dq.push_front(node->left);
        }
      }
      answer.push_back(level);
      reverse = !reverse;
    }

    return answer;
  }
};
