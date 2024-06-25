class SkillTree:
    """
    Class for Character's Trace Tree. Technically, it is actually a forest.

    Args:
        skill_tree_nodes : A list of dicts under skill_trees from mihomo API

    Attributes:
        self.nodes : A list of SkillTreeNode objects
    """
    def __init__(self, skill_tree_nodes):
        self.nodes = []
        for node in skill_tree_nodes:
            skill_tree_node = SkillTreeNode(node['id'], bool(node['level']), node['parent'])
            self.nodes.append(skill_tree_node)

    def getTree(self):
        """
        Return a forest as a list, with 4 trees inside. Each branch of a tree is its own separate list.

        >               root
                         |
                         n1
                        |   |
                        n2  n3
                            | |
                           n4 n5

        > print(SkillTree.getTree())
        > [[root, n1, [[n2], [n3, [[n4], [n5] ] ]  ] ]]

        """
        tree = []
        roots = list(filter(lambda x: x.parent_node is None, self.nodes))
        for root in roots:
            branch = self.getBranch(root=root, nodes=self.nodes)
            tree.append(branch)
        return tree

    @staticmethod
    def getBranch(root, nodes):
        """
        Args:
            root: The SkillTreeNode object whose branch has to be returned
            nodes: The nodes attribute of the SkillTree

        Return the branch of the root as a list.
        """

        branch = [root]
        it = root

        while True:
            childList = [node for node in nodes if node.parent_node == it.id]
            if len(childList) == 0:
                break
            elif len(childList) == 1:
                it = childList[0]
                branch.append(it)
            else:
                branch_list = []
                for child in childList:
                    child_branch = SkillTree.getBranch(child, nodes)
                    branch_list.append(child_branch)

                branch.append(branch_list)
                break

        return branch


class SkillTreeNode:
    """
    Class for node of the SkillTree.

    Args:
        node_id: The id of the node. A string like '15124'.
        activated: Bool for whether the node is activated or not.
        parent_node_id: Id of the parent node.
    """

    def __init__(self, node_id, activated, parent_node_id):
        self.id = node_id
        self.activated = activated
        self.parent_node = parent_node_id
