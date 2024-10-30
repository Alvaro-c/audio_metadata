import argparse
import json
import subprocess
from ffmpy import FFprobe
import mutagen
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, ID3NoHeaderError, TIT2, TPE1, TALB, TCON, TDRC, TPOS, TRCK, TXXX


class Track:
    class TagID3v2:
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

    class TagVorbis:
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

    def __init__(self, format):
        if format == 'mp3':
            tag_class = Track.TagID3v2

        elif format == 'flac':
            tag_class = Track.TagVorbis
        else:
            raise ValueError('Unsupported format')

        for attr in dir(tag_class):
            if not attr.startswith('__'):
                setattr(self, attr, getattr(tag_class, attr))


parser = argparse.ArgumentParser(
    "Extract metadata from mp3 files to JSON files")
parser.add_argument(
    "low_audio", help="Path to the audio that will be removed", type=str)
parser.add_argument(
    "high_audio", help="Path to the audio that will be added", type=str)


def get_metadata(audio_file):
    probe = FFprobe(
        global_options='-v quiet -print_format json -show_format',
        inputs={audio_file: None}
    )

    stdout, stderr = probe.run(stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    metadata = json.loads(stdout.decode('utf-8'))
    return metadata['format']['tags'], metadata['format']['format_name']


def main():
    args = parser.parse_args()

    # 1. Get metadata from low audio
    metadata = get_metadata(args.low_audio)[0]
    _, format_high = get_metadata(args.high_audio)

    if format_high == 'mp3':
        high_audio = ID3(args.high_audio)
        high_audio.add(TIT2(encoding=3, text=metadata['title']))
        high_audio.save()


    # 2. Copy tags from origin


    # 4. Copy upgrade to destination with the same name, so path is the same

    # 5. Remove tags in new

    # 5. Add tags to destination

    # 6. Calculate Audio Fingerprint



if __name__ == "__main__":
    main()
