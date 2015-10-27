/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var hashMap = {};
    for (var i = 0; i < nums.length; i++) {
        /* In JS always save reused variable to improve performance */
        var curr = nums[i];
        var pair = target - curr;
        var match = hashMap[pair];
        if (match === undefined) {
            hashMap[curr] = i + 1;
        } else {
            return match > i + 1 ? [i + 1, match] : [ match, i + 1];
        }

    }
};
