/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const res = [];
    for (let i in arr)
        res.push(fn(arr[i], Number(i)));
    return res;
};