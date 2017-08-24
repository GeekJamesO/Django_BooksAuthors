# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
# Create your models here.
class BookManager(models.Manager):
    def Creator(self, aDictionary ):
        results = {'errors': [] , 'newbook' : None }
        print ('inside Creator')
        if len(aDictionary['name']) == 0:
            results['errors'].append("Name Cannot be empty")
        if len(aDictionary['name']) > 255:
            results['errors'].append("Name Cannot be larger than 255 characters")

        if len(aDictionary['desc']) == 0:
            results['errors'].append("Desc Cannot be empty")
        if len(aDictionary['desc']) > 1000:
            results['errors'].append("Description Cannot be larger than 1000 characters")

        if (len(results['errors']) == 0):
            print "  Book '{0}' added.".format(aDictionary['name'])
            abook = books(name=aDictionary['name'], desc=aDictionary['desc'])
            if (None == abook):
                results['errors'].append("Unable to create book")
            else:
                abook.save()
                results['newbook'] = abook
        else:
            print ('errors in Creator')

            for error in results['errors']:
                print error
        return results

class books(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    def authors():
        Writers = []
        r = books_authors.objects.filter(book_id=self)
        for each in r:
            Writers.append( "{0} {1}".format(each.first_name, each.last_name) )
        return Writers

class AuthorManager(models.Manager):
    def Creator(self, aDictionary ):
        results = {'errors': [], 'newAuthor' : None }
        if len(aDictionary['first_name']) < 2:
            results['errors'].append("first name must be 3 or more characters")
        if not (aDictionary['first_name']).isalpha():
            results['errors'].append("first name must be alphabetic characters")

        if len(aDictionary['last_name']) < 2:
            results['errors'].append("last name must be 3 or more characters")
        if not (aDictionary['last_name']).isalpha():
            results['errors'].append("last name must be alphabetic characters")

        regexResult = re.search(r'\w+@\w+',aDictionary['email'])
        if not regexResult:
            results['errors'].append("Email is not valid")

        if len(results['errors']) == 0:
            print "  Author '{0} {1}'  added.".format(aDictionary['first_name'], aDictionary['last_name'] )
            auth = authors(first_name=aDictionary['first_name'], last_name=aDictionary['last_name'], email=aDictionary['email'] )
            auth.save()
            results['newAuthor']=auth
        else:
            for error in results['errors']:
                print error
        return results;

class authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()
    def books():
        publishedWorks = []
        r = books_authors.objects.filter(author_id=self)
        for each in r:
            publishedWorks.append(each.name)
        return Writers

class Books_AuthorsManager(models.Manager):
    def Creator(self, aBook, anAuthor ):
        results = {'errors': [], 'publishedBook' : None }
        if (None == aBook):
            results['errors'].append("Book does not exist.")
        if (None == anAuthor):
            results['errors'].append("Author does not exist.")
        if len(results['errors']) == 0:
            print "No Errors in Books_Authors"
            newcombo = books_authors(book_id=aBook, author_id=anAuthor)
            newcombo.save()
            results['publishedBook'] = newcombo
        else:
            for error in results['errors']:
                print error
        return results;

class books_authors(models.Model):
    book_id = models.ForeignKey(books)
    author_id = models.ForeignKey(authors)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = Books_AuthorsManager()

"""
...Example of how to create values at the shell...

from apps.BookAuthors_app.models import *
fran = authors.objects.Creator({"first_name":"Fran", "last_name":"Stewart", "email":"fran@fran.com"})
books.objects.count()
adventure = books.objects.Creator({"name" : "BookTitle", "desc" : "Adventures in DnD"})
ReleaseParty = books_authors.objects.Creator(adventure['newbook'], fran['newAuthor'])
print ReleaseParty["errors"]
print ReleaseParty['publishedBook'].author_id.first_name
print ReleaseParty['publishedBook'].book_id.name
"""
