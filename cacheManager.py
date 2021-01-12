# Initialising required global scope lists.
cache = []
requests = []

# Sorts a list of tuples by specific index of tuple. Returns the sorted list.
# Iterates over a list of items, moving the larger values to the end of the list by a series of swaps. 
def tupleSort(lst, index):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j][index] > lst[j + 1][index]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
    return lst


# Applies tupleSort twice to return tuple with the smallest number that also has least number of hits.
def evictedValue(lst):
    tupleSort(lst, 1)
    
    lowestCount = lst[0][1]
    subLst = []
    for i in lst:
        if i[1] == lowestCount:
            subLst.append(i)
    
    tupleSort(subLst, 0)

    return subLst[0]


# FIFO (First In First Out).
def fifo(req, cache):

    # Iterate requests.
    for x in req:
        if (x in cache):
            print( x, ": HIT - " + str(x) + " already in cache.")
            
        elif (len(cache) < 8):
            print( x, ": MISS - Add " + str(x) + " to cache.")
            cache.append(x)
        
        elif (len(cache) == 8):
            evicted = cache[0]
            print( x, ":MISS - Evict " + str(evicted) + ". Add " + str(x) + " to cache.")
            cache.pop(0)
            cache.append(x)
                
    return print("\nFinal FIFO Cache: ", cache)


# LFU (Least Frequently Used).
def lfu(req, cache):

    # Iterate requests, tracking and logging number of times value in the cache is requested.
    requestTracker = []
    for x in req:
        # Log cache items as (value, hit count) tuple.
        requestTracker.append(x)
        hitCount = requestTracker.count(x)
        xTuple = (x, hitCount)
        existingTuple = (x, hitCount - 1)

        if (existingTuple in cache):
            print( x, ": HIT - " + str(x) + " already in cache. Increment hit count by 1.")
            cache.remove(existingTuple)
            cache.append(xTuple)
            
        elif (len(cache) < 8):
            print(x, ": MISS - Add " + str(x) + " to cache.")
            cache.append(xTuple)
        
        # Find and remove eviction value using evictedValue function. Also remove backlog of evicted value from requestTracker to reset hitcount to zero.
        elif (len(cache) == 8):
            evicted = evictedValue(cache)
            print( x, ": MISS - Evict " + str(evicted[0]) + ". Add " + str(x) + " to cache.")
            for _ in range(hitCount):
                requestTracker.remove(evicted[0])
            cache.remove(evicted)
            cache.append(xTuple)

    # Final cache presented as tuples of (value, hitcount).
    return print("\nFinal LFU Cache: ", cache)


# Main Menu + Input Function.
def cacheManager():
    print("\nMAIN MENU\nPlease Input Requests (Integers):")
    print("To finalise requests enter 0.")
    
    # Iterating request inputs untill 0 entered. Prints final list of requests.
    reqInput = 1
    while (reqInput != 0):
        reqInput = int(input("--> "))
        requests.append(reqInput)
    requests.pop()
    print("\nRequests: ", requests)

    # System selector menu.
    print("\nPlease choose which managment system you would like to use:")
    print("Enter 1 for FIFO.\nEnter 2 for LFU.\nEnter Q to QUIT.")
    managerInput = input("--> ")

    if (managerInput == "1"):
        print("\nProcessing FIFO cache managment system.\n")
        fifo(requests, cache)

    elif (managerInput == "2"):
        print("\nProcessing LFU cache managment system.\n")
        lfu(requests, cache)
    
    elif (managerInput == "Q"):
        quitQuestion = input("\nYou are about to close the program.\n-> Are you sure? [yes]: ")
        if (quitQuestion == "yes"):
            print("Closing Program...")
            exit()
        else:
            print("Please start again...")
    
    else:
        print("Please enter a valid menu ption...")

    # Clear requests and cache lists at the end before restarting the program.
    requests.clear()
    cache.clear()

    return cacheManager()


# Calling main function to begin program.
cacheManager()
