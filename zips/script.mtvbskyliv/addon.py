import time
import xbmc
import os
import xbmcgui
import urllib2

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Sky Living Links[/COLOR][/B]', ['[B][COLOR=white]      Sky Living Link 1[/COLOR][/B]' , '[B][COLOR=white]      Sky Living Link 2[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-2]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]CerebroTV[/COLOR]",""+str(func)+" -3","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    else:
        func = funcs[call]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]CerebroTV[/COLOR]",""+str(func)+" +0","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    return 


def function1():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.livehub/?description=Sky%20Living%20Sky%20Living%20Sky%20Living%20Sky%20Living%20&iconimage=http%3a%2f%2fswiftstreamz.com%2fSwiftStream%2fimages%2fthumbs%2f25693_skyliving1.jpg&mode=10&name=%5bB%5d%5bCOLOR%20white%5dSky%20Living%5b%2fCOLOR%5d%5b%2fB%5d&url=snappystreams%3ahttp%3a%2f%2f51.15.6.129%3a8081%2flarge%2fSkyLiving%2fplaylist.m3u8",return)')

def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.livehub/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dSky%20Living%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2f26cb04f6748172109489d18b64feca2e.m3u8",return)')
     

menuoptions()