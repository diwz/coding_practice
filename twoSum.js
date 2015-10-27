/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var hashMap = {};
    for (var i = 0; i < nums.length; i++) {
        var pair = target - nums[i];
        if (hashMap[pair] === undefined) {
            hashMap[nums[i]] = i + 1;
        } else {
            return hashMap[pair] > i + 1 ? [i + 1, hashMap[pair]] : [hashMap[pair], i + 1];
        }

    }
};
