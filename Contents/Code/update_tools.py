# Import internal tools
from logging import Logging

# Setup logger
log = Logging()


class AlbumUpdateTool:
    UPDATE_URL = 'https://api.audnex.us/books/'

    def __init__(self, force, lang, media, metadata):
        self.date = None
        self.force = force
        self.genres = None
        self.lang = lang
        self.media = media
        self.metadata = metadata
        self.rating = None
        self.series = ''
        self.series2 = ''
        self.thumb = ''
        self.volume = ''
        self.volume2 = ''

    def parse_api_response(self, response):
        """
            Parses keys from API into helper variables if they exist.
        """
        if 'authors' in response:
            self.author = response['authors']
        if 'releaseDate' in response:
            self.date = response['releaseDate']
        if 'genres' in response:
            self.genres = response['genres']
        if 'narrators' in response:
            self.narrator = response['narrators']
        if 'rating' in response:
            self.rating = response['rating']
        if 'seriesPrimary' in response:
            self.series = response['seriesPrimary']['name']
            if 'position' in response['seriesPrimary']:
                self.volume = response['seriesPrimary']['position']
        if 'seriesSecondary' in response:
            self.series2 = response['seriesSecondary']['name']
            if 'position' in response['seriesSecondary']:
                self.volume2 = response['seriesSecondary']['position']
        if 'publisherName' in response:
            self.studio = response['publisherName']
        if 'summary' in response:
            self.synopsis = response['summary']
        if 'image' in response:
            self.thumb = response['image']
        if 'title' in response:
            self.title = response['title']

    # Writes metadata information to log.
    def writeInfo(self):
        log.separator(msg='New data', log_level="info")

        # Log basic metadata
        data_to_log = [
            {'ID': self.metadata.id},
            {'Title': self.metadata.title},
            {'Release date': str(self.metadata.originally_available_at)},
            {'Studio': self.metadata.studio},
            {'Summary': self.metadata.summary},
            {'Poster URL': self.thumb},
        ]
        log.metadata(data_to_log, log_level="info")

        # Log basic metadata stored in arrays
        multi_arr = [
            {'Genres': self.metadata.genres},
            {'Moods(Authors)': self.metadata.moods},
            {'Styles(Narrators)': self.metadata.styles},
        ]
        log.metadata_arrs(multi_arr, log_level="info")

        log.separator(log_level="info")


class ArtistUpdateTool:
    UPDATE_URL = 'https://api.audnex.us/authors/'

    def __init__(self, force, lang, media, metadata):
        self.date = None
        self.force = force
        self.genres = None
        self.lang = lang
        self.media = media
        self.metadata = metadata
        self.thumb = ''

    def parse_api_response(self, response):
        """
            Parses keys from API into helper variables if they exist.
        """
        if 'description' in response:
            self.description = response['description']
        if 'genres' in response:
            self.genres = response['genres']
        if 'name' in response:
            self.name = response['name']
        if 'image' in response:
            self.thumb = response['image']

    # Writes metadata information to log.
    def writeInfo(self):
        log.separator(msg='New data', log_level="info")

        # Log basic metadata
        data_to_log = [
            {'ID': self.metadata.id},
            {'Title': self.metadata.title},
            {'Summary': self.metadata.summary},
            {'Poster URL': self.thumb},
        ]
        log.metadata(data_to_log, log_level="info")

        # Log basic metadata stored in arrays
        multi_arr = [
            {'Genres': self.metadata.genres},
        ]
        log.metadata_arrs(multi_arr, log_level="info")

        log.separator(log_level="info")