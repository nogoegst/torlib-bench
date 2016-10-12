import sys
import time
import os
import stem.descriptor

def measure_average_advertised_bandwidth(path):
  start_time = time.time()
  total_bw, count = 0, 0
  for filename in os.listdir(path):
    for desc in stem.descriptor.parse_file(path+filename):
      try:
        total_bw += min(desc.average_bandwidth, desc.burst_bandwidth, desc.observed_bandwidth)
      except:
        print(desc)
	continue
      if count%100 == 0:
        sys.stderr.write(".")
      count += 1

  runtime = time.time() - start_time
  print("Finished measure_average_advertised_bandwidth('%s')" % path)
  print('  Total time: %i seconds' % runtime)
  print('  Processed server descriptors: %i' % count)
  print('  Average advertised bandwidth: %i' % (total_bw / count))
  print('  Time per server descriptor: %0.5f seconds' % (runtime / count))
  print('')

if __name__ == '__main__':
  measure_average_advertised_bandwidth('descriptors/recent/relay-descriptors/server-descriptors/') #/2016-06-22-18-05-14-server-descriptors')
