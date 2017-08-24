# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BookManager(models.Manager):
    def Creator(self, aDictionary ):
        results = {'errors': [], newbook : None }

        if len(aDictionary['name']) == 0:
            results['errors'].append("Name Cannot be empty")
        if len(aDictionary['name']) > 255:
            results['errors'].append("Name Cannot be larger than 255 characters")

        if len(aDictionary['desc']) == 0:
            results['errors'].append("Desc Cannot be empty")
        if len(aDictionary['desc']) > 1000:
            results['errors'].append("Description Cannot be larger than 1000 characters")

            if (len(results['errors']) == 0):
                results['newbook'] = books(name=aDictionary['name'], desc=aDictionary['desc'])
                results['newbook'].save()
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
            Writers.append(join (each.first_name, each.last_name) )
        return Writers

class AuthorManager(models.Manager):
    def Creator(self, aDictionary ):
        results = {'errors': [], newAuthor : None }
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
            results['newAuthor'] = authors( first_name=aDictionary['first_name'], last_name=aDictionary['last_name'], email=aDictionary['email'] )
            results['newAuthor'].save()
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
        thisBook = books.objects.get(aBook).first()
        if (None == thisBook):
            results['errors'].append("Book does not exist.")
        thisAuthor = authors.objects.get(anAuthor).first()
        if (None == thisAuthor):
            results['errors'].append("Author does not exist.")
        #TODO, should I switch this to use the discovered values?
        if len(results['errors']) == 0:
            books_authors( book_id=aBook, author_id=anAuthor )
        return results;

class books_authors(models.Model):
    book_id = models.ForeignKey(books)
    author_id = models.ForeignKey(authors)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = Books_AuthorsManager()

    # from apps.BookAuthors_app.models import *
    # fran = authors(first_name="Fran", last_name="Stewart", email="Fran@google.com")
    # adventure = books(name="BookTitle", desc="Adventures in DnD")
    # books.objects.all().count()
