from django.db import models


class DocProject():
    project_name = models.CharField(max_length=100)
    infile_name = models.CharField(max_length=100)
    infile_path = models.FileField(upload_to="../data/input/")
    infile_size = models.IntegerField()
    word_count_all = models.IntegerField()
    word_count_word = models.IntegerField()
    page_count = models.IntegerField()
    mdsum = models.CharField(max_length=255)
    outfile_path = models.FileField(upload_to="../data/output/")
    outfile_name = models.CharField()
    outfile_size = models.IntegerField()
    billing_status = models.CharField()
