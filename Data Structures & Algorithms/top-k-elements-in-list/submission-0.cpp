#include <ranges>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::vector<int> answer{};
        if (nums.empty()) {
            return answer;
        }

        std::unordered_map<int, int> count{};
        for (const auto &e : nums) {
            count[e] += 1;
        }

        std::vector<std::vector<int>> buckets(nums.size() + 1);
        for (const auto &e : count) {
            buckets[static_cast<std::size_t>(e.second)].push_back(e.first);
        }

        for (const auto &element : std::views::reverse(buckets)) {
            for (const auto &inner : element) {
                answer.push_back(inner);
                if (static_cast<int>(answer.size()) == k) {
                    return answer;
                }
            }
        }

        return answer; 
    }

};