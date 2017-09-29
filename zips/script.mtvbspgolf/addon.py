import time
import xbmc
import os
import xbmcgui
import urllib2

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Sky Sports Golf Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky Sports Golf Link 1[/COLOR][/B]',
    '[B][COLOR=white]      Sky Sports Golf Link 2[/COLOR][/B]',
    '[B][COLOR=white]      Sky Sports Golf Link 3[/COLOR][/B]',])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-3]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

    
def function1():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dSky%20Sports%20Golf%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2fbdadcc55dfd64f6a02581bb5801440e7.m3u8")')
  
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.supremacy/?url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Furl%3Dhttp%3A%2F%2Flive.thecableguytv.com%3A25461%2Flive%2Fwade%2Fwade%2F384.ts%26amp%3Bstreamtype%3DTSDOWNLOADER%26amp%3Bname%3DSUPREMACY%0D&mode=12")')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://script.module.streamhublive/?url=swift:http://185.21.217.33:9091/routernew/Gold/playlist.m3u8&mode=10&name=%5BB%5D%5BCOLOR+white%5DGold%5B%2FCOLOR%5D%5B%2FB%5D&iconimage=http%3A%2F%2Fswiftstreamz.com%2FSwiftStream%2Fimages%2Fthumbs%2F1648_28932_gold.jpg&description=GoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGoldGold")')
    
menuoptions()