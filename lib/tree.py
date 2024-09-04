class Tree:
    def __init__(self, root=None):
        self.root = root

    """
    {
    'tag_name': 'h1',
    'id': 'heading',
    'text_content': 'Title',
    'children': []
    }
    """

    # Depth-First Approach
    # def get_element_by_id(self, id):
    #     nodes_to_visit = [self.root]
    #     while len(nodes_to_visit) > 0:
    #         node = nodes_to_visit.pop(0)
    #         if node["id"] == id:
    #             return node
    #         else:
    #             nodes_to_visit = node["children"] + nodes_to_visit
    #     return None

    # Breadth First Approach
    def get_element_by_id(self, id):
        nodes_to_visit = [self.root]
        while len(nodes_to_visit) > 0:
            node = nodes_to_visit.pop(0)
            if node["id"] == id:
                return node
            else:
                nodes_to_visit += node["children"]
        return None
