lists=['Nvidia','AMD','Intel','Gigabyte','Zotac']
ltlist=['Nvidia GeForce RTX 3070','AMD Radeon™ RX 6000Series ','Intel® Iris® Xegraphics',
        'GigabyteAORUS GeForce RTX 2080 Ti XtremeWaterforce 11G ',
        'ZOTACGAMING GeForce RTX2060Twin Fan 12GB']
user=int(input('''which company latest and best graphic card you want
1->NVIDIA
2->AMD
3->INTEL
4->GIGABYTE
5->ZOTAC
6->ALL OF THEM
just type serial number
'''))
if user==6:
    for i in range(len(lists)):
        print(lists[i],':',ltlist[i])
else:
    print(lists[user-1],':',ltlist[user-1])

