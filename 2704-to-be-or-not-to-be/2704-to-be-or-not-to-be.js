/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    function toBe(val1){
        if (val !== val1)
            throw Error("Not Equal");
        else
            return true;
    }
    function notToBe(val1){
        if (val === val1)
            throw Error("Equal");
        else
            return true;
    }
    return {
        toBe, notToBe
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */