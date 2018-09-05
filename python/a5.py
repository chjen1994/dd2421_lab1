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