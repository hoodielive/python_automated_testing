MENU_PROMPT = 'Enter "c" to create a blog, "l" to list a blog, "r" to read one, "p" to create a post and "q" to quit.'
blogs = dict() # mapping blog_name to blog_object

def menu():
    # Show the user the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually

    print_blogs()
    selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))