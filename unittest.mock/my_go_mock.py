blogs = dict() # {} is also the notation also creates a set so stick with dict() or set()

def menu():
    print_blogs()

def print_blogs():
    for key, blog in blogs.items(): #[{blog_name: blog}]
       print('- {}'.format(blog))

