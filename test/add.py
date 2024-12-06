def NeededFunc():
    import sys
    import os
    from dotenv import load_dotenv
    load_dotenv()
    # Expand and normalize the path
    project_dir = os.path.expanduser("~/Laptop/Project/Lexi-Ai")
    sys.path.insert(0, project_dir)