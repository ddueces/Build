# -*- coding: utf-8 -*-

'''
    showboxarize2 Add-on

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import os,sys,urlparse
from resources.lib.modules import control
from resources.lib.modules import trakt
import xbmcaddon
__addon__ = xbmcaddon.Addon()
__icon__ = __addon__.getAddonInfo('icon')
sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1]) ; control.moderator()

artPath = control.artPath() ; addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = control.lang(32065).encode('utf-8')


class navigator:
    def root(self):
        self.addDirectoryItem('OFFLINE', 'nothing', __icon__, 'DefaultFolder.png')
        #self.addDirectoryItem('[COLOR green]Click Here to Pair[/COLOR] - (Do this once every 4 hours)', 'pair', __icon__, 'DefaultFolder.png')
        #self.addDirectoryItem('[COLOR gold]Cerebro ShowBox[/COLOR] - Main Menu', 'ShowChangelog', __icon__, 'DefaultFolder.png')
        #self.addDirectoryItem('[COLOR red]• [/COLOR]Search Movies / TV Shows', 'searchNavigator', 'search.png', 'DefaultFolder.png')
        #self.addDirectoryItem('[COLOR red]• [/COLOR]Movies Menu', 'movieNavigator', 'movies.png', 'DefaultMovies.png')
        #self.addDirectoryItem('[COLOR red]• [/COLOR]TV Shows Menu', 'tvNavigator', 'tvshows.png', 'DefaultTVShows.png')

        #if not control.setting('lists.widget') == '0':
        #    self.addDirectoryItem('[COLOR red]• [/COLOR]My Movies (IMDB / Trakt)', 'mymovieNavigator', 'mymovies.png', 'DefaultVideoPlaylists.png')
        #    self.addDirectoryItem('[COLOR red]• [/COLOR]My TV Shows (IMDB / Trakt)', 'mytvNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')

        #self.addDirectoryItem('[COLOR red]• [/COLOR]Sky Cinema on Demand', 'channels', 'channels.png', 'DefaultMovies.png')
        #if (traktIndicators == True and not control.setting('tv.widget.alt') == '0') or (traktIndicators == False and not control.setting('tv.widget') == '0'):
        #    self.addDirectoryItem('[COLOR red]• [/COLOR]Latest TV Episodes', 'tvWidget', 'latest-episodes.png', 'DefaultRecentlyAddedEpisodes.png')
        #if not control.setting('movie.widget') == '0':
        #    self.addDirectoryItem('[COLOR red]• [/COLOR]Latest Movies', 'movieWidget', 'latest-movies.png', 'DefaultRecentlyAddedMovies.png')

        #self.addDirectoryItem('[COLOR red]• [/COLOR]Tools (Clear Providers, API Keys, etc.)', 'toolNavigator', 'tools.png', 'DefaultAddonProgram.png')

        #downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0 or len(control.listDir(control.setting('tv.download.path'))[0]) > 0) else False
        #if downloads == True:
        #    self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')

        #self.addDirectoryItem(32010, 'searchNavigator', 'search.png', 'DefaultFolder.png')
        
        #self.addDirectoryItem('Join The Private Facebook Group Called - Jesus Box Media Support & Kodi', 'ShowChangelog', 'icon.png', 'DefaultFolder.png')

        self.endDirectory()


    def movies(self, lite=False):
        self.addDirectoryItem('[COLOR green]Click Here to Pair[/COLOR] - (Do this once every 4 hours)', 'pair', __icon__, 'DefaultFolder.png')
        self.addDirectoryItem('[COLOR gold]Cerebro ShowBox[/COLOR] - Movies Menu', 'ShowChangelog', __icon__, 'DefaultFolder.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Search For a Movie', 'movieSearch', 'search.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Sky Cinema on Demand', 'channels', 'channels.png', 'DefaultMovies.png')
        if not control.setting('movie.widget') == '0':
            self.addDirectoryItem('[COLOR red]• [/COLOR]Latest Movies', 'movieWidget', 'latest-movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Movies by Genres', 'movieGenres', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Movies by Year', 'movieYears', 'years.png', 'DefaultMovies.png')
        #self.addDirectoryItem('[COLOR red]• [/COLOR]Movies by Actor/Actress', 'moviePersons', 'people.png', 'DefaultMovies.png')
        #self.addDirectoryItem(32014, 'movieLanguages', 'languages.png', 'DefaultMovies.png')
        #self.addDirectoryItem(32015, 'movieCertificates', 'certificates.png', 'DefaultMovies.png')
        #self.addDirectoryItem(32017, 'movies&url=trending', 'people-watching.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Popular Movies', 'movies&url=popular', 'most-popular.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Most Voted Movies', 'movies&url=views', 'most-voted.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Box Office Hits', 'movies&url=boxoffice', 'box-office.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Oscar Winners', 'movies&url=oscars', 'oscar-winners.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]In Theaters Now', 'movies&url=theaters', 'in-theaters.png', 'DefaultRecentlyAddedMovies.png')
        #self.addDirectoryItem(32005, 'movieWidget', 'latest-movies.png', 'DefaultRecentlyAddedMovies.png')

        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem('[COLOR red]• [/COLOR] My Movies (IMDB / Trakt)', 'mymovieliteNavigator', 'mymovies.png', 'DefaultVideoPlaylists.png')

            self.addDirectoryItem('[COLOR red]• [/COLOR]Search by Persons Name (MOVIES)', 'moviePerson', 'people-search.png', 'DefaultMovies.png')
            #self.addDirectoryItem(32010, 'movieSearch', 'search.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Tools (Clear Providers, API Keys, etc.)', 'toolNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.endDirectory()


    def mymovies(self, lite=False):
        self.accountCheck()

        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32034, 'movies&url=imdbwatchlist', 'imdb.png', 'DefaultMovies.png', queue=True)

        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png', queue=True, context=(32551, 'moviesToLibrary&url=traktwatchlist'))

        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=imdbwatchlist', 'imdb.png', 'DefaultMovies.png', queue=True)
            self.addDirectoryItem(32033, 'movies&url=imdbwatchlist2', 'imdb.png', 'DefaultMovies.png', queue=True)

        if traktCredentials == True:
            self.addDirectoryItem(32035, 'movies&url=traktfeatured', 'trakt.png', 'DefaultMovies.png', queue=True)

        elif imdbCredentials == True:
            self.addDirectoryItem(32035, 'movies&url=featured', 'imdb.png', 'DefaultMovies.png', queue=True)

        if traktIndicators == True:
            self.addDirectoryItem(32036, 'movies&url=trakthistory', 'trakt.png', 'DefaultMovies.png', queue=True)

        self.addDirectoryItem(32039, 'movieUserlists', 'userlists.png', 'DefaultMovies.png')

        if lite == False:
            self.addDirectoryItem(32031, 'movieliteNavigator', 'movies.png', 'DefaultMovies.png')
            self.addDirectoryItem(32028, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
            self.addDirectoryItem(32010, 'movieSearch', 'search.png', 'DefaultMovies.png')

        self.endDirectory()


    def tvshows(self, lite=False):
        self.addDirectoryItem('[COLOR green]Click Here to Pair[/COLOR] - (Do this once every 4 hours)', 'pair', __icon__, 'DefaultFolder.png')
        self.addDirectoryItem('[COLOR gold]Cerebro ShowBox[/COLOR] - TV Menu', 'ShowChangelog', __icon__, 'DefaultFolder.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Search For a Show', 'tvSearch', 'search.png', 'DefaultTVShows.png')
        if (traktIndicators == True and not control.setting('tv.widget.alt') == '0') or (traktIndicators == False and not control.setting('tv.widget') == '0'):
            self.addDirectoryItem('[COLOR red]• [/COLOR]Latest TV Espidoes', 'tvWidget', 'latest-episodes.png', 'DefaultRecentlyAddedEpisodes.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]TV Shows by Genre', 'tvGenres', 'genres.png', 'DefaultTVShows.png')
        #self.addDirectoryItem('[COLOR red]• [/COLOR]TV Catch Up (Networks)', 'tvNetworks', 'networks.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32014, 'tvLanguages', 'languages.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32015, 'tvCertificates', 'certificates.png', 'DefaultTVShows.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Trending TV Shows', 'tvshows&url=trending', 'people-watching.png', 'DefaultRecentlyAddedEpisodes.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Popuar TV Shows', 'tvshows&url=popular', 'most-popular.png', 'DefaultTVShows.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Highly Rated TV Shows', 'tvshows&url=rating', 'highly-rated.png', 'DefaultTVShows.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Most voted for TV Shows', 'tvshows&url=views', 'most-voted.png', 'DefaultTVShows.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]TV Shows Due Out Today', 'tvshows&url=airing', 'airing-today.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32025, 'tvshows&url=active', 'returning-tvshows.png', 'DefaultTVShows.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]New TV Shows', 'tvshows&url=premiere', 'new-tvshows.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32006, 'calendar&url=added', 'latest-episodes.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
        #self.addDirectoryItem(32027, 'calendars', 'calendar.png', 'DefaultRecentlyAddedEpisodes.png')

        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem('[COLOR red]• [/COLOR] My TV Shows (IMDB / Trakt)', 'mytvliteNavigator', 'mytvshows.png', 'DefaultVideoPlaylists.png')

            self.addDirectoryItem('[COLOR red]• [/COLOR]Search by Persons Name (TV SHOWS)', 'tvPerson', 'people-search.png', 'DefaultTVShows.png')
            #self.addDirectoryItem(32010, 'tvSearch', 'search.png', 'DefaultTVShows.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Tools (Clear Providers, API Keys, etc.)', 'toolNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.endDirectory()


    def mytvshows(self, lite=False):
        self.accountCheck()

        if traktCredentials == True and imdbCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(32034, 'tvshows&url=imdbwatchlist', 'imdb.png', 'DefaultTVShows.png')

        elif traktCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktcollection'))
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png', context=(32551, 'tvshowsToLibrary&url=traktwatchlist'))

        elif imdbCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=imdbwatchlist', 'imdb.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32033, 'tvshows&url=imdbwatchlist2', 'imdb.png', 'DefaultTVShows.png')

        if traktCredentials == True:
            self.addDirectoryItem(32035, 'tvshows&url=traktfeatured', 'trakt.png', 'DefaultTVShows.png')

        elif imdbCredentials == True:
            self.addDirectoryItem(32035, 'tvshows&url=trending', 'imdb.png', 'DefaultMovies.png', queue=True)

        if traktIndicators == True:
            self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'trakt.png', 'DefaultTVShows.png', queue=True)
            self.addDirectoryItem(32037, 'calendar&url=progress', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
            self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'trakt.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)

        self.addDirectoryItem(32040, 'tvUserlists', 'userlists.png', 'DefaultTVShows.png')

        if traktCredentials == True:
            self.addDirectoryItem(32041, 'episodeUserlists', 'userlists.png', 'DefaultTVShows.png')

        if lite == False:
            self.addDirectoryItem(32031, 'tvliteNavigator', 'tvshows.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32028, 'tvPerson', 'people-search.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32010, 'tvSearch', 'search.png', 'DefaultTVShows.png')

        self.endDirectory()


    def tools(self):
        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32044, 'openSettings&query=3.1', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32045, 'openSettings&query=1.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32046, 'openSettings&query=6.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32047, 'openSettings&query=2.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem("[B]SETTINGS[/B] : Library", 'libraryNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32048, 'openSettings&query=5.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32049, 'viewsNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32050, 'clearSources', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32052, 'clearCache', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32073, 'authTrakt', 'trakt.png', 'DefaultAddonProgram.png')

        self.endDirectory()

    def library(self):
        self.addDirectoryItem(32557, 'openSettings&query=4.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem("[B]LIBRARY[/B] : Update Library...", 'updateLibrary&query=tool', 'library_update.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem("[B]LIBRARY[/B] : Movies Folder", control.setting('library.movie'), 'movies.png', 'DefaultMovies.png', isAction=False)
        self.addDirectoryItem("[B]LIBRARY[/B] : TV Shows Folder", control.setting('library.tv'), 'tvshows.png', 'DefaultTVShows.png', isAction=False)

        if trakt.getTraktCredentialsInfo():
            self.addDirectoryItem(32561, 'moviesToLibrary&url=traktcollection', 'trakt.png', 'DefaultMovies.png')
            #self.addDirectoryItem(32562, 'moviesToLibrary&url=traktwatchlist', 'trakt.png', 'DefaultMovies.png')
            self.addDirectoryItem(32563, 'tvshowsToLibrary&url=traktcollection', 'trakt.png', 'DefaultTVShows.png')
            #self.addDirectoryItem(32564, 'tvshowsToLibrary&url=traktwatchlist', 'trakt.png', 'DefaultTVShows.png')

        self.endDirectory()

    def downloads(self):
        #movie_downloads = control.setting('movie.download.path')
        #tv_downloads = control.setting('tv.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'movies.png', 'DefaultMovies.png', isAction=False)
        if len(control.listDir(tv_downloads)[0]) > 0:
            self.addDirectoryItem(32002, tv_downloads, 'tvshows.png', 'DefaultTVShows.png', isAction=False)

        self.endDirectory()


    def search(self):
        self.addDirectoryItem('[COLOR green]Click Here to Pair[/COLOR] - (Do this once every 4 hours)', 'pair', __icon__, 'DefaultFolder.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Search for a Movie', 'movieSearch', 'search.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLOR red]• [/COLOR]Search for a TV Show', 'tvSearch', 'search.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32029, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
        #self.addDirectoryItem(32030, 'tvPerson', 'people-search.png', 'DefaultTVShows.png')

        self.endDirectory()


    def views(self):
        try:
            control.idle()

            items = [ (control.lang(32001).encode('utf-8'), 'movies'), (control.lang(32002).encode('utf-8'), 'tvshows'), (control.lang(32054).encode('utf-8'), 'seasons'), (control.lang(32038).encode('utf-8'), 'episodes') ]

            select = control.selectDialog([i[0] for i in items], control.lang(32049).encode('utf-8'))

            if select == -1: return

            content = items[select][1]

            title = control.lang(32059).encode('utf-8')
            url = '%s?action=addView&content=%s' % (sys.argv[0], content)

            poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()

            item = control.item(label=title)
            item.setInfo(type='Video', infoLabels = {'title': title})
            item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'banner': banner})
            item.setProperty('Fanart_Image', fanart)

            control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=False)
            control.content(int(sys.argv[1]), content)
            control.directory(int(sys.argv[1]), cacheToDisc=True)

            from resources.lib.modules import views
            views.setView(content, {})
        except:
            return


    def accountCheck(self):
        if traktCredentials == False and imdbCredentials == False:
            control.idle()
            control.infoDialog(control.lang(32042).encode('utf-8'), sound=True, icon='WARNING')
            sys.exit()


    def infoCheck(self, version):
        try:
            control.infoDialog('', control.lang(32074).encode('utf-8'), time=5000, sound=False)
            return '1'
        except:
            return '1'


    def clearCache(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheSearch(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_search()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')
        
    def clearCacheSearch2(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_search2()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def addDirectoryItem(self, name, query, thumb, icon, context=None, queue=False, isAction=True, isFolder=True):
        try: name = control.lang(name).encode('utf-8')
        except: pass
        url = '%s?action=%s' % (sysaddon, query) if isAction == True else query
        thumb = os.path.join(artPath, thumb) if not artPath == None else icon
        cm = []
        if queue == True: cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))
        if not context == None: cm.append((control.lang(context[0]).encode('utf-8'), 'RunPlugin(%s?action=%s)' % (sysaddon, context[1])))
        item = control.item(label=name)
        item.addContextMenuItems(cm)
        item.setArt({'icon': thumb, 'thumb': thumb})
        if not addonFanart == None: item.setProperty('Fanart_Image', addonFanart)
        control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)


    def endDirectory(self):
        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=True)


