/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const keyMap = new Map();
    for (const obj of arr1)
        keyMap.set(obj["id"], obj);
    
    for (const obj of arr2)
        if (keyMap.has(obj["id"]))
            for (const keys in obj)
                keyMap.get(obj["id"])[keys] = obj[keys]
        else
            keyMap.set(obj["id"], obj);
        
    const arr = [];
    for (const obj of keyMap)
        arr.push(obj[1]);
    arr.sort((a, b) => a["id"] - b["id"]);
    return arr;
};