import failure_sim
import sys



for x in range(int(sys.argv[1])):
    try:
        failure_sim.execute()
    except:
        e = sys.exc_info()[0]
        print(e)
