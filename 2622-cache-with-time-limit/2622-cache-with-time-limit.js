
var TimeLimitedCache = function() {
    this.memo = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    let ans = this.memo.has(key);
    if (ans)
        clearTimeout(this.memo.get(key).timeout);

    const timeout = setTimeout(() => this.memo.delete(key), duration)
    
    this.memo.set(key, {value, timeout})
    return ans
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (!this.memo.has(key))
        return -1;
    return this.memo.get(key).value;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.memo.size
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */