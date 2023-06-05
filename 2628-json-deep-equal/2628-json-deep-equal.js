/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    if (typeof o1 !== typeof o2)
        return false;
    if (typeof o1 !== 'object' || !o1 || !o2)
        return o1 === o2;
    if (Array.isArray(o1) !== Array.isArray(o2))
        return false;
    if (Object.keys(o1).length !== Object.keys(o2).length)
        return false;
    for (let i in o1)
        if (!areDeeplyEqual(o1[i], o2[i]))
            return false;
    return true;
};