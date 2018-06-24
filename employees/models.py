from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255)
    job_title= models.TextField(blank=True, max_length=255)
    years_experience = models.IntegerField()

    PRODUCTION = 'PR'
    RESEARCH_DEVELOPMENT= 'R&D'
    PURCHASING = 'PU'
    MARKETING = 'MA'
    HUMAN_RESOURCES = 'HR'
    ACCOUTING = 'AC'
    DEPARTMENT_CHOICES = (
        (PRODUCTION, 'Production'),
        (RESEARCH_DEVELOPMENT, 'Research and Development'),
        (PURCHASING, 'Purchasing'),
        (MARKETING, 'Marketing'),
        (HUMAN_RESOURCES, 'Human Resource Management'),
        (ACCOUTING, 'Accounting')
    )
    # department has a fixed number of choices
    department = models.CharField(max_length=2,
                                      choices=DEPARTMENT_CHOICES,
                                      default=PRODUCTION)




    def __str__(self):
        return self.name
