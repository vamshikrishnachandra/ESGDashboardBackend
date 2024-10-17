from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

class ESGData(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    environmental = models.FloatField()
    social = models.FloatField()
    governance = models.FloatField()
    esg_score = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company.name} - ESG Score: {self.esg_score}"
