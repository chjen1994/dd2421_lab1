import monkdata as m
import dtree as d


#information gain for the 6 attributes in dataset 1
print(d.averageGain(m.monk1, m.attributes[0]));
print(d.averageGain(m.monk1, m.attributes[1]));
print(d.averageGain(m.monk1, m.attributes[2]));
print(d.averageGain(m.monk1, m.attributes[3]));
print(d.averageGain(m.monk1, m.attributes[4]));
print(d.averageGain(m.monk1, m.attributes[5]));


#information gain for the 6 attributes in dataset 3
print(d.averageGain(m.monk2, m.attributes[0]));
print(d.averageGain(m.monk2, m.attributes[1]));
print(d.averageGain(m.monk2, m.attributes[2]));
print(d.averageGain(m.monk2, m.attributes[3]));
print(d.averageGain(m.monk2, m.attributes[4]));
print(d.averageGain(m.monk2, m.attributes[5]));


#information gain for the 6 attributes in dataset 3
print(d.averageGain(m.monk3, m.attributes[0]));
print(d.averageGain(m.monk3, m.attributes[1]));
print(d.averageGain(m.monk3, m.attributes[2]));
print(d.averageGain(m.monk3, m.attributes[3]));
print(d.averageGain(m.monk3, m.attributes[4]));
print(d.averageGain(m.monk3, m.attributes[5]));