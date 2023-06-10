/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    const obj = {};
    for (const ele of this){
        let key = fn(ele);
        if (obj.hasOwnProperty(key))
            obj[key].push(ele)
        else
            obj[key] = [ele]
    }
    return obj;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */