''' discussion
- Is timestamp unique?
- Is timstamp ordered or not?
- When calling `get`, check if a `set` is called first.
    + if `set` was called, check the timestamp; set_timestamp <= get_timestamp, return st
    + if  set_timestamp > get_timestamp, return st
    + if `set` was not called & no values, return ""
- What's the constraints on time&space complexity?
- Is key unique (can it be replaced? should we store the outdated data when a new status
is added by `set`?)
'''
class TimeMap:

    def __init__(self):
        # key-timestamp mapping
        self.kt={}
        # time array, an array that stores timestamp-key info
        # self.ta=[0]*1001
        # timestamp-value mapping
        self.tv={}
    def set(self, key: str, value: str, timestamp: int) -> None:
        # set would load a new status to certain key
        self.kt.setdefault(key, []).append(timestamp)
        self.tv[timestamp]=value
    def get(self, key: str, timestamp: int) -> str:
        # set timestamp array for key
        if key in self.kt.keys():
            ta=self.kt[key]
            # a set was called
            if ta is not None:
                # find the biggest `int`<`target`(timestamp) in sorted `array`(self.ct)
                # typical binary search, find the max possible case
                l=0
                r=len(ta)-1
                while l<=r:
                    m=(l+r)//2
                    midTime=ta[m]
                    if midTime<=timestamp:
                        # when the condition is met, shrink left bound
                        l=m+1
                    elif midTime>timestamp:
                        r=m-1
                # return right bound
                # print(f'found the biggest prev timestamp, at pos {r}, recorded timestamp: {ta}')
                if r>=0:
                    # previous timestamp
                    prevT=ta[r]
                    return self.tv[prevT]
        return ""
            