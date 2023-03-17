from xbmcplugin import addDirectoryItem, endOfDirectory
from xbmcgui    import ListItem
from sys        import argv as args
handle = int(args[1])
hello = ListItem('Hello, World!')
addDirectoryItem(handle, args[0], hello, False)
endOfDirectory(handle, True, cacheToDisc=False)