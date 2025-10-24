import sys

sys.path.append("..")
print(sys.path)
from pac1.modulo import pachar

pachar()

sys.path.remove("..")
sys.path.append("/home/frils/Documents/reviews/review-airflow/enough_python/pcap/exam_prep/paquetes/pac2")
print(sys.path.index("/home/frils/Documents/reviews/review-airflow/enough_python/pcap/exam_prep/paquetes/pac2"))

import coca.cola.coke as c

c.cokewithlemon()
sys.path.remove(
    "/home/frils/Documents/reviews/review-airflow/enough_python/pcap/exam_prep/paquetes/pac2")  # print(sys.path.index("/home/frils/Documents/reviews/review-airflow/enough_python/pcap/exam_prep/paquetes/pac2"))
