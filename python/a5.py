import monkdata as m
import dtree as d
import drawtree_qt5 as draw



#built a tree for monk1 and compute the performance on the test and training data

t=d.buildTree(m.monk1, m.attributes);
print(d.check(t, m.monk1));
print(d.check(t, m.monk1test));

t=d.buildTree(m.monk2, m.attributes);
print(d.check(t, m.monk2));
print(d.check(t, m.monk2test));

t=d.buildTree(m.monk3, m.attributes);
print(d.check(t, m.monk3));
print(d.check(t, m.monk3test));




print ("First Node IG")
for i in range(0,6):
	print(d.averageGain(m.monk1, m.attributes[i]));

a5_1 = d.select(m.monk1, m.attributes[4],1)
a5_2 = d.select(m.monk1, m.attributes[4],2)
a5_3 = d.select(m.monk1, m.attributes[4],3)
a5_4 = d.select(m.monk1, m.attributes[4],4)

print ("subset a5_1 IG")
for i in range(6):
	print(d.averageGain(a5_1, m.attributes[i]));

print ("subset a5_2 IG")
for i in range(6):
	print(d.averageGain(a5_2, m.attributes[i]));
	
print ("subset a5_3 IG")
for i in range(6):
	print(d.averageGain(a5_3, m.attributes[i]));

print ("subset a5_4 IG")
for i in range(6):
	print(d.averageGain(a5_4, m.attributes[i]));

	
a5_2_a4_1 = d.select(a5_2, m.attributes[3],1)
a5_2_a4_2 = d.select(a5_2, m.attributes[3],2)
a5_2_a4_3 = d.select(a5_2, m.attributes[3],3)

a5_3_a6_1 = d.select(a5_3, m.attributes[5],1)
a5_3_a6_2 = d.select(a5_3, m.attributes[5],2)

a5_4_a1_1 = d.select(a5_4, m.attributes[0],1)
a5_4_a1_2 = d.select(a5_4, m.attributes[0],2)
a5_4_a1_3 = d.select(a5_4, m.attributes[0],3)

print(d.mostCommon(a5_1))
print(d.mostCommon(a5_2))
print(d.mostCommon(a5_3))
print(d.mostCommon(a5_4))
print(" ")
print(d.mostCommon(a5_2_a4_1))
print(d.mostCommon(a5_2_a4_2))
print(d.mostCommon(a5_2_a4_3))
print(" ")
print(d.mostCommon(a5_3_a6_1))
print(d.mostCommon(a5_3_a6_2))
print(" ")
print(d.mostCommon(a5_4_a1_1))
print(d.mostCommon(a5_4_a1_2))
print(d.mostCommon(a5_4_a1_3))


#compare the result with the ID3 algroithm
t=d.buildTree(m.monk1, m.attributes, 2);
draw.drawTree(t)
