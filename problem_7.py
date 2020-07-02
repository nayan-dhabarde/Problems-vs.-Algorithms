# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler, not_found_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = root_handler
        self.not_found_handler = not_found_handler

    def insert(self, path_components, handler = ""):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        for comp in path_components:
            if comp not in current_node.children:
                current_node.insert(comp)
            current_node = current_node.children[comp]

        if handler is None or handler == "":
            current_node.handler = self.root_handler
        else:
            current_node.handler = handler

    def find(self, path_components):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        if len(path_components) == 1 and path_components[0] == '/':
            return self.root.handler

        current_node = self.root
        for comp in path_components:
            if comp in current_node.children:
                current_node = current_node.children[comp]
            else:
                return self.not_found_handler

        if current_node.handler is None:
            return self.not_found_handler
        else:
            return current_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        self.handler = None
        self.children = {}
        # Initialize the node with children as before, plus a handler

    def insert(self, path_component):
        # Insert the node as before
        self.children[path_component] = RouteTrieNode()

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        self.invalid_path_handler = "invalid path handler"
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handler, not_found_handler)

    def add_handler(self, path, handler):
        if path is None or path == "":
            return

        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.router.insert(self.split_path(path), handler)

    def lookup(self, path):
        if path is None or path == "":
            return self.invalid_path_handler
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        return self.router.find(self.split_path(path))

    def split_path(self, path):

        output_list = []
        comp = ""
        index = 0
        while index != len(path):
            if path[index] == '/' or index == len(path) - 1:
                if index == len(path) - 1:
                    comp += path[index]
                output_list.append(comp)
                comp = ""
            else:
                comp += path[index]
            index += 1

        return output_list

        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("a")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

## Edge cases
print(router.lookup("/notpresent")) # should print 'not found handler' or None if you did not implement one
print(router.lookup(None)) # should print 'invalid path handler'
router.add_handler("", "about handler")  # will not add a route
router.add_handler(None, "about handler")  # will not add a route
print(router.lookup("")) # should print 'invalid path handler'




