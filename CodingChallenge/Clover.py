# Create a simple stop watch class that can be used to track time.

# Here's an example Java interface you'll implement.
# interface Stopwatch {
#   void start();
#   void stop();
#   long getElapsedTime();
#   void reset();
# }

# Copy paste try/catch block to verify behavior

# try {
#   // new stopwatch has 0 elapsed time
#   Stopwatch sw = new StopwatchImpl();
#   System.out.println("prints '0': " + sw.getElapsedTime());

#   // record 10 millisecond interval
#   sw.start();
#   Thread.sleep(10);
#   sw.stop();
#   System.out.println("prints '10': " + sw.getElapsedTime());

#   // let 3 milliseconds elapse after a stop
#   Thread.sleep(3);
#   System.out.println("prints '10': " + sw.getElapsedTime());

#   // start again and let 2 millis elapse
#   sw.start();
#   Thread.sleep(2);
#   System.out.println("prints '12': " + sw.getElapsedTime());

#   // let 4 millis elapse
#   Thread.sleep(4);
#   System.out.println("prints '16': " + sw.getElapsedTime());

#   // let 1 milliseconds elapse then stop
#   Thread.sleep(1);
#   sw.stop();
#   System.out.println("prints '17': " + sw.getElapsedTime());

#   // let 3 millis go by while stopped
#   Thread.sleep(3);
#   System.out.println("prints '17': " + sw.getElapsedTime());
# } catch(InterruptedException e) {
# }


# Required Behavior
# Calling start() after start() is illegal.
# Calling stop() after stop(), or after object construction, is illegal.
# illegal start() and stop() calls must not blow up the thread.
# reset() should set the elapsed time to zero and stop the stopwatch if it is running

# interface Stopwatch {
#   void start();
#   void stop();
#   long getElapsedTime();
#   void reset();
# }

# class Stopwatch {
#   public void start() {

#   }

#   public void stop() {

#   }

#   public long getElapsedTime() {

#   }

#   public void reset() {

#   }
# }

# time.time to get the current time
import time
class Stopwatch(object):

    def __init__(self):
        self.startTime = 0
        self.endTime = 0
        self.elapsedTime = 0
        self.totalElapaedTime = 0
        self.isStarted = False;

    def reset(self):
        self.elapsedTime = 0

    # return the total elapsed time after object is instantiated
    def getElapsedTime(self):
        # handle if watch is started but not stopped
        if self.startTime != 0:
            return self.totalElapaedTime + (time.time() - self.startTime)# valid in started state
        else:
            return self.totalElapaedTime #valid in stopped state

    def start(self):
        if self.startTime != 0:
            raise Exception("You shouldn't start a stopwatch without stopping it")
        self.startTime = time.time()
        self.isStarted = True
        self.endTime = 0

    def stop(self):
        if self.endTime != 0:
            raise Exception("You shouldn't stop a stopwatch without starting it")
        self.endTime = time.time()
        self.elapsedTime = self.endTime - self.startTime
        self.totalElapaedTime += self.elapsedTime
        self.isStarted = False
        self.startTime = 0

sw = Stopwatch()
sw.start()
time.sleep(0.5)
sw.stop()
time.sleep(0.5)
sw.start()
time.sleep(1)
sw.stop()
print sw.getElapsedTime() # expect 1.5, got 1
sw.start()
time.sleep(0.25)
print sw.getElapsedTime() # 1.75
