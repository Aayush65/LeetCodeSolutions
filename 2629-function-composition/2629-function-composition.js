/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = (functions) => {
    const fn = (acc, f) => f(acc);
    return (x) => {
        return functions.reduceRight(fn, x);
    }
}

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */