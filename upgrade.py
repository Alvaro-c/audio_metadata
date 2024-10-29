from mutagen.mp3 import MP3
from mutagen.id3 import ID3, ID3NoHeaderError, TIT2, TPE1, TALB, TCON, TDRC, TPOS, TRCK, TXXX

class track:
    class tag_id3v2:
        title = 'TIT2'
        artist = 'TPE1'
        tracknumber = 'TRCK'
        album = 'TALB'
        discnumber = 'TPOS'
        date = 'date'
        genre = 'TCON'
        media = 'TMED'
        originaldate = 'TDOR'
        script = 'TXXX:SCRIPT'
        isrc = 'TSRC'
        albumartistsort = 'TSO2'
        albumartist = 'TPE2'
        asin = 'TXXX:ASIN'
        originalyear = None
        label = 'TPUB'
        barcode = 'TXXX:BARCODE'
        artists = 'TXXX:ARTISTS'
        releasetype = 'TXXX:MusicBrainz Album Type'
        catalognumber = 'TXXX:CATALOGNUMBER'
        releasestatus = 'TXXX:MusicBrainz Album Status'
        releasecountry = 'TXXX:MusicBrainz Album Release Country'
        acoustid_id = 'TXXX:Acoustid Id'
        musicbrainz_albumid = 'TXXX:MusicBrainz Album Id' 
        musicbrainz_artistid = 'TXXX:MusicBrainz Artist Id'
        musicbrainz_albumartistid = 'TXXX:MusicBrainz Album Artist Id'
        musicbrainz_releasegroupid = 'TXXX:MusicBrainz Release Group Id'
        musicbrainz_trackid = 'TXXX:MusicBrainz Release Track Id'
        acoustid_fingerprint = 'TXXX:Acoustid Fingerprint'
        



    class tag_vorbis:
        title = 'TITLE'
        artist = 'ARTIST'
        tracknumber = 'TRACKNUMBER'
        album = 'ALBUM'
        discnumber = 'DISCNUMBER'
        date = 'date'
        genre = 'GENRE'
        media = 'MEDIA'
        originaldate = 'ORIGINALDATE'
        script = 'SCRIPT'
        isrc = 'ISRC'
        albumartistsort = 'ALBUMARTISTSORT'
        albumartist = 'ALBUMARTIST'
        asin = 'ASIN'
        originalyear = 'ORIGINALYEAR'
        label = 'LABEL'
        barcode = 'BARCODE'
        artists = 'ARTISTS'
        releasetype = 'RELEASETYPE'
        catalognumber = 'CATALOGNUMBER'
        releasestatus = 'RELEASESTATUS'
        releasecountry = 'RELEASECOUNTRY'
        acoustid_id = 'ACOUSTID_ID'
        musicbrainz_albumid = 'MUSICBRAINZ_ALBUMID'
        musicbrainz_artistid = 'MUSICBRAINZ_ARTISTID'
        musicbrainz_albumartistid = 'MUSICBRAINZ_ALBUMARTISTID'
        musicbrainz_releasegroupid = 'MUSICBRAINZ_RELEASEGROUPID'
        musicbrainz_trackid = 'MUSICBRAINZ_RELEASETRACKID'
        acoustid_fingerprint = 'ACOUSTID_FINGERPRINT'
    
    
    
    
    title = ''

def main():
    # 1. Get both files
    original = ''
    upgrade = ''

    # 2. Copy tags from origin

    
    # 3. Remove original

    # 4. Copy upgrade to destination

    # 5. Remove tags in new


    # 5. Add tags to destination

    # 6. Calculate Audio Fingerprint


if __name__ == "__main__":
    main()
