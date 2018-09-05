import monkdata as m
import dtree as d
import drawtree_qt5 as draw
import random



def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]




monk1train, monk1val = partition(m.monk1, 0.6)
#monk2train, monk2val = partition(m.monk2, 0.6)
monk3train, monk3val = partition(m.monk3, 0.6)

t1=d.buildTree(monk1train, m.attributes);
t3=d.buildTree(monk3train, m.attributes);
#d.allPruned(t1);
#d.allPruned(t2);


def checkperformance(tree, monk1val):
	pruned_trees = d.allPruned(tree);
	t1_better_performance = -1;
	best_tree = None;
	for t in pruned_trees:
		if t1_better_performance < d.check(t,monk1val):
			t1_better_performance = d.check(t,monk1val);
			best_tree = t;

	if t1_better_performance >= d.check(tree,monk1val):
		return checkperformance(best_tree, monk1val)

	return tree


prunedTree = checkperformance(t1, monk1val);

print(d.check(prunedTree, m.monk1test));
draw.drawTree(prunedTree);

#print(d.check(t1, monk1val));
#print(d.check(t3, monk3val));