class Record:
    """Class to store records for the tree algorithm.

    Attributes:
        node_id (int): The id of the current record.
        parent_id (int): The id of the parent of the current record.
        children (list): List of class objects that represent the child records of the current record.
    """
    def __init__(self, node_id, parent_id):
        """Initialize the record with its id, its parent's id and list of its children ids"""
        self.node_id = node_id
        self.parent_id = parent_id
        self.children = []

def BuildTree(records):
    """Function builds a tree algorithm.

    Args:
        records (list): List of all the records in the tree.

    Return:
        class object: tree algorithm.
    """

    records.sort(key=lambda x: x.node_id)
    ordered_id = [record.node_id for record in records]
    if records:
        # Checks for missing records.
        if ordered_id != list(set(ordered_id)) or ordered_id[-1] != len(ordered_id) - 1 or ordered_id[0] != 0:
            raise ValueError('Record id is invalid or out of order.')

    # Creates the tree algorithm and checks for invalid records.
    for record in records:
        # Checks that only the root is equal to his parent.
        if record.node_id == record.parent_id and record.node_id != 0:
            raise ValueError('Only root should have equal record and parent id.')
        # Checks that the id of the node is smaller that the parent's id.
        if record.parent_id > record.node_id:
            raise ValueError('Node parent_id should be smaller than its record_id.')

    # Put records under their parents.
    for record in records:
        if record.node_id != 0:
            records[record.parent_id].children.append(record)

    if not records:
        return None
    return records[0]