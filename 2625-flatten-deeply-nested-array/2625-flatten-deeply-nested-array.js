/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    let flattened = [];
    for (let i of arr)
        if (!n || typeof i === "number")
            flattened.push(i);
        else {
            nestedList = flat(i, n - 1)
            for (let j of nestedList)
                flattened.push(j)
        }
    return flattened;
    
};