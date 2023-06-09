/**
 * @param {Object} object
 * @param {Function} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj === null || obj === undefined || typeof classFunction !== "function")
        return false;
    let currObj = Object.getPrototypeOf(obj);
    while (currObj && currObj !== classFunction.prototype)
        currObj = Object.getPrototypeOf(currObj);
    return currObj === classFunction.prototype;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */