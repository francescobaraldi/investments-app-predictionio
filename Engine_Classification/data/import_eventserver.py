#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Import sample data for classification engine
"""

import predictionio
import argparse

def import_events(client, file):
  f = open(file, 'r')
  count = 0
  print("Importing data...")
  for line in f:
    data = line.rstrip('\r\n').split(",")
    status = data[0]
    features = data[1].split(" ")
    client.create_event(
      event="$set",
      entity_type="company",
      entity_id=str(count), # use the count num as user ID
      properties= {
        "market" : float(features[0]),
        "total_investment" : float(features[1]),
        "funding_rounds" : float(features[2]),
        "age_first_funding" : float(features[3]),
        "age_last_funding" : float(features[4]),
        "status" : float(status)
      }
    )
    count += 1
  f.close()
  print("%s events are imported." % count)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description="Import sample data for classification engine")
  parser.add_argument('--access_key', default='invald_access_key')
  parser.add_argument('--url', default="http://localhost:7070")
  parser.add_argument('--file', default="./data/data.txt")

  args = parser.parse_args()
  print(args)

  client = predictionio.EventClient(
    access_key=args.access_key,
    url=args.url,
    threads=5,
    qsize=500)
  import_events(client, args.file)
