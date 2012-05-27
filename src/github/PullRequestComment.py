# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import NamedUser

class PullRequestComment( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )
        self.__completed = completion != LazyCompletion
        if completion == ImmediateCompletion:
            self.__complete() # pragma: no cover

    @property
    def body( self ):
        self.__completeIfNeeded( self.__body )
        return self.__body

    @property
    def commit_id( self ):
        self.__completeIfNeeded( self.__commit_id )
        return self.__commit_id

    @property
    def created_at( self ):
        self.__completeIfNeeded( self.__created_at )
        return self.__created_at

    @property
    def id( self ):
        self.__completeIfNeeded( self.__id )
        return self.__id

    @property
    def original_commit_id( self ):
        self.__completeIfNeeded( self.__original_commit_id )
        return self.__original_commit_id

    @property
    def original_position( self ):
        self.__completeIfNeeded( self.__original_position )
        return self.__original_position

    @property
    def path( self ):
        self.__completeIfNeeded( self.__path )
        return self.__path

    @property
    def position( self ):
        self.__completeIfNeeded( self.__position )
        return self.__position

    @property
    def updated_at( self ):
        self.__completeIfNeeded( self.__updated_at )
        return self.__updated_at

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    @property
    def user( self ):
        self.__completeIfNeeded( self.__user )
        return self.__user

    def delete( self ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ),
            None,
            None
        )

    def edit( self, body ):
        post_parameters = {
            "body": body,
        }
        status, headers, data = self.__requester.request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self.__useAttributes( data )

    def __initAttributes( self ):
        self.__body = None
        self.__commit_id = None
        self.__created_at = None
        self.__id = None
        self.__original_commit_id = None
        self.__original_position = None
        self.__path = None
        self.__position = None
        self.__updated_at = None
        self.__url = None
        self.__user = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete() # pragma: no cover

    def __complete( self ): # pragma: no cover
        status, headers, data = self.__requester.request(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( data )
        self.__completed = True

    def __useAttributes( self, attributes ):
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "body" in attributes and attributes[ "body" ] is not None: # pragma no branch
            self.__body = attributes[ "body" ]
        if "commit_id" in attributes and attributes[ "commit_id" ] is not None: # pragma no branch
            self.__commit_id = attributes[ "commit_id" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            self.__created_at = attributes[ "created_at" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            self.__id = attributes[ "id" ]
        if "original_commit_id" in attributes and attributes[ "original_commit_id" ] is not None: # pragma no branch
            self.__original_commit_id = attributes[ "original_commit_id" ]
        if "original_position" in attributes and attributes[ "original_position" ] is not None: # pragma no branch
            self.__original_position = attributes[ "original_position" ]
        if "path" in attributes and attributes[ "path" ] is not None: # pragma no branch
            self.__path = attributes[ "path" ]
        if "position" in attributes and attributes[ "position" ] is not None: # pragma no branch
            self.__position = attributes[ "position" ]
        if "updated_at" in attributes and attributes[ "updated_at" ] is not None: # pragma no branch
            self.__updated_at = attributes[ "updated_at" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            self.__url = attributes[ "url" ]
        if "user" in attributes and attributes[ "user" ] is not None: # pragma no branch
            assert isinstance( attributes[ "user" ], dict )
            self.__user = NamedUser.NamedUser( self.__requester, attributes[ "user" ], completion = LazyCompletion )
