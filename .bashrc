# this simply adds the current working directory to sys.path so the code remains DRY. 
# It's so the plugins can access OnlineTimeline without always having to do sys.path.append(os.getcwd())
export PYTHONPATH="{PYTHONPATH}:./"