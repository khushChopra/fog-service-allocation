from cluster_head import Cluster_head
from node import Node
from pprint import pprint
from random import randint, random

my_cluster_head = Cluster_head()
descriptor = my_cluster_head.make_nodes()
pprint(descriptor)
pprint(my_cluster_head.describe())
print()

k = input()
no_of_service = int(k)
services = [ i for i in range(no_of_service) ]
setup_payloads = [ [1,1,0,3] for i in range(no_of_service) ]
payloads = [ [1+random(), 0.5+random(), randint(0,5)] for i in range(no_of_service) ]

my_cluster_head.setup_service(services, setup_payloads, policy="random")
random_result = my_cluster_head.execute(services, payloads)
print(random_result)
my_cluster_head.setup_service(services, setup_payloads, policy="my algo")
my_algo_result = my_cluster_head.execute(services, payloads)
print(my_algo_result)

