blogs = dict() # mapping blog_name to blog_object

def menu():
    # Show the user the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually

    print_blogs()

def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))