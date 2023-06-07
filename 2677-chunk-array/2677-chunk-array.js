/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    const res = [];
    for (let i = 0; i < arr.length; i += size) {
        let row = [];
        for (let j = i; j < Math.min(arr.length, i + size); j ++) {
            row.push(arr[j])
        }
        res.push(row);
    }
    return res;
};
