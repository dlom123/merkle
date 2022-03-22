"""
Reference:
https://gist.github.com/PyPatel/018e2a696510ba894a6104a1d54d2b89
"""

import hashlib

transactions = {}


def merk(values):
    """Returns a hash of all values combined hierarchically."""
    if not values:
        return "No data."
    elif len(values) % 2:
        # odd number of nodes; duplicate the odd node
        values.extend(values[-1:])

    # hash node pairs
    nodes = []
    for v in [values[x:x+2] for x in range(0, len(values), 2)]:
        hasher = hashlib.sha256()
        hasher.update((v[0] + v[1]).encode())
        nodes.append(hasher.hexdigest())
    if len(nodes) == 1:
        # arrived at the Merkle root
        return nodes[0]  # root hash
    return merk(nodes)


def add_transaction(data):
    k = hashlib.sha256(data.encode()).hexdigest()
    transactions.update({k: data})


add_transaction("user1->user2:$3")
add_transaction("user3->user4:$5")
add_transaction("user5->user6:$5")
add_transaction("user7->user8:$7")
for k, v in transactions.items():
    print(f"{k}: {v}")
print()
print(merk(list(transactions.keys())))
