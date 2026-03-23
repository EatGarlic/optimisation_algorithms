import time



class Timer:
    
    @staticmethod
    def timeFunction(function, *args, **kwargs):
        timer = Timer()
        timer.start()
        function(*args, **kwargs)
        timer.end()

        print(timer)


    def __init__(self):
        self.__start = None
        self.__end = None

    def start(self):
        self.__start = time.time()

    def end(self):
        self.__end = time.time()

    def elapsed(self):
        if self.__start == None:
            return None
        
        if self.__end == None:
            return time.time() - self.__start()
        
        return self.__end - self.__start
    
    def __str__(self):
        elapsed = self.elapsed()
        if elapsed == None:
            return 'not started'
        return f'{elapsed} seconds'
    

global_timer = Timer()


if __name__ == '__main__':
    def timeWaste(n):
        for i in range(n):
            f = (i*1.321+0.231)**0.213

    
    timer = Timer()
    timer.start()
    timeWaste(100000)
    timer.end()
    print(timer)

    Timer.timeFunction(timeWaste, 100000)