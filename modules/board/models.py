from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    '''
        Modelo que representa as vagas cadastradas
    '''
    JOB_TYPE = (('ESTAGIO', 'Estagio'),
                ('EMPREGO', 'Emprego'),
                ('FREELANCER', 'FREELANCER'),)

    title = models.CharField(max_length=255)
    description = models.TextField()
    salary_min = models.DecimalField(max_digits=10, decimal_places=2)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2)
    # novos campos de acordo com requisitos do sistema
    jobtype = models.CharField(max_length=10, choices=JOB_TYPE)
    workload = models.DecimalField(max_digits=2, decimal_places=1)
    validity = models.DateTimeField()
    open_job = models.BooleanField(default=True)
    internal_job = models.BooleanField(default=False)

    author = models.ForeignKey(User)
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'

    def __str__(self):
        return self.title
