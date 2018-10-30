import msprime
import numpy as np

tables = msprime.TableCollection(1.0)

tables.edges.add_row(left=0, right=1, parent=4, child=0)
tables.edges.add_row(left=0, right=1, parent=4, child=1)
tables.edges.add_row(left=0, right=1, parent=5, child=2)
tables.edges.add_row(left=0, right=1, parent=5, child=3)
tables.edges.add_row(left=0, right=1, parent=6, child=4)
tables.edges.add_row(left=0, right=1, parent=6, child=5)

time = np.array([0, 0, 0, 0, 1, 4, 10])
flags = [1]*len(time)
tables.nodes.set_columns(time=time, flags=flags)

tables.sites.set_columns(position=np.array([0.1, 0.2, 0.3, 0.4]),
                         ancestral_state=['0']*4, ancestral_state_offset=[0]*5)

tables.mutations.add_row(site=0, node=4, derived_state='1')
tables.mutations.add_row(site=1, node=5, derived_state='1')
tables.mutations.add_row(site=2, node=0, derived_state='1')
tables.mutations.add_row(site=3, node=5, derived_state='1')


ts = tables.tree_sequence()

t = next(ts.trees())

fig=t.draw(path="tree.svg", mutation_labels={0: 'm1', 1: 'm2', 2: 'm4', 3: 'm5'},
       node_labels={0: 'g0', 1: 'g1', 2: 'g2', 3: 'g3', 4: '4', 5: '5', 6: '6'},
       height=200,width=200)
