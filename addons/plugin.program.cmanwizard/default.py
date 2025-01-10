import xbmc
import xbmcgui
import xbmcplugin

def show_message():
    xbmcgui.Dialog().ok("CMAN Wizard", "Welcome to CMAN Wizard for Kodi!")

def main():
    show_message()
    xbmcplugin.endOfDirectory(handle=int(sys.argv[1]))

if __name__ == '__main__':
    main()
