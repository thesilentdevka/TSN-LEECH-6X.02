class DirectDownloadLinkException(Exception):
    """NO METHOD FOUND FOR EXTRACTING DIRECT DOWNLOAD LINK FROM THE HTTPS LINK"""
    pass


class NotSupportedExtractionArchive(Exception):
    """THE ARCHIVE FORMAT USED IS NOT SUPPORTED"""
    pass
